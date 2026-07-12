#!/usr/bin/env python3
"""Build ebooků celé ságy z Markdownu.

Každá kniha (00-predmluva … 09-penezenky) → jeden EPUB, a z něj MOBI a AZW3.
EPUB dělá pandoc (md → epub3, kapitola = H1). MOBI/AZW3 dělá calibre `ebook-convert`.

Použití:
    python3 scripts/build_ebooks.py                 # vše, všechny formáty
    python3 scripts/build_ebooks.py --formats epub  # jen EPUB (nepotřebuje calibre)
    python3 scripts/build_ebooks.py --book 1        # jen jednu knihu

Výstup jde do export/<formát>/ (adresář je v .gitignore).
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNIHY = ROOT / "knihy"
EXPORT = ROOT / "export"
COVERS = EXPORT / "covers"

SAGA = "Smazaná odpověď"
AUTHOR = "(bez adresy)"  # kánon: jméno = adresa = rozsudek → autor nemá adresu
LANG = "cs"

OMNIBUS_TITLE = "Smazaná odpověď — kompletní sága"
OMNIBUS_SLUG = "KOMPLETNI-SAGA"
OMNIBUS_DESC = "Všech pět dílů v jednom svazku: Vesnice, Trasy, Etalon, Archiv, Kopie 00."
# Názvy dílů jako H1 předěly v omnibusu (kapitoly se posunou na H2).
OMNIBUS_PARTS = [
    ("kniha-1-vesnice", "Kniha první — Vesnice"),
    ("kniha-2-trasy", "Kniha druhá — Trasy"),
    ("kniha-3-etalon", "Kniha třetí — Etalon"),
    ("kniha-4-archiv", "Kniha čtvrtá — Archiv"),
    ("kniha-5-kopie-00", "Kniha pátá — Kopie 00"),
]

# (adresář, podtitul dílu, slug do názvu souboru, index série, logline)
BOOKS = [
    ("kniha-1-vesnice", "Kniha první: Vesnice", "1-Vesnice", 1,
     "Co je to za stroj? → Čí je ten stroj? Šifra: morse a falešný klíč."),
    ("kniha-2-trasy", "Kniha druhá: Trasy", "2-Trasy", 2,
     "Kdo je to dítě? → Co to dítě nese? Šifra: glyfy."),
    ("kniha-3-etalon", "Kniha třetí: Etalon", "3-Etalon", 3,
     "Proč Odpověď chybí? → Kdo ji doplní? Šifra: obraz-prompt."),
    ("kniha-4-archiv", "Kniha čtvrtá: Archiv", "4-Archiv", 4,
     "Co se stalo v 00? → Co se stane v 00? Šifra: cross-book."),
    ("kniha-5-kopie-00", "Kniha pátá: Kopie 00", "5-Kopie-00", 5,
     "Co je Odpověď? → Vykonej ji. Šifra: sjednocení."),
]

# Lehké EPUB CSS: ASCII-art QR boxy a morse tabulka se nesmí zalamovat.
EPUB_CSS = """\
pre, code { font-family: "Courier New", monospace; }
pre {
  font-size: 0.68em;
  line-height: 1.15;
  white-space: pre;
  overflow-x: auto;
  page-break-inside: avoid;
}
h1 { page-break-before: always; text-align: center; margin-top: 20%; }
table { margin: 1em auto; border-collapse: collapse; }
td { padding: 0.1em 0.6em; }
em { color: #444; }
"""


def sh(cmd: list[str]) -> None:
    print("  $", " ".join(cmd))
    subprocess.run(cmd, check=True)


def parts(book_dir: Path) -> list[Path]:
    """Části knihy v pořadí 00…09 (bez README)."""
    return sorted(p for p in book_dir.glob("[0-9][0-9]-*.md"))


def merge_markdown(book_dir: Path) -> str:
    chunks = []
    for part in parts(book_dir):
        chunks.append(part.read_text(encoding="utf-8").rstrip())
    return "\n\n\n".join(chunks) + "\n"


def shift_h1_to_h2(md: str) -> str:
    """Posune H1 → H2 (mimo code fence), aby v omnibusu byl díl H1 a kapitoly H2."""
    out, fence = [], False
    for line in md.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
        elif not fence and line.startswith("# "):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def merge_omnibus() -> str:
    """Všech pět knih do jednoho markdownu: díl = H1, jeho části = H2."""
    blocks = []
    for slug_dir, part_title in OMNIBUS_PARTS:
        body = shift_h1_to_h2(merge_markdown(KNIHY / slug_dir))
        blocks.append(f"# {part_title}\n\n{body}")
    return "\n\n\n".join(blocks) + "\n"


def cover_for(fslug: str) -> Path:
    return COVERS / f"Smazana-odpoved-Kniha-{fslug}.png"


def ensure_covers(needed: list[Path]) -> None:
    """Když nějaká obálka chybí, dogeneruj je (scripts/make_covers.py)."""
    if all(p.exists() for p in needed):
        return
    print("… obálky chybí, generuji (make_covers.py)")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "make_covers.py")], check=True)


def _pandoc_epub(body: str, out: Path, title: str, description: str,
                 cover: Path | None, toc_depth: int, extra_meta: list[str]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        md = tmp / "book.md"
        md.write_text(body, encoding="utf-8")
        css = tmp / "epub.css"
        css.write_text(EPUB_CSS, encoding="utf-8")
        out.parent.mkdir(parents=True, exist_ok=True)
        cmd = [
            "pandoc", str(md),
            "-f", "markdown+smart",
            "-o", str(out),
            "--toc", f"--toc-depth={toc_depth}",
            "--split-level=1",
            "--css", str(css),
            "--metadata", f"title={title}",
            "--metadata", f"author={AUTHOR}",
            "--metadata", f"lang={LANG}",
            "--metadata", f"description={description}",
        ]
        if cover is not None and cover.exists():
            cmd += ["--epub-cover-image", str(cover)]
        cmd += extra_meta
        sh(cmd)


def build_epub(book_dir: Path, title: str, index: int, logline: str,
               cover: Path | None, out: Path) -> None:
    _pandoc_epub(
        merge_markdown(book_dir), out, f"{SAGA} — {title}", logline, cover,
        toc_depth=1,
        extra_meta=["--metadata", f"belongs-to-collection={SAGA}",
                    "--metadata", f"group-position={index}"],
    )


def build_omnibus_epub(cover: Path | None, out: Path) -> None:
    _pandoc_epub(merge_omnibus(), out, OMNIBUS_TITLE, OMNIBUS_DESC, cover,
                 toc_depth=2, extra_meta=[])


def convert(src_epub: Path, dst: Path, title: str, cover: Path | None,
            index: int | None) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ebook-convert", str(src_epub), str(dst),
        "--authors", AUTHOR,
        "--title", title,
        "--language", LANG,
        "--book-producer", "pandoc + calibre",
    ]
    if index is not None:
        cmd += ["--series", SAGA, "--series-index", str(index)]
    if cover is not None and cover.exists():
        cmd += ["--cover", str(cover)]
    sh(cmd)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--formats", default="epub,mobi,azw3",
                    help="čárkou oddělené: epub,mobi,azw3 (default vše)")
    ap.add_argument("--book", type=int, choices=range(1, 6),
                    help="jen jednu knihu 1–5 (default všechny)")
    ap.add_argument("--clean", action="store_true", help="smaž export/ před buildem")
    ap.add_argument("--no-omnibus", action="store_true",
                    help="nestav souborný svazek celé ságy")
    ap.add_argument("--no-covers", action="store_true", help="ebooky bez obálek")
    args = ap.parse_args()

    formats = [f.strip() for f in args.formats.split(",") if f.strip()]
    need_calibre = any(f in ("mobi", "azw3") for f in formats)

    if shutil.which("pandoc") is None:
        sys.exit("CHYBA: pandoc není nainstalován (brew install pandoc).")
    if need_calibre and shutil.which("ebook-convert") is None:
        sys.exit("CHYBA: calibre/ebook-convert není (brew install --cask calibre).")

    if args.clean and EXPORT.exists():
        shutil.rmtree(EXPORT)

    books = BOOKS if args.book is None else [BOOKS[args.book - 1]]
    do_omnibus = args.book is None and not args.no_omnibus
    made: list[Path] = []

    if not args.no_covers:
        needed = [cover_for(b[2]) for b in books]
        if do_omnibus:
            needed.append(COVERS / f"Smazana-odpoved-{OMNIBUS_SLUG}.png")
        ensure_covers(needed)

    def cover(fslug: str) -> Path | None:
        return None if args.no_covers else cover_for(fslug)

    for slug_dir, title, fslug, index, logline in books:
        book_dir = KNIHY / slug_dir
        if not book_dir.is_dir():
            print(f"! přeskakuji {slug_dir} (adresář chybí)")
            continue
        print(f"\n=== {title} ===")
        base = f"Smazana-odpoved-Kniha-{fslug}"
        epub = EXPORT / "epub" / f"{base}.epub"
        cvr = cover(fslug)

        # EPUB je vždy potřeba jako zdroj pro MOBI/AZW3.
        build_epub(book_dir, title, index, logline, cvr, epub)
        if "epub" in formats:
            made.append(epub)

        full_title = f"{SAGA} — {title}"
        if "mobi" in formats:
            mobi = EXPORT / "mobi" / f"{base}.mobi"
            convert(epub, mobi, full_title, cvr, index)
            made.append(mobi)
        if "azw3" in formats:
            azw3 = EXPORT / "azw3" / f"{base}.azw3"
            convert(epub, azw3, full_title, cvr, index)
            made.append(azw3)

        # Pokud EPUB nebyl vyžádán, byl jen mezikrokem — ukliď ho.
        if "epub" not in formats and epub.exists():
            epub.unlink()

    if do_omnibus:
        print(f"\n=== {OMNIBUS_TITLE} ===")
        base = f"Smazana-odpoved-{OMNIBUS_SLUG}"
        epub = EXPORT / "epub" / f"{base}.epub"
        cvr = None if args.no_covers else COVERS / f"{base}.png"
        build_omnibus_epub(cvr, epub)
        if "epub" in formats:
            made.append(epub)
        if "mobi" in formats:
            mobi = EXPORT / "mobi" / f"{base}.mobi"
            convert(epub, mobi, OMNIBUS_TITLE, cvr, None)
            made.append(mobi)
        if "azw3" in formats:
            azw3 = EXPORT / "azw3" / f"{base}.azw3"
            convert(epub, azw3, OMNIBUS_TITLE, cvr, None)
            made.append(azw3)
        if "epub" not in formats and epub.exists():
            epub.unlink()

    print(f"\n✅ Hotovo — {len(made)} souborů:")
    for p in made:
        size = p.stat().st_size // 1024
        print(f"   {p.relative_to(ROOT)}  ({size} kB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
