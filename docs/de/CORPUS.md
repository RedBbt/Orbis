# ORBIS — Der Satzkorpus: Aufbau, IDs, Rollen, Kennzahlen

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

Dieses Kapitel beschreibt, wie Orbis-Sätze im Repository geführt werden: welche Bestände es
gibt, wie die IDs vergeben sind, welche Rollen ein Satz tragen kann, welche Felder Pflicht
sind, und was mit Sätzen geschieht, die nach 0.9.3 **nicht bildbar** sind.

Der Korpus ist **Prüfmaterial, keine Regelquelle.** Wahrheit ist allein
`Orbis-Grammatik-0.9.3.md`. Weicht ein Korpussatz von der Grammatik ab, gilt die Grammatik,
und die Abweichung ist ein Befund.

---

## 1. Die Bestände

| Bestand | Datei | Sätze | Inhalt |
|---|---|---|---|
| **Testkorpus 0.1** | `Orbis-Testkorpus-0_1.md` (Prosafassung) · `language/corpus/tests/testkorpus-0_1.json` (maschinenlesbar) | 150 | Prüfsätze gegen die eingefrorene Grammatik, mit vollständiger Analyse je Satz |
| **Grammatikbeispiele** | `language/corpus/examples/grammatik-beispiele.json` | 71 | alle im Grammatiktext belegten Orbis-Beispiele, unverändert übernommen |
| **Testdaten** | `Orbis-Testdaten.json` | — | Rohdaten des Validatorlaufs |

Beide JSON-Bestände sind gegen `language/corpus/sentence.schema.json` validierbar.

**Nicht als Quelle verwenden:** `archive/corpus/Orbis-Testkorpus-0.1.md` (Version mit Punkt)
ist der archivierte Chat-Entwurf. Er bleibt als Referenz erhalten, wird nicht bearbeitet und
enthält Fehler, die die Prüffassung korrigiert (u. a. Satz 048: \*loşna → loşnla).

### 1.1 Die Grammatikbeispiele

Die 71 Sätze aus `grammatik-beispiele.json` sind die **Regressionsgrundlage**: Sie stammen
wörtlich aus der Grammatik und müssen mit den Regeldaten in `language/` vereinbar bleiben.
Alle 71 tragen `status = canonical` und die Rolle `example`. Ihre deutschen und englischen
Zeilen sind **null**, weil die Übersetzungen nicht überall Teil des Grammatiktextes sind.

Fundstellenverteilung (Auszug): §25.1 elf Sätze · §25.2 sieben · §12.2 fünf · §14 vier ·
§12.1, §12.3, §13.2, §13.3, §11.3, §17.1, §18.2, §18.3 je drei.

### 1.2 Der Anhang des Testkorpus

`Orbis-Testkorpus-0_1.md` enthält zusätzlich zwei Anhänge, die **keine Sätze** sind und
darum keine `ORB-SENT-`ID tragen:

- die **45-Endungen-Prüftabelle** auf dem ausdrücklich markierten `[TESTFORM]`-Stamm
  **pren-**. Diese 45 Formen sind **keine Wörter des Wortschatzes**; sie existieren
  ausschließlich zum morphologischen Test von §7–§9.
- die **Verbparadigmen** der unregelmäßigen Verben.

---

## 2. Stabile IDs: `ORB-SENT-*`

Jeder Korpussatz trägt eine stabile ID nach dem Muster `^ORB-SENT-[0-9]{6}$`
(`sentence.schema.json`).

| Block | Vergeben an | Bestand |
|---|---|---|
| `ORB-SENT-000001` – `ORB-SENT-000150` | Testkorpus 0.1, in der Reihenfolge der Testnummern | 150 |
| `ORB-SENT-900001` – `ORB-SENT-900071` | Grammatikbeispiele aus 0.9.3 | 71 |

Regeln zur ID-Vergabe (`VERSIONING.md`):

