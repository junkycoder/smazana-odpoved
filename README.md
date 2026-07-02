# Smazaná odpověď

> Pracovní název (placeholder). Pětidílná sága. Zdarma, digitálně. Volné šíření *je* ta věc — a je to Odkaz.

**Logline:** Internet padl — ne, někdo ho vypnul. Volný přenos dat je zločin. Pravda přežívá rozpůlená a schovaná jako odpad. Tahle kniha je její kus — zadarmo, šiř ji dál, staneš se kurýrem. Pět dílů, pět šifer, Odpověď, kterou nezná ani vypravěč. Slož ji.

---

## O čem to je

Svět **26 let po pádu.** Síť se nerozpadla — někdo ji rozpojil. Co projde povolenou sítí, je cenzurované; pravda se nedá vysílat, jen pašovat. **Otázku zná každý. Odpověď** někdo smazal — ze sítě i z hlav. Jeden člověk ji předtím **rozpůlil**, aby ji mazací stroj nesmazal z jednoho místa. Sága je hon za těmi dvěma polovinami — a zjištění, že obě celou dobu ležely doma.

Vypravěčem je **robot Cvok** — jediný funkční stroj ve vesnici, postavený v roce 2026 —, který přehrává nahrávku zmizelého dítěte a sám jí nerozumí. Tón: **satira, podaná deadpan.** Adams přes českou cyniku.

## Stav: SÁGA KOMPLETNÍ (1. průchod všech pěti knih)

| # | Kniha | Otázka → obrat | Šifra | Stav |
|---|---|---|---|---|
| 1 | [Vesnice](knihy/kniha-1-vesnice/) | Co je to za stroj? → Čí je ten stroj? | Morse + falešný klíč | ✅ 2. verze (přepis) |
| 2 | [Trasy](knihy/kniha-2-trasy/) | Kdo je to dítě? → Co to dítě nese? | Glyfy | ✅ + redakce |
| 3 | [Etalon](knihy/kniha-3-etalon/) | Proč Odpověď chybí? → Kdo ji doplní? | Obraz-prompt | ✅ + redakce |
| 4 | [Archiv](knihy/kniha-4-archiv/) | Co se stalo v 00? → Co se stane v 00? | Cross-book | ✅ + redakce |
| 5 | [Kopie 00](knihy/kniha-5-kopie-00/) | Co je Odpověď? → Vykonej ji. | Sjednocení | ✅ + redakce |

Každá kniha: předmluva (hlas Cvoka) + 6 kapitol (hlas sirotka) + **Klíč** (šifra dílu) + **Kolík** (protokol kurýra — reálný dead-drop: zkopíruj knihy na flash disk a polož je, kde se nekouká) + **Úřední údaje** (in-world zveřejněné BTC peněženky jako QR; adresy zatím `bc1q-DOPLNIT-…` — před vydáním nahradit reálnými).

## Struktura repozitáře

```
.
├── README.md                  # tenhle soubor
├── zadani/                    # zdrojová zadání ságy (v1–v6, v6 = kánon)
├── bible/                     # story bible — kánon, postavy, svět, pravidla
│   └── kanon.md
└── knihy/
    ├── kniha-1-vesnice/       # KNIHA 1: Vesnice (00-predmluva … 09-penezenky)
    ├── kniha-2-trasy/         # KNIHA 2: Trasy
    ├── kniha-3-etalon/        # KNIHA 3: Etalon
    ├── kniha-4-archiv/        # KNIHA 4: Archiv
    └── kniha-5-kopie-00/      # KNIHA 5: Kopie 00 (kapitoly nesou odpočet 05→00)
```

## Reálný přesah (in-world × realita)

- **Kolík (USB):** každá kniha končí protokolem kurýra — čtenář zkopíruje ságu na flash disk a „zatluče kolík" na dead-drop. Pointa K5: kniha je záloha kolíku; Cvok je kolík, který došel.
- **BTC peněženky:** oficiální peněženky jsou v tom světě povinně veřejné (transparentnost jako propaganda) — knihy je proto tisknou jako úřední údaj s QR. Čtenář může poslat skutečné satoshi komukoli, klidně ironicky (odměna za udání, Lhářova nadace, žebrací stanoviště 07, mrtvé peněženky převratu, nakonec „projekt drát"). Text ironii nikdy nekomentuje.

## Distribuce

Knihu **dáš zadarmo a vyzveš lidi, ať ji kopírují a posílají dál.** Čtenář se sdílením stává **kurýrem.** Žádné DRM; pirátství je *feature.* Nehromadíš (paywall = Horcrux), odkazuješ (free + šiř dál = Odkaz).

---

*Kompletní kánon světa viz [`bible/kanon.md`](bible/kanon.md). Nejnovější zdrojové zadání: [`zadani/smazana-odpoved-zadani-v6.md`](zadani/smazana-odpoved-zadani-v6.md).*
