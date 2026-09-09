#!/usr/bin/env python3
"""
set_doi.py — write one DOI into every file that carries it.

The DOI appears in seven independent places: the README badge, the README
citation block, CITATION.cff, the suggested attribution in LICENSE-CONTENT, the
DOI constant in build_site.py, and — through that constant — the landing page and
the twelve paper pages under docs/.  Editing
them by hand has gone wrong before, so this does all of them at once and then
tells you to rebuild the site.

    python3 code/set_doi.py 10.5281/zenodo.NNNNNNNN
    python3 code/build_site.py

Zenodo will reserve a DOI for you before you publish — the "Reserve DOI" button
on the upload form — so the number can be written into the files that go INSIDE
the archive, which is the only way the deposited copy can carry its own DOI.

Until a real DOI is set, the placeholder below is in place and audit.py fails on
it, so a release cannot be cut with a dead link.
"""
import os, re, sys

PLACEHOLDER = "10.5281/zenodo.RESERVED"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAT = re.compile(r"10\.5281/zenodo\.(?:\d+|RESERVED)")

TARGETS = ["README.md", "CITATION.cff", "LICENSE-CONTENT",
           os.path.join("code", "build_site.py")]

def current():
    s = open(os.path.join(ROOT, "CITATION.cff"), encoding="utf-8").read()
    m = PAT.search(s)
    return m.group(0) if m else None

def main():
    if len(sys.argv) != 2:
        print(__doc__)
        print("current DOI in the files:", current())
        sys.exit(2)
    new = sys.argv[1].strip().replace("https://doi.org/", "")
    if not re.fullmatch(r"10\.5281/zenodo\.\d+", new):
        print("that does not look like a Zenodo DOI:", new); sys.exit(2)
    old = current()
    n = 0
    for rel in TARGETS:
        p = os.path.join(ROOT, rel)
        s = open(p, encoding="utf-8").read()
        # the prime-number-studies DOI belongs to the other repository; leave it
        keep = "10.5281/zenodo.21638887"
        parts = s.split(keep)
        parts = [PAT.sub(new, x) for x in parts]
        s2 = keep.join(parts)
        if s2 != s:
            open(p, "w", encoding="utf-8").write(s2); n += 1
            print("  written:", rel)
    print(f"\n{old} -> {new} in {n} file(s).")
    print("Now run:  python3 code/build_site.py     (docs/ carries the DOI too)")
    print("Then:     python3 audit.py")

if __name__ == "__main__":
    main()
