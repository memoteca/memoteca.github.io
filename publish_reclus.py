#!/usr/bin/env python3
"""Copy the Reclus texts from the workshop (../reclus) into this site.

Each tramo becomes docs/reclus/<slug>/*.md with Jekyll front matter, its figures
go to assets/images/reclus/<slug>/ and the image links are rewritten to point
there. Relative links between pages get their .md extension turned into .html.
The workshop keeps the sources; run this again after editing them, then commit.
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKSHOP = ROOT.parent / "reclus"
DOCS = ROOT / "docs" / "reclus"
IMAGES = ROOT / "assets" / "images" / "reclus"
CREDIT = ("\n\n---\n\n*Mapas y láminas: Source gallica.bnf.fr / "
          "Bibliothèque nationale de France.*\n")

# slug: (source dir, markdown glob, image dir to publish, prefix used in the text)
TRAMOS = {
    "asia":            ("vol6_cap1",       "*.md",                   "images-blanco",  "images/"),
    "siberia":         ("vol6_siberie",    "*.md",                   "images-blanco",  "images-blanco/"),
    "amur":            ("vol6_amour",      "*.md",                   "images-blanco",  "images/"),
    "rumania":         ("vol1_roumanie",   "roumanie-*.md",          "figuras",        "figuras/"),
    "rumania_actual":  ("rumania_actual",  "rumania-actual-*.md",    "figuras",        "figuras/"),
    "tierra_del_fuego": ("tierra_del_fuego", "tierra-del-fuego-*.md", "figuras",       "figuras/"),
    "sahara":          ("Digitalización",  "sahara-occidental-*.md", "images-blanco",  "images/"),
    "castillas":       ("vol1_castillas",  "cap10-sec2-castillas-es.md", "figuras/blanco", "figuras/blanco/"),
    "novisima":        ("novisima-md",     "siberia.md",             None,             None),
}

H1 = re.compile(r"^# (.+)$", re.M)
MD_LINK = re.compile(r"\]\((?!https?://|/|#)([^)\s]+)\.md(#[^)]*)?\)")


def title_of(text: str) -> str:
    m = H1.search(text)
    t = m.group(1) if m else "Reclus"
    t = re.sub(r"[*_`]", "", t).replace('"', '\\"')
    return t


def publish(slug: str) -> int:
    src_dir, glob, img_dir, prefix = TRAMOS[slug]
    out = DOCS / slug
    out.mkdir(parents=True, exist_ok=True)
    if img_dir:
        dst = IMAGES / slug
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(WORKSHOP / src_dir / img_dir, dst)
    n = 0
    for src in sorted((WORKSHOP / src_dir).glob(glob)):
        text = src.read_text(encoding="utf-8")
        has_figures = False
        if prefix:
            has_figures = f"]({prefix}" in text
            text = text.replace(f"]({prefix}", "]({{ site.baseurl }}/assets/images/reclus/" + slug + "/")
        text = MD_LINK.sub(lambda m: f"]({m.group(1)}.html{m.group(2) or ''})", text)
        front = f'---\nlayout: default\ntitle: "{title_of(text)}"\n---\n\n'
        if has_figures:
            text = text.rstrip("\n") + CREDIT
        (out / src.name).write_text(front + text, encoding="utf-8")
        n += 1
    return n


def main() -> int:
    total = 0
    for slug in TRAMOS:
        n = publish(slug)
        print(f"publish_reclus: {slug}: {n} pages")
        total += n
    print(f"publish_reclus: {total} pages -> docs/reclus/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