- **IDs werden nie wiederverwendet.** Ein zurückgezogener Satz gibt seine Nummer nicht frei.
- Die ID ist unabhängig von der Testnummer. Das Feld `legacy_nummer` hält die alte Nummer
  aus `Orbis-Testkorpus-0_1.md` fest (1–150; bei den Grammatikbeispielen entfällt es).
- Die ID bleibt konstant, auch wenn der Satz seinen Status ändert — etwa wenn eine
  Regellücke geschlossen wird und aus `open` ein `canonical` wird.

---

## 3. Rollen

Ein Satz kann **mehrere** Rollen gleichzeitig tragen (`rollen` ist ein Array). Das Schema
zählt sechs Werte auf; eine ausformulierte Definition je Rolle steht dort **nicht**. Die
folgende Tabelle nennt darum die belegte Verwendung im Bestand und markiert, was noch
ungenutzt ist.

| Rolle | Belegte Verwendung | Anzahl |
|---|---|---|
| **test** | Prüfsatz: dient dem Nachweis, ob eine Regel trägt | 150 (alle Sätze des Testkorpus) |
| **example** | Lehrbeispiel: Satz ist nach 0.9.3 eindeutig bildbar und darf zitiert werden | 130 im Testkorpus + 71 Grammatikbeispiele |
| **learning** | noch **nicht vergeben** — vorgesehen für das Lernkorpus, `ROADMAP.md` Phase H | 0 |
| **dialogue** | noch **nicht vergeben** | 0 |
| **literary** | noch **nicht vergeben**; der Kurztext §25.2 ist als `example` geführt | 0 |
| **spoken** | noch **nicht vergeben** | 0 |

**Die Kopplung von Rolle und Status ist im Bestand 0.1 ausnahmslos:** Genau die 130
Sätze mit `status = canonical` tragen `["test", "example"]`; die 20 Sätze mit einem Befund
tragen nur `["test"]`. Ein Satz, der nach 0.9.3 nicht eindeutig bildbar ist, ist damit
**nie** ein Lehrbeispiel. Das ist die zentrale Schutzregel des Korpus: Ein nicht
entscheidbarer Fall darf nirgends als vorbildlich zitiert werden.

---

## 4. Pflichtfelder

### 4.1 Nach Schema (`sentence.schema.json`)

| Feld | Pflicht laut Schema | Inhalt |
|---|---|---|
| `id` | ja | `ORB-SENT-######` |
| `status` | ja | `canonical` · `open` · `conflict` · `unclear` · `testproblem` · `draft` |
| `de` | ja | deutsche Quelle, **semantische Autorität** |
| `syntax` | ja | Analyseobjekt, mindestens `syntax.typ` |
| `qualitaet` | ja | mindestens `qualitaet.validatorstatus` |
| `orbis` | typisiert `string \| null` | `null`, wenn nach 0.9.3 nicht eindeutig bildbar |
| `en` | typisiert `string \| null` | aus dem Deutschen abgeleitet, nie aus dem Orbis-Wort erraten |

`additionalProperties` ist auf **false** gesetzt: unbekannte Felder machen einen Satz
ungültig.

### 4.2 Nach Sprachpolitik (`TRANSLATION_POLICY.md` §3.2)

Für den Korpussatz sind **`orbis`, `de`, `en`** und der Übersetzungsstatus **Pflicht**;
ausgenommen sind offene Sätze ohne kanonische Orbis-Form (Abschnitt 7).

> **Abweichung auf Dokumentationsebene, hier gemeldet, nicht behoben:**
> `TRANSLATION_POLICY.md` §3.2 nennt das Feld `translation_status`, das Schema führt es als
> `en_status` (`missing` · `draft` · `derived` · `reviewed`). Kein Sprachbefund — eine
> Uneinheitlichkeit zwischen zwei Governance-Dateien.

Im Bestand 0.1 tragen **alle 150** Sätze `en_status = derived`.

