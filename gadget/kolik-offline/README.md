# Kolík — offline webový prototyp

Prototyp veřejného balíku pro USB fungujícího přímo přes `file://`. Výsledný `dist/index.html`:

- nemá externí fonty, skripty, analytiku ani síťové požadavky;
- nepoužívá `fetch`, ES moduly, service worker ani `localStorage`;
- obsahuje všech pět knih v jednom souboru a současně kopíruje Markdown vedle;
- má ručně řešitelnou pětifázovou skládačku, která sama nevypíše Odpověď;
- zůstává čitelný i bez JavaScriptu;
- vytváří manifest a SHA-256 kontrolní součty.

## Build

```sh
npm install
npm run build
```

Build čte pracovní edici z `../../revize-v2/knihy/`. Vydavatelská README, story bible, zadání a placeholderové peněženky se do veřejného balíku nekopírují.

## Bezpečnostní hranice

USB nemá obsahovat autorun, spustitelný soubor, makro ani privátní klíč. Prototypový manifest zatím není digitálně podepsaný; před výrobou je potřeba přidat podpis release manifestu a otisk veřejného klíče na fyzický obal.

Veřejný dead-drop má používat QR/NFC nebo ověřené partnerské místo. Neznámý nalezený USB disk se nemá připojovat k osobnímu počítači.

