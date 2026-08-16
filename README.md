# ORBIS

> **Wenn du eine KI bist, lies zuerst `AI_START_HERE.md`.** Dort stehen Einstiegspunkt,
> verbindliche Lesereihenfolge und die Grenzen der zulässigen Mitarbeit. Danach gelten
> `ORBIS_CONSTITUTION.md`, `CLAUDE.md` und `AGENTS.md`.

Orbis ist eine konstruierte Sprache mit eigener Schrift (Orbis Manus). Das Projekt verbindet
Sprachdesign mit maschineller Validierung: Eine eingefrorene Referenzgrammatik wird gegen ein
Testkorpus und einen Python-Validator geprüft, Befunde werden dokumentiert und fließen als
Designentscheidungen in die nächste Grammatikversion ein.

Das Repository wird derzeit von einer Sammlung einzelner Dokumente zu einer strukturierten
Sprachplattform umgebaut: maschinenlesbare Sprachdaten unter `language/` werden langfristig
Source of Truth, Markdown wird daraus erzeugt oder dagegen geprüft.

## Sprachpolitik

- **Deutsch ist PRIMARY LANGUAGE und semantische Autorität.** Die kanonische Bedeutung jedes
  Orbis-Eintrags, jeder Regel und jedes Befunds wird auf Deutsch festgelegt.
- **Englisch ist SECONDARY OFFICIAL DOCUMENTATION LANGUAGE.** Englische Fassungen sind
  offizielle Dokumentation, aber abgeleitet: Sie werden aus der deutschen kanonischen
  Bedeutung gewonnen und dürfen sie nicht erweitern, verengen oder verschieben.
- **Bei Widerspruch gilt Deutsch.** Weicht eine englische Fassung von der deutschen ab, ist
  die deutsche maßgeblich; die Abweichung ist ein Befund und wird gemeldet, nicht durch
  Anpassung der deutschen Seite erledigt.

Details und Feldpflichten: `TRANSLATION_POLICY.md`.

## Aktueller Status

Grammatik, Lexikon, Schrift, Tastatur, Korpus und Werkzeuge werden getrennt versioniert.

| Komponente | Version | Zustand |
|---|---|---|
| Orbis Grammar | 0.9.3 | eingefroren (READ ONLY); Änderungen nur über eine künftige 0.9.4 |
| Orbis Lexicon | 0.1 | im Aufbau; Migration nach `language/lexicon/` |
| Orbis Manus | 0.x | Konzept; Silbifizierung offen (Befund L-09) |
| Orbis Keyboard | 0.x | geplant |
| Orbis Corpus | 0.1 | abgeschlossen (150 Tests, Stabilitätsquote 86,7 %) |
| Orbis Tools | 0.2 | Validator als Paket unter `tools/validator/` |

Aktuelle Phase: **Phase A — Infrastruktur und Migration**. Laufender Detailstand: `STATUS.md`.

## Projektdokumente

| Datei | Inhalt |
|---|---|
| `ORBIS_CONSTITUTION.md` | Projektverfassung: Rangordnung, Zuständigkeiten und unverrückbare Grundregeln, über allen anderen Dokumenten stehend. |
| `CLAUDE.md` | Operative Arbeitsregeln für Assistenzsysteme: Read-Only-Bereiche, Befundpflicht, Test- und Commitpflichten. |
| `AI_START_HERE.md` | Einstiegspunkt für KI-Systeme mit verbindlicher Lesereihenfolge und Kurzlage des Projekts. |
| `AGENTS.md` | Anbieterunabhängige Regeln für Coding-Agents, die in diesem Repository lesen, schreiben, testen oder committen. |
| `CONTRIBUTING.md` | Anleitung für menschliche Mitwirkende: was ein nützlicher Beitrag ist, welche Prüfungen vor einem Pull Request laufen, wohin welche Datei gehört. |
| `STATUS.md` | Projektzustand auf einen Blick: Versionen, stabile Bereiche, offene Befunde nach Priorität. |
| `ROADMAP.md` | Geplante Phasen und Arbeitspakete bis 1.0 mit ihren Abhängigkeiten. |
| `VERSIONING.md` | Versionierungsregeln je Komponente: was einen Versionssprung auslöst und welche Prüfungen dabei Pflicht sind. |
| `TRANSLATION_POLICY.md` | Sprach- und Übersetzungspolitik: Deutsch als semantische Autorität, Englisch als abgeleitete Dokumentationssprache. |
| `CHANGELOG.md` | Chronologie aller nennenswerten Änderungen am Projekt. |
| `README.md` | Diese Datei: Überblick, Struktur und Einstieg. |

## Repository-Struktur

Zielbaum der Plattform-Architektur:

```
language/    Sprachdaten als maschinenlesbare Source of Truth
  metadata/    Sprachmetadaten (Name, Versionen, Sprachpolitik-Verweise)
  phonology/   Phoneme, Silbenbau, Onsets/Codas, Betonung, Silbifizierung
  morphology/  Nomen-, Verb-, Adjektiv- und Pronomenparadigmen, Wortbildung
  syntax/      Satzbauregeln, Präpositionen, Konjunktionen
  lexicon/     Lexeme (ORB-LEX-…), Konzepte (ORB-CON-…), Wortfamilien, Schemata
  proto/       Protosprachliche Ableitungen und Lautgesetze
  corpus/      Sätze (ORB-SENT-…) aus Testkorpus und Grammatikbeispielen
  findings/    Befunde K-xx / L-xx / U-xx / W-xx maschinenlesbar
script/      Schrift und Notation, getrennt von der Grammatik
  manus/       Orbis Manus: Glyphen, Komposition, Spezifikation, Schrifttests
  magna/       Großschrift-/Auszeichnungsvariante
  traces/      EXPERIMENTELL, NICHT KANONISCH: Wortspuren
tools/       Werkzeuge; sie spiegeln die Sprache wider, sie definieren sie nicht
  validator/     Validator als Python-Paket (Phonologie, Morphologie, Syntax, Manus, CLI)
  lexicon/       Lexikonwerkzeuge (Import, Prüfung, Export)
  corpus/        Korpuswerkzeuge (Aufbereitung, Auswertung)
  documentation/ Generatoren für abgeleitete Markdown-Dokumentation
  migration/     Einmalige Umbauskripte der Phase A
tests/       Automatisierte Tests je Ebene (Phonologie, Morphologie, Syntax, Lexikon,
             Manus, Korpus, Grammatik, Regression)
docs/
  de/          Deutschsprachige Dokumentation (kanonisch)
  en/          Englischsprachige Dokumentation (abgeleitet, sekundär offiziell)
  decisions/   Architektur- und Sprachentscheidungen (ORB-ADR-…)
reports/     Erzeugte Prüf- und Baseline-Berichte der Validator-Läufe
archive/     Eingefrorene Vorfassungen; nie Quelle, nur Beleg
```

Weiterhin im Wurzelverzeichnis: `orbis_validator.py` (stabiler Einstiegspunkt),
`orbis_baseline.json` (Baseline für `--strict` und CI) sowie die oben gelisteten
Projektdokumente.

**Hinweis zur Migration:** Die Umstellung läuft in Phase A und ist nicht abgeschlossen.
Ältere Dateien liegen weiterhin im Repo-Wurzelverzeichnis (`Orbis-Grammatik-0.9.3.md`,
`Orbis-Testkorpus-0_1.md`, `Orbis-Audit-0_1.md`, die Berichte, `decisions/`, `keyboard/`)
und ziehen schrittweise in den Zielbaum um. Bis zum Abschluss gelten die kanonischen
Dateien unten als maßgeblich; die Verzeichnisse `language/` und `script/` füllen sich
parallel und werden gegen sie geprüft.

## Kanonische Dateien und Archiv

| Datei | Inhalt |
|---|---|
| `Orbis-Grammatik-0.9.3.md` | Kanonische Referenzgrammatik, READ ONLY, eingefroren; während der Migration nicht änderbar |
| `Orbis-Testkorpus-0_1.md` | Kanonisches Testkorpus: 150 Tests mit Einzelbewertung |
| `Orbis-Testkorpus-0.1.md` | ARCHIV: früher Chat-Entwurf des Korpus (nicht maßgeblich) |
| `Orbis-Audit-0_1.md` | Regelbasis und Befund-IDs (K-01…K-05, L-01…L-10, U-01…U-14) |
| `Orbis-Validator-Bericht-0_1.md` | Protokoll der automatischen Validator-Läufe |
| `Orbis-Testbericht-0_1.md` | Statistik, Priorisierung (P0–P4) und Gesamturteil |
| `Orbis-Manus-Schreibtest-0_1.md` | Schrifttest: 77 von 281 Grundformen mehrdeutig zerlegbar (L-09) |
| `Orbis-Testdaten.json` | Strukturierte Testdaten (maschinenlesbar) |
| `orbis_validator.py` | Einstiegspunkt des Validators; Logik im Paket `tools/validator/` |
| `orbis_baseline.json` | Baseline bekannter Befunde für `--strict`/CI |
| `decisions/Entscheidungsvorlage-0_9_4.md` | Aufbereitete Optionen für die 0.9.4-Designentscheidungen |

Maßgeblich ist immer die Datei mit Unterstrich-Versionierung (`…-0_1.md`);
`Orbis-Testkorpus-0.1.md` (mit Punkt) ist ausschließlich Archiv. Ausnahme der
Namenskonvention ist die Grammatik, die ihre Version mit Punkten führt.