### 4.3 Das Analyseobjekt `syntax`

| Feld | Inhalt | Bestand 0.1 |
|---|---|---|
| `typ` | z. B. „Hauptsatz", „Hauptsatz + Nebensatz" | 150 gefüllt |
| `muster` | abstraktes Satzmuster, z. B. `NP-V-NP` | 130 gefüllt, 20 `null` |
| `v2`, `nebensatz`, `verbklammer` | Stellungsmerkmale | gefüllt, wo entscheidbar |
| `wortstellung_regel` | Regel-ID, z. B. `ORB-GRAM-SYN-010` | im Bestand 0.1 durchgehend `null` |
| `subjekt`, `finites_verb`, `objekte`, `kasus`, `tempus`, `person`, `numerus` | Analyse | gefüllt |

Weitere Felder je Satz: `lexeme` (verwendete Lexeme als `ORB-LEX-`IDs; im Bestand 0.1 bei
den 130 kanonischen Sätzen gefüllt, bei den 20 offenen leer), `regeln` (Paragraphen und/oder
Regel-IDs), `kategorie`, `schwierigkeit`, `themenbereich`.

**Noch nicht gefüllt:** `schwierigkeit` steht bei allen 150 Sätzen auf `unbestimmt`,
`themenbereich` bei allen 150 auf `null`, `wortstellung_regel` bei allen 150 auf `null`. Das
ist offene Redaktionsarbeit, kein Sprachbefund.

### 4.4 Das Qualitätsobjekt `qualitaet`

| Feld | Werte | Bestand 0.1 |
|---|---|---|
| `validatorstatus` | `ok` · `befund` · `nicht_pruefbar` · `ungeprueft` | 130 × `ok`, 20 × `nicht_pruefbar` |
| `befunde` | Liste von Befund-IDs | 20 Sätze tragen genau eine ID |
| `ergebnis_testkorpus` | Originalmarker, z. B. `[OK]` | 150 gefüllt |
| `anmerkung`, `letzte_pruefung` | frei / Datum | — / 2026-08-16 |

---

## 5. Kennzahlen des Testkorpus 0.1

| Ergebnis | Status im JSON | Anzahl | Anteil |
|---|---|---|---|
| **[OK]** | `canonical` | **130** | 86,7 % |
| **[REGELLÜCKE]** | `open` | **14** | 9,3 % |
| **[REGELKONFLIKT]** | `conflict` | **3** | 2,0 % |
| **[REGELUNKLARHEIT]** | `unclear` | **2** | 1,3 % |
| **[TESTPROBLEM]** | `testproblem` | **1** | 0,7 % |
| **Summe** | | **150** | 100 % |

**Stabilitätsquote: 86,7 %** (130 von 150). Sie misst, welcher Anteil der Prüfsätze nach
0.9.3 **eindeutig bildbar** ist — nicht, welcher Anteil „richtig" ist.

Gesamturteil des Testberichts: **NOT READY** für einen direkten Sprung auf 1.0; sechs
P1-Probleme, additiv lösbar (`Orbis-Testbericht-0_1.md`).

### 5.1 Zählkonvention

Der Testkorpus zählt einen offenen Punkt der Grammatik **nur bei den Tests**, die ihn
gezielt prüfen — dort steht der Satz ausdrücklich als „nicht eindeutig bildbar" oder „nicht
eindeutig entscheidbar". Tests, die dieselbe offene Stelle nur **berühren**, aber der
einheitlichen Beispielpraxis der Grammatik folgen (etwa das nachgestellte Genitivattribut),
erhalten **[OK]** mit Verweis auf die Befund-ID.

Die Statistik misst damit **die Zahl der offenen Stellen, nicht die Häufigkeit ihrer
Berührung.** Ohne diese Konvention wäre die Quote nicht vergleichbar: L-01 etwa berührt
zehn Sätze, ist aber ein einziger offener Punkt.

