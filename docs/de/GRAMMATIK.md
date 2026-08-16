# ORBIS — Grammatik: Überblick und Einstieg

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Die verbindliche Referenz

Die **verbindliche Referenz der Sprache Orbis ist `Orbis-Grammatik-0.9.3.md`**. Diese
Dokumentation unter `docs/de/` beschreibt sie; sie ersetzt sie nicht, erweitert sie nicht
und verengt sie nicht.

| | |
|---|---|
| **Referenz** | `Orbis-Grammatik-0.9.3.md` — kanonisch, eingefroren, READ ONLY |
| **Diese Dokumentation** | `docs/de/*.md` — abgeleitete Beschreibung, kanonische Dokumentationssprache Deutsch |
| **Englische Fassung** | `docs/en/*.md` — aus dem Deutschen abgeleitet (`TRANSLATION_POLICY.md`) |
| **Maschinenlesbare Daten** | `language/*.json` — Abbild derselben Regeln, heute noch nicht Source of Truth |

Daraus folgen drei Grundsätze, die für jede Datei dieses Verzeichnisses gelten:

- **Weicht diese Dokumentation von der Grammatik ab, gilt die Grammatik.** Die Abweichung
  ist ein Befund und wird gemeldet, nicht still angeglichen.
- **Hier wird nichts entschieden.** Wo die Grammatik schweigt oder sich widerspricht, steht
  die Befund-ID aus `Orbis-Audit-0_1.md` und der Marker `[REGELLÜCKE]`,
  `[REGELKONFLIKT]` oder `[REGELUNKLARHEIT]`. Lücken werden benannt, nicht geschlossen.
- **Belegpflicht.** Jede Orbis-Form in dieser Dokumentation stammt aus der Grammatik
  (§24, §25), aus dem Testkorpus (`Orbis-Testkorpus-0_1.md`) oder ist ausdrücklich als
  regelabgeleitet gekennzeichnet. Ungrammatische Formen tragen **†**.

Schrift und gesprochene Sprache sind getrennte Ebenen: Manus-Regeln (§26) und
Grammatikregeln werden nicht vermischt, und ein Schriftbefund ist kein Grammatikbefund.

---

## 2. Die 18 Kapitel dieser Dokumentation

### 2.1 Lautebene

| Kapitel | Datei | Inhalt |
|---|---|---|
| Phonologie | `PHONOLOGIE.md` | Das Lautinventar: 19 Konsonanten und 5 Vokale (§2.1–2.2), die Diphthonge (§2.3), die beiden Klanggruppen (§3.2) und die Frage, welche dieser Aussagen verbindlich (§3.3) und welche bloß beschreibend sind (§3.4, §3.5). |
| Aussprache | `AUSSPRACHE.md` | Was die Grammatik zur Lautung sagt (§2.1–2.3), die Trennung der drei Ebenen A/B/C (§4) und die Betonungsregeln (§23) — mit dem ausdrücklichen Vorbehalt, dass 0.9.3 keine verbindliche IPA-Zuordnung enthält. |
| Phonotaktik | `PHONOTAKTIK.md` | §5: die erlaubten Silbenformen (§5.1), die Konsonantengruppen am Silbenanfang (§5.2) und am Silbenende (§5.3) sowie Wortlänge und Wortausgang (§5.4), samt den Vorbehalten K-01 und L-09. |

### 2.2 Formenlehre

| Kapitel | Datei | Inhalt |
|---|---|---|
| Formenlehre | `MORPHOLOGIE.md` | Der Überblick über alles, was flektiert oder abgeleitet wird: das agglutinierende Aufbauprinzip (§8), die drei Nomengruppen, Verb und Adjektiv im Kurzriss, die Klangregeln (§3.5) und die Fugenregel (§21.4). |
| Nomen | `NOMEN.md` | §6–§11: Klassenkonsonant und Themavokal (§6), die 45 regulären Geschlechtsendungen (§7), die vier Fälle (§8), der Plural (§9), die 15 Kernwörter und die 10-Prozent-Gruppe (§10) sowie der Artikel (§11). |
| Adjektiv | `ADJEKTIVE.md` | §12: die zwei Zustände attributiv (§12.1) und prädikativ (§12.2), Steigerung (§12.3), Adverbbildung (§12.4), Nominalisierung (§12.5) und die 20 Grundadjektive (§24.7). |
| Pronomen | `PRONOMEN.md` | §13, getrennt nach Reifegrad: die vollständig deklinierten Personalpronomen mit Höflichkeitsform und Possessiv (§13.1–§13.3) und der offene Bestand der übrigen Pronomen (§13.4) mit L-02, L-04, L-06 und K-02. |
| Verb | `VERBEN.md` | §14–§16: Wurzel + Tempusvokal + Personendung (§14), die regelmäßige Konjugation und die acht unregelmäßigen Verben (§15), Modalverben (§16.1), die Möglichkeitsform *mai* (§16.2) und das Passiv (§16.3). |
| Wortbildung | `WORTBILDUNG.md` | §21: die drei Verfahren Suffixableitung (§21.1), Vorsilbenableitung (§21.2) und Zusammensetzung (§21.3), darüber die Fugenregel (§21.4) — und die Feststellung, dass Produktivität kein neues Lexem schafft. |

