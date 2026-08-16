# CLAUDE.md — Projektgedaechtnis ORBIS

Arbeitsgedaechtnis fuer alle Sitzungen. **Uebergeordnet gilt `ORBIS_CONSTITUTION.md`**
(Artikel 1–20, hoechste Norm): widerspricht diese Datei der Verfassung, gilt die
Verfassung, und der Widerspruch ist ein Befund, kein Anlass zur stillen Angleichung.
Ergaenzend verbindlich: `VERSIONING.md` und `TRANSLATION_POLICY.md`.

## 1. Was ist Orbis
Orbis ist eine konstruierte Sprache mit eigener Schrift (Orbis Manus). Dieses Repository
(GitHub: RedBbt/Orbis) enthaelt Referenzgrammatik, Lexikon, Testkorpus, Audits, Berichte,
Entscheidungsvorlagen und die Werkzeugkette. Orbis wird als sechs getrennt versionierte
Komponenten gefuehrt — Grammar, Lexicon, Manus, Keyboard, Corpus, Tools — die nicht
zusammengelegt werden. Claude Code ist hier Pruef- und Werkzeug-Assistent; sprachliche
Entscheidungen treffen die Sprachdesigner.

## 2. Aktuelle kanonische Grammatikversion
- Kanonisch ist **Orbis Grammar 0.9.3**, Datei `Orbis-Grammatik-0.9.3.md`. Weitere
  Staende: Lexicon 0.1, Corpus 0.1, Tools 0.2, Manus 0.x, Keyboard 0.x (Keyboard ohne
  freigegebene Fassung, setzt eine nummerierte Manus-Version voraus).
- Pruefstand Corpus 0.1 (`Orbis-Testkorpus-0_1.md`): 150 Tests, 130 OK, 14 REGELLUECKE,
  3 REGELKONFLIKT, 2 REGELUNKLARHEIT, 1 TESTPROBLEM, Stabilitaetsquote 86,7 %.
- Urteil **NOT READY** fuer einen direkten Sprung auf 1.0. Kein P0. Sechs P1-Probleme,
  alle additiv loesbar: L-01 Genitivstellung, L-02 Relativsatz, L-03 Fragewortkasus,
  L-04 Reflexivpronomen, L-05 Passiv-Agens, K-05 Modalverb im Nebensatz.
- Befund-IDs stehen in `Orbis-Audit-0_1.md`: K-01..K-05 (Konflikte), L-01..L-10 (Luecken),
  U-01..U-14 (Unklarheiten), W-01 (Wortschatzluecke).

## 3. Hauptsprache Deutsch, Englisch sekundaer
- **Deutsch ist PRIMARY LANGUAGE und semantische Autoritaet**; die deutsche Definition
  legt die Bedeutung fest.
- **Englisch ist SECONDARY OFFICIAL DOCUMENTATION LANGUAGE**: aus der deutschen
  kanonischen Bedeutung abgeleitet, ohne sie zu veraendern, zu erweitern oder zu verengen.
  Bei Widerspruch gilt Deutsch; korrigiert wird die englische Fassung, nie umgekehrt.
- Projektdateien auf Deutsch, UTF-8 ohne BOM, Unix-Zeilenenden. Pflichtfelder und
  Uebersetzungsstatus (`missing`, `draft`, `derived`, `reviewed`): `TRANSLATION_POLICY.md`.

## 4. Aktuelle Projektphase — Phase A (Infrastruktur)
Phase A ueberfuehrt ein gewachsenes Dokumentenrepository in eine strukturierte,
maschinenlesbare Datenbasis: Zielverzeichnisse (Abschnitt 7), Extraktion bestehender
Regeln aus der Grammatik 0.9.3 nach `language/*.json`, Einfuehrung von ID-System,
Sprachpolitik, Versionsregeln und Verfassung, Trennung von Bestand und Archiv.

**Phase A aendert die Sprache nicht.** Alles, was hier entsteht, ist Abbild bestehender
Regeln, nicht neue Regel; die Grammatik 0.9.3 bleibt waehrend der Migration unveraendert
und nicht aenderbar. Vorhanden: `language/` (metadata, phonology, morphology, syntax,
proto, findings), `tools/migration/`, `reports/baseline/`. Offen: `language/lexicon`,
`language/corpus`, `script/`, `tests/`, `docs/`, `keyboard/`.

## 5. Was READ ONLY ist
- `Orbis-Grammatik-0.9.3.md` — eingefroren. Niemals aendern, auch nicht "still"
  (Tippfehler, Formatierung, Umbrueche). Neue Versionen (0.9.4 usw.) entstehen nur auf
  expliziten Auftrag der Sprachdesigner als **neue Datei**, nie durch Ueberschreiben.