Ein zweiter Hinweis desselben Typs betrifft **K-01**: Formen wie *est, em, granz, trelm,
aul, eird* sind vom Silbenformen-Konflikt K-01 (§5.1) betroffen. Das ist ein zentraler
Befund der Grammatik, kein Fehler einzelner Sätze; die Phonotaktik-Zeile vermerkt ihn, das
Ergebnis bleibt davon unberührt.

---

## 6. Verteilung nach Kategorien

| Block | Kategorie (`kategorie`) | Tests | Sätze | canonical | open | conflict | unclear | testproblem |
|---|---|---|---|---|---|---|---|---|
| A | `einfache_hauptsaetze` | 001–020 | 20 | 20 | — | — | — | — |
| B | `akkusativ_dativ` | 021–035 | 15 | 13 | 2 | — | — | — |
| C | `genitiv` | 036–045 | 10 | 8 | 2 | — | — | — |
| D | `adjektive` | 046–060 | 15 | 13 | — | 1 | 1 | — |
| E | `plural` | 061–070 | 10 | 9 | 1 | — | — | — |
| F | `fragen` | 071–080 | 10 | 7 | 3 | — | — | — |
| G | `negation` | 081–090 | 10 | 10 | — | — | — | — |
| H | `nebensaetze` | 091–105 | 15 | 9 | 3 | 2 | — | 1 |
| I | `modalverben` | 106–115 | 10 | 9 | — | — | 1 | — |
| J | `vergangenheit` | 116–125 | 10 | 10 | — | — | — | — |
| K | `zukunft` | 126–135 | 10 | 10 | — | — | — | — |
| L | `passiv` | 136–140 | 5 | 3 | 2 | — | — | — |
| M | `mai_konditional` | 141–145 | 5 | 5 | — | — | — | — |
| N | `komplex` | 146–150 | 5 | 4 | 1 | — | — | — |
| | **Summe** | | **150** | **130** | **14** | **3** | **2** | **1** |

Die Blöcke B, C, D, F und H tragen ausdrücklich **Stresstests**: B enthält die
Reflexiv-Stresstests, C den Genitiv-Stresstest A, F den Fragen-Stresstest C, H die
Relativ- und Modal-Stresstests. Dass die Befunde sich dort ballen, ist Absicht — der
Testkorpus sucht die offenen Stellen gezielt auf.

**Fünf Kategorien sind vollständig sauber:** einfache Hauptsätze, Negation, Vergangenheit,
Zukunft und `mai`/Konditional bestehen zu 100 %.

---

## 7. Umgang mit nicht bildbaren Sätzen

Die Regel ist einfach und ausnahmslos:

> **Ein Satz, der nach 0.9.3 nicht eindeutig bildbar ist, trägt `orbis = null` und eine
> Befund-ID.** Es wird keine Form geraten, keine Lücke geschlossen, keine Wahl getroffen.

Konkret bedeutet das:

| Feld | Wert bei einem nicht bildbaren Satz |
|---|---|
| `orbis` | `null` |
| `de` | gefüllt — der deutsche Satz existiert unabhängig davon |
| `en` | gefüllt — aus dem Deutschen abgeleitet |
| `status` | `open` · `conflict` · `unclear` · `testproblem` |
| `rollen` | nur `["test"]`, **nie** `example` |
| `qualitaet.validatorstatus` | `nicht_pruefbar` |
| `qualitaet.befunde` | mindestens eine ID |
| `syntax.muster` | `null` |
| `lexeme` | leer |

Die Prosafassung `Orbis-Testkorpus-0_1.md` schreibt an derselben Stelle statt einer
Orbis-Zeile den Text „— nicht bildbar: …" oder „— nicht eindeutig bildbar: …" und führt die
konkurrierenden Kandidaten mit Fragezeichen vor. Diese Kandidaten sind **keine
Orbis-Sätze**; sie dokumentieren, woran die Entscheidung hängt.

