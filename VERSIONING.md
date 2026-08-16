# VERSIONING — Versionierungsregeln fuer Orbis

Status: verbindlich
Gilt fuer: Repository RedBbt/Orbis, alle Komponenten (Grammar, Lexicon, Manus, Keyboard, Corpus, Tools)
Bezug: CLAUDE.md, TRANSLATION_POLICY.md, CHANGELOG.md, Orbis-Grammatik-0.9.3.md (READ ONLY),
Orbis-Audit-0_1.md, decisions/Entscheidungsvorlage-0_9_4.md

Dieses Dokument regelt, wie Orbis-Komponenten versioniert werden, was einen
Versionssprung ausloest und welche Pruefungen dabei verpflichtend sind. Es regelt
nicht den Inhalt der Sprache Orbis selbst; sprachliche Entscheidungen treffen
ausschliesslich die Sprachdesigner.

---

## 1. Grundsatz: getrennte Versionierung

Orbis ist kein einzelnes Produkt, sondern ein Verbund aus mehreren Ebenen mit
unterschiedlicher Reife. Jede Ebene traegt eine **eigene, unabhaengige
Versionsnummer**. Es gibt keine gemeinsame "Orbis-Version" und keine
Sammelversion, die alle Komponenten zusammenfasst.

| Komponente | Aktuelle Version | Status | Primaerartefakte |
|---|---|---|---|
| Orbis Grammar | 0.9.3 | eingefroren (READ ONLY) | `Orbis-Grammatik-0.9.3.md`, `language/syntax/`, `language/morphology/`, `language/phonology/` |
| Orbis Lexicon | 0.1 | im Aufbau | `language/lexicon/`, IDs `ORB-LEX-*`, `ORB-CON-*` |
| Orbis Manus | 0.x | Konzept | `script/manus/`, `script/magna/`, `Orbis-Manus-Schreibtest-0_1.md`, IDs `ORB-MANUS-*` |
| Orbis Keyboard | 0.x | geplant | `keyboard/` (Layout, Belegung; noch ohne freigegebene Fassung) |
| Orbis Corpus | 0.1 | kanonisch | `Orbis-Testkorpus-0_1.md`, `language/corpus/`, IDs `ORB-SENT-*` |
| Orbis Tools | 0.2 | in Nutzung | `orbis_validator.py`, `tools/validator/`, `tools/migration/`, `orbis_baseline.json` |

Erlaeuterung zu den Statuswerten:

- **eingefroren**: Die Fassung wird nicht mehr geaendert, auch nicht redaktionell.
  Aenderungen entstehen nur als neue Datei einer neuen Version.
- **kanonisch**: Die Fassung ist die verbindliche Wahrheit fuer ihre Ebene und
  wird gepflegt, aber nicht eingefroren.
- **im Aufbau / Konzept / geplant**: Die Fassung ist unvollstaendig; Verweise
  darauf duerfen nicht als abgeschlossene Festlegung dargestellt werden.

Die Ebenen `0.x` bei Manus und Keyboard bedeuten ausdruecklich, dass noch keine
nummerierte Freigabe existiert. Solange das so ist, wird in Berichten `0.x`
geschrieben und keine Scheingenauigkeit erzeugt.

---

## 2. Warum getrennt versioniert wird

Der zentrale Grund: **die Reifegrade laufen auseinander, und eine gemeinsame
Nummer wuerde die schwaechste Ebene zur Bremse aller anderen machen.**

- Die Grammatik kann 1.0 erreichen, waehrend das Lexikon erst bei 0.2 steht. Ein
  vollstaendiges, konfliktfreies Regelwerk ist ein anderer Meilenstein als ein
  vollstaendiger Wortschatz; beides gleichzeitig zu verlangen, verzoegert beides.
- Umgekehrt darf ein wachsendes Lexikon die Grammatik nicht scheinbar
  "veraendern". Neue Lexeme sind additiv und beruehren die Regelbasis nicht.
- Manus und Keyboard haengen an offenen Befunden (L-09 Mehrdeutigkeit der
  Zerlegung, L-10 undefinierte Strichstaerken, U-10 Tastenzahl in §26.8). Diese
  Befunde blockieren die Schrift- und Tastaturebene, nicht aber die Grammatik.
- Die Werkzeuge folgen einem eigenen Rhythmus: `orbis_validator.py` wird
  fortlaufend erweitert, ohne dass sich an der Sprache etwas aendert. Ein
  Werkzeug-Release ist kein Sprach-Release.
- Berichte und Audits muessen praezise sagen koennen, *welche* Ebene sich geaendert
  hat. Eine Sammelnummer wuerde genau diese Information vernichten.