### 2.3 Satzebene

| Kapitel | Datei | Inhalt |
|---|---|---|
| Syntax | `SYNTAX.md` | Der Überblick über §17–§20: die beiden Verbstellungen, die Verbklammer, die Satzgliedfolge, Fragetypen (§18.1, §18.2), Negation (§18.3), das Präpositionssystem (§19) und die Konjunktionen (§20). |
| Satzstellung | `SATZSTELLUNG.md` | Jede belegbare Satzkonstruktion einzeln — 22 Abschnitte von der Grundstellung bis zur Informationsstruktur, jeweils mit Beleg, Muster, gültigen und ungültigen Umstellungen und Regel-ID. |

### 2.4 Wortschatz und Bedeutung

| Kapitel | Datei | Inhalt |
|---|---|---|
| Lexikon | `LEXIKON.md` | Aufbau des maschinenlesbaren Lexikons unter `language/lexicon/` zum eingefrorenen Wortschatz aus §24: Pflichtfelder eines Eintrags, Statusmodell, Häufigkeitsstufen und die Wortschatzlücke W-01. |
| Semantik | `SEMANTIK.md` | Wie Bedeutung im Datenmodell abgebildet wird — Konzept (`ORB-CON-*`) und Lexem (`ORB-LEX-*`), Relationstypen, die Pflicht zur Synonymdifferenzierung, die neun belegten Antonympaare (§24.7) und Homonymie. |
| Korpus | `CORPUS.md` | Wie Orbis-Sätze geführt werden: die Bestände, die stabilen IDs `ORB-SENT-*`, Rollen und Pflichtfelder eines Satzes, die Kennzahlen des Testkorpus 0.1 und der Umgang mit nicht bildbaren Sätzen. |
| Proto-Orbis | `PROTO_ORBIS.md` | §22: die sieben historischen Lautgesetze mit ihren Belegen, ihre Einordnung als Ebene C (§4.3) — Sprachgeschichte, keine Aussprachehinweise — und die Statuswerte für Etymologien. |

### 2.5 Schrift und Eingabe

| Kapitel | Datei | Inhalt |
|---|---|---|
| Manus | `MANUS.md` | §26 vollständig: Silbenformel (§26.1), die 20 Kernformen in 8 Familien (§26.2), zweiter Anfangskonsonant (§26.3), Vokalpunkte und Diphthonge (§26.4), ein und zwei Endkonsonanten (§26.5–26.6), Coda und Satzabschluss (§26.7), Tastatureingabe (§26.8), Schreibregeln (§26.9) — mit L-09, L-10, U-10. |
| Magna | `MAGNA.md` | §27: Orbis Magna als feierliche Ausführung derselben Kernformen, nicht als zweite Schrift — kurz gehalten wie §27 selbst, samt dem, was dort ausdrücklich offen bleibt. |
| Tastatur | `TASTATUR.md` | Der Planungsstand der Eingabe: was §26.8 vorgibt, die Architekturskizze der Verarbeitungskette und warum L-09, L-10 und U-10 den Bau blockieren — eine Planung, keine Spezifikation. |

---

## 3. Kurzübersicht des Sprachsystems

Diese Übersicht ist ein Wegweiser in die Kapitel, keine Regelquelle. Maßgeblich sind die
genannten Paragraphen der Grammatik.

### 3.1 Lautsystem

- **19 Konsonanten und 5 Vokale** (§2.1–2.2); dazu Diphthonge (§2.3). Die Sonderzeichen
  *ş*, *ñ* und *ç* sind eigene Konsonanten, keine Schreibvarianten.
- **Zwei Klanggruppen** (§3.2); §3.3 unterscheidet verbindliche Regeln von den bloß
  beschreibenden Richtlinien in §3.4 und §3.5.
- **Silbenformen** V · KV · KVK · KKV · KKVK · KVKK (§5.1), Anfangsgruppen (§5.2),
  Coda-Bedingungen (§5.3), Wortlänge und Wortausgang (§5.4). Ein Wort, das dagegen
  verstößt, ist kein gültiges Orbis (§3.3).
- **Betonung** nach §23. Eine verbindliche IPA-Zuordnung gibt es in 0.9.3 nicht.
- **Historische Lautgesetze** (§22) gehören zur Ebene C und sind ausdrücklich keine
  Aussprachehinweise (§4.3).

