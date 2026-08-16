# ORBIS — Projektverfassung

**Version:** 1.0
**Stand:** 2026-08-16
**Status:** verbindlich für alle Beteiligten und alle Werkzeuge des Projekts
**Zitierweise:** `ORBIS-VERF Art. N` (z. B. `ORBIS-VERF Art. 5`)

---

## Präambel

Orbis ist eine konstruierte Sprache mit eigener Schrift (Orbis Manus). Das Projekt verbindet
Sprachdesign mit maschineller Prüfung: Eine eingefrorene Referenzgrammatik wird gegen ein
Testkorpus und einen Validator geprüft, Befunde werden dokumentiert und fließen als
Designentscheidungen in die jeweils nächste Version ein.

Diese Verfassung regelt **das Verfahren, nicht den Sprachinhalt**. Sie legt fest, wer
entscheidet, in welcher Sprache die Wahrheit steht, welche Datei bei Widerspruch gilt, wie
Änderungen dokumentiert werden und wo die Grenzen maschineller Mitarbeit liegen. Was Orbis
grammatisch ist, steht ausschließlich in der jeweils gültigen Referenzgrammatik (derzeit
`Orbis-Grammatik-0.9.3.md`, eingefroren, READ ONLY).

**Rangordnung bei Widerspruch:**

1. Diese Verfassung (Verfahren, Zuständigkeit, Dokumentationspflichten)
2. Die kanonische Referenzgrammatik (Sprachinhalt)
3. Maschinenlesbare Sprachdaten und Entscheidungen (ADR) in ihrer jeweils gültigen Fassung
4. Arbeitsregeln für Werkzeuge (`CLAUDE.md`), Berichte, Prüfprotokolle
5. Archivierte Fassungen — niemals maßgeblich (Art. 18)

**Entscheidungshoheit:** Alle Sprach- und Designentscheidungen treffen die Sprachdesigner.
Werkzeuge, Berichte und KI-Systeme prüfen, markieren und schlagen vor; sie entscheiden nicht.

**Getrennte Versionierung:** Orbis Grammar, Orbis Lexicon, Orbis Manus, Orbis Keyboard und
Orbis Corpus werden getrennt versioniert und nicht zusammengelegt.

---

## Kurzübersicht der Artikel

| Art. | Grundsatz | Abschnitt |
|---|---|---|
| 1 | Deutsch ist kanonische Referenzsprache | I Sprachhoheit |
| 2 | Englisch ist sekundäre offizielle Übersetzung | I Sprachhoheit |
| 6 | Keine stillen Bedeutungsänderungen | I Sprachhoheit |
| 3 | Maschinenlesbare Sprachdaten sind Source of Truth | II Datenhoheit |
| 7 | Keine stillen Umbenennungen | II Datenhoheit |
| 13 | Beispiele müssen nachvollziehbar sein | II Datenhoheit |
| 18 | Archivierte Fassungen sind keine aktuelle Quelle | II Datenhoheit |
| 5 | Kein kanonisches Wort ohne vollständigen Lexikoneintrag | III Wortschatz |
| 8 | Keine lexikalischen Übernahmen aus realen Sprachen | III Wortschatz |
| 9 | Reale Sprachen dürfen nur strukturell inspirieren | III Wortschatz |
| 10 | Neue Lexeme erfüllen Phonologie und Phonotaktik | III Wortschatz |
| 11 | Historische Formen sind mit Proto-Orbis vereinbar | III Wortschatz |
| 12 | Synonyme werden semantisch unterschieden | III Wortschatz |
| 4 | Grammatikänderungen brauchen dokumentierte Entscheidungen (ADR) | IV Änderungsprozess |
| 14 | Änderungen erscheinen im CHANGELOG | IV Änderungsprozess |
| 15 | Jede neue Version besteht Regressionstests | IV Änderungsprozess |
| 16 | KI schließt offene Sprachentscheidungen nicht eigenständig | V KI-Zusammenarbeit |
| 17 | Offene Punkte werden markiert, nicht versteckt | V KI-Zusammenarbeit |
| 19 | Manus und gesprochene Sprache werden getrennt modelliert | VI Schrift und Experimente |
| 20 | Experimentelle Systeme sind als EXPERIMENTAL zu kennzeichnen | VI Schrift und Experimente |