Konsequenz fuer die Praxis: Jede Aussage ueber "die Orbis-Version" ist
unvollstaendig. Korrekt ist immer die Nennung von Komponente plus Version, zum
Beispiel "Orbis Grammar 0.9.3 mit Orbis Corpus 0.1".

---

## 3. Semantik der Versionsspruenge je Komponente

Alle Komponenten verwenden das Schema `MAJOR.MINOR[.PATCH]`. Was ein Sprung
bedeutet, ist jedoch **je Komponente eigens definiert**, weil "inkompatibel" auf
jeder Ebene etwas anderes heisst.

### 3.1 Orbis Grammar

| Sprung | Bedeutung | Beispiele |
|---|---|---|
| **Major** | Strukturelle Regelaenderung: eine bestehende Regel wird ersetzt, umgekehrt oder in ihrer Wirkung eingeschraenkt. Bestehende korrekte Saetze koennen dadurch falsch werden. | Aenderung der Grundwortstellung, Umbau des Kasussystems, Wegfall eines Affixes |
| **Minor** | Neue Regel, rein additiv: bisher Ungeregeltes wird geregelt, ohne bestehende Regeln zu entwerten. Bisher korrekte Saetze bleiben korrekt. | Schliessung von L-01 bis L-05, Aufloesung von K-05 |
| **Patch** | Redaktion ohne Regelwirkung: Tippfehler, Nummerierung, Formulierungsschaerfe, Beispielkorrekturen. Die Regelmenge bleibt identisch. | Korrektur von U-10 (§26.8: 19 Konsonanten + 1 Vokaltraeger statt "20 Konsonantentasten") |

Wichtig: Der Uebergang **0.9.3 → 0.9.4** ist nach dieser Definition ein
Minor-Sprung. Der Testbericht 0.1 stuft die sechs P1-Probleme (L-01 Genitivstellung,
L-02 Relativsatz, L-03 Fragewortkasus, L-04 Reflexivpronomen, L-05 Passiv-Agens,
K-05 Modalverb im Nebensatz) ausdruecklich als **additiv loesbar** ein — deshalb
lautet das Urteil "NOT READY fuer einen direkten 1.0-Sprung", nicht "Major noetig".

Ein Grammar-**1.0** setzt zusaetzlich voraus, dass kein P0 offen ist, alle P1
entschieden sind und die Stabilitaetsquote des kanonischen Korpus die von den
Sprachdesignern festgelegte Schwelle erreicht. Die Schwelle selbst ist noch nicht
festgelegt: `[REGELLUECKE]`-artige Governance-Luecke, zu entscheiden per ADR.

### 3.2 Orbis Lexicon

| Sprung | Bedeutung | Beispiele |
|---|---|---|
| **Major** | Bedeutungsumbau: bestehende Lexeme aendern ihre kanonische deutsche Bedeutung, werden zurueckgezogen oder neu abgegrenzt. Bestehende Uebersetzungen und Korpussaetze koennen ungueltig werden. | Neuzuschnitt eines Konzeptfelds, Ruecknahme eines Lexems |
| **Minor** | Neue Lexeme oder neue Konzepte, additiv. Bestehende Eintraege bleiben unveraendert gueltig. | Schliessung von W-01, Ergaenzung von `ORB-LEX-*`-Eintraegen |
| **Patch** | Redaktion ohne Bedeutungswirkung: Feldformatierung, ergaenzte englische Ableitung nach TRANSLATION_POLICY.md, Quellenangaben, Tippfehler in Kommentarfeldern | Nachtragen einer fehlenden `en`-Ableitung |

Die deutsche Bedeutungsangabe ist die semantische Autoritaet (TRANSLATION_POLICY.md).
Eine Aenderung ausschliesslich an einer englischen Ableitung ist deshalb nie ein
Major-Sprung; weicht sie inhaltlich ab, ist das ein Befund und kein Versionsanlass.

Neue Lexeme entstehen ausschliesslich auf expliziten Auftrag der Sprachdesigner
(CLAUDE.md). Ein Minor-Sprung des Lexikons ist damit immer die Folge einer
Beauftragung, nie das Ergebnis einer Werkzeuglaufzeit.

### 3.3 Orbis Manus

