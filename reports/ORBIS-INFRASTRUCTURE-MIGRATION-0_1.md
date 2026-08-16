# ORBIS — Infrastruktur-Migration 0.1

*Abschlussbericht der Phase A. Umbau des Repositories von einer Sammlung einzelner Dokumente zu einer versionierten Sprachplattform. **Die Referenzgrammatik `Orbis-Grammatik-0.9.3.md` wurde während der gesamten Migration nicht verändert** — der Nachweis steht in Abschnitt 11.*

---

## 1. Ausgangszustand

Vor der Migration lagen 16 versionierte Dateien flach im Wurzelverzeichnis:

| Datei | Rolle |
|---|---|
| `Orbis-Grammatik-0.9.3.md` (1153 Zeilen) | Referenzgrammatik, eingefroren |
| `orbis_validator.py` (1153 Zeilen) | Validator — Sprachdaten **hartkodiert** |
| `Orbis-Testkorpus-0_1.md` (3571 Zeilen) | 150 Tests, kanonisch |
| `Orbis-Testkorpus-0.1.md` | Chat-Entwurf, faktisch Archiv |
| `Orbis-Audit-0_1.md`, `Orbis-Testbericht-0_1.md`, `Orbis-Validator-Bericht-0_1.md`, `Orbis-Manus-Schreibtest-0_1.md` | Berichte |
| `Orbis-Testdaten.json`, `orbis_baseline.json` | Daten |
| `README.md`, `CLAUDE.md`, `CHANGELOG.md`, `.github/workflows/orbis-ci.yml`, `decisions/…` | Projektdateien |

**Kernproblem:** Sprachregeln existierten doppelt — als Prosa in der Grammatik und als Python-Konstanten im Validator. Bei wachsendem Lexikon wäre die Divergenz unvermeidlich gewesen.

---

## 2. Neue Architektur

```
language/     Sprachdaten — maschinenlesbare Source of Truth (317 JSON-Dateien)
  metadata/     Sprachmetadaten, Versionen, ID-Präfixe, Statuswerte
  phonology/    Phoneme, Diphthonge, Onsets, Codas, Silbenformen, Silbifizierung, Betonung
  morphology/   Kasus, Nomenklassen, Plural, Kernwörter, Artikel, Adjektive, Pronomen,
                Verben, unregelmäßige Verben, Modale, Wortbildung, Zahlen
  syntax/       Satzbauregeln (ORB-GRAM-SYN-010…025), Präpositionen, Konjunktionen
  lexicon/      281 Lexeme, 131 Konzepte, Wortfamilien, Index, Schemata
  proto/        Lautgesetze §22
  corpus/       150 Testsätze + 71 Grammatikbelege
  findings/     33 Befunde maschinenlesbar
script/       Schrift, getrennt von der Grammatik (manus, magna, traces)
tools/        Werkzeuge — spiegeln die Sprache, definieren sie nicht
  validator/    12 Module: data, phonology, morphology, syntax, lexicon, corpus,
                manus, reports, schema, cli
  lexicon/      Kollisions- und Ähnlichkeitsanalyse
  documentation/ Generator für abgeleitete Markdown-Dokumentation
  migration/    5 einmalige Umbauskripte der Phase A
tests/        92 automatisierte Tests in 6 Suiten
docs/de, docs/en, docs/decisions, docs/generated
reports/      Prüfberichte und eingefrorene Baselines
archive/      Vorfassungen — nie Quelle, nur Beleg
```

**Datenfluss:** `language/*.json` → `tools/validator/data.py` → alle übrigen Module. `data.py` ist die einzige Stelle, an der Sprachdaten in die Werkzeuge gelangen; keine Regel ist mehr in Python hartkodiert.

---

## 3. Verschobene Dateien

| Von | Nach | Grund |
|---|---|---|
| `Orbis-Testkorpus-0.1.md` | `archive/corpus/` | Chat-Entwurf, nicht kanonisch (Git-Historie erhalten, `git mv`) |
| `orbis_validator.py` (Monolith) | `archive/orbis_validator-0_1-monolith.py` | Migrationsgrundlage, als Beleg eingefroren |