---

## Abschnitt I — Sprachhoheit

### Art. 1 — Deutsch ist kanonische Referenzsprache

**Grundsatz:** Deutsch ist die primäre Projektsprache und die semantische Autorität. Bei jedem
Widerspruch zwischen einer deutschen und einer anderssprachigen Fassung gilt die deutsche
Fassung.

Bedeutungen, Regeltexte, Befunde und Entscheidungen entstehen zuerst auf Deutsch; nur so gibt
es genau eine Instanz, gegen die Übersetzungen geprüft werden können. Ohne eine festgelegte
Autoritätssprache driften Bedeutungen zwischen den Fassungen auseinander, ohne dass ein
Werkzeug den Drift bemerken kann. Diese Festlegung ist eine Verfahrensregel und sagt nichts
darüber aus, wie Orbis selbst gebaut ist.

*Beispiel:* Referenzgrammatik, `Orbis-Audit-0_1.md`, `Orbis-Testkorpus-0_1.md` und die
Entscheidungsvorlagen sind deutsch. Weicht eine englische Wortbedeutung von der deutschen ab,
ist die englische Fassung fehlerhaft — nicht die deutsche.

### Art. 2 — Englisch ist sekundäre offizielle Übersetzung

**Grundsatz:** Englisch ist die zweite offizielle Dokumentationssprache. Englische Fassungen
werden aus der deutschen kanonischen Fassung abgeleitet und dürfen deren Bedeutung nicht
verändern, erweitern oder verengen.

Eine offizielle englische Ebene macht das Projekt außerhalb des deutschen Sprachraums prüfbar
und zitierfähig, ohne die Autorität aus Art. 1 aufzuweichen. Englische Texte sind Übersetzung
und Erläuterung, niemals Quelle einer neuen Festlegung. Wer beim Übersetzen eine Unschärfe
bemerkt, meldet sie als Befund gegen die deutsche Fassung, statt sie in der Übersetzung zu
glätten.

*Beispiel:* `docs/en/` spiegelt `docs/de/`; ein Lexikoneintrag führt die deutsche Bedeutung als
kanonisches Feld und die englische Übersetzung als abgeleitetes Feld.

### Art. 6 — Keine stillen Bedeutungsänderungen

**Grundsatz:** Die Bedeutung eines kanonischen Wortes, einer Regel oder eines Befundes wird nur
durch eine dokumentierte Entscheidung geändert (Art. 4), sichtbar im CHANGELOG (Art. 14).
Bedeutungsverschiebungen „nebenbei" — beim Redigieren, Übersetzen, Umformatieren oder
Migrieren — sind unzulässig.

Sprachprojekte sterben an unbemerkter Semantikdrift: Wenn eine Bedeutung sich unbemerkt
verschiebt, entwerten sich rückwirkend alle Beispielsätze, Korpusbewertungen und Testergebnisse,
die auf der alten Bedeutung beruhten. Eine dokumentierte Änderung ist billig, eine stille
Änderung kostet die Nachvollziehbarkeit des gesamten Bestands. Auch Präzisierungen sind
Änderungen und werden als solche behandelt.

*Beispiel:* Die Homonymie von *fai* („Relativpronomen" in §13.4, „dass" in §20) darf nicht durch
eine beiläufige Umformulierung aufgelöst werden; sie ist Gegenstand der offenen Entscheidung zu
Befund L-02.

---

## Abschnitt II — Datenhoheit

### Art. 3 — Maschinenlesbare Sprachdaten sind langfristig Source of Truth

**Grundsatz:** Langfristig sind die strukturierten, maschinenlesbaren Sprachdaten (JSON unter
`language/`, `script/`) die Quelle der Wahrheit; Markdown-Dokumente werden daraus generiert oder
gegen sie geprüft.

Nur strukturierte Daten lassen sich vollständig, wiederholbar und automatisch prüfen —
Fließtext lässt sich nur lesen. Damit werden Vollständigkeit (Art. 5), Phonotaktik (Art. 10) und
Regressionen (Art. 15) maschinell nachweisbar statt bloß behauptet. Bis die Umstellung
abgeschlossen ist, gilt weiterhin die eingefrorene Referenzgrammatik als inhaltliche Wahrheit;
die Migration verschiebt die Trägerform, nicht den Inhalt.

