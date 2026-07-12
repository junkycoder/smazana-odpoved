# Návrh fyzických gadgetů a distribuční vrstvy

## Doporučení v jedné větě

Základ distribuce má být zdarma stažitelný podepsaný ZIP; fyzickou masovou branou má být QR/NFC **Odkaz** a USB **Kolík** má být volitelná, ověřitelná offline kopie předávaná z ruky do ruky — ne anonymní flashka pohozená na lavičce.

## Tři vrstvy jednoho obsahu

| Vrstva | Co je | Pro koho | Zásada |
|---|---|---|---|
| **Odkaz** | levná černá karta/záložka s QR + NFC + vytištěnou URL | masové šíření, akce, knihovny, kavárny | bezpečná brána ke stažení celého balíku |
| **Kolík** | zapečetěné dual USB-A/USB-C s úplnou offline edicí | čtenář bez sítě, dárce, kurýrské předání | žádný autorun, executable ani exkluzivní obsah |
| **Kopie 00** | kouřově černý polykarbonátový artefakt se zlatými žilkami, Odkazem a Kolíkem | sběratelská/fundraisingová edice | platí se za předmět, nikdy za jedinou kopii pravdy |

Obsah všech tří vrstev musí být totožně dostupný zdarma. Fyzická edice smí přidat materiál, sériové číslo a rituál prvního čtení, ne zamčenou kapitolu nebo nutný klíč.

## Doporučený produkt: kurýrský set

Nejvěrnější projektu není jeden drahý kus, který si majitel vystaví, ale sada určená k rozdělení:

- 1× Odkazová karta pro čtenáře;
- 2× další karta k předání;
- volitelně 1× zapečetěný Kolík s kompletní offline kopií;
- skládací papírový protokol s release ID, SHA-256 hashem a otiskem podpisového klíče;
- jasná věta: „Neznámé nalezené USB nepřipojuj. Vezmi si URL a ověř původ.“

Tím se fyzický předmět chová jako Odkaz, ne jako Horcrux: výrobek je hotový teprve ve chvíli, kdy se část sady rozdá.

## Kolík — technická specifikace prototypu

### Hardware