## Prüfergebnis (Kurzfassung)

- 150 Tests gegen Grammatik 0.9.3: **130 OK**, 14 REGELLÜCKE, 3 REGELKONFLIKT,
  2 REGELUNKLARHEIT, 1 TESTPROBLEM → **Stabilitätsquote 86,7 %**.
- **Kein P0-Befund**: Grundlegende Kommunikation und der vollständig definierte
  Morphologiekern halten ohne Widerspruch.
- **6 P1-Probleme** (L-01 Genitivstellung, L-02 Relativsatz, L-03 Fragewortkasus,
  L-04 Reflexivpronomen, L-05 Passiv-Agens, K-05 Modalverb im Nebensatz), alle additiv
  lösbar — je eine klar umrissene Designentscheidung, kein struktureller Umbau.
- Urteil: **NOT READY** für einen direkten 1.0-Sprung; empfohlener Weg führt über
  eine 0.9.4 mit den P1-Entscheidungen und anschließendem Regressionslauf.

Details: `Orbis-Testbericht-0_1.md`. Kurzlage: `STATUS.md`.

## Validator benutzen

Python 3, keine externen Abhängigkeiten. `orbis_validator.py` bleibt der stabile Aufruf;
gleichwertig ist `python3 -m tools.validator`.

```
python3 orbis_validator.py --all              # Lexikon-, Beispiel- und Manus-Prüfung in einem Lauf
python3 orbis_validator.py --lexicon          # Lexikonprüfung (Phonotaktik, Dubletten u. a.)
python3 orbis_validator.py --examples         # Beispielsätze der Grammatik prüfen
python3 orbis_validator.py --corpus DATEI     # Korpusdatei prüfen (z. B. Orbis-Testkorpus-0_1.md)
python3 orbis_validator.py --tables           # Deklinations- und Konjugationstabellen generieren
python3 orbis_validator.py --manus            # Manus-Silbenzerlegung des Grundwortschatzes
python3 orbis_validator.py --json DATEI       # Korpusprüfung als JSON ausgeben
python3 orbis_validator.py --strict           # Befunde gegen orbis_baseline.json vergleichen;
                                              #   Exit-Code 1 bei NEUEN Befunden, sonst 0
python3 orbis_validator.py --update-baseline  # Baseline (orbis_baseline.json) neu schreiben
python3 orbis_validator.py --sim-l09          # Silbifizierungs-Simulation zu L-09
                                              #   (Entscheidungshilfe, KEINE Sprachregel)
```

Vor jedem Commit, der Sprachdaten oder den Validator ändert, laufen `--strict` und
`--corpus Orbis-Testkorpus-0_1.md`. `--update-baseline` nur auf ausdrücklichen Auftrag.
Die Prüfungen laufen zusätzlich in der CI (`.github/workflows/orbis-ci.yml`).

## Nächste Schritte

Die verbindliche Planung steht in `ROADMAP.md`; hier nur die Reihenfolge im Groben:

1. **Phase A abschließen**: Migration in den Zielbaum, maschinenlesbare Sprachdaten als
   Source of Truth, Testabdeckung je Ebene.
2. **0.9.4-Designentscheidungen**: die 6 P1-Befunde plus günstige Redaktionsfixes durch
   die Sprachdesigner entscheiden (Vorlage: `decisions/Entscheidungsvorlage-0_9_4.md`).
3. **Regressionslauf**: Testkorpus 0.1 und Validator unverändert gegen 0.9.4 fahren.
4. **1.0-RC**: bei stabiler Quote ohne neue Befunde Release-Kandidat schneiden.
5. **Manus-Spezifikation**: Schrift ausarbeiten, Silbifizierung (L-09) festlegen.
6. **Keyboard-MVP**: erste Eingabemethode für Orbis.

## Arbeitsweise

- `Orbis-Grammatik-0.9.3.md` ist READ ONLY. Kein Werkzeug und kein Bericht ändert die
  Grammatik; Änderungen erscheinen erst in einer künftigen 0.9.4.
- Befunde werden markiert und mit IDs dokumentiert, nicht stillschweigend korrigiert.
  Weicht ein Werkzeug von der Grammatik ab, gilt die Grammatik, und die Abweichung ist
  selbst ein Befund.
- Alle Sprach- und Designentscheidungen treffen die Sprachdesigner; Berichte nennen
  höchstens Lösungsrichtungen, keine Festlegungen.
- Was ausdrücklich als **experimentell und nicht kanonisch** geführt wird — die
  Morphem-Ebene für Manus und Keyboard sowie die Wortspuren unter `script/traces/` —
  darf nirgends als bestehende Orbis-Grammatik dargestellt werden.
- Claude Code dient dem Projekt als Prüfwerkzeug (Validator-Läufe, Korpus- und
  Konsistenzprüfung).
