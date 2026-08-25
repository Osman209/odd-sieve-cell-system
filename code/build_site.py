#!/usr/bin/env python3
"""
build_site.py — regenerate docs/ : one landing page and one abstract page per paper,
in the same template as the author's other site (prime-number-studies).

Each paper page carries Google Scholar citation meta tags, which is what makes the
work indexable; the body is the abstract only, with the full text in the PDF and on
GitHub.  That deliberately keeps the site clear of the LaTeX-rendering problems that
Jekyll would otherwise introduce.

    python3 code/build_site.py
"""
import html
import os
import shutil

REPO = "https://github.com/Osman209/odd-sieve-cell-system"
SITE = "https://osman209.github.io/odd-sieve-cell-system"
ORCID = "0009-0004-5912-999X"
DOI = "10.5281/zenodo.22085627"
DATE = "2026-08-25"

CSS = """<style>body{max-width:52rem;margin:2.5rem auto;padding:0 1.2rem;font:16px/1.6 Georgia,"DejaVu Serif",serif;color:#1a1a1a}
h1{font-size:1.6rem;line-height:1.3;margin-bottom:.2rem}h2{font-size:1.05rem;font-weight:400;color:#555;margin-top:0}
a{color:#0b4f8a}.meta{color:#555;font-size:.92rem}.abs{margin:1.4rem 0}
ul{list-style:none;padding:0}li{margin:1.15rem 0;padding-left:.9rem;border-left:3px solid #e3e3e3}
.t{font-weight:600}.s{color:#555;font-size:.95rem}.tag{font-size:.78rem;color:#777;text-transform:uppercase;letter-spacing:.05em}
code{background:#f5f5f5;padding:.1em .3em;border-radius:3px;font-size:.9em}</style>"""

