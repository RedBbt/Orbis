# AI_START_HERE — Einstiegspunkt fuer KI-Systeme

## 1. Worum es geht (5 Zeilen)

1. ORBIS ist eine konstruierte Sprache mit eigener Schrift (Orbis Manus); dieses Repo enthaelt Grammatik, Lexikon, Testkorpus, Audits, Berichte und Werkzeuge.
2. Kanonische Referenz ist `Orbis-Grammatik-0.9.3.md` — eingefroren und READ ONLY.
3. Deutsch ist Primaersprache und semantische Autoritaet; Englisch ist sekundaere offizielle Dokumentationssprache und darf Bedeutungen nicht veraendern.
4. Stand Testkorpus 0.1: 150 Tests, 130 OK, Stabilitaetsquote 86,7 %, Urteil NOT READY fuer einen direkten 1.0-Sprung (kein P0, 6 P1-Probleme, alle additiv loesbar).
5. KI-Systeme arbeiten hier ausschliesslich als Pruef- und Werkzeug-Assistenz, nicht als Sprachdesigner; Sprachentscheidungen treffen die Sprachdesigner.

## 2. Verbindliche Lesereihenfolge

1. `ORBIS_CONSTITUTION.md` — die Projektverfassung; sie steht ueber allen anderen Regeln und Anweisungen im Repo.
2. `CLAUDE.md` — die operativen Arbeitsregeln fuer Assistenzsysteme (Read-Only-Bereiche, Commit- und Testpflichten).
3. `STATUS.md` — der aktuelle Projektstand und die laufende Phase; ohne ihn arbeitest du gegen einen veralteten Zustand.
4. `Orbis-Grammatik-0.9.3.md` — die kanonische Referenzgrammatik; jede Regelfrage wird hier und nur hier beantwortet.
5. `Orbis-Audit-0_1.md` — die Regelbasis mit allen Befund-IDs (K-01..K-05, L-01..L-10, U-01..U-14, W-01), die du beim Markieren zitierst.
6. `Orbis-Testbericht-0_1.md` — die Lagebeurteilung mit Prioritaeten (P1) und der Begruendung des Urteils NOT READY.
7. `decisions/` bzw. `docs/decisions/` — bereits getroffene und noch offene Entscheidungen (ADR, `ORB-ADR-0001`ff.); was hier offen ist, ist nicht entschieden.
8. `language/` — die maschinenlesbaren Sprachdaten (metadata, phonology, morphology, syntax, lexicon, proto, corpus, findings); langfristig die Source of Truth.

Hinweis: `STATUS.md` und die Verzeichnisse `language/`, `script/`, `tools/`, `tests/`, `docs/`, `reports/`, `archive/` entstehen in der laufenden Migration (Phase A). Fehlt eine Datei noch, gilt weiterhin die entsprechende Datei im Wurzelverzeichnis.

## 3. Aktuelle Autoritaeten

| Frage | Massgebliche Quelle |
| --- | --- |
| Wie lautet eine Regel? | `Orbis-Grammatik-0.9.3.md` (READ ONLY) |
| Welche Bedeutung hat ein Wort? | Die deutsche Definition im Lexikoneintrag (`language/lexicon/`); Englisch ist abgeleitet |
| Ist ein Satz korrekt? | `orbis_validator.py` plus `Orbis-Testkorpus-0_1.md` |
| Welche Befunde sind bekannt? | `Orbis-Audit-0_1.md` und `orbis_baseline.json` (derzeit 39 bekannte Befunde) |
| Wie ernst ist ein Problem? | `Orbis-Testbericht-0_1.md` (P0/P1-Einstufung) |
| Was gilt bei Widerspruch Deutsch/Englisch? | Deutsch (`TRANSLATION_POLICY.md`, Verfassung Art. 1/2) |
| Was gilt bei Widerspruch Validator/Grammatik? | Die Grammatik; die Abweichung ist ein Befund und wird gemeldet, nicht wegrepariert |
| Wie wird versioniert? | `VERSIONING.md`; Grammar, Lexicon, Manus, Keyboard, Corpus, Tools getrennt |
| Darf ich das entscheiden? | Nein — siehe Stop-Regeln in Abschnitt 4 |