Alle übrigen Dateien blieben zunächst am Ort; Verweise in den Governance-Dokumenten wurden auf die neuen Pfade gezogen. Die kanonische Grammatik, das kanonische Testkorpus und die vier Berichte liegen bewusst weiterhin im Wurzelverzeichnis — sie sind die Bezugsgrößen der laufenden Phase.

---

## 4. Neue Dokumente

**Governance (Wurzelverzeichnis):** `ORBIS_CONSTITUTION.md` (20 Artikel) · `CLAUDE.md` (Projektgedächtnis) · `AI_START_HERE.md` · `AGENTS.md` · `CONTRIBUTING.md` · `STATUS.md` · `ROADMAP.md` (Phasen A–K) · `VERSIONING.md` · `TRANSLATION_POLICY.md` · `CHANGELOG.md` · `README.md` (neu, UTF-8 statt der defekten UTF-16-Datei).

**Entscheidungen:** `docs/decisions/DECISIONS.md` (Register) · `ORB-ADR-0001` (entschieden: Sprachdaten als Source of Truth) · `ORB-ADR-0002…0010` als *vorbereitet* eingetragen, inhaltlich aufbereitet in `decisions/Entscheidungsvorlage-0_9_4.md`.

**Fachdokumentation:** `docs/de/` und `docs/en/` mit je rund 19 Kapiteln, aus der Referenzgrammatik geschrieben, mit Paragraphenverweisen und expliziter Kennzeichnung aller offenen Punkte.

**Generiert:** 566 Dateien unter `docs/generated/` (Lexikon-Detailseiten deutsch und englisch, zwei Indizes, Befundregister, Paradigmentabellen), jeweils mit `AUTO-GENERATED — DO NOT EDIT DIRECTLY`.

---

## 5. Neue Datenmodelle

| Schema | Zweck | Kernpunkte |
|---|---|---|
| `lexicon.schema.json` | Lexem | Identität, Sprache, deutsche **kanonische** Bedeutung, englische abgeleitete Bedeutung, Grammatik, Phonologie, Manus, Semantik, Wortfamilie, Etymologie, Gebrauch, Beispiele, Qualität |
| `concept.schema.json` | Bedeutungskonzept | von Lexemen getrennt; Ober-/Unterbegriffe, Domäne — Grundlage der Synonymdifferenzierung |
| `sentence.schema.json` | Korpussatz | Orbis + Deutsch + Englisch, volle Syntaxanalyse, Lexem- und Befundverweise, Rollen |
| `findings.schema.json` | Befund | Typ, Priorität, Status, betroffene Regeln/Wörter/Sätze, Entscheidungs-ID |

**ID-System (stabil, lemma-unabhängig):** `ORB-LEX-nnnnnn` · `ORB-CON-nnnnnn` · `ORB-SENT-nnnnnn` · `ORB-GRAM-PHON/MOR/SYN-nnn` · `ORB-ADR-nnnn` · `ORB-FIND-*`; Befunde behalten zusätzlich ihre gewachsenen Kürzel K-xx/L-xx/U-xx/W-xx.

**Statusmodelle:** Lexeme `draft…rejected`; Regeln `canonical / provisional / open / conflict / deprecated / experimental`; Übersetzungen `missing / draft / derived / reviewed`; Etymologie `documented / reconstructed / provisional / unknown`.

Entscheidend: **Wo die Grammatik schweigt, trägt der Datensatz einen Status und eine Befund-ID — keine erfundene Regel.** Beispiel `language/morphology/tenpct_nouns.json`: `"deklination_plural": {"status": "open", "befund": "L-07"}`.

---

## 6. Lexikonmigration