*Beispiel:* `Orbis-Testdaten.json` und `orbis_baseline.json` sind bereits maschinenlesbar;
`orbis_validator.py --strict` vergleicht die aktuellen Befunde gegen die Baseline und liefert
Exit-Code 1, sobald ein NEUER Befund auftritt.

### Art. 7 — Keine stillen Umbenennungen

**Grundsatz:** Bezeichner — Dateinamen, IDs, Regelnummern, Feldnamen, Befund-IDs — werden nicht
ohne dokumentierte Entscheidung und CHANGELOG-Eintrag umbenannt. Wird umbenannt, bleibt die
Zuordnung alt → neu dauerhaft nachvollziehbar.

Bezeichner sind die Adressen, unter denen Berichte, Tests, Entscheidungen und externe Verweise
aufeinander zeigen; eine stille Umbenennung bricht alle diese Verweise gleichzeitig und
unsichtbar. Besonders empfindlich ist das Projekt an den Stellen, an denen ähnliche Namen
unterschiedliche Gültigkeit haben. Umbenennungen im Zuge einer Restrukturierung sind erlaubt,
aber immer als Migrationsschritt zu protokollieren.

*Beispiel:* `Orbis-Testkorpus-0_1.md` (kanonisch, Unterstrich) und `archive/corpus/Orbis-Testkorpus-0.1.md`
(Archiv, Punkt) unterscheiden sich um ein Zeichen; die Befund-IDs K-01…K-05, L-01…L-10,
U-01…U-14 und W-01 bleiben über Versionsgrenzen hinweg stabil.

### Art. 13 — Beispiele müssen nachvollziehbar sein

**Grundsatz:** Jeder Orbis-Beispielsatz nennt seine Quelle und ist gegen die geltenden Regeln
prüfbar. Beispiele, die eine noch nicht getroffene Entscheidung voraussetzen, sind ausdrücklich
als hypothetisch und nicht kanonisch zu kennzeichnen.

Ein Beispiel ist im Sprachbau kein Schmuck, sondern eine Behauptung über die Regeln; unbelegte
Beispiele werden zu heimlichen Regeln, sobald jemand sie zitiert. Prüfbarkeit heißt: Ein
Werkzeug oder ein Leser kann Wortformen, Kasus und Stellung aus benannten Paragraphen ableiten.
Nicht prüfbare Beispiele werden entfernt oder als offener Punkt markiert (Art. 17).

*Beispiel:* `orbis_validator.py --examples` prüft die Beispielsätze der Grammatik;
`decisions/Entscheidungsvorlage-0_9_4.md` kennzeichnet alle Sätze in den Optionskästen
ausdrücklich als hypothetisch und nicht kanonisch.

### Art. 18 — Archivierte Fassungen sind keine aktuelle Quelle

**Grundsatz:** Archivierte Dokumente werden aufbewahrt und dürfen zitiert werden, um Historie zu
belegen — niemals aber als Beleg für den aktuellen Stand der Sprache, des Lexikons oder der
Schrift.

Historische Fassungen sind für die Rekonstruktion von Entscheidungswegen wertvoll, enthalten
aber Formen und Regeln, die bewusst verworfen wurden. Wer sie als Quelle verwendet, führt
verworfene Festlegungen unbemerkt wieder ein. Archivierte Dateien werden deshalb erkennbar
abgelegt und nicht mehr inhaltlich bearbeitet.

*Beispiel:* `archive/corpus/Orbis-Testkorpus-0.1.md` ist der archivierte Chat-Entwurf; maßgeblich ist
ausschließlich `Orbis-Testkorpus-0_1.md` mit 150 Tests. Archivstände liegen unter `archive/`
bzw. `reports/baseline/`.

---

## Abschnitt III — Wortschatz

### Art. 5 — Kein kanonisches Wort ohne vollständigen Lexikoneintrag

