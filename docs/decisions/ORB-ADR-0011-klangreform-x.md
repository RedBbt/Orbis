# ORB-ADR-0011 — Klangreform: Entlastung des Lautes x

- **ID:** ORB-ADR-0011
- **Datum:** 2026-08-18
- **Status:** vorbereitet (Optionen liegen vor, die Sprachdesigner haben noch nicht entschieden)
- **Version:** frühestens Grammar 0.9.4 — `Orbis-Grammatik-0.9.3.md` bleibt eingefroren;
  jede Umsetzung entsteht als **neue** Grammatikdatei plus Datenänderung mit Tests,
  CHANGELOG und neuer Baseline.

## Problem

Auftrag der Sprachdesigner: Orbis wirkt durch den Laut **x** (hinten im Rachen, §2)
überladen und soll klanglich in Richtung Italienisch/Französisch rücken.

Messung (Korpus 0.1, 130 kanonische Sätze, 571 Wörter):

| Kennzahl | Wert |
|---|---|
| Wörter mit x im Korpus | 141 von 571 (**25 %**) |
| davon Artikelformen (xra/xla/xna …) | 107 (**76 %** aller x-Wörter) |
| Lemmata mit x im Lexikon | 38 von 281 |
| x außerhalb von Lemmata | Infinitiv-Suffix **-ex** (vandex, esex …), Negation **xa**, Präfix **xa-** |

Der Eindruck „zu viel x" entsteht also vor allem durch die **Grammatikwörter**, nicht
durch den Wortschatz: Artikel, Infinitivendung und Negation tragen x in fast jeden Satz.

Zwei Fakten aus der Referenzgrammatik sind für die Entscheidung zentral:

1. **j und ç sind tote Buchstaben.** Beide stehen im Alphabet (§2) — j als
   „französisch *jour*", ç als „*tsch*" — aber **kein einziges** der 281 Lemmata
   benutzt sie. Sie sind kollisionsfreie Landeplätze.
2. §23 (flüssige Rede) schwächt Artikel-x **schon heute** ab: „xr-, xl-, xn- am
   Wortanfang: x wird zum Hauch — *xra* → [ʰra]". Die Härte ist in schneller Rede
   teilweise Schriftbild, nicht Klang.

## Simulation (Analysewerkzeug, keine Sprachregel)

Alle 38 x-Lemmata plus Artikelparadigma wurden je Kandidat transformiert und gegen
Phonotaktik (§5) und den Gesamtbestand geprüft:

| Kandidat | Phonotaktik-Verstöße | harte Kollisionen | Verwechslungsnachbarn (Levenshtein 1) | nötige §5.2-Ergänzung |
|---|---|---|---|---|
| **x → j** | 0 | **0** | 20 — exakt so viele wie heute | Onsets **jr, jl, jn** |
| **x → ç** | 0 | **0** | 20 — exakt so viele wie heute | Onsets **çr, çl, çn** |
| x → ş | 0 | **1: xlan → şlan** (existiert bereits: „şlan") | 38 — deutlich schlechter | Onset şn |

Der heutige Bestand hat bereits 20 Levenshtein-1-Nachbarn um die x-Wörter (xra↔vra
usw.); x→j und x→ç verschlechtern das **nicht**. x→ş scheidet praktisch aus.

## Optionen

### Option A — Vollreform x → j („französisch")

Jedes x wird j (/ʒ/ wie *jour*): *jra, jla, jna, vandej, ja, jarn …*
- Passt zur Klangordnung der Grammatik: j ist **Fließlaut** (§3.2), x ist Härtelaut —
  der Fluss-Anteil des Gesamtwortschatzes steigt genau dort, wo die Frequenz sitzt.
- Kollisionfrei, phonotaktisch sauber; §5.2 wird um jr/jl/jn ergänzt (Ersatz für xr/xl/xn).
- Kosten: 38 Lemmata umbenannt, Artikelparadigma, -ex, xa, alle Korpora, Doku, Manus-Umschrift.

### Option B — Vollreform x → ç („italienisch")

Jedes x wird ç (/tʃ/ wie *ciao*): *çra, çla, çna, vandeç, ça, çarn …*
- Klingt italienisch, ist aber laut §3.2 ein **Härtelaut** wie x — der Fluss-Gewinn ist
  gering, und /tʃr/-Anlaute (*çra*) sind artikulatorisch sperrig.
- Kollisionfrei; §5.2 bräuchte çr/çl/çn.

### Option D — Teilreform: nur grammatisches x → j

Artikel (x- → j-), Infinitiv -ex → -ej, Negation xa → ja, Präfix xa- → ja-;
**Wortschatz-Lemmata behalten x** (xarn, xelm, xerp …).
- Reduziert x im Korpus von 25 % auf rund 6 %; x bleibt als seltene lexikalische Farbe
  erhalten (wie harte Laute im Italienischen auch existieren).
- Geringste Umbenennungslast (0 Lexem-Umbenennungen außer Funktionswörtern).
- Preis: x und j teilen sich die Rolle „ehemals x" — etymologische Notiz nötig.

### Option E — Nur Aussprache/Orthographie präzisieren

§23 zur Norm erheben: Artikel-x ist [ʰ]; Schreibung unverändert oder x→' im Artikel.
- Kein Eingriff in den Wortbestand, aber der Schrifteindruck bleibt; erfüllt den
  Auftrag „ändere von allen Orten" vermutlich nicht.

### Option F — Artikelsystem neu entwerfen

Tiefster Eingriff (neue Artikelformen statt Lautersatz); braucht eine eigene
Designrunde und ist hier nur als Route vermerkt.

## Hörproben (SIMULATION — NICHT KANONISCH)

| Nr. | heute | A: x→j | B: x→ç |
|---|---|---|---|
| 1 | Xra valru melat. | Jra valru melat. | Çra valru melat. |
| 23 | Xla veiş dalvat xnaş şirneş xnan brasin. | Jla veiş dalvat jnaş şirneş jnan brasin. | Çla veiş dalvat çnaş şirneş çnan brasin. |
| 30 | Viñ milkamen xlan luiven. | Viñ milkamen jlan luiven. | Viñ milkamen çlan luiven. |
| 53 | Xla girnla kirva trelm est. | Jla girnla kirva trelm est. | Çla girnla kirva trelm est. |
| 92 | Ro maldat, grali xla kirva girn est. | Ro maldat, grali jla kirva girn est. | Ro maldat, grali çla kirva girn est. |
| 107 | Şet dolmaş nunda vandex. | Şet dolmaş nunda vandej. | Şet dolmaş nunda vandeç. |
| 121 | Xla kirva girn vot. | Jla kirva girn vot. | Çla kirva girn vot. |
| 150 | Viñ xa valnamen soñex, grali xra morda span xlaş kavlaş vran xarn est. | Viñ ja valnamen soñej, grali jra morda span jlaş kavlaş vran jarn est. | Viñ ça valnamen soñeç, grali çra morda span çlaş kavlaş vran çarn est. |

Option D unterscheidet sich von A nur bei Wortschatz-Lemmata, z. B. Satz 150:
*Viñ ja valnamen soñej, grali jra morda span jlaş kavlaş vran **xarn** est.*
(„stark" behält sein x.)

## Entscheidung

**Offen.** Die Wahl zwischen A, B, D, E, F treffen die Sprachdesigner
(ORBIS_CONSTITUTION Art. 16; CLAUDE.md Verbot 1 und 2: keine neue Grammatikregel,
keine Umbenennung bestehender Wörter ohne Nutzerentscheidung).

## Auswirkungen (bei A, B oder D)

- **Neue Grammatikversion** (0.9.4 oder höher) als neue Datei; 0.9.3 bleibt unverändert.
- `language/phonology/onsets.json` (§5.2-Gruppen), `language/morphology/articles.json`,
  `verbs.json` (-ex), 38 bzw. (bei D) 2 Lexemdateien, Konzepte, Korpus (150 Sätze),
  Beispiele (71), Doku de/en, generierte Doku, Manus-Schreibtest.
- Alte Formen bleiben als `historical` mit Lautgesetz-Eintrag in
  `language/proto/sound_laws.json` erhalten (x → j/ç als reguläres Lautgesetz — damit
  bleibt jede historische Form regelhaft ableitbar).
- Neue Baseline (`--update-baseline` nach explizitem Auftrag), voller Regressionslauf,
  CHANGELOG-Eintrag, Kompatibilitätsmatrix in `VERSIONING.md` fortschreiben.
- Offener Folgepunkt: Manus-Zeichen für x/j/ç (Gruppen MOR/ISH/KAI, §26) — die
  Schriftzuordnung wandert mit dem Laut; L-10 (Strichstärke) bleibt davon unberührt offen.

## Betroffene Regeln, Wörter, Tests

Regeln: ORB-GRAM-PHON-003 (Onsets), Artikelregel (§18), Infinitivbildung, §2/§3-Tabellen.
Wörter: 38 Lemmata (Liste in `reports/klangreform/simulation-0_1.md`). Tests: alle 150
Korpustests werden transformiert neu belegt; `tests/regression/test_baseline.py`
erhält nach Umsetzung eine neue Baseline.