### 3.2 Nomen

- Formel **Klassenkonsonant + Themavokal** (§6); das Geschlecht ist bei etwa 90 % der
  Nomen an der Endung erkennbar.
- Merksatz der Grammatik (§7.3): **r-k-d männlich · l-v-m weiblich · n-s-t sächlich.**
- Neun Klassenkonsonanten × fünf Themavokale = **45 reguläre Geschlechtsendungen** (§7).
- **Vier Fälle** — Nominativ, Akkusativ, Dativ, Genitiv (§8) — und ein regelmäßiger
  **Plural** (§9).
- Unregelmäßiger Bestand: die 15 Kernwörter und die 10-Prozent-Gruppe (§10); **Artikel**
  nach §11.
- Das **Adjektiv** ist attributiv kongruent (Stamm + *r / l / n* + *a* + Marker, §12.1)
  und prädikativ endungslos (§12.2); die Wörterbuchform ist die Grundform (§24.7).
- **Personalpronomen** sind in allen vier Fällen durchdekliniert (§13.1), mit
  Höflichkeitsform (§13.2) und Possessiv (§13.3).

### 3.3 Verben

- Formel **Wurzel + Tempusvokal + Personendung** (§14); kein Klassenkonsonant, kein
  Themavokal.
- **Personendungen** -m / -ş / -t im Singular, Plural durchgehend + **-en** (§14, §28).
- **Tempusvokale**: Gegenwart **-a-**, Vergangenheit **-o-**, Zukunft **-ai-** (§15).
- **Acht unregelmäßige Verben** (§15.2).
- **Modalität**: konjugiertes Modalverb auf Position 2, Vollverb im Infinitiv am Satzende
  (§16.1); Möglichkeitsform mit der Partikel *mai* unmittelbar vor dem finiten Verb
  (§16.2); **Passiv** mit der Vorsilbe *şu-*, Zustandspassiv mit Partizip + *esex* (§16.3).

### 3.4 Satzbau

- **Zwei Verbstellungen**: finites Verb auf Position 2 im Aussagehauptsatz (§17.1), am
  Ende im Nebensatz (§17.2).
- **Verbklammer** (§17.3, §16.1); Satzgliedfolge im Mittelfeld als ausdrückliche Tendenz
  Zeit – Grund – Art – Ort (§17.4); **keine Kopula-Auslassung** (§17.5).
- **Fragen**: Ja/Nein-Frage mit Verb auf Position 1 (§18.1), W-Fragen mit *kem*, *kelt*,
  *kur*, *kan*, *grais*, *kolm*, *kelra/kella/kelna* (§18.2).
- **Negation**: Partikel *xa* vor dem finiten Verb, attributiv dekliniertes *xan-* (§18.3).
- **Präpositionen** regieren feste Kasus, teils Dativ = Ort gegen Akkusativ = Richtung
  (§19); **Konjunktionen** teilen sich in nebenordnende mit Hauptsatzstellung und
  unterordnende mit Verbendstellung (§20).
- **Wortbildung**: Suffix, Vorsilbe, Zusammensetzung, darüber die Fugenregel (§21). Der
  Wortschatz ist ab 0.9.3 eingefroren (§24) — ein produktives Muster erzeugt kein neues
  Lexem.

### 3.5 Schrift

- **Orbis Manus** ist die Alltagsschrift und eine **Silbenschrift**: geschrieben wird
  Silbenblock für Silbenblock, nicht Buchstabe für Buchstabe (§26.1).
- **20 Kernformen in 8 Familien** (§26.2), zweiter Anfangskonsonant (§26.3), Vokalpunkte
  und zusammengesetzte Diphthonge (§26.4).
- Ein und zwei Endkonsonanten haben feste Plätze (§26.5–26.6); Coda und Satzabschluss sind
  zwei Ebenen, mit sechs Abschlusszeichen (§26.7).
- **Eingabe** nach dem Hangul-Prinzip in Sprechreihenfolge (§26.8); Schreibregeln und
  Strichstärke in §26.9.
- **Orbis Magna** ist keine zweite Schrift, sondern eine stilistische Schicht über
  denselben Kernformen, für Zitate, Inschriften, Symbole, Kunst und Titel (§27).
- Die **Morphem-Ebene** für Manus und Tastatur (sichtbare Kasus- und Tempuszeichen) sowie
  die **Wortspuren** (Möglichkeit, Erinnerung, gehört/berichtet, selbst erlebt) sind
  **EXPERIMENTELL und NICHT KANONISCH**; sie sind kein Bestandteil von Orbis 0.9.3.

---

## 4. Was ist offen