- `archive/corpus/Orbis-Testkorpus-0.1.md` (mit Punkt) — archivierter Chat-Entwurf; nicht bearbeiten,
  nicht als Quelle verwenden. Kanonisch ist `Orbis-Testkorpus-0_1.md` (Unterstrich).
- `archive/` — historische Fassungen, nur lesend. `reports/baseline/` — Messwerte vor der
  Migration, nicht nachtraeglich anpassen.
- `ORBIS_CONSTITUTION.md` — nur ueber das dort beschriebene Aenderungsverfahren.

## 6. Welche Daten Source of Truth sind
- **Heute:** Wahrheit ist die Grammatik 0.9.3; `orbis_validator.py` und alle JSON-Dateien
  spiegeln sie nur wider.
- **Langfristig (Zielzustand):** `language/*.json` wird Source of Truth, Markdown wird
  daraus generiert oder dagegen geprueft. Der Uebergang gilt erst als vollzogen, wenn die
  Sprachdesigner ihn ausdruecklich erklaeren.
- Weicht der Validator (oder eine JSON-Datei) von der Grammatik ab, gilt die Grammatik;
  die Abweichung ist ein Befund — melden, nicht wegfixen.
- Weitere Referenzen: `Orbis-Audit-0_1.md`, `Orbis-Validator-Bericht-0_1.md`,
  `Orbis-Testbericht-0_1.md`, `Orbis-Manus-Schreibtest-0_1.md`, `Orbis-Testdaten.json`.
- **ID-System:** `ORB-LEX-000001` (Lexeme), `ORB-CON-000001` (Konzepte),
  `ORB-SENT-000001` (Saetze), `ORB-GRAM-PHON-001` / `-MOR-` / `-SYN-` (Grammatikregeln),
  `ORB-MANUS-001` (Schriftregeln), `ORB-ADR-0001` (Entscheidungen). Befunde behalten
  ihre Kennungen K-xx, L-xx, U-xx, W-xx.

## 7. Verzeichnisstruktur (Zielstruktur)

| Pfad | Inhalt |
|---|---|
| `language/metadata/` | Sprachstammdaten, Versionen, ID-Praefixe, Statuswerte |
| `language/phonology/` | Phoneme, Silbenformen, Onsets, Codas, Diphthonge, Betonung |
| `language/morphology/` | Kasus, Numerus, Wortklassen, Verben, Pronomen, Wortbildung |
| `language/syntax/` | Satzbau, Praepositionen, Konjunktionen |
| `language/lexicon/` | `entries/` Lexeme (`ORB-LEX-*`), `concepts/` Konzepte (`ORB-CON-*`) |
| `language/proto/` | Proto-Orbis: Lautgesetze, historische Formen |
| `language/corpus/` | `examples/` Beispielsaetze (`ORB-SENT-*`), `tests/` Saetze mit Sollergebnis; `language/findings/` Befunde (K/L/U/W) |
| `script/manus/` | `spec/` Regelwerk, `glyphs/` Zeichen mit Strichfolge und -staerke, `composition/` Silben- und Wortbildung, `tests/` Schreib- und Zerlegungstests |
| `script/magna/`, `script/traces/` | Grossform der Schrift; EXPERIMENTELL: Wortspuren |
| `keyboard/` | Tastaturbelegung (setzt nummerierte Manus-Version voraus) |
| `tools/` | `validator/` Pruefregeln, `lexicon/`, `corpus/`, `documentation/` Markdown-Generierung, `migration/` Einmalskripte |
| `tests/` | Regressionstests je Ebene (phonology, morphology, syntax, lexicon, corpus, manus, grammar, regression) |
| `docs/` | `de/` kanonische Doku, `en/` abgeleitete Doku, `decisions/` (`ORB-ADR-*`) |
| `reports/`, `archive/` | Berichte und Messwerte (inkl. `baseline/`); historische Fassungen |

Dateinamen tragen Versionsnummern mit Unterstrich (`...-0_1.md`); Ausnahme ist die
Grammatik mit Punkten (`Orbis-Grammatik-0.9.3.md`).

## 8. Regeln fuer neue Woerter
- Neue Woerter, Wurzeln oder Affixe werden nicht erfunden — ausser auf expliziten Auftrag.
- `canonical` wird ein Wort erst bei vollstaendigem Eintrag: ID, Form, Wortklasse,
  deutsche Definition, abgeleitete englische Bedeutung, Flexionsverhalten, Phonologie-
  und Phonotaktik-Nachweis, Proto-Orbis-Bezug, Beleg oder Beispielsatz, Status, Version.
- Neue Lexeme erfuellen Phonologie und Phonotaktik der Grammatik 0.9.3; historische Formen
  sind mit den Lautgesetzen in `language/proto/` vereinbar.