PAPERS = [
    dict(
        slug="overview_the_cell_system",
        title="The Cell System: an Overview",
        sub="Every result of the set stated once, with its status attached: proved, proved under hypothesis, or measured",
        abs="A single pass over the seven documents. The coordinates; the exact window histogram; "
            "the exact transport of a census over a sieve cycle; what survives the move to a short "
            "interval; what the framework decides outright; where it stops, stated from inside the "
            "construction rather than quoted; the pattern the work keeps arriving at; and what an "
            "external ingredient would have to supply. No progress toward the twin-prime conjecture "
            "is claimed, and no new bound.",
    ),
    dict(
        slug="paper_0_quadratic_staircase",
        title="An Exact Histogram for a Quadratic Staircase",
        sub="Five values, five multiplicities, and no error term — a paper about no prime numbers at all",
        abs="For odd n, the increments of the staircase floor(2j^2/n) take only the values 0 to 4, and "
            "their five multiplicities are given exactly by A = floor((n+7)/8). The proof is a tiling "
            "argument and carries no error term, which is the surprise: a probabilistic model of the "
            "same count returns the same answer and would normally carry one. A companion theorem "
            "counts the interior local maxima of 2j^2 mod n, exactly 2A for every odd n at least 51, "
            "and turns on four residues whose squares always sum to 84. The paper states plainly how "
            "the object differs from the Sturmian word it resembles: the analogy is one of form only, "
            "and the factor complexity and imbalance are measured against the Sturmian values to show "
            "how far it fails. Independent of the rest of the set.",
        pre="quadratic_staircase.pdf",
    ),
    dict(
        slug="paper_I_cells_and_lines",
        title="Cells and Lines",
        sub="The coordinates: lines, cells, the window between prime squares, and the central factor",
        abs="Each odd prime p is a line L_p(k) = p^2 + 2pk; the numbers 6m plus or minus 1 form a cell; "
            "and the window between consecutive prime squares is where every line that matters is "
            "already present. Includes the central-factor theorem — for odd m the two divisors nearest "
            "the square root are reached in exactly a + b + 2 steps — with its handover corollary, and "
            "a section saying which of these statements are restatements rather than results.",
    ),
    dict(
        slug="paper_II_inheritance_law_on_the_cycle",
        title="The Inheritance Law on the Cycle",
        sub="Exact transport of a divisor census, and of weights, over a sieve cycle",
        abs="Adding a line q multiplies the cycle by q and the census transports with no error at all. "
            "The refined version tracks the full distribution of inheritance depth through a "
            "finite-state generating function, so that any weight depending on the number of sieve "
            "lines met can be evaluated exactly on the cycle; a size-binned refinement reproduces "
            "Richert's weight to 0.4 per cent. Section 6 gives the correlation ladder from which the "
            "singular series of Paper V is built, and names it as the Hardy-Littlewood series it is.",
    ),
    dict(
        slug="paper_III_from_cycle_to_window",
        title="From Cycle to Window",
        sub="What survives when an exact periodic law is evaluated on a short interval",
        abs="An exact law on a sieve cycle is not an exact law on a window, and the loss is not uniform "
            "across the quantities one might evaluate. Soft weights transfer almost exactly; sharp "
            "indicators do not. The distinction is measured rather than asserted, and it governs the "
            "transfer measurements of Paper V.",
    ),
    dict(
        slug="paper_IV_twin_criterion",
        title="The Twin Criterion",
        sub="What the framework proves outright about gap-two pairs, and how far a residue argument can compress the exceptions",
        abs="The six exceptional positions in a sector; the belt between consecutive prime squares and its reach; the birth of a line and what it can remove on its own first window. The six positions are exact quadratics in the sector index, so the phases of the lines 5 and 7 depend on one residue class alone and the scan over them is a proof rather than a sample: those two lines cut six open positions to three, and three occur only when (M+2, M+4) is itself a twin, so a twin follows from three open cells rather than seven. Section 3.3 carries this over a full period of 35 tiling sectors, where the budget falls to 31, and shows that no finite set of lines lowers it further: of the 28 maximal configurations, 27 are killed by a fixed prime divisor once the quadratic partner conditions are included, and the survivor - 59 polynomials of total degree 90 - is admissible at every prime, so the residues can be chosen simultaneously against any finite list. The order in which the lines are born adds nothing either. Section 3.4 then lengthens the block: the ceilings over 3, 5, 7 and 9 consecutive periods are 67, 100, 138 and 163, and a quadratic shadow argument gives the order - each exception type forbids 2 or 3 residue classes per prime on average, so the five index sets are sifted in dimensions 2, 2, 3, 3, 3 and the ceiling is of order L/log^2 L. The density of hiding places therefore tends to zero, which lowers the number required and leaves the missing ingredient untouched: what the survivor side must supply is an existence statement, not a rate of growth. One statement is proved under a stated hypothesis and verified numerically beyond it, and is labelled that way wherever it appears.",
    ),
    dict(
        slug="paper_V_where_the_framework_stops",
        title="Where the Framework Stops",
        sub="The obstruction derived from inside the construction, and how much of the difficulty it can localise first",
        abs="Two test cases are followed to their end - almost-primes between consecutive squares, and Jacobsthal's function - and both land on the same wall. The construction produces Buchstab's identity, the Hardy-Littlewood singular series and the sifting limit without importing any of them, which is the finding: the framework has no blind spot of its own, and reaches the field's barrier in its own vocabulary. Section 7.6 measures the transfer in three layers - the mean is exact, the state totals move by the two-dimensional Buchstab factor e^(2 gamma)/4 confirmed to three decimals at X = 10^10, and the shape carries a residual that saturates - and shows that the quantity a weighted sieve argument actually evaluates transfers with a relative error of 0.36 per cent, so the computation is not the obstruction by a wide margin. Section 7.7 identifies the correlation series as a Hardy-Littlewood quadruple normalised by the square of the twin constant, and measures the order of its sum as quadratic in the logarithm, which turns the observed sub-Poisson dispersion from a number into a consequence. Section 7.8 records what the exception budget of Paper IV means: the local route is closed by proof, and the whole remaining difficulty is a lower bound on the survivor count, exceeded by a factor of six thousand in measurement and still unproved. Section 6.7 puts the same question to the line geometry rather than to the sieve, in one explicit window, and follows five natural routes to the point where each stops: prime gaps carry no bias across twenty-nine gap classes, the capacity of the lines above the cut equals the output instead of bounding it, the two members of a cell are independent to three parts in a thousand, the two small factors of a doubly-composite cell are independent, and the exact Bezout relation every such cell carries is local - nothing telescopes to the ends of the window. The same measurement supplies a number stated only qualitatively elsewhere: the region in which the sieve is vacuous holds 59.4 per cent of the composite endpoints. A claim withdrawn during the work is recorded in place rather than quietly replaced, and a null that was got wrong twice before it was got right is recorded with it.",
    ),
]