| Sprung | Bedeutung | Beispiele |
|---|---|---|
| **Major** | Aenderung der Zeichenzuordnung oder der Zerlegungslogik: bereits geschriebene Texte werden anders oder gar nicht mehr lesbar. | Neuzuweisung eines Grundzeichens, Umbau der Silbengliederung |
| **Minor** | Neue Zeichen, neue Varianten oder erstmalige Festlegung eines bisher undefinierten Merkmals, ohne bestehende Zeichen umzudeuten. | Festlegung der Strichstaerke fuer `f s ş x v z j ç` (L-10) |
| **Patch** | Redaktion und Darstellung ohne Wirkung auf Lesbarkeit oder Zuordnung. | Korrektur der Tastenzahl-Angabe in §26.8 (U-10) |

Manus-Regeln und Grammatikregeln werden nicht vermischt (CLAUDE.md). Ein
Manus-Sprung loest daher **keinen** Grammar-Sprung aus und umgekehrt. Ausnahme
ist der Fall, dass eine Designer-Entscheidung beide Ebenen zugleich betrifft;
dann werden zwei getrennte Versionsspruenge gefuehrt, die im selben ADR begruendet sind.

Der Befund L-09 (77 von 281 Grundformen mehrdeutig zerlegbar) ist fuer die
Grammatik P2, fuer Manus und Keyboard aber blockierend. Solange er offen ist,
bleibt Manus bei `0.x` und Keyboard ohne nummerierte Fassung.

### 3.4 Orbis Keyboard

Keyboard folgt der Manus-Semantik mit einer Zusatzbedingung: Ein Keyboard-Sprung
setzt eine passende, freigegebene Manus-Version voraus. Eine Tastaturbelegung
ohne festgelegte Zeichenmenge ist nicht versionierbar. Bis dahin gilt `0.x` =
"geplant, keine freigegebene Fassung".

### 3.5 Orbis Corpus

| Sprung | Bedeutung |
|---|---|
| **Major** | Umbau des Testkorpus: Tests werden entfernt oder ihre Erwartung wird umgedreht; frueher Ergebniszahlen sind nicht mehr vergleichbar. |
| **Minor** | Neue Tests, additiv. Bestehende Tests und ihre IDs bleiben unveraendert. |
| **Patch** | Redaktion an Testtexten ohne Aenderung des erwarteten Ergebnisses. |

Test-IDs und `ORB-SENT-*`-IDs werden nie wiederverwendet. Ein zurueckgezogener
Test wird als zurueckgezogen markiert, nicht geloescht und nicht ueberschrieben.
Der aktuelle Stand von Corpus 0.1: 150 Tests, 130 OK, 14 REGELLUECKE,
3 REGELKONFLIKT, 2 REGELUNKLARHEIT, 1 TESTPROBLEM, Stabilitaetsquote 86,7 %.

### 3.6 Orbis Tools

| Sprung | Bedeutung | Beispiele |
|---|---|---|
| **Major** | Aenderung der Aufrufschnittstelle oder des Ausgabeformats, die bestehende Aufrufe oder CI-Konfigurationen bricht. | Umbenennung oder Wegfall eines Schalters, inkompatibles JSON-Schema, geaenderte Exit-Code-Bedeutung |
| **Minor** | Neue Pruefungen, neue Schalter, neue Werkzeuge — rueckwaertskompatibel. | Ergaenzung eines Migrationswerkzeugs unter `tools/migration/` |
| **Patch** | Fehlerbehebung ohne Schnittstellenaenderung; die Menge der gemeldeten Befunde bleibt gleich oder wird korrekter. | Behebung eines Falschalarms |

Der Validator spiegelt die Grammatik nur wider; er ist nie ihre Quelle
(CLAUDE.md). Eine Abweichung zwischen Validator und Grammatik ist ein Befund
und wird gemeldet, nicht durch eine Werkzeugversion "weggefixt".

Eine Aenderung von `orbis_baseline.json` ist **kein** Tools-Versionssprung,
sondern ein dokumentationspflichtiger Vorgang: `--update-baseline` wird nur nach
Ruecksprache bzw. auf expliziten Auftrag ausgefuehrt (CLAUDE.md), und die neue
Befundzahl wird im CHANGELOG vermerkt. Aktueller Stand: 39 bekannte Befunde.

---

## 4. Dateinamenskonvention

- **Regel:** Versionsnummern in Dateinamen werden mit **Unterstrich** geschrieben:
  `Orbis-Testkorpus-0_1.md`, `Orbis-Audit-0_1.md`, `Orbis-Testbericht-0_1.md`,
  `decisions/Entscheidungsvorlage-0_9_4.md`.
- **Ausnahme:** Die Referenzgrammatik traegt ihre Version mit **Punkten**:
  `Orbis-Grammatik-0.9.3.md`. Diese Ausnahme ist historisch und wird nicht
  nachtraeglich vereinheitlicht, weil die Datei eingefroren ist.
