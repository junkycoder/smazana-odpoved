#!/usr/bin/env python3
"""Generátor obálek ságy — SVG → PNG (přes rsvg-convert).

Jedna série, jeden layout, akcent per díl. Motiv: „smazaná odpověď" —
kolem názvu dílu jsou začerněné (redigované) řádky; název je to jediné,
co zůstalo čitelné. Dole morse zakódovaný z názvu dílu (ladí se šiframi).

Použití:
    python3 scripts/make_covers.py            # 5 dílů + omnibus → export/covers/*.png
    python3 scripts/make_covers.py --show 1    # jen vypíše cestu k jedné

Rozměr 1600×2560 = poměr 1:1.6 (doporučení Kindle / KDP).
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COVERS = ROOT / "export" / "covers"

W, H = 1600, 2560
PAPER = "#efe9db"          # světlá pro text
INK = "#0d0d11"            # pozadí
MUTED = "#8b8b99"
FAINT = "#5a5a66"
REDACT = "#24242e"         # začerněný řádek na tmavém pozadí

MORSE = {
    "A": "·−", "B": "−···", "C": "−·−·", "D": "−··", "E": "·", "F": "··−·",
    "G": "−−·", "H": "····", "I": "··", "J": "·−−−", "K": "−·−", "L": "·−··",
    "M": "−−", "N": "−·", "O": "−−−", "P": "·−−·", "Q": "−−·−", "R": "·−·",
    "S": "···", "T": "−", "U": "··−", "V": "···−", "W": "·−−", "X": "−··−",
    "Y": "−·−−", "Z": "−−··", "0": "−−−−−",
}

# (číslo, řím., ASCII do souboru, název, akcent, šifra, pořadí, morse-zdroj)
BOOKS = [
    (1, "I", "1-Vesnice", "VESNICE", "#c9a24b",
     "Morse + falešný klíč", "PRVNÍ ZE PĚTI", "VESNICE"),
    (2, "II", "2-Trasy", "TRASY", "#5b9bd5",
     "Glyfy", "DRUHÁ ZE PĚTI", "TRASY"),
    (3, "III", "3-Etalon", "ETALON", "#d0605f",
     "Obraz-prompt", "TŘETÍ ZE PĚTI", "ETALON"),
    (4, "IV", "4-Archiv", "ARCHIV", "#5cbf8a",
     "Cross-book", "ČTVRTÁ ZE PĚTI", "ARCHIV"),
    (5, "V", "5-Kopie-00", "KOPIE 00", "#ced2dc",
     "Sjednocení", "PÁTÁ ZE PĚTI", "KOPIE 00"),
]


def morse_line(text: str) -> str:
    out = []
    for ch in text.upper():
        if ch == " ":
            out.append("  ")
        elif ch in MORSE:
            out.append(MORSE[ch])
    return "   ".join(out)


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def title_size(name: str) -> int:
    n = len(name)
    if n <= 5:
        return 250
    if n <= 6:
        return 220
    if n <= 7:
        return 195
    return 150  # "KOPIE 00"


def spaced(s: str, gap: str = " ") -> str:
    return gap.join(list(s))


def redacted_rows(cx: int, rows: list[tuple[int, int]]) -> str:
    """Začerněné 'řádky textu' — (y, šířka); evokují smazaný okolní text."""
    out = []
    for y, w in rows:
        x = cx - w // 2
        out.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="4" fill="{REDACT}"/>'
        )
    return "\n  ".join(out)


def build_svg(rom: str, name: str, accent: str, cipher: str,
              order: str, morse_src: str) -> str:
    cx = W // 2
    ts = title_size(name)
    morse = esc(morse_line(morse_src))
    ghost = rom  # velký vodoznak čísla za názvem
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="vig" cx="50%" cy="42%" r="75%">
      <stop offset="0%" stop-color="#15151b"/>
      <stop offset="60%" stop-color="{INK}"/>
      <stop offset="100%" stop-color="#050507"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="{INK}"/>
  <rect width="{W}" height="{H}" fill="url(#vig)"/>
  <rect x="70" y="70" width="{W-140}" height="{H-140}" fill="none"
        stroke="{accent}" stroke-opacity="0.55" stroke-width="3"/>
  <rect x="88" y="88" width="{W-176}" height="{H-176}" fill="none"
        stroke="{accent}" stroke-opacity="0.18" stroke-width="1.5"/>

  <!-- Horní blok: série -->
  <text x="{cx}" y="300" text-anchor="middle" font-family="Georgia, serif"
        font-size="46" letter-spacing="2" fill="{PAPER}">{spaced("SMAZANÁ")}</text>
  <text x="{cx}" y="372" text-anchor="middle" font-family="Georgia, serif"
        font-size="46" letter-spacing="2" fill="{PAPER}">{spaced("ODPOVĚĎ")}</text>
  <line x1="{cx-120}" y1="430" x2="{cx+120}" y2="430" stroke="{accent}" stroke-width="2"/>
  <text x="{cx}" y="500" text-anchor="middle" font-family="'Courier New', monospace"
        font-size="30" letter-spacing="6" fill="{MUTED}">{esc(order)}</text>

  <!-- Hero: vodoznak čísla + název, kolem něj smazané řádky -->
  <text x="{cx}" y="1330" text-anchor="middle" font-family="Georgia, serif"
        font-size="820" font-weight="bold" fill="{accent}" fill-opacity="0.06">{ghost}</text>

  <text x="{cx}" y="1075" text-anchor="middle" font-family="'Courier New', monospace"
        font-size="34" letter-spacing="8" fill="{accent}" fill-opacity="0.9">SVAZEK {rom}</text>
  {redacted_rows(cx, [(1120, 760), (1168, 1000)])}

  <text x="{cx}" y="1440" text-anchor="middle" font-family="Georgia, serif"
        font-size="{ts}" font-weight="bold" letter-spacing="6" fill="{PAPER}">{esc(name)}</text>
  <line x1="{cx - min(1120, int(ts*len(name)*0.60))//2}" y1="1505"
        x2="{cx + min(1120, int(ts*len(name)*0.60))//2}" y2="1505"
        stroke="{accent}" stroke-width="6"/>

  {redacted_rows(cx, [(1570, 940), (1618, 640), (1666, 840)])}

  <!-- Šifra -->
  <text x="{cx}" y="1830" text-anchor="middle" font-family="Georgia, serif"
        font-size="42" font-style="italic" fill="{MUTED}">Šifra: {esc(cipher)}</text>

  <!-- Morse zakódovaný z názvu -->
  <text x="{cx}" y="2010" text-anchor="middle" font-family="'Courier New', monospace"
        font-size="40" fill="{FAINT}">{morse}</text>

  <!-- Pata -->
  <text x="{cx}" y="2230" text-anchor="middle" font-family="Georgia, serif"
        font-size="60" font-style="italic" fill="{accent}">Nenech to ležet.</text>
  <line x1="{cx-260}" y1="2300" x2="{cx+260}" y2="2300" stroke="{FAINT}" stroke-width="1"/>
  <text x="{cx}" y="2370" text-anchor="middle" font-family="'Courier New', monospace"
        font-size="30" letter-spacing="4" fill="{MUTED}">zdarma · kopíruj · šiř dál</text>
  <text x="{cx}" y="2425" text-anchor="middle" font-family="Georgia, serif"
        font-size="30" font-style="italic" fill="{FAINT}">vypráví robot Cvok</text>
</svg>'''


def build_omnibus_svg() -> str:
    cx = W // 2
    accents = [b[4] for b in BOOKS]
    dots = ""
    n = len(accents)
    span = 560
    step = span // (n - 1)
    x0 = cx - span // 2
    for i, col in enumerate(accents):
        dots += (f'<circle cx="{x0 + i*step}" cy="1500" r="26" fill="{col}"/>\n  '
                 f'<text x="{x0 + i*step}" y="1600" text-anchor="middle" '
                 f'font-family="Georgia, serif" font-size="34" fill="{MUTED}">'
                 f'{["I","II","III","IV","V"][i]}</text>\n  ')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="vig" cx="50%" cy="42%" r="75%">
      <stop offset="0%" stop-color="#15151b"/>
      <stop offset="60%" stop-color="{INK}"/>
      <stop offset="100%" stop-color="#050507"/>
    </radialGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      {"".join(f'<stop offset="{int(i/(n-1)*100)}%" stop-color="{c}"/>' for i,c in enumerate(accents))}
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="{INK}"/>
  <rect width="{W}" height="{H}" fill="url(#vig)"/>
  <rect x="70" y="70" width="{W-140}" height="{H-140}" fill="none"
        stroke="url(#rule)" stroke-opacity="0.6" stroke-width="3"/>

  <text x="{cx}" y="560" text-anchor="middle" font-family="Georgia, serif"
        font-size="150" font-weight="bold" letter-spacing="6" fill="{PAPER}">SMAZANÁ</text>
  <text x="{cx}" y="720" text-anchor="middle" font-family="Georgia, serif"
        font-size="150" font-weight="bold" letter-spacing="6" fill="{PAPER}">ODPOVĚĎ</text>
  <rect x="{cx-300}" y="800" width="600" height="6" fill="url(#rule)"/>

  <text x="{cx}" y="1050" text-anchor="middle" font-family="'Courier New', monospace"
        font-size="40" letter-spacing="10" fill="{MUTED}">KOMPLETNÍ SÁGA</text>
  <text x="{cx}" y="1200" text-anchor="middle" font-family="Georgia, serif"
        font-size="54" font-style="italic" fill="{PAPER}">všech pět dílů v jednom svazku</text>

  {dots}

  <text x="{cx}" y="1850" text-anchor="middle" font-family="Georgia, serif"
        font-size="44" font-style="italic" fill="{MUTED}">Vesnice · Trasy · Etalon · Archiv · Kopie 00</text>

  <text x="{cx}" y="2230" text-anchor="middle" font-family="Georgia, serif"
        font-size="64" font-style="italic" fill="{PAPER}">Nenech to ležet.</text>
  <line x1="{cx-260}" y1="2300" x2="{cx+260}" y2="2300" stroke="{FAINT}" stroke-width="1"/>
  <text x="{cx}" y="2370" text-anchor="middle" font-family="'Courier New', monospace"
        font-size="30" letter-spacing="4" fill="{MUTED}">zdarma · kopíruj · šiř dál</text>
  <text x="{cx}" y="2425" text-anchor="middle" font-family="Georgia, serif"
        font-size="30" font-style="italic" fill="{FAINT}">vypráví robot Cvok</text>
</svg>'''


def render(svg: str, out_png: Path) -> None:
    out_png.parent.mkdir(parents=True, exist_ok=True)
    svg_path = out_png.with_suffix(".svg")
    svg_path.write_text(svg, encoding="utf-8")
    subprocess.run(
        ["rsvg-convert", "-w", str(W), "-h", str(H), str(svg_path), "-o", str(out_png)],
        check=True,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--keep-svg", action="store_true", help="ponech i .svg zdroje")
    args = ap.parse_args()

    if not __import__("shutil").which("rsvg-convert"):
        sys.exit("CHYBA: rsvg-convert není (brew install librsvg).")

    made = []
    for num, rom, fslug, name, accent, cipher, order, msrc in BOOKS:
        out = COVERS / f"Smazana-odpoved-Kniha-{fslug}.png"
        render(build_svg(rom, name, accent, cipher, order, msrc), out)
        made.append(out)

    omni = COVERS / "Smazana-odpoved-KOMPLETNI-SAGA.png"
    render(build_omnibus_svg(), omni)
    made.append(omni)

    if not args.keep_svg:
        for p in COVERS.glob("*.svg"):
            p.unlink()

    print(f"✅ {len(made)} obálek → {COVERS.relative_to(ROOT)}/")
    for p in made:
        print(f"   {p.name}  ({p.stat().st_size // 1024} kB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
