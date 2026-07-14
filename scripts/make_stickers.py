#!/usr/bin/env python3
"""Generátor „lepítek" — sticker odkazů na stažení do headeru README.

Motiv: na obálku ságy se přes knihu nalepí papírová lepítka — jedno na formát
(PDF · EPUB · MOBI · AZW3). Každé lepítko má ikonu (kolečko se šipkou „stáhni")
a je to zároveň klikací odkaz ke stažení.

Vyrobí dvojí sadu:
    export/header/sticker-<fmt>.png   samostatná klikací lepítka (rovná, do řádku)
    export/header/hero-saga.png       obálka ságy s lepítky nalepenými přes knihu

Použití:
    python3 scripts/make_stickers.py

Potřebuje jen Pillow (pip install Pillow).
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
COVERS = ROOT / "export" / "covers"
OUT = ROOT / "export" / "header"

SS = 4  # supersampling — kreslíme velké, pak zmenšíme (hladké hrany)

# --- paleta (sjednotná s obálkami) ---
PAPER = (239, 233, 219)     # #efe9db  tělo lepítka
PAPER_HI = (247, 243, 233)  # světlejší papír / šipka
EDGE = (206, 198, 178)      # #cec6b2  vnitřní linka lepítka
INK = (23, 23, 29)          # #17171d  text
MUTED = (106, 106, 118)     # #6a6a76  podtitulek

# formát -> (akcent, popisek na obálce, podtitulek = kam to je)
FORMATS = {
    "PDF": ((208, 96, 95), "PDF", "počítač · tisk"),
    "EPUB": ((92, 191, 138), "EPUB", "čtečky · telefon"),
    "MOBI": ((201, 162, 75), "MOBI", "Amazon Kindle"),
    "AZW3": ((91, 155, 213), "AZW3", "Kindle (novější)"),
}

FONT_DIR = Path("/usr/share/fonts/truetype")
MONO_BOLD = FONT_DIR / "dejavu" / "DejaVuSansMono-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "liberation" / "LiberationSerif-Italic.ttf"


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def mul(rgb, f: float):
    return tuple(max(0, min(255, int(c * f))) for c in rgb)


def rounded(draw: ImageDraw.ImageDraw, box, r, **kw) -> None:
    draw.rounded_rectangle(box, radius=r, **kw)


def download_glyph(d: ImageDraw.ImageDraw, cx: int, cy: int, r: int, col) -> None:
    """Šipka dolů do „podložky" — univerzální ikona stažení, kreslená ručně."""
    # dřík
    w = int(r * 0.20)
    d.rounded_rectangle(
        [cx - w, cy - int(r * 0.55), cx + w, cy + int(r * 0.10)],
        radius=w, fill=col,
    )
    # hrot (trojúhelník)
    d.polygon(
        [(cx - int(r * 0.42), cy - int(r * 0.02)),
         (cx + int(r * 0.42), cy - int(r * 0.02)),
         (cx, cy + int(r * 0.48))],
        fill=col,
    )
    # podložka (U)
    t = max(2, int(r * 0.13))
    y = cy + int(r * 0.60)
    x0, x1 = cx - int(r * 0.50), cx + int(r * 0.50)
    d.line([(x0, y - int(r * 0.10)), (x0, y), (x1, y), (x1, y - int(r * 0.10))],
           fill=col, width=t, joint="curve")


