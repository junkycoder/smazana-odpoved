# Generální audit knihy 5 a návrh fyzických gadgetů

**Projekt:** Smazaná odpověď  
**Auditováno:** 11. 7. 2026  
**Kánon:** `zadani/smazana-odpoved-zadani-v6.md`; při rozporu s bible platí v6.  
**Rozsah čtení:** kořenový `README.md`, celý `bible/kanon.md`, README všech pěti knih, všechny soubory knihy 5 a všech šest verzí zadání v `zadani/`. Zdrojové texty nebyly měněny.

## Verdikt

Kniha 5 je emocionálně nejsilnější díl a má několik výborných, skutečně pentalogických payoffů: Kolík konečně vstoupí do Cvoka, Síto uzavře motiv stání i talíře, Lhářova nepopsatelnost se vrátí jako hladké místo a poslední věta fyzicky přeteče do předmluvy knihy 1. Závěr tedy není potřeba znovu vymýšlet; potřebuje **kauzálně zpevnit, odmlžit geografický rozsah a přestavět čtenářskou šifru**.

V současné podobě však finále ještě není připravené k vydání. Čtyři závady jsou blokující:

1. **Meta-slib není splněn.** Kniha tvrdí, že čtenář Odpověď sám složí, ale publikované soubory mu nedávají skutečný morseový ciphertext ani konkrétní tvar, který by šel přiložit na slova. Zároveň kapitola 01 Odpověď prakticky vysloví.
2. **Kopie 00 funguje jako nezasloužený zázračný uzel.** Kritická infrastruktura je nehlídaná, dvojice v ní tři dny staví převod bez obsluhy či alarmu a Lhář čtvrtou noc přijde s kavelerií, ale nechá předposlední a poslední část zprávy doběhnout.
3. **Text střídá zemi a svět.** Kánon výslovně říká, že každá země má vlastní etalon a vlastní nebe. Kniha 5 jednou vysílá „celé zemi“, jindy „všechna světla světa“ a vyvozuje pád vlády všude. Současná kauzalita stačí nanejvýš na jednu elektrizační soustavu.
4. **Reálný dead-drop s nalezenou USB flashkou je bezpečnostně problematický.** Knihy povzbuzují k pokládání a zvedání cizích USB médií; to je přesně vzorec, před kterým bezpečnostní autority varují. Kolík musí být volitelná sběratelská/distribuční kopie od známého vydavatele, ne výzva strkat anonymní nalezené zařízení do osobního počítače.

## Prioritizace zásahů

| Priorita | Závada | Dopad | Doporučený zásah |
|---|---|---|---|
| **P0** | Neexistující finální šifra + explicitně řečená Odpověď | Rozbíjí hlavní slib celé ságy | Buď dodat skutečné vstupy a funkční offline skládání, nebo přestat slibovat řešitelnou šifru. Doporučuji první možnost. Vyjmout explicitní formulaci z kap. 01. |
| **P0** | Vstup do Kopie 00 a tři dny nerušené práce | Finále působí jako deus ex machina | Z Kopie 00 udělat starý fyzický uzel s živým řídicím kanálem; přístup koupit Rozpůlitelovým credentialem a ukázat slepou zónu bezpečnosti. |
| **P0** | Lhář může vysílání zastavit, ale neudělá to | Padouch musí být pasivní, aby hrdinové vyhráli | Zavést fail-safe: po prvním pulzu je zpráva rozkopírovaná do podružných uzlů; vypnutí kmene by shodilo pánovo nebe a stejně nespálilo kopie. Lhář pak volí mezi dvěma prohrami. |
| **P0** | „Země“ vs. „svět“ | Odporuje atomizovanému světu a zveličuje vítězství | Rozhodnout: lokální vítězství s otevřeným šířením přes hranice, nebo mezinárodní synchronizace. Doporučení: první; je věrohodnější a tematicky silnější. |
| **P0** | Neznámé USB jako veřejný dead-drop | Reálné bezpečnostní riziko a reputační problém | Pro veřejný provoz použít QR/NFC kartu nebo autorizovaná výdejní místa; USB jen zapečetěné a ověřitelné. Přepsat zadní stránky Kolík. |
| **P1** | Vyrvaný modul 214-K-07 nemá finální payoff | Nevyplacená „živá mina“ z knihy 3 | Modul buď umožní Lháři poznat Cvoka a vysvětluje jeho osobní příchod, nebo se po pádu Core stane první nově nalezenou kopií. |
| **P1** | „Jednou přehraješ, máš“ u obyčejného USB | Kolík se chová jako Odkaz bez vysvětlení | Jednou větou říct, že Cvok po úspěšném importu médium protokolárně vymazal/přepsal. |
| **P1** | Pád režimu je převážně definice, ne událost | Emocionální triumf předbíhá materiální svět | Přidat tři krátké důkazy: rozkaz, který operátor neprovede; klony, které odejdou; rozpad nebo otevření veřejných peněženek/oblohy. |
| **P1** | „Klíč drží vesnice. Celá.“ | Technicky nepravdivé a ve skutečnosti nebezpečné | Popsat prahový multisig: klíč není jeden, několik podílů drží různí lidé a k útratě je třeba např. 2 ze 3. |
| **P1** | Sirotek odejde od zklidněné vesnice bez jasně zajištěné péče | Jeho svoboda může působit jako opuštění bezmocných | Uvést časový odstup a předání: zůstane týdny, obnoví trasy péče, teprve pak zmizí. |
| **P2** | Schránkův člověk po rozhodující scéně mizí z textu | Otevřený osud klíčového spojence | Jedna konkrétní věta o návratu, smrti nebo nové trase. |
| **P2** | Odpočet se podle README „krátí“, ale fakticky ne | Formální slib není vidět | Buď přestat tvrdit, že kapitoly monotónně krátí, nebo přestavět rozsahy. |
| **P2** | Nadměrné vysvětlování „slova–tvar–význam–hlavy“ | Obrazy už pointu unesly samy | Z kap. 04, 02, 01 a Klíče ubrat přibližně čtvrtinu abstraktních dovětků. |