### 7.1 Die 20 Sätze im Einzelnen

| ID | Test | Deutsch | Status | Befund |
|---|---|---|---|---|
| ORB-SENT-000033 | 033 | Er sieht sich. | open | L-04 |
| ORB-SENT-000035 | 035 | Sie spricht über sich. | open | L-04 |
| ORB-SENT-000036 | 036 | Das Haus des Mannes ist alt. | open | L-01 |
| ORB-SENT-000039 | 039 | Das Buch meines Freundes ist neu. | open | L-01 |
| ORB-SENT-000051 | 051 | Das gefundene Buch ist alt. | unclear | U-02 |
| ORB-SENT-000060 | 060 | Die Erinnerung vergeht langsam. | conflict | K-04 |
| ORB-SENT-000070 | 070 | Zwei Männer kommen. | open | L-08 |
| ORB-SENT-000074 | 074 | Wen siehst du? | open | L-03 |
| ORB-SENT-000075 | 075 | Wem gibst du das Buch? | open | L-03 |
| ORB-SENT-000076 | 076 | Wessen Buch liest du? | open | L-03 |
| ORB-SENT-000100 | 100 | Der Mann, der kommt, ist mein Freund. | open | L-02 |
| ORB-SENT-000101 | 101 | Die Frau, die ich sehe, spricht. | open | L-02 |
| ORB-SENT-000102 | 102 | Der Mann, dem ich das Buch gebe, wartet. | open | L-02 |
| ORB-SENT-000103 | 103 | Ich weiß, dass der Mann morgen in die Stadt gehen muss. | conflict | K-05 |
| ORB-SENT-000104 | 104 | Sie sagt, dass sie kommt. | testproblem | W-01 |
| ORB-SENT-000105 | 105 | Er weiß, dass sie das Buch nicht lesen kann. | conflict | K-05 |
| ORB-SENT-000111 | 111 | Ich mag das Wort. | unclear | U-03 |
| ORB-SENT-000137 | 137 | Das Haus wird vom Mann gebaut. | open | L-05 |
| ORB-SENT-000138 | 138 | Das Buch wurde von der Frau gelesen. | open | L-05 |
| ORB-SENT-000149 | 149 | Der Mann, der gestern kam, gab dem Kind das Brot des Hauses. | open | L-02 |

### 7.2 Häufigkeit der Befunde im Korpus