Der Audit 0.1 (`Orbis-Audit-0_1.md`) verzeichnet zu 0.9.3 **kein P0**. Sechs Befunde sind
als **P1** eingestuft; sie sind alle additiv lösbar, also ohne Änderung bestehender Regeln.
Zwei weitere Befunde blockieren Schrift und Tastatur.

### 4.1 Die sechs P1-Befunde

| ID | Typ | Betrifft | Was offen ist |
|---|---|---|---|
| **L-01** | [REGELLÜCKE] | §8, §17 | Die Stellung des Genitivattributs ist nicht festgelegt; alle Beispiele stellen es nach, aber eine Regel für Nomen-Genitive — samt Reihenfolge bei Stapelung mit dem Possessiv — gibt es nicht. |
| **L-02** | [REGELLÜCKE] | §13.4, §17 | Der Relativsatzbau fehlt vollständig: Kasus, Kongruenz und Verbstellung von *fai* sind ungeregelt, dazu kommt die Homonymie mit *fai* „dass" (§20). |
| **L-03** | [REGELLÜCKE] | §18.2 | Die Deklination von *kem* und *kelt* ist undefiniert; „wen?", „wem?", „wessen?" sind nicht bildbar, und weder Kasusformen noch Indeklinabilität sind festgelegt. |
| **L-04** | [REGELLÜCKE] | §13.4 | Für das Reflexivpronomen *se* fehlen die Kasusformen; ungeklärt bleibt auch, ob es indeklinabel ist und für welche Personen es gilt. |
| **L-05** | [REGELLÜCKE] | §16.3 | Das Agens im Passiv ist undefiniert: „Das Haus wird vom Mann gebaut" ist nicht bildbar, da §16.3 nur die Vorsilbe *şu-* regelt. |
| **K-05** | [REGELKONFLIKT] | §16.1 ↔ §17.2 | Modalverb im Nebensatz: Infinitiv (§16.1) und finites Verb (§17.2) beanspruchen beide das Satzende; kein Beispiel in 0.9.3 enthält diesen Fall. |

### 4.2 Die beiden blockierenden Befunde

| ID | Typ | Betrifft | Was offen ist |
|---|---|---|---|
| **L-09** | [REGELLÜCKE] | §5, §26 | Es gibt keine Silbifizierungs-Präferenzregel; 77 von 281 Grundformen haben mehr als eine regelkonforme Manus-Schreibung. Blockiert Manus und damit die Tastatur. |
| **L-10** | [REGELLÜCKE] | §26.9 | Für *f s ş x v z j ç* ist keine Strichstärke definiert; die Strichstärkenregel deckt nicht alle 19 Konsonanten. Blockiert die Fertigstellung der Schriftspezifikation. |

### 4.3 Wie mit diesen Punkten umzugehen ist

**Diese Punkte entscheiden die Sprachdesigner.** Weder diese Dokumentation noch die
Werkzeugkette schließen sie: keine Analogiebildung, keine Interpretation, keine
Zwischenlösung, die sich später wie eine Regel liest. Bis zu einer dokumentierten
Entscheidung mit Decision-ID (`ORB-ADR-*`) bleiben die Fälle mit ihrem Marker und ihrer
Befund-ID sichtbar markiert.

Die Silbifizierungs-Simulation `--sim-l09` des Validators ist ein Analysewerkzeug zur
Quantifizierung von L-09 und **keine Sprachregel**; sie darf nie als Regel zitiert werden.

Die Regelbefunde K-01 bis K-05, L-01 bis L-10 und U-01 bis U-14 stehen in
`Orbis-Audit-0_1.md` (§A). Die Wortschatz- und Dokumentationsbefunde W-01 bis W-04 stammen
aus Phase 7 des Testberichts bzw. sind bei der Migration hinzugekommen; das vollständige
Register mit allen 33 Befunden ist `language/findings/findings.json`. Das Gesamturteil für
einen direkten Sprung auf 1.0 lautet **NOT READY**.

---

## 5. Querverweise

| Datei | Inhalt |
|---|---|
| `Orbis-Grammatik-0.9.3.md` | die verbindliche Referenz (READ ONLY) |
| `Orbis-Audit-0_1.md` | alle Befunde K-xx, L-xx, U-xx, W-xx |
| `Orbis-Testkorpus-0_1.md` | Testkorpus 0.1, 150 Prüfsätze |
| `ORBIS_CONSTITUTION.md` | höchste Norm des Projekts, Artikel 1–20 |
| `TRANSLATION_POLICY.md` | Sprach- und Übersetzungspolitik, Deutsch als semantische Autorität |
| `VERSIONING.md` | getrennte Versionierung von Grammar, Lexicon, Manus, Keyboard, Corpus, Tools |
| `docs/en/GRAMMAR.md` | die abgeleitete englische Fassung dieses Kapitels |
