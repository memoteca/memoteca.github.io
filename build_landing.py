#!/usr/bin/env python3
"""Assemble index.md (the Memoteca landing page) from landing.md.

landing.md is a Markdown task list: one line per block, in display order.
    - [x] slug — Title      -> landing/slug.md is included
    - [ ] slug — Title      -> block left out
Leading indentation is allowed (purely visual). Only the checkbox and the slug
matter; the title after the dash is a comment. landing/_header.md holds the
front matter and the intro that always open the page.

GitHub Pages cannot run this, so index.md is committed: run it before pushing.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LIST = ROOT / "landing.md"
SECTIONS = ROOT / "landing"
HEADER = SECTIONS / "_header.md"
OUT = ROOT / "index.md"
FOOTER = "\n---\n"
ITEM = re.compile(r"^\s*- \[([ xX])\]\s+([A-Za-z0-9_-]+)")


def main() -> int:
    chosen, listed = [], set()
    for n, line in enumerate(LIST.read_text(encoding="utf-8").splitlines(), 1):
        m = ITEM.match(line)
        if not m:
            continue
        on, slug = m.group(1).lower() == "x", m.group(2)
        if slug in listed:
            sys.exit(f"landing.md:{n}: '{slug}' listed twice")
        listed.add(slug)
        path = SECTIONS / f"{slug}.md"
        if not path.exists():
            sys.exit(f"landing.md:{n}: no file landing/{slug}.md")
        if on:
            chosen.append(path)
    for path in sorted(SECTIONS.glob("*.md")):
        if path.stem not in listed and not path.name.startswith("_"):
            print(f"build_landing: landing/{path.name} is not in landing.md", file=sys.stderr)
    header = HEADER.read_text(encoding="utf-8").rstrip("\n") + "\n"
    body = "\n".join(p.read_text(encoding="utf-8").strip() + "\n" for p in chosen)
    OUT.write_text(header + "\n" + body + FOOTER, encoding="utf-8")
    print(f"build_landing: {len(chosen)} of {len(listed)} blocks -> index.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