**Grundsatz:** Ein Wort ist erst dann kanonischer Bestandteil von Orbis, wenn es einen
vollständigen Lexikoneintrag besitzt: stabile ID, Form, Wortart, deutsche kanonische Bedeutung,
englische Übersetzung, Flexionsklasse, Phonotaktik-Nachweis, Beleg und Aufnahmeversion. Wörter
ohne vollständigen Eintrag gelten als Vorschlag, nicht als Sprache.

Unvollständige Einträge erzeugen scheinbaren Wortschatz: Der Form nach existiert das Wort, aber
niemand kann es korrekt flektieren, übersetzen oder maschinell prüfen. Die Vollständigkeitsregel
hält den Wortschatz in einem Zustand, in dem er jederzeit vollständig validierbar ist.
Fehlt eine Angabe, wird sie als offener Punkt markiert (Art. 17) und nicht geraten.

*Beispiel:* Lexeme tragen IDs der Form `ORB-LEX-000001`, Konzepte `ORB-CON-000001`; ein
Kandidatenwort ohne belegte Bedeutung bleibt Kandidat und geht nicht in Korpus oder Beispiele
ein.

### Art. 8 — Keine lexikalischen Übernahmen aus realen Sprachen

**Grundsatz:** Wörter, Wurzeln und Affixe realer Sprachen werden nicht in das Orbis-Lexikon
übernommen — weder unverändert noch in lautlich leicht angepasster Form.

Orbis soll ein eigenständiges Lexikon besitzen; Übernahmen erzeugen unbeabsichtigte
Bedeutungsanhängsel, kulturelle Konnotationen und falsche Erwartungen an Flexion und Ableitung.
Auch „naheliegende" Internationalismen sind Übernahmen. Neue Wörter entstehen ausschließlich als
Auftrag der Sprachdesigner und nach den Regeln aus Art. 5, 10 und 11.

*Beispiel:* Beim Schließen der Wortschatzlücke W-01 wird kein reales Sprachmaterial entlehnt;
zulässig ist nur eine Neubildung nach Orbis-Phonotaktik oder eine Umschreibung mit vorhandenen
Lexemen.

### Art. 9 — Reale Sprachen dürfen nur strukturell, phonologisch oder rhythmisch inspirieren

**Grundsatz:** Reale Sprachen dürfen als Vorbild für Strukturen, Lautinventare, Silben- und
Rhythmusmuster dienen. Sie liefern niemals Wortmaterial (Art. 8).

Die Trennung hält Orbis lernbar und ästhetisch stimmig, ohne es zu einer Ableitung einer
existierenden Sprache zu machen. Strukturelle Anleihen sind offen zu benennen, damit spätere
Leser Absicht von Zufall unterscheiden können. Eine Anleihe ist ein Argument in einer
Entscheidung, keine Regel für sich.

*Beispiel:* Die Grammatik orientiert den Satzbau ausdrücklich eng am Deutschen (§1) — das ist
eine strukturelle Anleihe. Sie rechtfertigt keine Übernahme deutscher Wortformen.

### Art. 10 — Neue Lexeme müssen Orbis-Phonologie und -Phonotaktik erfüllen

**Grundsatz:** Jede neue Wortform wird vor Aufnahme gegen das Lautinventar und die
phonotaktischen Regeln der geltenden Grammatik geprüft. Formen, die dagegen verstoßen, werden
nicht aufgenommen — auch nicht als Ausnahme.

Ein einziges regelwidriges Wort zwingt entweder zu einer Sonderregel oder macht die
Phonotaktikprüfung wertlos; beides schwächt die Sprache stärker als der Verzicht auf die eine
Form. Die Prüfung ist maschinell möglich und daher zumutbar. Soll das Lautsystem erweitert
werden, ist das eine Grammatikentscheidung nach Art. 4, kein Nebeneffekt einer Wortaufnahme.

*Beispiel:* `orbis_validator.py --lexicon` prüft Phonotaktik und Dubletten; in der
Entscheidungsvorlage zu L-02 sind die möglichen Formen *fain*, *faiş*, *fais* ausdrücklich als
phonotaktisch geprüft ausgewiesen (§5.3).

### Art. 11 — Historische Formen müssen mit Proto-Orbis vereinbar sein

