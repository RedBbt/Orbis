# Changelog

Alle nennenswerten Änderungen am Projekt ORBIS werden in dieser Datei dokumentiert.
Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/).
Versionierung (Governance): Orbis Grammar (aktuell 0.9.3), Orbis Lexicon (0.x), Orbis Manus (0.x) und Orbis Keyboard (0.x) werden getrennt versioniert.

## [Unreleased]

### Geplant
- Designentscheidungen für Grammatik 0.9.4 zu den Befunden L-01 bis L-05 und K-05 (durch die Sprachdesigner); Vorlage: `decisions/Entscheidungsvorlage-0_9_4.md`.
- Redaktionskorrekturen K-01, K-03, K-04, U-01, U-10. (U-14 und K-02 sind Grenzfälle: die Korrekturform hängt an einer Designer-Entscheidung, siehe Entscheidungsvorlage.)

## Infrastruktur 0.1 — Sprachplattform (Phase A) — 2026-08-16

Umbau des Repositories zu einer versionierten Sprachplattform. **Die Sprache selbst wurde
nicht verändert:** alle Validator-Läufe sind byte-identisch zur eingefrorenen Baseline,
die Referenzgrammatik hat keinen Commit erhalten. Nachweis: `reports/ORBIS-INFRASTRUCTURE-MIGRATION-0_1.md`.

### Hinzugefügt
- `language/` als maschinenlesbare Source of Truth (317 JSON-Dateien): Phonologie, Morphologie,
  Syntax, Proto-Orbis, Metadaten, Lexikon, Korpus, Befunde. Offene Regeln tragen
  `status: open|conflict|unclear` mit Befund-ID statt einer erfundenen Regel.
- Lexikon: 281 Lexeme (`ORB-LEX-*`) und 131 davon getrennte Konzepte (`ORB-CON-*`),
  Wortfamilien, 9 Antonympaare; deutsche Bedeutung kanonisch, englische abgeleitet (281/281).
- Korpus: 150 Sätze als `ORB-SENT-*` mit Orbis unverändert, Deutsch, Englisch, Syntaxanalyse,
  Satzmuster und Lexemverweisen; zusätzlich die 71 Grammatikbelege als eigener Beispielkorpus.
- Schemata für Lexem, Konzept, Satz und Befund; Prüfung ohne externe Abhängigkeiten.
- Befundregister mit 33 Einträgen (29 aus dem Audit erhalten, dazu W-01 bis W-04).
- Governance: `ORBIS_CONSTITUTION.md`, `AI_START_HERE.md`, `AGENTS.md`, `CONTRIBUTING.md`,
  `STATUS.md`, `ROADMAP.md`, `VERSIONING.md`, `TRANSLATION_POLICY.md`.
- Entscheidungsregister `docs/decisions/` mit `ORB-ADR-0001` (entschieden) und 0002–0010
  (vorbereitet, Optionen in `decisions/Entscheidungsvorlage-0_9_4.md`).
- Dokumentationsgenerator `tools/documentation/`: 566 Seiten mit AUTO-GENERATED-Kopf,
  `--check` hält sie in CI aktuell.
- Kollisionsanalyse `tools/lexicon/similarity.py` (Homonymie, Flexionskollision,
  Editierdistanz, Phonemähnlichkeit, Manus-Silhouette).
- 92 automatisierte Tests in 6 Suiten.
- Zweisprachige Fachdokumentation unter `docs/de/` und `docs/en/`.

### Geändert
- Validator ist ein Paket (`tools/validator/`, 12 Module) und liest seine Regeldaten aus
  `language/`. `orbis_validator.py` bleibt als Einstiegspunkt bestehen; alle dokumentierten
  Aufrufe gelten unverändert.
- `--sim-l09` deckt jetzt vier Silbifizierungsstrategien ab (A–D) — Analysewerkzeug, keine Regel.
- Neue Modi `--schema`, `--ids`, `--translations`, `--relations`.
- CI prüft zusätzlich Schema, Lexikon, Manus, Tests, generierte Doku und die Prüfsumme der
  Referenzgrammatik.

### Verschoben
- `Orbis-Testkorpus-0.1.md` → `archive/corpus/` (Chat-Entwurf, mit Git-Historie).
- Monolithischer Validator → `archive/orbis_validator-0_1-monolith.py`.

### Unverändert (ausdrücklich)
- `Orbis-Grammatik-0.9.3.md` — keine Zeile, keine stille Korrektur.
- Kennzahlen: 150 Tests, 130 OK, 14/3/2/1, 86,7 %, 281 Grundformen, 77 Manus-Ambiguitäten.
- Keine Designerentscheidung getroffen: L-01…L-05, K-05, L-09 und W-02 bleiben offen;
  Morphem-Ebene und Wortspuren ausschließlich als EXPERIMENTAL dokumentiert.

## Stabilitätstest 0.1 — 2026-08-16

### Hinzugefügt
- `Orbis-Audit-0_1.md`: Audit der Regelbasis mit Befund-IDs K-01..K-05 (Regelkonflikte), L-01..L-10 (Regellücken), U-01..U-14 (Unklarheiten).
- `orbis_validator.py`: automatischer Validator (`--all`, `--lexicon`, `--examples`, `--corpus DATEI`, `--tables`, `--manus`, `--json DATEI`, `--strict` mit Baseline-Vergleich gegen `orbis_baseline.json`, `--update-baseline`, `--sim-l09` als Silbifizierungs-Simulation ohne Sprachregel-Status).
- `Orbis-Testkorpus-0_1.md`: kanonisches Testkorpus mit 150 Tests. Ergebnis: 130 OK, 14 REGELLÜCKE, 3 REGELKONFLIKT, 2 REGELUNKLARHEIT, 1 TESTPROBLEM — Stabilitätsquote 86,7 %.
- `Orbis-Validator-Bericht-0_1.md` und `Orbis-Testbericht-0_1.md`: Berichte zum Testlauf. Urteil: NOT READY für einen direkten 1.0-Sprung; 6 P1-Probleme, additiv lösbar.
- `Orbis-Manus-Schreibtest-0_1.md`: Schreibtest Orbis Manus; 77 von 281 Grundformen mehrdeutig zerlegbar (Befund L-09).
- `Orbis-Testdaten.json`: maschinenlesbare Testdaten.

### Geprüft
- Unabhängige Verifikation des Testlaufs ohne Fehlerbefund (Claude Code als Prüfwerkzeug).

## Grammatik 0.9.3 — 2026-08-16

### Hinzugefügt
- `Orbis-Grammatik-0.9.3.md` als kanonische Referenzgrammatik eingecheckt (READ ONLY, eingefroren; Änderungen nur über eine künftige 0.9.4 durch die Sprachdesigner).
- `archive/corpus/Orbis-Testkorpus-0.1.md` (Chat-Entwurf) archiviert.