- **Archivfassung:** `archive/corpus/Orbis-Testkorpus-0.1.md` (mit Punkt) ist der archivierte
  Chat-Entwurf. Er wird nicht bearbeitet und nicht als Quelle verwendet. Der
  Punkt im Namen ist hier kein Formatfehler, sondern das Unterscheidungsmerkmal
  zur kanonischen Fassung `Orbis-Testkorpus-0_1.md`.
- Verzeichnisbasierte Artefakte unter `language/`, `script/`, `tools/`, `tests/`,
  `docs/` und `reports/` tragen die Version im Inhalt (Metadatenfeld), nicht im
  Dateinamen. Der Dateiname bleibt dort stabil, damit Verweise nicht bei jedem
  Versionssprung brechen.
- Historische Fassungen wandern nach `archive/` und behalten ihren
  Originalnamen. Sie werden nie ueberschrieben.

Merksatz: Unterstrich ist die Regel, der Punkt markiert entweder die eingefrorene
Grammatik oder die Archivfassung des Korpus — nie etwas Drittes.

---

## 5. Was eine neue Grammatikversion ausloest

Eine neue Grammatikversion entsteht **ausschliesslich durch entschiedene ADRs**
(`ORB-ADR-*`, abgelegt unter `docs/decisions/`). Kein anderer Vorgang loest sie aus.

Insbesondere loesen **keine** neue Grammatikversion aus:

- ein Testlauf, ein Audit oder ein Bericht,
- ein neuer Befund (`K-xx`, `L-xx`, `U-xx`, `W-xx`),
- eine Validator-Aenderung,
- eine Interpretation, eine Plausibilitaetsannahme oder eine "offensichtliche" Korrektur.

Befunde sind **Eingangsmaterial** fuer Entscheidungen, nicht die Entscheidung
selbst. Regelluecken und Regelkonflikte werden markiert, nicht entschieden
(CLAUDE.md).

Der Weg von einem Befund zu einer neuen Grammatikversion:

1. **Befund** entsteht im Audit oder Testlauf und erhaelt eine ID
   (`K-01..K-05`, `L-01..L-10`, `U-01..U-14`, `W-01`).
2. **Aufbereitung** als Entscheidungsvorlage mit Optionen und Folgekosten,
   ohne Empfehlung als Festlegung (`decisions/Entscheidungsvorlage-0_9_4.md`).
3. **Entscheidung** durch die Sprachdesigner, festgehalten als ADR mit Status
   "entschieden" und Angabe der betroffenen Befund-IDs.
4. **Neue Datei** mit der neuen Versionsnummer. Die alte Fassung wird nie
   ueberschrieben (CLAUDE.md); `Orbis-Grammatik-0.9.3.md` bleibt unveraendert
   bestehen.
5. **Regressionslauf** nach Abschnitt 6.
6. **CHANGELOG-Eintrag** mit Nennung der Komponente, der neuen Version und der
   geschlossenen Befund-IDs.

Ein ADR im Status "offen", "in Diskussion" oder "abgelehnt" loest nichts aus. Ein
ADR kann mehrere Befunde zugleich schliessen; mehrere ADRs koennen in einer
Version zusammengefasst werden. Die Zuordnung ADR → Version wird im ADR selbst
und im CHANGELOG dokumentiert, damit jederzeit nachvollziehbar bleibt, welche
Entscheidung welche Regel erzeugt hat.

Fuer alle anderen Komponenten gilt sinngemaess dasselbe Prinzip bei
inhaltlichen Aenderungen (Lexicon, Manus, Keyboard, Corpus). Tools sind davon
ausgenommen: Werkzeugaenderungen brauchen kein ADR, solange sie die Sprache nicht
beruehren.

---

## 6. Regressionspflicht bei jedem Versionswechsel

Vor jedem Versionswechsel **jeder** Komponente — und vor jedem Commit, der
Sprachdaten oder den Validator aendert — ist der Regressionslauf verpflichtend:

```
python3 orbis_validator.py --strict
python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md
```

Regeln dazu:

- `--strict` vergleicht gegen `orbis_baseline.json`. **Exit-Code 1 = NEUE Befunde
  → nicht committen, nicht freigeben.** Der Versionswechsel ist blockiert, bis die
  neuen Befunde entweder behoben oder als bewusste Folge der Entscheidung
  dokumentiert und per Auftrag in die Baseline uebernommen sind.
- `--update-baseline` wird nur nach Ruecksprache bzw. auf expliziten Auftrag
  ausgefuehrt. Eine stillschweigende Baseline-Anpassung, um einen Versionswechsel
  durchzubekommen, ist unzulaessig.