| Kennzahl | Wert |
|---|---|
| Lexeme | **281** (= Grundformenbestand der Baseline) |
| davon Nomen / Pronomen / Artikel / Verben / Adjektive / Partikeln / Präpositionen / Zahlen / Konjunktionen | 71 / 58 / 36 / 34 / 20 / 20 / 16 / 15 / 11 |
| Konzepte | **131**, von den Lexemen getrennt |
| Wortfamilien | 2 (mel-, tal- — die einzigen in §21.1 belegten) |
| Antonympaare | 9, symmetrisch eingetragen |
| Deutsche Bedeutung | 281/281 |
| Englische Kurzglosse | 281/281, Status `derived` |
| Einträge mit offenen Befunden | 125 |
| Manus blockiert (L-09) | 77 |

**Grenzen bewusst eingehalten:** `de.short` ist die Wörterbuchglosse **unverändert**. `de.definition` ergänzt ausschließlich strukturelle Angaben aus der Grammatik (Klasse, Ableitung, Fundstelle) — keine semantische Anreicherung. Jeder Eintrag trägt deshalb den Befund `W-04` („ausformulierte Definition steht aus"): das ist Designerarbeit, kein Werkzeugoutput. Etymologie steht durchgängig auf `unknown`, weil die Grammatik für einzelne Lexeme keine Herleitungen nennt.

---

## 7. Korpusmigration

150 Sätze als `ORB-SENT-000001…000150`, **Orbis-Formen unverändert übernommen**.

| Status | Anzahl |
|---|---|
| `canonical` | 130 |
| `open` (Regellücke) | 14 |
| `conflict` | 3 |
| `unclear` | 2 |
| `testproblem` | 1 |

Stabilitätsquote **86,7 %** — identisch zur Baseline. Jeder Satz trägt jetzt zusätzlich: englische Übersetzung (150/150, aus dem Deutschen abgeleitet), abstraktes Satzmuster (z. B. `NP-V-NP-NP`), Kasusliste, Lexemverweise und Befund-IDs. Sätze ohne eindeutige Orbis-Form tragen `orbis: null` — es wurde **keine** Form erfunden, um eine Lücke zu füllen. Zusätzlich sind die 71 Belege der Referenzgrammatik als eigener Beispielkorpus erfasst.

---

## 8. Validatorumbau

Aus einer 1153-Zeilen-Datei wurden 12 Module. Der Wurzel-Einstiegspunkt `orbis_validator.py` bleibt bestehen (28 Zeilen Hülle), damit alle dokumentierten Aufrufe, CI-Schritte und Anleitungen unverändert gelten.

**Neue Modi:** `--schema` (Struktur, Pflichtfelder, Referenzintegrität) · `--ids` · `--translations` · `--relations`. Ohne externe Abhängigkeiten — die Schemaprüfung ist selbst geschrieben, damit CI kein `pip install` für die Sprachprüfung braucht.

**`--sim-l09` auf vier Strategien erweitert** (Auftragspunkt 19):

| Strategie | eindeutig | von 77 mehrdeutigen gelöst | Fehlschläge |
|---|---|---|---|
| A — Onset-Maximierung ohne Diphthong-Vorrang | 280/281 | 77 | `suvr-` (gebundene Wurzel) |
| B — nur Diphthong-Vorrang (Minimal-Onset) | 279/281 | 77 | `suvr-`, `taivbreun` (Restcoda *vb*) |
| C — Onset-Maximierung + Diphthong-Vorrang | 280/281 | 77 | `suvr-` |
| D — lexikalisch gespeicherte Silbengrenzen | 0/281 | 0 | 281 (§5 definiert keine) |

Zehn Formen entscheiden A/C und B verschieden (*velkra, velkran, zaldre, kavla, drovna, vresto, melisto, talisto, nestuma, luivresto*). **Ergebnis ist ein Bericht; die Grammatik wurde nicht angefasst.**

---

## 9. Tests

**92 Tests in 6 Suiten**, alle grün:

| Suite | prüft |
|---|---|
| `tests/phonology/` | 19 Konsonanten, 5 Vokale, keine Fremdlaute, 25 Onsets, Diphthongstatus (inkl. *ou* bleibt gesperrt), Coda-Regeln, K-01-Wörter bleiben sichtbar |
| `tests/morphology/` | 45 Endungen, Genus-Endung-Kopplung, **360er-Matrix phonotaktisch sauber**, Deklinationen, Kernwortmuster, L-07 bleibt offen, kein unbestimmter Plural, 6×3-Konjugation, alle 8 unregelmäßigen Verben, Fugenregel, Adjektivkongruenz, Steigerung |
| `tests/lexicon/` | 281 Einträge, ID-Eindeutigkeit, deutsche Bedeutung überall, englische Glosse überall, Konzept- und Relationsverweise gültig, 77 Manus-Ambiguitäten, symmetrische Antonyme |
| `tests/corpus/` | genau 150 Sätze, Kennzahlen unverändert, lückenlose IDs, de+en überall, offene Sätze ohne erfundene Form, alle kanonischen Sätze bestehen die Automatik |
| `tests/manus/` | 281 Formen, 77 mehrdeutig, Tastaturbeispiele eindeutig, *mela* bleibt mehrdeutig, Simulation ändert keine Daten |
| `tests/regression/` | **Ausgabe-Identität gegen die eingefrorene Baseline**, `--strict` grün, `--schema` grün, generierte Doku aktuell |

---

## 10. CI

`.github/workflows/orbis-ci.yml` prüft bei jedem Push und Pull Request:

1. Schema- und Integritätsprüfung der Sprachdaten
2. `--strict` gegen die Befund-Baseline (neuer Befund → rot)
3. Korpus-Regression über 150 Sätze
4. Lexikonprüfung
5. Manus-Zerlegung
6. Unit- und Regressionstests (pytest)
7. Testdaten-JSON parsebar
8. **Prüfsumme der Referenzgrammatik** — eine Änderung an `Orbis-Grammatik-0.9.3.md` bricht den Build

---

## 11. Baseline vorher/nachher — der Migrationsnachweis

Vor dem ersten Umbauschritt wurde die vollständige Werkzeugausgabe eingefroren (`reports/baseline/`). Nach dem Umbau wurde sie erneut erzeugt und verglichen:

| Lauf | Ergebnis |
|---|---|
| `--lexicon` | **byte-identisch** |
| `--examples` | **byte-identisch** |
| `--manus` | **byte-identisch** |
| `--tables` | **byte-identisch** |
| `--corpus Orbis-Testkorpus-0_1.md` | **byte-identisch** |
| `--strict` | Exit 0, 39 bekannte Befunde, keine neuen |
| `--sim-l09` | bewusst erweitert (2 → 4 Strategien); Vorfassung archiviert als `validator-sim-l09-2strategien-vor-erweiterung.txt` |

Zusätzlich wurden alle **47 migrierten Datenstrukturen** direkt gegen die hartkodierten Vorfassungen verglichen — identisch. Die Referenzgrammatik hat seit dem Einchecken **keinen einzigen Commit** (`git log -- Orbis-Grammatik-0.9.3.md`), Prüfsumme unverändert `8bfec2c1810011225ddb870839b6da20`.

**Kennzahlen vorher → nachher:** 150 Tests → 150 · 130 OK → 130 · 14/3/2/1 → 14/3/2/1 · 86,7 % → 86,7 % · 281 Grundformen → 281 Lexeme · 77 Manus-Ambiguitäten → 77 · 29 Audit-Befunde → 29 (+4 Wortschatz-/Dokumentationsbefunde neu dokumentiert, keiner verloren).

---

## 12. Bekannte offene Probleme

Unverändert offen, jetzt maschinenlesbar in `language/findings/findings.json`:

| Priorität | Anzahl | IDs |
|---|---|---|
| P0 | **0** | — |
| P1 | 6 | L-01, L-02, L-03, L-04, L-05, K-05 |
| P2 | 11 | L-06, L-07, L-08, L-09, U-02, U-03, U-04, U-08, W-01, W-02, W-04 |
| P3 | 16 | K-01, K-02, K-03, K-04, L-10, U-01, U-05, U-06, U-07, U-09, U-10, U-11, U-12, U-13, U-14, W-03 |

Neu während der Migration dokumentiert (kein Sprachbefund, sondern ein Datenzustand): **W-04** — die 281 Lexeme tragen die migrierte Wörterbuchglosse und strukturelle Angaben, aber noch keine ausformulierte Definition. Insgesamt führt das Register damit **33 Befunde** (29 aus dem Audit, dazu W-01 bis W-04).

Die Kollisionsanalyse bestätigt unabhängig **W-02** (`velkran` = Akkusativ von `velkra`) als einzige harte Flexionskollision im Bestand; dazu 295 Paare mit Editierdistanz 1, die dokumentiert, aber nicht bewertet sind.

---

## 13. Nicht getroffene Designerentscheidungen

Der Auftrag verlangte ausdrücklich, keine Sprachfrage selbst zu schließen. Offen gelassen und als Vorlage aufbereitet:

- **L-01** Genitivstellung · **L-02** Relativsatzbau · **L-03** Fragewortkasus · **L-04** Reflexivkasus · **L-05** Passiv-Agens · **K-05** Modalverb im Nebensatz
- **L-09** Silbifizierung (Simulation liegt vor, Entscheidung nicht)
- **W-02** `velkran` (Optionen beschrieben, keine Umbenennung vorgenommen)
- **K-01/K-02/K-03/K-04/U-01/U-10/U-14** Redaktionskandidaten — auch diese wurden **nicht** in die Grammatik geschrieben
- **Diphthong `ou`** bleibt gesperrt, solange die Grammatik ihn als offen führt
- **Morphem-Ebene und Wortspuren** ausschließlich als `EXPERIMENTAL / NOT CANONICAL` dokumentiert; die Architektur ist vorbereitet (MorphologyEngine → Syllabifier → ManusComposer), aber kein Zeichen wurde kanonisiert

---

## 14. Empfohlene nächste Schritte

1. **Designerrunde zu den 6 P1-Punkten** anhand von `decisions/Entscheidungsvorlage-0_9_4.md`; Reihenfolge E1 (Relativsatz) und E2 (Modal im Nebensatz) zuerst, da beide das Nebensatz-Endfeld betreffen.
2. **L-09 entscheiden**, weil Orbis Manus und die Tastatur ohne Silbifizierungsregel blockiert sind (Strategie C ist technisch vollständig, aber die Wahl ist Designersache).
3. **0.9.4 schreiben** (Sprachdesigner), einschließlich der Redaktionsfixes.
4. **Datenmodell nachziehen** (Prüfstand): JSON aktualisieren, Baseline neu setzen, Regression fahren — die 20 offenen Testsätze müssen dann `canonical` werden.
5. **Definitionsarbeit W-04**: 281 Lexeme mit ausformulierten deutschen Definitionen versehen, danach englische Fassungen von `derived` auf `reviewed` heben.
6. Erst danach Lexikonausbau in Stufen (500–1000 Kernlexeme), Manus 1.0, Keyboard-MVP.

---

## 15. Konkrete Vorbereitung für Grammar 0.9.4

Was für die nächste Grammatikversion bereits bereitliegt:

- **Entscheidungsvorlage** mit Optionen, Beispielsätzen und Folgekosten je P1-Punkt; alle hypothetischen Formen (*fain, kemen, sen, velkuma* …) sind maschinell phonotaktik- und kollisionsgeprüft.
- **ADR-Register** mit vorbereiteten Einträgen 0002–0010; nach der Entscheidung ist je Punkt nur noch die ADR-Datei zu füllen.
- **Befundregister** mit den Feldern `resolved_version` und `decision_id` — jeder Befund lässt sich mit einem Versionssprung und einer ADR verknüpfen.
- **Regressionsapparat**: Testkorpus, 360er-Matrix, Baseline-Vergleich und CI stehen; eine 0.9.4 wird gegen denselben Apparat gefahren wie 0.9.3.
- **Erwartungswert**: Werden die 6 P1-Punkte entschieden, wechseln 20 Testsätze von `open`/`conflict`/`unclear`/`testproblem` auf `canonical` — die Stabilitätsquote steigt rechnerisch von 86,7 % auf bis zu 100 %, abhängig davon, ob die Entscheidungen neue Testfälle nötig machen.

---

## Verifikationscheckliste (Auftragspunkt 51)

- [x] Orbis-Grammatik 0.9.3 wurde während der Migration nicht semantisch verändert *(Prüfsumme + kein Commit + Baseline-Identität)*
- [x] Deutsch ist offiziell Primary Language *(Verfassung Art. 1, CLAUDE.md, TRANSLATION_POLICY, README)*
- [x] Englisch ist Secondary Official Documentation Language *(Verfassung Art. 2)*
- [x] `ORBIS_CONSTITUTION.md` existiert *(20 Artikel)*
- [x] `CLAUDE.md` existiert *(ausführliches Projektgedächtnis)*
- [x] `AI_START_HERE.md` existiert
- [x] `AGENTS.md` existiert
- [x] `CHANGELOG.md` existiert
- [x] `STATUS.md` existiert
- [x] `ROADMAP.md` existiert *(Phasen A–K)*
- [x] `VERSIONING.md` existiert *(6 Komponenten getrennt versioniert)*
- [x] `TRANSLATION_POLICY.md` existiert
- [x] Lexikon besitzt ein maschinenlesbares Schema
- [x] Concepts und Lexemes sind getrennt *(131 vs. 281)*
- [x] Bestehende Wörter wurden migriert *(281/281)*
- [x] Deutsche Bedeutungen wurden erhalten *(Glossen unverändert)*
- [x] System für englische Übersetzungen existiert *(Felder, Status, Prüfung; 281/281 gefüllt)*
- [x] Synonymrelationen können Bedeutungsunterschiede speichern *(Pflichtfeld, CI-geprüft)*
- [x] Antonyme und semantische Relationen können gespeichert werden *(10 Relationstypen)*
- [x] Wortfamilien können gespeichert werden *(`word_families.json`)*
- [x] Proto-Orbis-Herkunft kann gespeichert werden *(Etymologieblock mit Statusmodell)*
- [x] Corpus besitzt stabile Satz-IDs *(ORB-SENT-000001…000150)*
- [x] Corpus unterstützt Orbis + Deutsch + Englisch *(150/150)*
- [x] Syntaxtransformationen haben eigene Struktur *(`syntax/rules.json`, Satzmuster je Satz, `docs/de/SATZSTELLUNG.md`)*
- [x] Validator liest maschinenlesbare Regeldaten *(`data.py`, keine hartkodierten Regeln mehr)*
- [x] Alte Validatorergebnisse wurden gegen neue verglichen *(6 Läufe, byte-identisch)*
- [x] Bekannte K/L/U-Befunde gingen nicht verloren *(29/29, maschinell gegengeprüft)*
- [x] Manus-Ambiguität L-09 ist weiterhin sichtbar *(77/281, Test sichert die Zahl)*
- [x] Experimentelle Morphem-Ebene wurde NICHT als kanonisch ausgegeben
- [x] Experimentelle Wortspuren wurden NICHT als kanonisch ausgegeben
- [x] CI existiert *(8 Schritte)*
- [x] Tests existieren *(92)*
- [x] Dokumentations-/ID-Validierung existiert *(`--schema`, `--ids`, `--relations`, `--translations`, Generator-`--check`)*
- [x] Kein großer Wortschatz wurde ungeprüft automatisch erfunden *(kein einziges neues Orbis-Wort)*

---

*Erstellt zum Abschluss der Phase A. Die Sprache selbst ist unverändert; verändert wurde nur, wie sie gespeichert, geprüft und dokumentiert wird.*
