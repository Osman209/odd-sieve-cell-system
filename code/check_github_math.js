// check.js — the seven passes. Run before ANY push of math-bearing markdown.
const fs = require('fs'), katex = require('katex');
const DENY = ['operatorname', '\\rm ', '\\bf ', '\\it ', '\\sf ', '\\tt ', '\\cal ',
              'mathchoice', '\\def', 'newcommand', '\\href', 'includegraphics'];
const ESC = /\\([!-\/:-@\[-`{-~])/g;               // GitHub's full ASCII-punct unescape

function spans(t) {
  const out = [];
  const disp = /\$\$([\s\S]*?)\$\$/g;
  let m, masked = t;
  while ((m = disp.exec(t))) out.push({ tex: m[1], disp: true, at: m.index });
  masked = t.replace(disp, s => ' '.repeat(s.length));
  const inl = /(?<!\$)\$(?!\$)([^\$\n]+?)\$(?!\$)/g;
  while ((m = inl.exec(masked))) out.push({ tex: m[1], disp: false, at: m.index });
  return out;
}
function lineOf(t, i) { return t.slice(0, i).split('\n').length; }

let grand = 0;
for (const f of process.argv.slice(2)) {
  const t = fs.readFileSync(f, 'utf8');
  const S = spans(t);
  let esc = 0, fail = 0, silent = 0, deny = 0, pipe = 0;
  const msgs = [];
  for (const s of S) {
    if (ESC.test(s.tex)) { esc++; msgs.push(`  L${lineOf(t, s.at)} escape-stripped: ${s.tex.slice(0,70)}`); }
    ESC.lastIndex = 0;
    const un = s.tex.replace(ESC, '$1');
    for (const d of DENY) if (un.includes(d)) { deny++; msgs.push(`  L${lineOf(t, s.at)} DENIED macro "${d.trim()}": ${un.slice(0,60)}`); }
    if (/(?<!\\)\|/.test(un)) pipe++;
    let html = '';
    try { html = katex.renderToString(un, { displayMode: s.disp, throwOnError: true }); }
    catch (e) { fail++; msgs.push(`  L${lineOf(t, s.at)} RENDER FAIL: ${e.message.slice(0,80)} :: ${un.slice(0,60)}`); continue; }
    const probe = un.replace(/\{,\}/g, '').replace(/\\(?:frac|binom|dfrac|tfrac)\{[^{}]*\}\{[^{}]*\}/g, 'X')
                    .replace(/\\begin\{[a-z*]+\}|\\end\{[a-z*]+\}/g, '');
    if (/[A-Za-z0-9)\]]\}\d/.test(probe)) { silent++; msgs.push(`  L${lineOf(t, s.at)} lost-subscript? ${un.slice(0,60)}`); }
    if (/(?<![\\_^a-zA-Z])\{[^{}]*,[^{}]*\}/.test(probe) && !/\\lbrace|\\begin/.test(un)) {
      silent++; msgs.push(`  L${lineOf(t, s.at)} vanished-braces? ${un.slice(0,60)}`);
    }
  }
  // tables: group consecutive |-rows, require constant unescaped pipe count per block
  const L = t.split('\n'); let i = 0, badT = 0;
  while (i < L.length) {
    if (L[i].trim().startsWith('|')) {
      let j = i, counts = [];
      while (j < L.length && L[j].trim().startsWith('|')) {
        counts.push((L[j].match(/(?<!\\)\|/g) || []).length); j++;
      }
      if (new Set(counts).size > 1) { badT++; msgs.push(`  L${i+1} TABLE pipe counts vary: ${[...new Set(counts)].join(',')}`); }
      i = j;
    } else i++;
  }
  const bad = esc + fail + silent + deny + badT;
  grand += bad;
  console.log(`${f}\n  formulas ${S.length} | escape-stripped ${esc} | render-fail ${fail} | silent-risk ${silent} | denied ${deny} | broken tables ${badT} | raw-pipe spans ${pipe}`);
  msgs.filter(m=>/FAIL|DENIED|escape|TABLE/.test(m)).concat(msgs.filter(m=>!/FAIL|DENIED|escape|TABLE/.test(m))).slice(0, 14).forEach(m => console.log(m));
  if (msgs.length > 14) console.log(`  ... and ${msgs.length - 14} more`);
}
console.log(`\nTOTAL problems: ${grand}`);
process.exit(grand ? 1 : 0);
