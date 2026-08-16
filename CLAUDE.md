# CLAUDE.md — Projektregeln fuer ORBIS

ORBIS ist eine konstruierte Sprache; dieses Repo (GitHub: RedBbt/Orbis) enthaelt
Referenzgrammatik, Testkorpus, Audits, Berichte und den Validator. Claude Code
dient hier ausschliesslich als Pruef- und Werkzeug-Assistent, nicht als Sprachdesigner.

## 1. Referenzgrammatik ist READ ONLY
- `Orbis-Grammatik-0.9.3.md` ist eingefroren. Niemals aendern, auch nicht "still" (Tippfehler, Formatierung).
- Neue Versionen (0.9.4 usw.) entstehen nur auf expliziten Auftrag der Sprachdesigner — als neue Datei, nie durch Ueberschreiben.

## 2. Keine neuen Woerter
- Erfinde keine neuen Orbis-Woerter, Wurzeln oder Affixe ohne expliziten Auftrag.
- Uebernimm keine Woerter aus realen Sprachen ins Orbis-Lexikon.

## 3. Regelluecken und -konflikte markieren, nicht entscheiden
- Fehlt eine Regel oder widersprechen sich Regeln: markiere den Fall als
  `[REGELLUECKE]`, `[REGELKONFLIKT]` oder `[REGELUNKLARHEIT]` mit Befund-ID
  nach `Orbis-Audit-0_1.md` (K-01..K-05, L-01..L-10, U-01..U-14).
- Rate nicht, entscheide nicht selbst, "repariere" nicht per Interpretation. Entscheidungen treffen die Sprachdesigner.

## 4. Regressionslauf vor jedem Commit
- Vor jedem Commit, der Sprachdaten oder den Validator aendert, fuehre aus:
  - `python3 orbis_validator.py --strict` (Vergleich gegen `orbis_baseline.json`; Exit-Code 1 = NEUE Befunde → nicht committen)
  - `python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md`
- Weitere Aufrufe: `--all | --lexicon | --examples | --tables | --manus | --json DATEI | --update-baseline | --sim-l09`.
- `--update-baseline` nur nach Ruecksprache bzw. explizitem Auftrag ausfuehren.

## 5. Manus (Schrift) und Grammatik trennen
- Manus-/Schriftregeln (§26) und Grammatikregeln nicht vermischen.
- Silbifizierungs-Simulationen (`--sim-l09`) sind Analysewerkzeuge, keine Sprachregeln — nie als Regel zitieren.

## 6. Kanonische Datenquellen
- Wahrheit ist die Grammatik 0.9.3; `orbis_validator.py` spiegelt sie nur wider.
- Weicht der Validator von der Grammatik ab, gilt die Grammatik; die Abweichung ist ein Befund (melden, nicht wegfixen).
- Kanonischer Testkorpus: `Orbis-Testkorpus-0_1.md` (150 Tests; 130 OK / 14 REGELLUECKE /
  3 REGELKONFLIKT / 2 REGELUNKLARHEIT / 1 TESTPROBLEM; Stabilitaetsquote 86,7 %).
- Weitere Referenzen: `Orbis-Audit-0_1.md` (Regelbasis, Befund-IDs), `Orbis-Validator-Bericht-0_1.md`,
  `Orbis-Testbericht-0_1.md` (Urteil: NOT READY fuer direkten 1.0-Sprung; 6 P1-Probleme, additiv loesbar),
  `Orbis-Manus-Schreibtest-0_1.md` (77 von 281 Grundformen mehrdeutig zerlegbar, L-09), `Orbis-Testdaten.json`.
- Governance: Orbis Grammar (0.9.3), Orbis Lexicon (0.x), Orbis Manus (0.x) und Orbis Keyboard (0.x) werden getrennt versioniert — nicht zusammenlegen.

## 7. Dateinamenskonventionen
- Versionsnummern in Dateinamen mit Unterstrich schreiben: `...-0_1.md`.
- `Orbis-Testkorpus-0.1.md` (mit Punkt) ist der ARCHIVIERTE Chat-Entwurf — nicht bearbeiten, nicht als Quelle verwenden.
- Ausnahme: Die Grammatik traegt ihre Version mit Punkten (`Orbis-Grammatik-0.9.3.md`).

## 8. Git-Workflow
- Committe auf `claude/aufgabe-bbjpbm` bzw. den jeweils beauftragten Branch, nie direkt auf main.
- Pushe nach Abschluss der Aufgabe.

## Allgemein
- Schreibe Projektdateien auf Deutsch, UTF-8 ohne BOM, Unix-Zeilenenden.
- Keine Modell-/AI-Namen in Dateien; erlaubt ist nur der vereinbarte Hinweis, dass Claude Code als Pruefwerkzeug dient.