**Grundsatz:** Angaben zur Wortgeschichte, zu Wurzeln und zu Ableitungsketten müssen mit dem
dokumentierten Proto-Orbis-Stand vereinbar sein. Widerspricht eine historische Angabe dem
Proto-Bestand, ist entweder die Angabe oder der Proto-Bestand zu korrigieren — per Entscheidung,
nicht durch Nebeneinanderstehenlassen.

Eine erfundene Sprachgeschichte, die sich selbst widerspricht, entwertet jede spätere Ableitung
und jede Etymologie. Konsistenz erlaubt es, neue Wörter regelhaft aus Wurzeln zu bilden, statt
sie einzeln zu erfinden. Der Proto-Stand ist damit ein Werkzeug der Wortbildung, nicht bloß
Beiwerk.

*Beispiel:* Proto-Material wird unter `language/proto/` geführt; Etymologieangaben in
Lexikoneinträgen verweisen auf diesen Bestand und werden gegen ihn geprüft.

### Art. 12 — Synonyme müssen semantisch unterschieden werden

**Grundsatz:** Zwei kanonische Lexeme dürfen nicht dieselbe Bedeutung tragen. Jedes Synonympaar
erhält im Lexikon eine ausdrückliche Unterscheidung (Bedeutungsnuance, Register, Kollokation
oder Verwendungsbereich).

Ununterschiedene Synonyme machen Übersetzungen unentscheidbar: Weder Mensch noch Werkzeug kann
begründen, welche Form korrekt ist, und Testkorpora werden mehrdeutig bewertbar. Die
Unterscheidung darf schmal sein, muss aber benannt und prüfbar sein. Lässt sich kein Unterschied
angeben, ist eine der Formen kein eigenes Lexem.

*Beispiel:* Der Validator meldet Dubletten in der Lexikonprüfung; jede gemeldete Dublette ist
entweder zu unterscheiden oder aufzulösen, bevor die Formen kanonisch werden.

---

## Abschnitt IV — Änderungsprozess

### Art. 4 — Grammatikänderungen brauchen dokumentierte Entscheidungen (ADR)

**Grundsatz:** Jede Änderung an der Grammatik, am Regelbestand oder an einer kanonischen
Festlegung beruht auf einer schriftlichen Entscheidung (Architecture Decision Record) mit
stabiler ID, Problembeschreibung, geprüften Optionen, Begründung und Folgeänderungen. Ohne ADR
keine Regeländerung.

Der Wert eines Sprachprojekts liegt nicht nur in den Regeln, sondern in den Gründen dafür; ohne
festgehaltene Gründe werden dieselben Fragen jahrelang neu verhandelt. ADRs machen zudem
sichtbar, welche Folgeparagraphen eine Entscheidung mitzieht. Die eingefrorene Referenzgrammatik
wird nie überschrieben; Änderungen erscheinen in einer neuen Versionsdatei.

*Beispiel:* `decisions/Entscheidungsvorlage-0_9_4.md` bereitet die sechs P1-Entscheidungen
(L-01 Genitivstellung, L-02 Relativsatz, L-03 Fragewortkasus, L-04 Reflexivpronomen,
L-05 Passiv-Agens, K-05 Modalverb im Nebensatz) mit Optionen und Folgeänderungen auf; die
beschlossenen Fassungen erhalten IDs der Form `ORB-ADR-0001`.

### Art. 14 — Änderungen erscheinen im CHANGELOG

**Grundsatz:** Jede inhaltlich wirksame Änderung an Sprachdaten, Regeln, Werkzeugen oder
kanonischen Dokumenten wird im `CHANGELOG.md` festgehalten, mit Datum, betroffener Komponente
und Verweis auf die zugehörige Entscheidung oder den Befund.

Das CHANGELOG ist die einzige Stelle, an der sich die Geschichte des Projekts vollständig lesen
lässt, ohne Commits zu rekonstruieren. Es macht die Regeln aus Art. 6 und Art. 7 überprüfbar:
Was nicht im CHANGELOG steht, gilt als stille Änderung und ist zu beanstanden. Der Eintrag
gehört zur Änderung, nicht in einen späteren Aufräumschritt.

