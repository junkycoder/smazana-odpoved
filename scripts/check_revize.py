#!/usr/bin/env python3
"""Small continuity gate for the public-facing revision."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BOOKS = [
    "kniha-1-vesnice",
    "kniha-2-trasy",
    "kniha-3-etalon",
    "kniha-4-archiv",
    "kniha-5-kopie-00",
]


def public_files(book: Path) -> list[Path]:
    return sorted(path for path in book.glob("0[0-8]-*.md") if path.name != "README.md")


def paragraphs(text: str) -> list[str]:
    return [
        re.sub(r"\s+", " ", chunk.strip())
        for chunk in re.split(r"\n\s*\n", text)
        if chunk.strip() and not chunk.lstrip().startswith("#")
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default="revize-v2/knihy")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    failures: list[str] = []
    warnings: list[str] = []
    totals: dict[str, int] = {}

    for name in BOOKS:
        book = root / name
        required = ["README.md", "00-predmluva.md", *[f"0{i}-kapitola.md" for i in range(1, 7)], "07-klic.md", "08-kolik.md", "09-penezenky.md"]
        missing = [filename for filename in required if not (book / filename).exists()]
        if missing:
            failures.append(f"{name}: chybí {', '.join(missing)}")
            continue
        text = "\n".join(path.read_text(encoding="utf-8") for path in public_files(book))
        totals[name] = len(re.findall(r"\w+", text, flags=re.UNICODE))

        lowered = text.casefold()
        if "dávat slovům význam" in lowered:
            failures.append(f"{name}: veřejná próza přímo vyslovuje Odpověď")
        if "bc1q-doplnit" in lowered:
            failures.append(f"{name}: placeholder peněženky pronikl do veřejné vrstvy 00–08")

    all_public = "\n".join(
        path.read_text(encoding="utf-8")
        for name in BOOKS
        for path in public_files(root / name)
    )
    lowered_all = all_public.casefold()
    if "všechna světla světa" in lowered_all:
        failures.append("K5 stále tvrdí globální dosah přes všechna světla světa")

    for name in BOOKS[2:]:
        book_text = "\n".join(path.read_text(encoding="utf-8") for path in public_files(root / name))
        if "214-K-07" not in book_text:
            failures.append(f"{name}: chybí kauzální stopa modulu 214-K-07")

    k2_preface = (root / BOOKS[1] / "00-predmluva.md").read_text(encoding="utf-8").casefold()
    if "mluvil, jak šel" in k2_preface or "šel, když mluvil" in k2_preface:
        failures.append("K2 předmluva stále tvrdí živé nahrávání za chůze")

    k4_text = "\n".join(path.read_text(encoding="utf-8") for path in public_files(root / BOOKS[3])).casefold()
    late_recording_conflicts = [
        "nahrával jsem do bedny všechno od kráteru",
        "jsem mu pak v noci přehrál",
        "nahrával do mě od kráteru",
    ]
    for phrase in late_recording_conflicts:
        if phrase in k4_text:
            failures.append(f"K4 odporuje pozdnímu vzniku ságy: „{phrase}“")

    k1_preface = (root / BOOKS[0] / "00-predmluva.md").read_text(encoding="utf-8")
    k5_final = (root / BOOKS[4] / "06-kapitola.md").read_text(encoding="utf-8")
    anchors = paragraphs(k1_preface)[:3]
    normalized_final = re.sub(r"\s+", " ", k5_final)
    for index, anchor in enumerate(anchors, 1):
        if anchor not in normalized_final:
            failures.append(f"Smyčka K5 → K1 není doslovná v kotevním odstavci {index}")

    dangerous_drop = re.compile(r"\b(lavičk\w*|parapet\w*|za radiátor\w*|najdeš cizí kolík|cizí kolík)\b", re.IGNORECASE)
    for name in BOOKS:
        kolik = (root / name / "08-kolik.md").read_text(encoding="utf-8")
        match = dangerous_drop.search(kolik)
        if match:
            failures.append(f"{name}/08-kolik.md: nebezpečný anonymní USB protokol („{match.group(0)}“)")

    local_lords = len(re.findall(r"pán světa", lowered_all))
    if local_lords:
        warnings.append(f"„pán světa“ zůstává {local_lords}×; ověřit, že jde o ironický lokální titul")

    print("Rozsah veřejné vrstvy 00–08:")
    for name, words in totals.items():
        print(f"  {name}: {words:,} slov".replace(",", " "))

    for warning in warnings:
        print(f"WARN: {warning}")
    for failure in failures:
        print(f"FAIL: {failure}")

    if failures:
        print(f"\nKontrola selhala: {len(failures)} závad.")
        return 1
    print("\nKontrola prošla.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