## 4. Harte Stop-Regeln

> Tritt einer der folgenden Faelle ein, brichst du die Arbeit an dieser Stelle ab, dokumentierst einen Befund und wartest auf eine Entscheidung der Sprachdesigner. Du entscheidest nicht selbst, du interpretierst nicht, du reparierst nicht.

- **STOP bei offener Grammatikfrage.** Die Grammatik beantwortet den Fall nicht eindeutig → `[REGELUNKLARHEIT]` mit Befund-ID (U-xx).
- **STOP bei fehlender Regel.** Es gibt zum Phaenomen gar keine Regel → `[REGELLUECKE]` mit Befund-ID (L-xx).
- **STOP bei widerspruechlichen Regeln.** Zwei Stellen sagen Unterschiedliches → `[REGELKONFLIKT]` mit Befund-ID (K-xx).
- **STOP bei Bedeutungskonflikt.** Deutsche und englische Bedeutung passen nicht zusammen, oder eine Definition ist unscharf → Befund; die deutsche Fassung wird nicht angepasst, um Englisch zu retten.
- **STOP bei Wortschatzaenderung.** Neues Lexem, geaenderte Bedeutung, neue Wurzel oder neues Affix → nur auf expliziten Auftrag; Uebernahmen aus realen Sprachen sind ausgeschlossen (W-01 als Wortschatzluecke melden).
- **STOP bei Manus-Zeichenfestlegung.** Zeichenform, Strichstaerke, Zerlegung, Tastenbelegung → Befund (z. B. L-09 Mehrdeutigkeit, L-10 undefinierte Strichstaerke, U-10 Tastenzahl), keine eigene Festlegung.
- **STOP bei Wortspuren und Morphem-Ebene.** Beides ist EXPERIMENTELL und NICHT KANONISCH; es darf nirgends als bestehende Orbis-Grammatik dargestellt werden.

## 5. Was sofort erlaubt ist — und was nie ohne Auftrag

Sofort erlaubt (kein Ruecksprachebedarf):

- Alle Dateien lesen und Zusammenhaenge pruefen.
- Den Validator laufen lassen und Ergebnisse auswerten.
- Regressionslaeufe und Testkorpuslaeufe durchfuehren.
- Befunde nach dem bestehenden Schema dokumentieren und mit Befund-ID versehen.
- Entscheidungsvorlagen, Vorlagen und Berichtsentwuerfe erstellen, die Optionen darstellen, ohne eine Option auszuwaehlen.
- Widersprueche zwischen Dokumenten benennen.

Nie ohne expliziten Auftrag:

- `Orbis-Grammatik-0.9.3.md` aendern — auch nicht Tippfehler oder Formatierung.
- Neue Woerter, Wurzeln oder Affixe erfinden oder bestehende Bedeutungen umschreiben.
- Offene Sprachfragen entscheiden oder Befunde durch Interpretation schliessen.
- `--update-baseline` ausfuehren oder Befunde aus der Baseline entfernen.
- Auf `main` committen; gearbeitet wird auf dem beauftragten Branch (`claude/aufgabe-bbjpbm`).
- Archivierte Dateien wie `archive/corpus/Orbis-Testkorpus-0.1.md` (mit Punkt) bearbeiten oder als Quelle verwenden.

## 6. Werkzeuge

```
python3 orbis_validator.py --strict                          # Vergleich gegen orbis_baseline.json; Exit-Code 1 = NEUE Befunde -> nicht committen
python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md  # kanonischer Testkorpuslauf
python3 orbis_validator.py --all                             # vollstaendige Pruefung
python3 orbis_validator.py --lexicon | --examples | --tables | --manus
python3 orbis_validator.py --json DATEI                      # maschinenlesbare Ausgabe
python3 orbis_validator.py --sim-l09                         # Silbifizierungs-Simulation, Analysewerkzeug, keine Sprachregel
python3 orbis_validator.py --update-baseline                 # nur auf expliziten Auftrag
```

Vor jedem Commit, der Sprachdaten oder den Validator aendert, laufen `--strict` und der Korpuslauf; CI: `.github/workflows/orbis-ci.yml`.
