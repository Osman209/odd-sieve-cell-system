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
DOI = "10.5281/zenodo.22661626"
DATE = "2026-09-11"

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
        abs="A single pass over the twelve papers. The coordinates; the exact window histogram; "
            "the exact transport of a census over a sieve cycle; what survives the move to a short "
            "interval; what the framework decides outright; where it stops, stated from inside the "
            "construction rather than quoted; the pattern the work keeps arriving at; and what an "
            "external ingredient would have to supply. No progress toward the twin-prime conjecture "
            "is claimed, and no new bound.",
    ),
    dict(
        slug="paper_01_quadratic_staircase",
        title="Paper 1. An Exact Histogram for a Quadratic Staircase",
        sub="The increments of floor(2j^2/n), and the local maxima of 2j^2 mod n",
        abs="An exact histogram for the increments of a quadratic staircase, and the local maxima of 2j^2 mod n, proved rather than observed.",
    ),
    dict(
        slug="paper_02_cells_and_lines",
        title="Paper 2. Cells and Lines",
        sub="A coordinate system for the odd sieve",
        abs="The odd numbers coprime to 6 are read as cells and the primes as lines striking them, which turns the sieve into a discrete geometry with exact laws.",
    ),
    dict(
        slug="paper_03_inheritance_law_on_the_cycle",
        title="Paper 3. The Inheritance Law on the Cycle",
        sub="Exact transport of the divisor census, and of weights, over a sieve cycle",
        abs="Adding a line q multiplies the cycle by q and the census transports with no error at all; a finite-state refinement evaluates any weight depending on the number of lines met.",
    ),
    dict(
        slug="paper_04_from_cycle_to_window",
        title="Paper 4. From Cycle to Window",
        sub="What survives when an exact periodic law is evaluated on a short interval",
        abs="An exact law on a sieve cycle is not an exact law on a window, and the loss is not uniform: soft weights transfer almost exactly, sharp indicators do not.",
    ),
    dict(
        slug="paper_05_gap_alphabet",
        title="Paper 5. The Gap Alphabet",
        sub="Which gaps can occur between consecutive odd composites, and where the ladder of proofs stops",
        abs="The gap between consecutive odd composites takes only the values 2, 4 and 6, and a gap of 6 is a twin pair; everything settleable without prime input is settled here.",
    ),
    dict(
        slug="paper_06_twin_criterion",
        title="Paper 6. The Twin Criterion: Six Exception Positions",
        sub="A single open cell in a sector is a twin pair unless it sits at one of six named places",
        abs="After switching on every line up to M in the sector between M^2 and (M+6)^2, at most six cells can be open without being a twin, and their positions are explicit quadratics in M.",
    ),
    dict(
        slug="paper_07_clocks_and_inheritance",
        title="Paper 7. Clocks and Inheritance",
        sub="Primality as a zero-test, and the capacity of a single line across sectors",
        abs="The same window in two further units: a clock in which primality is the statement that no clock reads zero, and an inheritance law that transports exactly from sector to sector.",
    ),
    dict(
        slug="paper_08_belts_and_short_windows",
        title="Paper 8. Belts and Short Windows",
        sub="What a line can do between its own square and the next, and the anatomy of the window between consecutive squares",
        abs="The belt between consecutive prime squares has an exact size and a reach that depends on the gap rather than the size of the line; the short window is then read in depth.",
    ),
    dict(
        slug="paper_09_the_exact_obstruction",
        title="Paper 9. The Exact Form of the Obstruction",
        sub="An identity for the twin count with no error term, and why an ordinary sieve cannot cross it",
        abs="Under a depth cut the twin count satisfies T = C - R + S with no error term, which turns the twin problem into a comparison of two counts and shows the comparison needs a sign, not a bound.",
    ),
    dict(
        slug="paper_10_four_tests",
        title="Paper 10. Four Tests of the Cell System",
        sub="Jacobsthal, almost-primes between squares, shared cofactors, and collisions",
        abs="Four independent tests of the same framework, each carried to the point where it stops, with the reason it stops given in each case.",
    ),
    dict(
        slug="paper_11_what_a_continuation_needs",
        title="Paper 11. What a Continuation Would Have to Supply",
        sub="The external ingredient, the limitations, and the routes already tried",
        abs="What an external ingredient would have to supply for the identity to become a theorem, why the stopping point is the right one, and an appendix of routes already tried, each recorded at the width its own measurement supports.",
    ),
    dict(
        slug="paper_12_paired_almost_primes",
        title="Paper 12. Paired Almost Primes in Square Windows and in Short Intervals",
        sub="A dimension-two sieve on the same window, with certified coefficients, and the exact distance to four factors",
        abs="Every sufficiently large window between consecutive squares carries a pair (a, a+2) with at most five prime factors on each side and at most eight in total; in an interval of length x^theta the same argument gives at most five for theta above 0.38, four above 0.52 and three above 0.78. The four weight coefficients are certified by interval arithmetic. This part uses no object from the cell system.",
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
<meta name="description" content="A coordinate system for the odd sieve: what it proves, what it measures, and where it stops. Twelve papers, one overview and thirty-three verification scripts. No twin-prime claim.">
{CSS}</head><body>
<h1>The Cell System</h1>
<h2>A coordinate system for the odd sieve &mdash; what it proves, what it measures, and where it stops</h2>
<p class="meta">Mohamed Osman &middot; ORCID <a href="https://orcid.org/{ORCID}">{ORCID}</a> &middot; independent researcher</p>
<p>Twelve papers, one overview and thirty-three verification scripts. Papers 1 to 4 build the coordinates
and the transport laws; papers 5 to 8 are the construction and what it decides about twin pairs;
papers 9 to 11 derive the point at which it stops <em>from inside the construction</em> rather than
quoting it, and measure how much of the difficulty the framework can localise before failing to
cross it.
<strong>Every headline result reached here already exists in the literature</strong>, and each paper names
the source. <strong>No progress toward the twin-prime conjecture is claimed, and no new bound.</strong>
Priority is not claimed for any result.</p>
<p>What the collection offers instead: a construction that produces Buchstab's decomposition, the
Hardy&ndash;Littlewood singular series and the exact factor-of-two loss without importing them, and
then stops exactly where the field stops; negative results and withdrawn claims kept rather than deleted; and a
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