- Reale Sprachen duerfen nur strukturell inspirieren, nie lexikalisch liefern.
  Wortschatzluecken werden als Befund (W-xx) markiert, nicht durch Erfindung geschlossen.

## 9. Regeln fuer neue Grammatik
- Eine neue oder geaenderte Regel entsteht nur durch eine dokumentierte
  Designerentscheidung mit Decision-ID (`ORB-ADR-*`). Vorlage fuer den naechsten Sprung:
  `decisions/Entscheidungsvorlage-0_9_4.md`.
- Fehlt eine Regel oder widersprechen sich Regeln, wird der Fall als `[REGELLUECKE]`,
  `[REGELKONFLIKT]` oder `[REGELUNKLARHEIT]` mit Befund-ID markiert — nicht raten,
  nicht selbst entscheiden, nicht per Interpretation "reparieren".

## 10. Regeln fuer Bedeutungsaenderungen
- Bedeutungen werden nie still geaendert; jede Aenderung braucht Decision-ID,
  CHANGELOG-Eintrag und Tests. Eine Bedeutungsverschiebung ohne Formaenderung ist
  versionsrelevant nach `VERSIONING.md`.
- Aenderungsgegenstand ist die deutsche Definition; die englische Fassung wird danach
  neu abgeleitet und auf `derived` bzw. `reviewed` gesetzt.
- Ersetzte Bedeutungen bleiben als `deprecated` oder `historical` erhalten.

## 11. Regeln fuer Synonyme
- Synonyme werden semantisch unterschieden; zwei kanonische Lexeme mit identischer
  Definition sind ein Befund, kein zulaessiger Zustand. Verknuepft wird ueber das
  gemeinsame Konzept (`ORB-CON-*`).
- Jedes Paar braucht eine dokumentierte Abgrenzung: Register, Konnotation,
  Verwendungsbereich, Kollokation oder historische Schicht. Laesst sie sich nicht belegen,
  wird der Fall als offene Frage markiert, nicht durch eine erfundene Bedeutung geschlossen.

## 12. Regeln fuer Corpus-Saetze
- Jeder Satz traegt ID (`ORB-SENT-*`), Orbis-Form, deutsche Uebersetzung, abgeleitete
  englische Uebersetzung, Glossierung und erwartetes Pruefergebnis.
- Beispiele muessen nachvollziehbar sein: jede Form ist auf eine Regel oder einen
  Lexikoneintrag zurueckfuehrbar. Beruehrt ein Satz eine offene Frage, wird er mit
  Befund-ID markiert und nicht als Beleg fuer eine Regel verwendet.
- Kanonisch ist `Orbis-Testkorpus-0_1.md`; Saetze werden ergaenzt, nicht ersetzt,
  bestehende Test-IDs behalten ihre Nummer.

## 13. Regeln fuer Manus (Schrift)
- Manus-/Schriftregeln (§26) und Grammatikregeln werden nicht vermischt; Schrift und
  gesprochene Sprache sind getrennt modellierte Ebenen. Silbifizierungs-Simulationen
  (`--sim-l09`) sind Analysewerkzeuge, keine Sprachregeln — nie als Regel zitieren.
- Offene Befunde: L-09 (77 von 281 Grundformen mehrdeutig zerlegbar), L-10 (Strichstaerke
  fuer f s sh x v z j ç undefiniert), U-10 (§26.8 nennt faelschlich "20 Konsonantentasten";
  korrekt 19 Konsonanten + 1 Vokaltraeger — Redaktionsfehler, nicht eigenmaechtig zu
  korrigieren).
- Morphem-Ebene fuer Manus/Keyboard (sichtbare Kasus-/Tempuszeichen) und Wortspuren
  (Moeglichkeit, Erinnerung, gehoert/berichtet, selbst erlebt) sind **EXPERIMENTELL und
  NICHT KANONISCH**: nie als bestehende Orbis-Grammatik darstellen, stets so kennzeichnen.

## 14. Regeln fuer Tastatur (Keyboard)
- Orbis Keyboard hat keine freigegebene Fassung und wird nicht als kompatibel gefuehrt.
- Ein Layout setzt eine nummerierte Manus-Version voraus und wird aus der
  Manus-Spezifikation abgeleitet, nicht umgekehrt: ein Layoutwunsch aendert keine
  Schriftregel. Solange L-09, L-10, U-10 offen sind, sind Layouts Entwuerfe
  (`experimental`).

## 15. Regeln fuer Proto-Orbis
- Proto-Orbis ist die historische Vorstufe und begruendet heutige Formen; es dient nicht
  ihrer nachtraeglichen Rechtfertigung. Proto-Formen sind nie kanonische
  Gegenwartsformen; sie tragen den Status `historical`.