- 8–16 GB; text, EPUB, PDF, audio a web potřebují zlomek kapacity;
- dual USB-A + USB-C, aby nebyla nutná proprietární redukce; konektor definuje [USB-IF](https://www.usb.org/usb-type-cr-cable-and-connector-specification);
- jedna běžná mass-storage partition ve formátu exFAT; specifikaci zveřejňuje [Microsoft](https://learn.microsoft.com/en-us/windows/win32/fileio/exfat-specification);
- žádná emulace klávesnice, síťové karty nebo virtuální CD mechaniky;
- černé jednoduché tělo, laserové release ID, tamper-evident obal;
- privátní BTC ani podpisové klíče na médiu nikdy nejsou.

### Obsah

```text
KOLIK_00/
├── START-HERE.txt
├── index.html
├── knihy/                    # otevřený Markdown, později EPUB/PDF
├── release-manifest.json
└── SHA256SUMS.txt
```

Prototyp je v [`gadget/kolik-offline/`](../gadget/kolik-offline/). Build vědomě vynechává story bible, zadání, autorské README a placeholderové peněženky.

### Proč jeden `index.html`

Při dvojkliku se web otevře jako `file://`. V tomto režimu mohou ES moduly a lokální požadavky narazit na CORS, service worker potřebuje HTTP(S) a chování `localStorage` pro lokální soubory není definované. Viz [MDN k modulům](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), [MDN k registraci service workeru](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register) a [MDN k localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

Proto finální offline web:

- má inline CSS a klasický inline JavaScript;
- nepoužívá `fetch`, modulové importy, CDN, webfonty ani service worker;
- obsahuje kapitoly už při buildu, nečte je za běhu z disku;
- zůstává čitelný bez JavaScriptu;
- stav skládačky drží jen v paměti aktuální stránky a dovoluje reset/export.

### Integrita a verze

Kolík je neměnný snapshot s release ID. Aktualizace je nový celý ZIP, ne kód, který se z USB automaticky přepisuje. SHA-256 umí odhalit změnu jen proti důvěryhodné referenci; před výrobou se proto podepíše `release-manifest.json` offline vydavatelským klíčem. NIST popisuje hash ve [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) a digitální podpis ve [FIPS 186-5](https://csrc.nist.gov/pubs/fips/186-5/final).

## Bezpečnostní rozhodnutí

Microsoft použití AutoRun pro distribuované aplikace na výměnných médiích nedoporučuje kvůli malwaru ([AutoRun guidance](https://learn.microsoft.com/en-us/windows/win32/shell/autoplay-reg)). Přenosná média obecně vyžadují procedurální, fyzické i technické kontroly ([NIST SP 1334](https://csrc.nist.gov/pubs/sp/1334/final)).

Proto:

- USB se předává z ruky do ruky nebo přes označený safepoint;
- veřejný anonymní drop je QR/NFC karta, ne aktivní periferie;
- žádný soubor se nespouští automaticky;
- výroba používá dohledatelného dodavatele a plný read-back každého kusu;
- obal uvádí release ID, URL a krátký fingerprint;
- reálný protokol v knihách se přepíše tak, aby nenabádal k připojování náhodných nalezených USB.

## Odkaz — QR/NFC karta

Karta má kouřově černý nebo průsvitný polykarbonát, jemné zlaté žilky a žádnou ostrou skleněnou hranu. Nese:

- QR na krátkou projektovou HTTPS URL;
- stejnou URL jako standardní NFC NDEF URI;
- URL vytištěnou lidsky čitelně;
- release ID a krátký hash/fingerprint;
- výzvu ke stažení celého offline ZIPu.

Android podporuje NDEF URI systémově ([Android NFC basics](https://developer.android.com/develop/connectivity/nfc/nfc)); podporované iPhony umějí HTTPS NDEF otevřít přes background tag reading ([Apple Core NFC](https://developer.apple.com/documentation/CoreNFC)). QR a textová URL zůstávají povinná záloha. QR není úložiště knihy — DENSO uvádí jen několik kB kapacity ([QR FAQ](https://www.qrcode.com/en/faq.html)); nese stabilní odkaz na balík.

NFC tag se po testu zamkne read-only. Pokud bude artefakt kovový, musí mít tag ferritovou/on-metal vrstvu; jednodušší první série je polykarbonát.

## „Přečti jednou“ bez falešného DRM

Digitální jednorázovost nelze poctivě vynutit: reset prohlížeče, screenshot nebo kopie souboru ji obejdou. Serverový jednorázový token by navíc vytvořil centrální evidenci čtenářů a první člověk by mohl spálit obsah všem dalším.

Správné řešení je rituální:

- stránka po přečtení lokálně ztmavne;
- čtenář si úlomek převezme do pracovní plochy;
- celý rituál lze vědomě resetovat;
- žádný nutný obsah se nenávratně neničí;
- sběratelská karta může mít fyzickou stírací vrstvu nebo trhací pečeť.

## Sběratelská Kopie 00

Doporučený obsah:

- kouřově černá Odkazová karta se zlatým okrajem, QR/NFC a stírací pečetí;
- černý dual USB Kolík se shodným sériovým číslem;
- papírový protokol s veřejným hashem, fingerprintem a licencí ke kopírování;
- obal bez magnetu vedeného přes NFC anténu;
- žádný exkluzivní děj, tajný seed nebo privátní klíč.

Limitovanost smí platit pro výrobní sérii, ne pro informaci. Designové soubory karty a obalu je vhodné zveřejnit, aby si mohl vlastní Odkaz vyrobit kdokoli.

## Bitcoinové QR — rozhodnutí odložit

Placeholdery `bc1q-DOPLNIT-…` se nesmějí dostat do release. Před generováním QR je potřeba rozhodnout:

1. kdo reálně drží klíče;
2. zda „projekt drát“ bude transparentní projektová peněženka nebo autorská peněženka;
3. jak se reportují příjmy a výdaje;
4. jaký platební URI a fallback podporují cílové peněženky;
5. jaké právní a daňové povinnosti se vztahují na skutečné dary.

Text „klíč drží vesnice celá“ vyžaduje skutečný prahový multisig, ne zkopírovaný jeden privátní klíč. Dokud není custody a odpovědnost rozhodnutá, prototyp peněženky vědomě vynechává.

## Pilot

1. Dokončit a slepě otestovat pětifázovou šifru.
2. Otestovat offline web přes `file://` na Windows, macOS a Linuxu; bez sítě a bez JavaScriptu.
3. Vyrobit 20 QR/NFC karet a 10 USB kusů, ne plnou sérii.
4. Každý USB kus celý přečíst zpět a porovnat hash.
5. Otestovat sken QR na matném i lesklém povrchu a NFC přes finální materiál.
6. Teprve po pilotu rozhodnout výrobu sběratelské Kopie 00.

## Go / no-go kritéria

Do výroby se nejde, dokud:

- čtyři z pěti testovacích čtenářů bez ústní pomoci nesloží správný postup;
- žádný nutný obsah není jen online;
- offline čtení funguje i s vypnutým JavaScriptem;
- manifest je podepsaný a fyzický obal nese jeho fingerprint;
- Kolík neobsahuje executable, autorun, makro ani privátní klíč;
- bezpečnostní instrukce výslovně odmítá připojování anonymních nalezených USB;
- licence dovolující zamýšlené kopírování je zvolená a vložená do balíku.