def page(p):
    slug, title, sub = p["slug"], p["title"], p["sub"]
    e = html.escape
    extra = ""
    if p.get("pre"):
        extra = (f' &middot; <a href="{p["pre"]}">standalone LaTeX preprint (PDF)</a>')
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="citation_title" content="{e(title)}">
<meta name="citation_author" content="Osman, Mohamed">
<meta name="citation_author_orcid" content="{ORCID}">
<meta name="citation_publication_date" content="{DATE.replace('-', '/')}">
<meta name="citation_online_date" content="{DATE.replace('-', '/')}">
<meta name="citation_technical_report_institution" content="The Cell System (independent)">
<meta name="citation_pdf_url" content="{SITE}/papers/{slug}.pdf">
<meta name="citation_abstract_html_url" content="{SITE}/papers/{slug}.html">
<meta name="citation_language" content="en">
<meta name="description" content="{e(p['abs'][:290])}">
{CSS}</head><body>
<p class="meta"><a href="../index.html">&larr; The Cell System</a></p>
<h1>{e(title)}</h1><h2>{e(sub)}</h2>
<p class="meta">Mohamed Osman &middot; ORCID <a href="https://orcid.org/{ORCID}">{ORCID}</a> &middot; independent researcher &middot; {DATE}</p>
<p><a href="{slug}.pdf"><strong>Download the PDF</strong></a> &middot;
<a href="{REPO}/blob/main/papers/{slug}.md">source on GitHub</a> &middot;
<a href="https://doi.org/{DOI}">concept DOI</a>{extra}</p>
<div class="abs"><strong>Abstract.</strong> {e(p['abs'])}</div>
<p class="meta">No progress toward the twin-prime conjecture is claimed, and no new bound. Priority is
not claimed for any result. Every number printed is regenerated by a script in <code>code/</code> of the
repository. Licence: CC BY 4.0 (text), MIT (code).</p>
</body></html>
"""


def index():
    e = html.escape
    items = "".join(
        f'<li><span class="t"><a href="papers/{p["slug"]}.html">{e(p["title"])}</a></span><br>'
        f'<span class="s">{e(p["sub"])}</span><br>'
        f'<span class="tag">{DATE} &middot; <a href="papers/{p["slug"]}.pdf">PDF</a></span></li>'
        for p in PAPERS
    )
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Cell System &mdash; Mohamed Osman</title>
<meta name="description" content="A coordinate system for the odd sieve: what it proves, what it measures, and where it stops. Seven documents, six verification scripts. No twin-prime claim.">
{CSS}</head><body>
<h1>The Cell System</h1>
<h2>A coordinate system for the odd sieve &mdash; what it proves, what it measures, and where it stops</h2>
<p class="meta">Mohamed Osman &middot; ORCID <a href="https://orcid.org/{ORCID}">{ORCID}</a> &middot; independent researcher</p>
<p>Papers I&ndash;IV build a construction and prove what it decides. Paper V derives the point at which
it stops <em>from inside the construction</em> rather than quoting it, and measures how much of the
difficulty the framework can localise before failing to cross it.
<strong>Every headline result reached here already exists in the literature</strong>, and each paper names
the source. <strong>No progress toward the twin-prime conjecture is claimed, and no new bound.</strong>
Priority is not claimed for any result.</p>
<p>What the collection offers instead: a construction that produces Buchstab's identity, the
Hardy&ndash;Littlewood singular series and the sifting limit without importing them and then stops
exactly where the field stops; negative results and withdrawn claims kept rather than deleted; and a
script in <code>code/</code> that regenerates every number printed.</p>
<p><a href="{REPO}">Repository</a> &middot;
<a href="https://doi.org/{DOI}">DOI {DOI}</a> &middot;
<a href="https://osman209.github.io/prime-number-studies/">Prime Number Studies (the author's other work)</a></p>
<h3>Papers</h3><ul>{items}</ul>
<p class="meta">Text CC BY 4.0 &middot; code MIT</p>
</body></html>
"""


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    docs = os.path.join(root, "docs")
    os.makedirs(os.path.join(docs, "papers"), exist_ok=True)
    for p in PAPERS:
        src = os.path.join(root, "papers", p["slug"] + ".pdf")
        if os.path.exists(src):
            shutil.copy(src, os.path.join(docs, "papers", p["slug"] + ".pdf"))
        with open(os.path.join(docs, "papers", p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(page(p))
        print("docs/papers/" + p["slug"] + ".html")
    pre = os.path.join(root, "papers", "quadratic_staircase.pdf")
    if os.path.exists(pre):
        shutil.copy(pre, os.path.join(docs, "papers", "quadratic_staircase.pdf"))
    with open(os.path.join(docs, "index.html"), "w", encoding="utf-8") as f:
        f.write(index())
    print("docs/index.html")