## Audit finále po částech

### Předmluva

Funguje dobře: slibuje přechod playbacku do přítomnosti, legitimizuje odpočet a předem rozliší díru po ztrátě od díry po Lháři. Výborná je věta „Nenech mě mluvit do prázdna.“

Problém je slib „k tomuhle klíči jsou potřeba všechny čtyři předchozí naráz“. V aktuálním artefaktu to není pravda v ověřitelném smyslu. Předmluvu ponechat jen tehdy, když se finální nástroj opravdu postaví a projde slepým testem s novými čtenáři.

### 05 — Návrat

Nejlepší návratový beat je „Jo. Cvok. Cvaká?“; správně shodí hrdinský patos. Kolík, zdířka a rodičův hlas splácejí Čechovovu pušku z knihy 1 přesně a s emocí. Rodičův zákaz spojení na jednom místě přirozeně otevře problém distribuce.

Potřebné opravy:

- vysvětlit, proč se běžný USB kolík po přehrání vyprázdní;
- připomenout, že Cvokova věta je v hlubší, distribuované paměti, zatímco vyrvaný modul nesl jeho „odkud“; jinak čtenář může oprávněně čekat, že bez modulu chybí rozhodující data;
- zvážit škrt třetího až čtvrtého zopakování „po kouskách“ v rodičově instrukci — motiv už je bezpečně usazený.

### 04 — Smyčka

Nápad „pán sám šíří tvar na nebi“ je čistý payoff knihy 3. Stejně dobré je, že řešení nevymyslí hrdina s proslovem, ale Síto jednou provozní větou. Její volba zůstat u kol přesně převrací move-or-die a připravuje emocionální cenu.