*Beispiel:* Der Stabilitätstest 0.1 ist mit Datum, neuen Dateien und Ergebniszahlen
(130 OK, Stabilitätsquote 86,7 %) im CHANGELOG dokumentiert; geplante Änderungen stehen unter
`[Unreleased]`.

### Art. 15 — Jede neue Version besteht Regressionstests

**Grundsatz:** Eine neue Version einer Komponente wird erst freigegeben, wenn der
Regressionslauf ohne NEUE Befunde durchläuft. Bekannte Befunde bleiben in der Baseline geführt;
neue Befunde blockieren die Freigabe oder erfordern eine ausdrückliche Entscheidung.

Ohne Regressionsschutz repariert jede Entscheidung an einer Stelle unbemerkt eine andere kaputt
— bei einer Sprache mit gekoppelten Regelbereichen ist das der Normalfall, nicht die Ausnahme.
Die Baseline trennt dabei sauber zwischen „bekannt und akzeptiert" und „neu entstanden". Die
Baseline wird nur auf ausdrücklichen Auftrag neu geschrieben.

*Beispiel:* `python3 orbis_validator.py --strict` vergleicht gegen `orbis_baseline.json`
(derzeit 39 bekannte Befunde) und beendet sich mit Exit-Code 1 bei neuen Befunden;
`python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md` fährt das kanonische Korpus mit
150 Tests. Beide Läufe sind Voraussetzung jeder Freigabe und laufen zusätzlich in der CI.

---

## Abschnitt V — KI-Zusammenarbeit

### Art. 16 — KI-Systeme dürfen ungelöste Sprachentscheidungen nicht eigenständig schließen

**Grundsatz:** Maschinelle Assistenz prüft, zählt, vergleicht, formuliert Optionen und legt
Entscheidungen vor. Sie trifft keine Sprachentscheidung, erfindet keine Wörter oder Regeln und
„repariert" keine Lücke durch Interpretation — auch dann nicht, wenn nur eine Option plausibel
erscheint.

Eine plausibel geratene Regel ist von einer beschlossenen Regel im Dokument nicht mehr zu
unterscheiden und wird binnen kurzem zitiert, getestet und weitergebaut. Damit verlagert sich
die Sprachhoheit unbemerkt vom Menschen zum Werkzeug. Vorschläge sind ausdrücklich erwünscht —
aber als Vorschlag gekennzeichnet und einer Entscheidung nach Art. 4 vorgelegt.

*Beispiel:* Die Befunde L-01…L-05 und K-05 sind seit dem Stabilitätstest offen; Berichte und
Vorlagen nennen dazu ausschließlich Lösungsrichtungen mit Kosten und Folgeänderungen, keine
Festlegungen. Claude Code dient dem Projekt als Prüfwerkzeug.

### Art. 17 — Offene Punkte werden markiert, nicht versteckt

**Grundsatz:** Fehlende Regeln, Widersprüche und Unklarheiten werden mit fester Kennzeichnung
und stabiler Befund-ID dokumentiert: `[REGELLUECKE]`, `[REGELKONFLIKT]`, `[REGELUNKLARHEIT]`.
Sie werden weder weggelassen, noch weggeschrieben, noch durch eine stillschweigende Auslegung
geschlossen.

Sichtbare offene Punkte sind ein Qualitätsmerkmal: Sie zeigen den echten Reifegrad und lenken
die nächste Entscheidungsrunde. Verdeckte offene Punkte tauchen später als Widersprüche in
Korpus, Schrift oder Tastatur wieder auf, dann jedoch teurer. Jeder Befund behält seine ID über
Versionsgrenzen hinweg, damit sein Weg bis zur Erledigung nachlesbar bleibt.

*Beispiel:* Das Korpus 0.1 weist offen 14 Regellücken, 3 Regelkonflikte, 2 Regelunklarheiten und
1 Testproblem aus; Befund U-10 hält fest, dass §26.8 fälschlich von „20 Konsonantentasten"
spricht, während 19 Konsonanten und 1 Vokalträger korrekt wären — korrigiert wird das durch eine
Entscheidung, nicht durch stilles Überschreiben der eingefrorenen Grammatik.

