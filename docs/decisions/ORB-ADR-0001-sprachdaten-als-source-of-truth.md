# ORB-ADR-0001 — Maschinenlesbare Sprachdaten als Source of Truth

- **ID:** ORB-ADR-0001
- **Datum:** 2026-08-16
- **Status:** entschieden
- **Version:** Orbis Tools 0.2 (Infrastruktur; keine Sprachversion betroffen)

## Problem

Die Sprachregeln lagen doppelt vor: als Prosa in `Orbis-Grammatik-0.9.3.md` und
hartkodiert in `orbis_validator.py`. Bei einer wachsenden Sprache (Ziel: fünfstellige
Lexemzahl) führt das zwangsläufig zu zwei auseinanderlaufenden Wahrheiten — jede
Änderung müsste an beiden Stellen von Hand nachgezogen werden.

## Optionen

- **(a) Beibehalten.** Billig, aber die Divergenz ist nur eine Frage der Zeit.
- **(b) Validator generiert sich aus der Markdown-Grammatik.** Setzt eine formale,
  parsebare Grammatikdatei voraus; die Referenz ist bewusst Prosa für Menschen.
- **(c) Sprachdaten in eigene JSON-Dateien, die alle Werkzeuge lesen.** Referenz bleibt
  Prosa und autoritativ; die Daten sind ihre maschinenlesbare Spiegelung.

## Entscheidung

**Option (c).** Die Sprachdaten liegen unter `language/` und werden von Validator,
Dokumentationsgenerator und künftigen Anwendungen gelesen. Die Referenzgrammatik bleibt
autoritativ: Weicht ein Datensatz von ihr ab, gilt die Grammatik, und die Abweichung ist
ein Befund.

## Begründung

Die Migration wurde als sprachneutral nachgewiesen: alle sechs Validator-Läufe
(`--lexicon`, `--examples`, `--manus`, `--tables`, `--corpus`, `--sim-l09`) sind
byte-identisch zur eingefrorenen Baseline unter `reports/baseline/`. Damit ist belegt,
dass die Umstellung kein Sprachverhalten verändert hat.

## Auswirkungen

- `orbis_validator.py` bleibt als Einstiegspunkt bestehen; die Logik liegt in
  `tools/validator/`. Alle dokumentierten Aufrufe gelten unverändert weiter.
- Offene Regeln tragen in den Daten `status: open|conflict|unclear` mit Befund-ID —
  eine fehlende Regel wird dadurch als Datenzustand sichtbar statt stillschweigend
  durch Code ersetzt.
- Neue Werkzeuge dürfen Sprachregeln nicht mehr hartkodieren (AGENTS.md).

## Betroffene Regeln, Wörter, Tests

Regeln: alle migrierten (Phonologie, Morphologie, Syntax, Proto-Orbis) — inhaltlich
unverändert. Wörter: keine. Tests: `tests/regression/test_baseline.py` sichert die
Ausgabe-Identität dauerhaft ab; CI bricht bei Abweichung.