Slabé místo je technická expozice. Zatěžování a odlehčování sítě by v reálné synchronní soustavě vyvolalo regulační odezvu; automatické rezervy se právě snaží frekvenci vracet k cíli. ENTSO-E popisuje rychlou aktivaci Frequency Containment Reserves a následnou obnovu frekvence. Srozumitelnější a věrohodnější fikční řešení je **řídicí/ripple kanál po silových vodičích**, nikoli hrubé škubání celou zátěží. Komunikace po elektrické síti je existující třída technologií; příklady pokrývají [ISO/IEC 14543-3-5 pro power-line řízení](https://webstore.iec.ch/en/publication/10117) a evropskou rodinu EN 50065 pro signalizaci na nízkém napětí. [ENTSO-E k regulaci frekvence](https://eepublicdownloads.entsoe.eu/clean-documents/SOC%20documents/LFC/ALFC_report_2023_Update_14102024.pdf).

Návrh: vesnické šlapání nevytváří viditelné poklesy samo. Síto zná starý servisní rytmus, kterým se po drátu přikazovalo lokálním regulátorům krátké/dlouhé „kontrolní pohasnutí“. Z vesnice dojde jen do tří rozvoden; Kopie 00 drží kořenový podpis pro celou zem. Tím zůstane proud, morse i fyzická práce, ale odpadne tvrzení, že každá moderní žárovka přímo kopíruje frekvenční vadu.

### 03 — Rána

Kopie 00 jako „nejošklivější a nejcelejší“ stavba je výborný fyzický cíl. Falešná Odpověď na podstavci splácí falešný klíč K1 bez vysvětlování a věta „po dlouhé cestě chce člověk, aby cíl vypadal jako cíl“ patří k nejlepším v dílu.

Neudržitelná je bezpečnost místa. Budova, přes kterou stále teče proud, nebe a rozkazy, nemůže být současně bez obsluhy a bez poplachů jen proto, že se lidé bojí jizvy. Oprava nemusí přidat akci; stačí tři konkrétní zámky:

1. Schránkův člověk zná starou jednosměrnou trasu pro zabavená média.
2. Rozpůlitel zanechal servisní credential nebo fyzický klíč ve svém posledním Odkazu.
3. Starý sál je z inventáře vyřazený, ale jeho měděný/řídicí kmen byl při modernizaci obejit, ne odpojen; monitoring vidí jen nový dohled, ne staré relé.

Pak je průnik důsledkem knih 3–4, ne darem scenáristy.

### 02 — Nula

Centrální obraz — Cvok nedělá nic nového, jen svět konečně poslouchá — je správný vrchol celé pentalogie. Stejně silný je pánův rozkaz „SVĚTELNÝM PORUCHÁM NEPŘIKLÁDEJTE VÝZNAM“; propaganda se sama stane návodem.

Tady jsou ale největší logické dluhy:

- „všechna světla světa“ je v rozporu s „celou zemí“ i s kánonem více etalonů;
- Lhář dorazí před koncem a může vypnout převod, zabít obsluhu nebo zničit Cvoka;
- jeho možnost „chtěl, aby to doběhlo“ přichází bez předchozího oblouku a bere vítězství hrdinům;
- rozkazy sice ztratí část autority, ale kavalerie, BTC, masátko a infrastruktura dál fyzicky existují.

Doporučená konstrukce scény:

- první noc rozdistribuuje přehrávací plán do podružných regulátorů; od té chvíle kmen jen potvrzuje takt;
- násilné vypnutí Kopie 00 by shodilo pánovo nebe a proud ve městech, zatímco vesnická záloha by dokončila poslední segment lokálně;
- Lhář přichází čtvrtou noc, protože v modulu 214-K-07 poznal Cvokův podpis — tím se splatí K3;
- nabídne sirotkovi dvě centralizace: zastavit proud, nebo převzít význam. Sirotek nevybírá ani jednu;
- Lhář vydá svůj kontraproduktivní rozkaz; poté vidíme tři materiální následky, ne jen výklad: operátor odmítne příkaz k odpojení, klonové opustí směnu, místní uzel nebe začne přebírat zprávy od lidí;
- vítězství je **v jedné zemi**. Poslední odstavec ukáže, že kurýři překládají rytmus přes hranice do dalších nebí. Naděje je nezvratná jako proces, ne jako okamžité kouzlo ve všech hlavách planety.

### 01 — Význam

Tohle je emocionální vrchol, nikoli 02. Zklidněná vesnice, obyčejné prádlo, ruce pamatující rytmus, mrtvá Síto a prázdný talíř tvoří soudržnou řadu fyzických obrazů. Naložení vlastního talíře je přesnější uzavření rodičovské i Sítiny lásky než jakýkoli dialog.

Blokující věta je:

> „protože význam se dává, to je celé, to je všechno, to je ta veliká smazaná odpověď…“

Tím text udělá přesně to, co Klíč zakazuje: odpoví za čtenáře. Doporučuji ji nahradit jednáním, například principem: sirotek si sedne ke klepajícímu klukovi, nepoví mu význam, ale vyklepá druhou část a nechá ho, aby spojení udělal sám. Výsledek nebude vyřčen, ale bude vykonán.

Je také potřeba stanovit, jak dlouho sirotek po návratu zůstává. Nahrává „večer za večerem“, ale zmizení bez zajištěné péče o paměťově poškozené lidi může čtenář přečíst jako útěk. Jedna věta o obnovení zásobovacích tras a předání péče Schránkově síti ochrání jeho nově nabytou svobodu před morálním stínem.

### 00 — Zmizení

Zmizení konečně nese význam: sirotek poprvé není zásilka, nemá adresu a nese jen sebe. „Zatím“ vrací dřívější obavu „mají mě rádi — zatím“ v opačné polaritě a přechod do Cvokova přímého hlasu je přesný. Smyčka do předmluvy K1 funguje.

Zacelení velké rány je ale vyhlášeno o několik odstavců dřív, než je prokázáno. Doplnění krátké stopy přes hranici a osudu Schránkova člověka by tento pocit výrazně zpevnilo. Smyčka má zůstat distribuční, nikoli časová: příběh se vrací na začátek, svět už ne.

### Klíč, Kolík, Úřední údaje

**Klíč:** jazykově funguje, technicky ne. „Přilož tvar na slova“ není návod, dokud čtenář žádný reprodukovatelný tvar ani slova nemá. Je nutné dodat skutečný artefakt, nebo celý oddíl přejmenovat z „Klíče“ na „Předání“ a přestat tvrdit, že je šifra řešitelná.

**Kolík:** „Kniha je záloha kolíku. Já jsem kolík.“ je nejčistší meta-payoff celé ságy. Zachovat. Přepsat však praktický protokol tak, aby nevyzýval k připojování anonymních médií a k odkládání elektroniky „za radiátor“, kde může být požární, úklidový i právní problém.

**Peněženka:** čtyři staré díry ve sloupu krásně převracejí odměnu z K1. Realita ale odporuje větě „klíč drží všichni“. Pokud všichni drží stejný privátní klíč, stačí kompromitovat jediného. Pokud jde o prahový multisig, musí se to tak napsat. Standardní threshold multisig popisuje např. [BIP 383](https://bips.dev/383/); bezpečný setup více podpisujících řeší [BIP 129](https://bips.dev/129/).

Navíc je zde tematický střet: uvnitř fikce drží peněženku vesnice, mimo fikci ji drží autor. Je třeba zvolit jednu pravdu:

- **autorská peněženka:** přiznat jediného správce, zveřejnit účel a reporting;
- **projektová multisig:** 2 ze 3 nezávislých správců, veřejná politika výdajů; to lépe odpovídá „projektu drát“.

## Payoff motivů

| Motiv | Co se vyplatilo | Co ještě chybí | Hodnocení |
|---|---|---|---|
| **Odpověď** | Význam vzniká v posluchači; pánův zákaz sám učí interpretovat | Skutečná řešitelná mechanika; odstranit explicitní odpověď | Silné téma, slabý artefakt |
| **Odkaz** | Falešné sklo v Kopii 00 splácí K1; sirotek předá sebe bez vlastnictví | Text málo odlišuje opakovatelný Cvokův záznam od read-once skla | Dobré, ale spíš konceptuální |
| **Kopie 00** | Nula je fyzická rána a místo obrácení proudu | Přístup, zabezpečení, monitoring a rozsah uzlu | Výborný obraz, slabá kauzalita |
| **Kolík / USB** | Kolík otevře Cvoka; prázdné médium nese nový příběh; Cvok = kolík | Vysvětlit vymazání a bezpečně přepsat reálný protokol | Nejlepší payoff ságy |
| **Síto** | Stání se změní v dosah; sklíčko, talíř, kola a „vstoje“ se uzavřou | Fyzicky méně přepnout oběť: směny + její poslední úsek | Emocionálně výborné |
| **Svatý drát** | K1 infrastruktura se stane kanálem svobody a peněženkou | Technicky zasít řídicí signalizaci před K5 | Silný motiv, pozdní schopnost |
| **Peněženky** | Od odměny za udání ke společnému proudu; čtyři stejné díry | Platné adresy, QR payload, custody, reporting | Dobrý rým, nehotová realita |
| **Modul 214-K-07** | Je objasněno, že věta přežila mimo modul | Modul označený jako „živá mina“ se už nevrátí | Nevyplacený Čechov |

## Emocionální uzavření

Co zachovat bez diskuse:

- anti-hrdinský návrat domů;
- rodičův hlas mladší než sirotek;
- Sítina ruka na tváři a později prázdný talíř;
- zlomená tužka jako jediný pomník tras;
- Cvokova rozhodující pasivita;
- „nezmizel nikdo a zmizeli všichni“;
- motorická paměť rukou;
- sirotkovo zmizení jako první svobodně zvolený pohyb;
- „Zatím“ a doslovný přechod do K1.

Co emoci oslabuje:

- abstraktní výklad po obrazu, který už pointu řekl;
- smrt Síta po pěti nocích bez spánku a šlapání, když jsou výslovně přítomni další šlapači — působí lehce naprogramovaně;
- rychlé prohlášení režimu za mrtvý bez konkrétního následku;
- odchod sirotka bez časového a pečovatelského mostu.

Nejlepší redakční pravidlo pro přepis: **po silném fyzickém obrazu nechat maximálně jednu interpretační větu.** Talíř, světla, hladké místo a klepající ruce nepotřebují každý ještě odstavec teze.

## Repetice a formální rytmus

V hlavním textu K5 se objevuje přibližně 11× „po kouskách“, 25× kořen „tvar“, 20× „proud“, 33× kořen „slov-“ a 45× kořen „svět-“. Část je záměrná hudba, ale ve druhé polovině se motivy přestanou posouvat a jen se znovu vysvětlují.

Nejvíc se opakuje tatáž teze v těchto místech:

1. rodičova instrukce v 05;
2. plán u drátu v 04;
3. popis vysílání v 02;
4. explicitní Odpověď v 01;
5. rekapitulace v Klíči;
6. znovu „slova–tvar–příběh“ v 00.

Doporučení: každé místo má mít jinou funkci — **pravidlo → plán → událost → cena → úkol čtenáře → předání**. V současnosti všech šest míst částečně plní i funkci výkladu.

README tvrdí, že kapitoly se k nule krátí, ale počet slov je: 05 **1103**, 04 **1156**, 03 **760**, 02 **918**, 01 **1018**, 00 **579**. Odpočet funguje názvem, nikoli monotónní kompresí. Jsou dvě dobré možnosti:

- změnit README na přesnější „odpočet vrcholí nejkratší nulou“;
- nebo skutečně komprimovat, např. 1100 → 950 → 800 → 700 → 550 → 350 slov. Druhá možnost je formálně působivější, ale vyžádá si největší řez právě v emocionální 01.

## Doporučený přepis K5 — minimální chirurgická verze

1. **05:** přidat jednu větu o automatickém vymazání kolíku po importu a jednu o vrstvě paměti, v níž přežila Cvokova věta.
2. **04:** přepsat „kolísání sítě“ na starý servisní/ripple-control kanál. Rozpůlitelův Odkaz dodá podpis kořenového regulátoru. Uvést, že Kopie 00 je kořen řídicího stromu jedné země.
3. **03:** doplnit tři bezpečnostní překážky a jejich payoff z K1–K4; žádný nový náhodný klíč.
4. **02:** po první noci zprávu replikovat do podružných uzlů. Lhář pozná Cvoka z 214-K-07. Nemůže zabránit šíření, jen zvolit cenu vypnutí. Vyjmout možnost, že celou věc tajně chtěl, pokud se pro ni nevytvoří oblouk dřív.
5. **02 konec:** ukázat tři konkrétní selhání poslušnosti. Všechna globální tvrzení nahradit zemskými; přeshraniční pokračování až v dozvuku.
6. **01:** odstranit větu, která Odpověď vysloví. Nechat sirotka vykonat ji s klepajícím klukem. Přidat čas a zajištění vesnice.
7. **00:** jednou větou uzavřít Schránkova člověka a ukázat první přenos za hranici. Smyčku ponechat beze změny.
8. **Klíč:** dodat skutečný vstup a otestovat jej. Pokud selže, nepředstírat šifru a přepsat oddíl na poetický protokol předání.
9. **Kolík:** odstranit návod na připojení nalezeného anonymního USB. Směrovat k autorizovaným výměnným místům nebo QR/NFC kartám.
10. **Peněženka:** použít platný payment URI, popsat skutečnou custody a odstranit placeholdery.

## Fyzické gadgety: doporučená produktová architektura

### Rozhodnutí

Nevyrábět jeden „magický“ předmět, který se snaží být zároveň archivem, jednorázovým Odkazem, aktualizovatelným webem a platební peněženkou. Tyto funkce si odporují. Doporučené jsou tři vrstvy se stejným bezplatným obsahem:

| Vrstva | Úloha | Výhoda | Slabina |
|---|---|---|---|
| **Kolík — USB offline edice** | Plná autonomní kopie ságy | Funguje bez sítě; nejsilnější diegetický objekt | Bezpečnost cizího USB, omezení `file://`, stárnutí flash |
| **Odkaz — QR + NFC karta** | Výchozí masová fyzická brána | Levná, bezpečnější, snadno aktualizovatelná | Potřebuje síť; doména může zaniknout |
| **Kopie 00 — sběratelská edice** | Artefakt, podpis a ritualizované předání | Silná identita a fundraising | Vyšší výroba; nesmí zamknout obsah |

Fyzický nosič neporuší kánon „zdarma, digitálně“, pokud **neobsahuje exkluzivní dějový nebo šifrovací kus**. Platí se za objekt a výrobu, ne za přístup k pravdě.

## Varianta A — USB Kolík s offline webem

### Doporučené minimum

- 8–16 GB, USB 2.0 nebo 3.x mass storage; rychlost není kritická;
- ideálně duální USB-A + USB-C, protože Type-C je standardní reverzibilní konektor pro novější zařízení; specifikaci zveřejňuje [USB-IF](https://www.usb.org/usb-type-cr-cable-and-connector-specification);
- jedna datová partition, **exFAT**; Microsoft zveřejňuje [exFAT specifikaci](https://learn.microsoft.com/en-us/windows/win32/fileio/exfat-specification) a Apple uvádí exFAT/FAT mezi podporovanými formáty externích médií na iPhonu i Macu ([Apple – external storage on iPhone](https://support.apple.com/en-au/guide/iphone/iph95baac91f/ios), [Apple – external drive formats on Mac](https://support.apple.com/en-us/101830));
- čitelný štítek `KOLIK_00`, sériové číslo výrobní série, human-readable URL a otisk vydavatelského veřejného klíče na obalu;
- žádné spustitelné soubory, instalátory, makra ani `autorun.inf`.

Microsoft používání AutoRun pro distribuované aplikace na výměnných médiích výslovně nedoporučuje kvůli šíření malwaru; uživatel má disk otevřít ručně ([Microsoft AutoRun guidance](https://learn.microsoft.com/en-us/windows/win32/shell/autoplay-reg)).

### Struktura média

```text
KOLIK_00/
├── START-HERE.txt
├── index.html                 # jediný soběstačný vstup
├── knihy/
│   ├── 01-vesnice.pdf
│   ├── 01-vesnice.epub
│   ├── ...
│   └── 05-kopie-00.epub
├── archiv/
│   ├── saga.zip               # kopie určená k dalšímu předání
│   └── zdrojove-texty.zip     # pokud licence dovolí
├── overeni/
│   ├── SHA256SUMS.txt
│   ├── release-manifest.json
│   ├── release-manifest.sig
│   └── PUBLIC-KEY.txt
├── licence/
│   └── LICENSE.txt
└── README-cz.txt
```

`index.html` musí být skutečně offline-first, nikoli běžná PWA zkopírovaná na disk.

### Omezení `file://` a jak je obejít

Při dvojkliku se stránka otevře jako `file://`. V tomto režimu:

- ES moduly mohou selhat na CORS; MDN přímo upozorňuje, že lokální `file://` moduly vyžadují server ([MDN JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules));
- `fetch()`, XHR, webfonty a další CORS požadavky na lokální soubory mohou narazit na opaque origin ([MDN CORS request not HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS/Errors/CORSRequestNotHttp));
- service worker nelze registrovat z `file://`; registrační URL musí být HTTP(S) a potenciálně důvěryhodný origin ([MDN ServiceWorkerContainer.register](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register));
- chování `localStorage` u `file:` URL není definované a může se mezi prohlížeči měnit ([MDN localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)).

Proto:

1. `index.html` má obsahovat inline CSS, inline **klasický** JavaScript bez `type="module"` a předgenerovaný vyhledávací index jako JS objekt.
2. Nepoužívat `fetch`, service worker, IndexedDB jako podmínku, webfonty, CDN ani vzdálené skripty.
3. Základní čtení a šifra musí fungovat i s vypnutým JavaScriptem; JS jen zpříjemní navigaci a skládání.
4. Stav šifry držet v URL fragmentu nebo nabídnout export/import malého textového kódu. Nespoléhat na `localStorage`.
5. PDF/EPUB dávat jako samostatné soubory pro mobilní čtečky. Na iOS je přístup k externím diskům podporovaný přes Files, ale offline HTML navigaci je nutné testovat zvlášť; nelze ji odvodit jen z toho, že systém disk připojí.
6. Volitelný lokální server lze přidat pouze jako pokročilou cestu (`python -m http.server` v návodu), ne jako jediný způsob. Nedodávat vlastní binární launcher.

### Aktualizace

Offline Kolík má být **číslovaný snapshot**, ne zařízení, které se potají aktualizuje:

- manifest obsahuje `release_id`, datum, hash každého souboru a canonical HTTPS URL;
- `index.html` může nabídnout obyčejný odkaz „ověřit novou verzi“, ale offline funkce na něm nezávisí;
- web nabízí celý nový `saga.zip`, ne inkrementální patch;
- uživatel aktualizuje kopií na nové médium nebo přepsáním, nikdy automatickým spouštěním kódu z USB;
- každá verze zůstává čitelná sama o sobě; starý Kolík není po aktualizaci „rozbitý“.

### Integrita a autenticita

Samotný SHA-256 odhalí poškození jen tehdy, když má čtenář důvěryhodný referenční hash. NIST uvádí, že hash slouží k detekci změny ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)); digitální podpis navíc ověřuje podepisujícího a neoprávněné změny ([FIPS 186-5](https://csrc.nist.gov/pubs/fips/186-5/final)). Prakticky:

- podepsat `release-manifest.json` offline vydavatelským klíčem;
- veřejný klíč a jeho krátký fingerprint vytisknout na kartě i webu;
- na webu nabídnout jednoduché „přetáhni manifest a podpis“ ověření;
- při výrobě udělat plný read-back a porovnat hash každého kusu s masterem.

### Bezpečnost

USB není pouze souborový systém; kompromitovaný firmware se může vydávat za jiný typ periferie. Microsoft mezi fileless vstupy uvádí i reprogramované USB periferie/BadUSB ([Microsoft – fileless threats](https://learn.microsoft.com/en-us/defender-endpoint/malware/fileless-threats)). NIST shrnuje, že přenosná média vyžadují procedurální, fyzické i technické kontroly ([NIST SP 1334](https://csrc.nist.gov/pubs/sp/1334/final)).

Bezpečnostní minimum produktu:

- nakupovat od dohledatelného dodavatele s pevně definovaným mass-storage firmwarem;
- žádná emulace klávesnice, síťové karty ani CD-ROM partition;
- tamper-evident obal a sériové číslo spojené s výrobním manifestem;
- jasně napsat: **nepřipojuj neznámý nalezený USB disk k osobnímu počítači**;
- veřejné dead-dropy realizovat QR/NFC kartou nebo přes partnerské knihovny/kluby, kde je původ média ověřený;
- obsah nešifrovat — je veřejný; šifrování by zhoršilo kompatibilitu a nepřidalo potřebnou ochranu;
- privátní klíče k BTC ani podpisový privátní klíč nikdy neukládat na distribuovanou flashku.

### Životnost

Flash není archiv „na generace“. I průmyslový výrobce uvádí u konkrétní řady 10 let retence na začátku životnosti, ale jen 1 rok na konci životnosti ([Swissbit U-56n fact sheet](https://www.swissbit.com/data/U-56n/U-56n_fact_sheet.pdf)). To není univerzální garance pro spotřební reklamní flashky; je to důvod neslibovat „přežije desítky let“.

Doporučení:

- kvalitní pSLC/SLC nebo alespoň značková MLC pro limitku; u masové série značkový controller a NAND s dokumentovanou retencí;
- refresh/read-verify každé 2–3 roky;
- vždy mít stejný ZIP na několika online mirrorech a dovolit nekonečné kopírování;
- skladovat v suchu, mimo vysoké teploty a UV; nevkládat dlouhodobě přímo za topení — literární „za radiátor“ odstranit z reálného návodu;
- obsah duplikovat: rozbalený web + samostatný ZIP + PDF/EPUB.

### Výrobní QA

1. Zafixovat master image a manifest; reprodukovatelný build.
2. Ověřit deklarovanou kapacitu každého vzorku celé série, ne jen kopírování několika MB.
3. Po nahrání celé médium znovu přečíst a porovnat SHA-256.
4. Testovat bootless/mass-storage identitu a vyloučit další USB profily.
5. Test matrix: Windows Chrome/Edge/Firefox, macOS Safari/Chrome/Firefox, běžná Linux distribuce, Android USB-C Files + PDF/EPUB, iPhone USB-C Files + PDF/EPUB.
6. Otestovat bez sítě, s vypnutým JS a s přejmenovaným mount pointem.
7. Namátkový test po teplotním transportu a po 3 měsících skladování.
8. U každé série archivovat několik zapečetěných referenčních kusů.

## Varianta B — QR + NFC Odkaz

Tohle má být **výchozí fyzická distribuce**, protože uživatel nemusí připojovat neznámou periferii.

Forma: záložka nebo karta velikosti platební karty, černá/průsvitná s jemnými zlatými žilkami. Nese:

- QR na krátkou canonical HTTPS URL;
- stejnou URL jako NFC NDEF URI record;
- URL vytištěnou textem pro přístupnost a případ selhání kamery/NFC;
- release ID a krátký fingerprint podepsaného manifestu;
- výzvu „stáhni celý ZIP a předej dál“, ne jen „čti na webu“.

NFC musí používat standardní NDEF URI, ne proprietární aplikaci. Android pro NDEF URI poskytuje systémový dispatch a doporučuje `RTD_URI` ([Android NFC basics](https://developer.android.com/develop/connectivity/nfc/nfc)); Apple na podporovaných iPhonech umí background reading NDEF URI a bez asociované aplikace otevře HTTPS v Safari ([Apple background tag reading](https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading)). NFC není podporováno na každém zařízení a Apple jej nepodporuje v macOS, proto je QR a vytištěná URL povinná záloha ([Apple Core NFC](https://developer.apple.com/documentation/CoreNFC)).

Výrobní pravidla:

- běžný Type 2 tag s dostatečnou pamětí pro krátkou URL; po zápisu jej uzamknout read-only;
- pokud je karta kovová, použít on-metal tag s ferritovou vrstvou; jednodušší je polykarbonát/akryl;
- QR držet krátký. QR technicky unese jen několik kB a pro telefonní praxi se nemá používat jako úložiště knihy; DENSO uvádí maximum přibližně 3 kB binárních dat ([DENSO QR FAQ](https://www.qrcode.com/en/faq.html)). Aktuální norma je [ISO/IEC 18004:2024](https://www.iso.org/standard/83389.html);
- dodržet čtyřmodulovou quiet zone a ověřit sken na matném i lesklém povrchu ([DENSO print guidance](https://www.qrcode.com/en/howto/code.html/index.html));
- nepoužívat cizí zkracovač URL. Doména a redirect musí být pod kontrolou projektu;
- NFC a QR mají vést na stejnou human-readable doménu, aby uživatel poznal přepsaný tag nebo přelepený kód.

### Aktualizovatelnost a link rot

QR/NFC má dvě adresy v jedné:

1. krátká stabilní URL, např. `/k/00`, může směrovat na nejnovější vydání;
2. na kartě je zároveň vytištěný neměnný release hash/CID nebo cesta k archivnímu snapshotu.

Tím lze web aktualizovat, ale stará karta stále dokazuje, ke které verzi patřila. Udržovat minimálně dvě nezávislé zrcadlové domény v manifestu a umožnit stažení celé offline kopie.

### Proč nedělat „jednorázový webový Odkaz“ jako bezpečnostní funkci

Návrh z v2–v6 „ukáže se jednou, pak zčerná“ je dobré divadlo, ale špatná kontrola:

- klientský flag smaže inkognito režim nebo jiný prohlížeč;
- serverový globální token může první návštěvník spálit všem, kteří dostali kopii stejné knihy;
- screenshot, cache a síťový záznam jednorázovost vždy obejdou;
- login nebo fingerprinting vytvoří centrální evidenci čtenářů, což jde proti tématu i soukromí;
- offline USB nemá autoritu, která by jednorázovost spolehlivě vynutila.

Použít jej pouze jako **přiznaný rituální efekt**: po odhalení stránka lokálně ztmavne, ale čtenář dostane export svého úlomku a může celý proces resetovat. Žádný nutný obsah nesmí být nenávratně zničen. Skutečně jednorázový pocit lze u sběratelské karty vytvořit analogově stírací vrstvou nebo trhací pečetí.

## Varianta C — sběratelská Kopie 00

Doporučená limitka kombinuje dvě fyzické metafory, ale žádný exkluzivní obsah:

- **Odkazová karta:** kouřově černý průsvitný polykarbonát (bezpečnější než sklo), zlatá fólie/metalizace po okrajích, NFC + QR, číslování, stírací pečeť přes „první čtení“;
- **Kolík:** robustní duální USB-A/USB-C v černém anodizovaném hliníku nebo jednoduchém pryžovém pouzdře, laserové číslo shodné s kartou;
- **papírový protokol:** release hash, veřejný podpisový fingerprint, stručný bezpečnostní návod a licence k dalšímu kopírování;
- **obal:** bez magnetického zavírání přímo přes NFC anténu; žádná skutečná ostrá špička ve tvaru hřebu.

Sběratelský efekt má být v materiálu, sériovosti a rituálu, ne v zamčené kapitole. Každý binární soubor na limitce musí být zároveň zdarma ke stažení.

## Bitcoinové QR: technické minimum před vydáním

1. Nahradit všechny `bc1q-DOPLNIT-…`; nejde o platné adresy.
2. QR nemá obsahovat jen holý text adresy, ale standardní `bitcoin:` payment URI. Aktuální [BIP 321](https://bips.dev/321/) nahrazuje BIP 21 a popisuje on-chain, Lightning, BOLT12 i Silent Payments instrukce; peněženka musí vždy vyžadovat potvrzení uživatele.
3. Vedle QR vytisknout adresu/instrukci i textem a krátký ověřovací fingerprint; čtenář musí mít možnost porovnat, kam platí.
4. U statické on-chain adresy vědomě přijmout veřejné linkování všech darů — v příběhu je to záměrná „transparentnost“, v realitě privacy trade-off.
5. Pro opakované platby zvážit reusable instrukci bez address reuse (např. BOLT12 offer nebo Silent Payment) pouze po testu podpory cílových peněženek; kompatibilní fallback může zůstat on-chain.
6. Privátní klíče držet mimo web, repozitář i výrobní master USB.
7. Pro „projekt drát“ použít skutečný 2-of-3 multisig nebo změnit text. Zálohy descriptoru, recovery postup a testovací malou transakci udělat před tiskem.
8. Vydat veřejnou provozní stránku: kdo drží klíče, k čemu peníze jdou, jak často se reportuje. To je důležitější než in-world ironie.

## Doporučené pořadí realizace

1. **Zmrazit rozhodnutí o finální šifře.** Dokud neexistuje řešitelný prototyp, netisknout gadget ani QR.
2. Postavit `index.html` jako single-file offline prototyp a testovat jej přímo přes `file://`.
3. Udělat slepý test: pět čtenářů dostane jen pět knih a Kolík; minimálně čtyři musí bez ústní pomoci pochopit, co mají udělat, a nikdo nesmí dostat Odpověď přímo z prózy.
4. Přepsat P0 kauzalitu K5 a znovu otestovat kontinuitu K3–K5.
5. Vyrobit 20 kusů QR/NFC karty a 10 kusů USB pilotu; otestovat platformy, sken, hash a fyzický transport.
6. Rozhodnout custody projektu Drát a teprve potom generovat finální QR.
7. Po pilotu vyrobit masovou QR/NFC variantu; USB držet jako volitelný, ověřitelný Kolík.

## Akceptační kritéria

### Příběh

- žádná věta v próze nevysloví Odpověď za čtenáře;
- všechny nezbytné vstupy šifry jsou skutečně přítomné a reprodukovatelné;
- Kopie 00 má jasný přístup, monitoring, geografický rozsah a důvod, proč ji nelze včas vypnout;
- Lhářova porážka je důsledkem jeho systému a činů hrdinů, ne jeho nevysvětlené pasivity;
- modul 214-K-07, Schránkův člověk a péče o vesnici dostanou alespoň stručné uzavření;
- „svět“ se používá jen tam, kde děj skutečně překročil jednu zemi.

### Gadget

- po dvojkliku funguje čtení na podporovaných desktopových prohlížečích bez sítě a bez lokálního serveru;
- bez JavaScriptu zůstávají knihy, navigace a návod dostupné;
- na USB není executable, autorun, makro, privátní klíč ani vzdálený skript;
- každý kus projde plným read-back hashem;
- QR i NFC vedou na stejnou kontrolovanou HTTPS doménu a URL je vytištěná textem;
- obsah je současně zdarma ke stažení a má podepsaný manifest;
- reálný protokol výslovně nedoporučuje připojovat anonymní nalezená USB média;
- Bitcoin QR byl otestován malou reálnou transakcí a custody odpovídá textu.

## Závěr

Jádro finále je správné: Cvok neprozře, sirotek se poprvé stane sám sobě cílem a věc zachrání ti, kdo ji odmítnou držet. Největší práce proto není další mytologie, ale **odstranit okamžiky, kde autor drží čtenáře za ruku příliš pevně, a naopak doplnit okamžiky, kde fyzický svět nedrží vůbec**.

Pro reálný přesah je nejlepší sestava: **zdarma web + stažitelný podepsaný ZIP jako základ; QR/NFC Odkaz jako bezpečná masová fyzická brána; ověřitelný USB Kolík jako volitelná offline a sběratelská kopie.** Tím se zachová „pirátství je feature“, aniž by projekt učil čtenáře připojovat náhodné flashky nebo stavěl celou ságu na křehkém `file://` webu.