- Lautgesetze stehen in `language/proto/sound_laws.json` und aendern sich nur mit
  Decision-ID. Eine neue Proto-Form muss sie regelmaessig auf die kanonische Form
  abbilden; Ausnahmen werden als Ausnahmen markiert und begruendet.

## 16. Regeln fuer Tests
- Jede Sprachaenderung braucht Tests; ohne Test kein kanonischer Status. Tests liegen
  unter `tests/` je Ebene, der Korpus bleibt fachlicher Bezugspunkt.
- **Regressionslauf-Pflicht vor jedem Commit**, der Sprachdaten oder den Validator aendert:
  - `python3 orbis_validator.py --strict` (Vergleich gegen `orbis_baseline.json`, derzeit
    39 bekannte Befunde; Exit-Code 1 = NEUE Befunde → nicht committen)
  - `python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md`
- Weitere Aufrufe: `--all | --lexicon | --examples | --tables | --manus | --json DATEI |
  --update-baseline | --sim-l09`. `--update-baseline` nur nach Ruecksprache bzw.
  explizitem Auftrag. CI-Pruefung: `.github/workflows/orbis-ci.yml`.
- Ein Test wird nicht abgeschwaecht, um ihn gruen zu bekommen; ein Fehlschlag ist ein Befund.

## 17. Regeln fuer Versionsaenderungen
- Grammar, Lexicon, Manus, Keyboard, Corpus und Tools werden getrennt versioniert
  (`VERSIONING.md`). Jede neue Version besteht zuvor die Regressionstests; eine
  Erwartung ersetzt keinen Lauf.
- Die Kompatibilitaetsmatrix (`VERSIONING.md` Abschnitt 7) wird bei jedem Versionswechsel
  fortgeschrieben; eine Zeile gilt erst nach durchgefuehrtem Lauf als geprueft.
  Versionsnummern werden nicht vorgreifend vergeben, nicht nachtraeglich umgedeutet.

## 18. Regeln fuer Changelog
- Jede Sprachaenderung braucht einen Eintrag in `CHANGELOG.md` mit: was geaendert wurde,
  betroffene IDs, Decision-ID, Version, Testergebnis.
- Reine Werkzeug- oder Formatierungsaenderungen werden getrennt gefuehrt. Offene Punkte
  stehen unter `[Unreleased]`, nie in einer veroeffentlichten Version.

## 19. Regeln fuer Archive
- Archivierte Fassungen sind Beleg, nie aktuelle Quelle; sie begruenden keine heutige
  Regel, und eine kanonische Datei wird nie durch eine archivierte ersetzt.
- Archivierte Dateien werden weder bearbeitet noch geloescht; ihr Name bleibt erhalten,
  der Archivstatus ergibt sich aus dem Pfad unter `archive/`.

## 20. Regeln fuer KI-Arbeit
- Claude Code arbeitet als Pruefwerkzeug: lesen, pruefen, messen, markieren, strukturieren,
  dokumentieren. Offene Sprachentscheidungen werden nicht eigenstaendig geschlossen;
  offene Punkte werden sichtbar markiert, nicht versteckt und nicht ueberdeckt.
- Bei Unsicherheit anhalten und melden, statt plausibel zu ergaenzen. Vermutungen werden
  als Vermutung gekennzeichnet und von Belegen getrennt. In Projektdateien stehen keine
  Modell- oder AI-Produktnamen; erlaubt ist nur der vereinbarte Hinweis, dass Claude Code
  als Pruefwerkzeug dient.
- Git-Workflow: committen auf `claude/aufgabe-bbjpbm` bzw. den jeweils beauftragten
  Branch, **nie direkt auf `main`**; nach Abschluss der Aufgabe pushen.

## 21. HARTE VERBOTE
Diese Regeln gelten woertlich und ohne Ausnahme:
1. Keine neue Grammatikregel ohne explizite Designerentscheidung.
2. Keine bestehenden Woerter umbenennen ausser der Nutzer entscheidet es.
3. Kein neues kanonisches Wort ohne vollstaendige Dokumentation.
4. Kein Wort aus Deutsch, Englisch, Kurdisch, Tuerkisch oder einer anderen realen
   Sprache kopieren.
5. Keine versteckten Reparaturen.
6. Bei Unsicherheit STOP als Befund, nicht kreativ auffuellen.
7. Jede Sprachaenderung braucht Tests.
8. Jede Sprachaenderung braucht CHANGELOG-Eintrag.
9. Jede groessere Entscheidung braucht Decision-ID.
10. Deutsche Definition ist semantische Autoritaet.
11. Englisch muss aus der deutschen kanonischen Bedeutung abgeleitet werden.