| Befund | Sätze | Kurz |
|---|---|---|
| L-02 | 4 | Relativsatzbau |
| L-03 | 3 | Deklination von *kem/kelt* |
| K-05 | 2 | Modalverb im Nebensatz |
| L-01 | 2 | Stellung des Genitivattributs |
| L-04 | 2 | Kasusformen von *se* |
| L-05 | 2 | Agens im Passiv |
| K-04 | 1 | *tolm* adverbial ohne *-un* |
| L-08 | 1 | Syntax der Kardinalzahlen |
| U-02 | 1 | Partizip attributiv |
| U-03 | 1 | Modalverb ohne Infinitiv |
| W-01 | 1 | Wortschatzlücke („sagen") |

### 7.3 Der Sonderfall `testproblem`

**[TESTPROBLEM]** trennt einen Mangel des **Tests** von einem Mangel der **Grammatik**.
Test 104 („Sie sagt, dass sie kommt") scheitert nicht an der Syntax — das *fai*-Gefüge ist
belegt und geregelt —, sondern daran, dass es **kein Verb „sagen"** gibt. *tal-* ist als
„sprechen" definiert (§24.5); *Lo talat, fai lo vandat* verschöbe die Bedeutung ohne
Wörterbuchgrundlage.

Der Fall wird darum als **W-01** (Wortschatzlücke) geführt, nicht als Regellücke, und zählt
nicht gegen die Grammatik. Diese Trennung ist die Voraussetzung dafür, dass die
Stabilitätsquote überhaupt etwas über die Grammatik aussagt.

---

## 8. Prüfung

| Aufruf | Zweck |
|---|---|
| `python3 orbis_validator.py --strict` | Vergleich gegen `orbis_baseline.json`; Exit-Code 1 = **neue** Befunde |
| `python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md` | Korpuslauf; reproduziert 130 [OK] und 86,7 % |
| `--all \| --lexicon \| --examples \| --tables \| --manus` | Teilprüfungen |
| `--json DATEI \| --update-baseline \| --sim-l09` | Ausgabe, Baseline, Silbifizierungssimulation |

`--update-baseline` nur auf ausdrücklichen Auftrag ausführen.

**Was der Validator prüft:** Lexik, Morphologie, Phonotaktik, NP-Kongruenz und die Zuordnung
Präposition → Kasus. **Was er nicht prüfen kann** und darum manuell geprüft ist
(`MANUELLE_PRÜFUNG`): V2-Stellung, Verbklammer, Nebensatz-Endstellung, Kongruenz über
Distanz, Semantik.

Genau deshalb tragen die 20 nicht bildbaren Sätze `validatorstatus = nicht_pruefbar` und
nicht etwa `befund`: Der Validator kann sie nicht bewerten, weil es keine Orbis-Zeile gibt.

---

## 9. Wachstum des Korpus

Für neue Sätze gelten dieselben Regeln:

1. **Deutsch zuerst.** Der deutsche Satz ist die semantische Autorität; Orbis und Englisch
   folgen (`TRANSLATION_POLICY.md` §1, §4).
2. **Keine neuen Wörter.** Fehlt ein Lexem, ist der Satz ein `testproblem` mit
   Wortschatzbefund — nicht ein Anlass, ein Wort zu erfinden (`CLAUDE.md` §2).
3. **Keine Entscheidung durch die Hintertür.** Ein Satz, der eine offene Stelle bräuchte,
   trägt `orbis = null` und die Befund-ID — nicht eine der Varianten (`CLAUDE.md` §3).
4. **Neue ID, nie eine wiederverwendete.**
5. **Regressionslauf vor dem Commit** (Abschnitt 8).

Geplant, aber noch nicht begonnen: das **Lernkorpus** mit den Rollen `learning`, `dialogue`,
`literary` und `spoken`, gestuft nach Lernstufen (`ROADMAP.md` Phase H). Bis dahin bleiben
diese vier Rollenwerte im Schema definiert und im Bestand unbenutzt.

---

## 10. Offene Punkte des Korpus

| Punkt | Art | Kurz |
|---|---|---|
| `schwierigkeit` | Redaktion | alle 150 Sätze auf `unbestimmt` |
| `themenbereich` | Redaktion | alle 150 Sätze auf `null` |
| `syntax.wortstellung_regel` | Redaktion | durchgehend `null`, obwohl die Regel-IDs `ORB-GRAM-SYN-010`…`-025` vorliegen |
| `translation_status` / `en_status` | Uneinheitlichkeit | zwei Namen für dasselbe Feld (Abschnitt 4.2) |
| Rollen `learning`/`dialogue`/`literary`/`spoken` | Bestand | definiert, unbenutzt |
| Deutsch/Englisch der Grammatikbeispiele | Bestand | 71 Sätze mit `de = null`, `en = null` |

Keiner dieser Punkte ist ein Sprachbefund. Die Sprachbefunde stehen in
`Orbis-Audit-0_1.md` §A und maschinenlesbar in `language/findings/findings.json`
(33 Einträge: 5 Konflikte, 10 Lücken, 14 Unklarheiten, 1 Wortschatzlücke,
2 Wortschatzkollisionen, 1 Dokumentationslücke; nach Priorität 6 × P1, 11 × P2, 16 × P3).

---

*Dokumentation zur Grammatik 0.9.3. Bei Abweichung gilt `Orbis-Grammatik-0.9.3.md`.*