def make_sticker(fmt: str, angle: float, card_w: int = 380, card_h: int = 118):
    """Jedno lepítko jako RGBA (i se stínem a náklonem)."""
    accent, label, sub = FORMATS[fmt]
    W, H = card_w * SS, card_h * SS
    pad = 34 * SS  # místo na stín + rotaci
    canvas = Image.new("RGBA", (W + 2 * pad, H + 2 * pad), (0, 0, 0, 0))

    # --- stín ---
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    rounded(sd, [pad, pad + 8 * SS, pad + W, pad + H + 8 * SS],
            r=26 * SS, fill=(0, 0, 0, 120))
    shadow = shadow.filter(ImageFilter.GaussianBlur(11 * SS))
    canvas.alpha_composite(shadow)

    # --- tělo lepítka: barevné pozadí (akcent), bez podtržení ---
    card = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    box = [pad, pad, pad + W, pad + H]
    fill = mul(accent, 0.92)        # jemně ztlumeno, ať světlý text drží kontrast
    rounded(cd, box, r=26 * SS, fill=fill + (255,))
    rounded(cd, box, r=26 * SS, outline=mul(accent, 0.70) + (255,), width=2 * SS)
    # jemná světlá „výseková" linka dovnitř — vzhled nalepeného lepítka
    inset = [pad + 3 * SS, pad + 3 * SS, pad + W - 3 * SS, pad + H - 3 * SS]
    rounded(cd, inset, r=23 * SS, outline=(255, 255, 255, 70), width=2 * SS)

    # --- ikona: papírové kolečko se šipkou stažení v akcentu ---
    chip_r = 38 * SS
    chip_cx = pad + 24 * SS + chip_r
    chip_cy = pad + H // 2
    cd.ellipse([chip_cx - chip_r, chip_cy - chip_r, chip_cx + chip_r, chip_cy + chip_r],
               fill=PAPER_HI + (255,))
    download_glyph(cd, chip_cx, chip_cy, chip_r, fill + (255,))

    # --- text (světlý na barevném pozadí) ---
    tx = chip_cx + chip_r + 26 * SS
    f_label = font(MONO_BOLD, 46 * SS)
    f_sub = font(SERIF_ITALIC, 27 * SS)
    cd.text((tx, pad + 28 * SS), label, font=f_label, fill=(250, 247, 240, 255))
    cd.text((tx + 2 * SS, pad + 78 * SS), sub, font=f_sub, fill=(255, 255, 255, 205))

    canvas.alpha_composite(card)
    if angle:
        canvas = canvas.rotate(angle, resample=Image.BICUBIC, expand=True)
    return canvas


def export_buttons() -> list[Path]:
    """Samostatná klikací lepítka do řádku (jemný náklon, ať vypadají nalepeně)."""
    OUT.mkdir(parents=True, exist_ok=True)
    tilt = {"PDF": -2.5, "EPUB": 2.0, "MOBI": -1.8, "AZW3": 2.4}
    made = []
    for fmt in FORMATS:
        img = make_sticker(fmt, tilt[fmt])
        # ořízni průhledný okraj (i se stínem), ať height v README sedí na lepítko
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
        # zmenši na 2× logickou velikost (ostré v README)
        img = img.resize((max(1, img.width // (SS // 2)),
                          max(1, img.height // (SS // 2))), Image.LANCZOS)
        p = OUT / f"sticker-{fmt.lower()}.png"
        img.save(p)
        made.append(p)
    return made


def export_hero() -> Path:
    """Obálka ságy s lepítky nalepenými přes knihu."""
    cover = Image.open(COVERS / "Smazana-odpoved-KOMPLETNI-SAGA.png").convert("RGBA")
    CW, CH = cover.size  # 1600×2560

    # lepítka ve vějíři nalepená přes střed knihy (titul i „Nenech to ležet" zůstanou volné)
    plan = [
        ("EPUB", 5.5, 300, 1010),
        ("MOBI", -5.0, 650, 1250),
        ("AZW3", 5.0, 250, 1490),
        ("PDF", -6.0, 660, 1730),
    ]
    target_w = 620  # šířka karty v prostoru obálky
    for fmt, ang, x, y in plan:
        st = make_sticker(fmt, ang)
        scale = target_w / (380 * SS)
        st = st.resize((max(1, int(st.width * scale)),
                        max(1, int(st.height * scale))), Image.LANCZOS)
        cover.alpha_composite(st, (x, y))

    hero = cover.convert("RGB")
    p = OUT / "hero-saga.png"
    hero.save(p)
    return p


def main() -> int:
    btns = export_buttons()
    hero = export_hero()
    made = btns + [hero]
    print(f"✅ {len(made)} souborů → {OUT.relative_to(ROOT)}/")
    for p in made:
        print(f"   {p.name}  ({p.stat().st_size // 1024} kB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
