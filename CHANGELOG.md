# Changelog

Alle nennenswerten Änderungen am Projekt ORBIS werden in dieser Datei dokumentiert.
Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/).
Versionierung (Governance): Orbis Grammar (aktuell 0.9.3), Orbis Lexicon (0.x), Orbis Manus (0.x) und Orbis Keyboard (0.x) werden getrennt versioniert.

## [Unreleased]

### Geplant
- Designentscheidungen für Grammatik 0.9.4 zu den Befunden L-01 bis L-05 und K-05 (durch die Sprachdesigner); Vorlage: `decisions/Entscheidungsvorlage-0_9_4.md`.
- Redaktionskorrekturen K-01, K-03, K-04, U-01, U-10. (U-14 und K-02 sind Grenzfälle: die Korrekturform hängt an einer Designer-Entscheidung, siehe Entscheidungsvorlage.)

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