---

## Abschnitt VI — Schrift und Experimente

### Art. 19 — Manus und gesprochene Sprache werden technisch getrennt modelliert

**Grundsatz:** Orbis Manus (Schrift) und die gesprochene bzw. grammatische Ebene werden in
getrennten Daten, Regelwerken und Versionsständen geführt. Schriftregeln sind keine
Grammatikregeln, und Werkzeuge zur Schriftanalyse erzeugen keine Sprachregeln.

Schrift und Sprache entwickeln sich unterschiedlich schnell und haben unterschiedliche
Fehlerklassen; vermischt man sie, blockiert jede Schriftfrage die Grammatik und umgekehrt. Die
Trennung erlaubt es, Manus und Keyboard eigenständig zu versionieren, ohne die eingefrorene
Grammatik anzufassen. Berührungspunkte werden ausdrücklich als Schnittstelle beschrieben.

*Beispiel:* Befund L-09 (77 von 281 Grundformen sind mehrdeutig zerlegbar) und L-10 (undefinierte
Strichstärke für f, s, sh, x, v, z, j, ç) sind Schriftbefunde. Die Silbifizierungs-Simulation
`orbis_validator.py --sim-l09` ist ein Analysewerkzeug und darf nie als Sprachregel zitiert
werden.

### Art. 20 — Experimentelle Systeme sind ausdrücklich als EXPERIMENTAL zu kennzeichnen

**Grundsatz:** Nicht beschlossene Konzepte werden an jeder Fundstelle sichtbar als
`EXPERIMENTAL` und `NICHT KANONISCH` gekennzeichnet — in Überschrift, Datei und Datenfeld. Sie
dürfen nirgends als bestehende Orbis-Grammatik, bestehendes Lexikon oder bestehende Schrift
dargestellt werden.

Experimente sind für die Weiterentwicklung notwendig, wandern aber erfahrungsgemäß per Zitat in
den kanonischen Bestand, sobald ihr Status nicht mitgeführt wird. Eine Kennzeichnung nur im
Vorwort genügt deshalb nicht; sie muss den einzelnen Abschnitt begleiten. Kanonisch wird ein
Experiment erst durch eine Entscheidung nach Art. 4 und die Erfüllung der Artikel 5, 10 und 11.

*Beispiel:* Die Morphem-Ebene für Manus und Keyboard (sichtbare Kasus- und Tempuszeichen) sowie
die Wortspuren (Möglichkeit, Erinnerung, gehört/berichtet, selbst erlebt) sind experimentell und
nicht Bestandteil der Grammatik 0.9.3.

---

## Änderung dieser Verfassung

1. **Zuständigkeit.** Diese Verfassung ändern ausschließlich die Sprachdesigner. Werkzeuge,
   Berichte, automatisierte Läufe und KI-Systeme dürfen Änderungen vorschlagen, aber weder
   beschließen noch selbsttätig ausführen.
2. **Verfahren.** Jede Änderung erfordert eine dokumentierte Entscheidung nach Art. 4 (ADR mit
   ID `ORB-ADR-nnnn`), die den betroffenen Artikel, den alten und den neuen Wortlaut, die
   Begründung und die Folgewirkungen auf bestehende Dokumente benennt.
3. **Sichtbarkeit.** Die Änderung wird im `CHANGELOG.md` eingetragen (Art. 14) und erhöht die
   Versionsnummer dieser Verfassung. Stille Änderungen — auch redaktionelle — sind unzulässig
   (Art. 6, Art. 7).
4. **Nummernstabilität.** Artikelnummern bleiben dauerhaft stabil und werden nicht neu vergeben.
   Ein aufgehobener Artikel bleibt mit seiner Nummer und dem Vermerk „aufgehoben durch
   `ORB-ADR-nnnn`" stehen; neue Artikel werden hinten angefügt.
5. **Vorrang.** Bis eine Änderung beschlossen und eingetragen ist, gilt der bestehende Wortlaut.
   Widerspricht eine andere Projektdatei dieser Verfassung, ist das ein Befund und wird nach
   Art. 17 markiert — nicht durch Anpassung der Verfassung erledigt.