- Der Korpuslauf gegen `Orbis-Testkorpus-0_1.md` liefert die Stabilitaetsquote.
  Die Quote vor und nach dem Versionswechsel wird im CHANGELOG genannt; ein
  Absinken ist begruendungspflichtig.
- Weitere Laeufe nach Bedarf: `--all`, `--lexicon`, `--examples`, `--tables`,
  `--manus`, `--json DATEI`. `--sim-l09` ist ein Analysewerkzeug und **keine
  Sprachregel**; seine Ausgabe wird nie als Regel zitiert (CLAUDE.md).
- Die CI (`.github/workflows/orbis-ci.yml`) fuehrt den Strict-Lauf ebenfalls aus.
  Ein roter CI-Lauf blockiert den Versionswechsel unabhaengig vom lokalen Ergebnis.
- Bei einem Grammar-Versionswechsel wird zusaetzlich geprueft, ob der Validator
  die neue Regelfassung ueberhaupt abbildet. Tut er das nicht, ist das ein
  Tools-Befund und ein Tools-Minor — nicht ein Grund, die Grammatik anzupassen.

---

## 7. Kompatibilitaetsmatrix

Die Matrix sagt, welche Komponentenstaende gemeinsam als geprueft gelten. "Geprueft"
heisst: gegen diese Kombination wurde der Regressionslauf nach Abschnitt 6
ausgefuehrt.

### 7.1 Lexicon zu Grammar

| Lexicon | Grammar 0.9.3 | Grammar 0.9.4 (geplant) | Grammar 1.0 (geplant) |
|---|---|---|---|
| **0.1** | geprueft (aktueller Stand) | erwartet kompatibel (additive Minor-Aenderung) | offen |
| **0.2** (geplant) | erwartet kompatibel | erwartet kompatibel | offen |

Begruendung: Solange Grammar-Spruenge Minor bleiben (additive Regeln), bleibt
jedes bestehende Lexem gueltig. Erst ein Grammar-Major koennte Lexikoneintraege
entwerten; dann ist die Matrix neu zu pruefen und nicht fortzuschreiben.

### 7.2 Gesamtstand aller Komponenten

| Komponente | Version | Passt zu Grammar 0.9.3 | Anmerkung |
|---|---|---|---|
| Orbis Lexicon | 0.1 | ja, geprueft | W-01 offen (Wortschatzluecke) |
| Orbis Corpus | 0.1 | ja, geprueft | 150 Tests, Stabilitaetsquote 86,7 % |
| Orbis Tools | 0.2 | ja, geprueft | Baseline `orbis_baseline.json`, 39 bekannte Befunde |
| Orbis Manus | 0.x | teilweise | blockiert durch L-09, L-10; U-10 als Redaktionsfehler in §26.8 |
| Orbis Keyboard | 0.x | nein | keine freigegebene Fassung; setzt eine nummerierte Manus-Version voraus |

Lesehilfe:

- **geprueft** — Regressionslauf gegen diese Kombination durchgefuehrt, ohne neue Befunde.
- **erwartet kompatibel** — aus der Sprungsemantik abgeleitet, aber noch nicht
  durch einen Lauf bestaetigt. Keine Freigabe.
- **teilweise** — nutzbar, aber mit offenen Befunden, die die Ebene blockieren.
- **offen** — noch nicht bewertbar, weil die Zielversion inhaltlich nicht feststeht.
- **nein** — nicht als kompatible Kombination fuehrbar.

Die Matrix wird bei jedem Versionswechsel fortgeschrieben. Eine Zeile wird erst
auf "geprueft" gesetzt, wenn der Regressionslauf nach Abschnitt 6 tatsaechlich
gelaufen ist; eine Erwartung ersetzt keinen Lauf.

---

## 8. Zusammenfassung in fuenf Saetzen

1. Jede Orbis-Komponente traegt ihre eigene Version; eine Sammelversion gibt es nicht.
2. Was Major, Minor und Patch bedeuten, ist je Komponente eigens definiert.
3. Dateinamen tragen Unterstrich-Versionen; Punkte markieren nur die eingefrorene
   Grammatik und die Archivfassung des Korpus.
4. Eine neue Grammatikversion entsteht nur aus entschiedenen ADRs, nie aus Befunden,
   Berichten oder Werkzeuglaeufen.
5. Kein Versionswechsel ohne bestandenen Regressionslauf und fortgeschriebene
   Kompatibilitaetsmatrix.

---

*Claude Code wird in diesem Projekt ausschliesslich als Pruef- und
Werkzeug-Assistent eingesetzt, nicht als Sprachdesigner.*
