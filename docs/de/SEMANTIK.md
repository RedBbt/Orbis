# ORBIS — Semantik: wie Bedeutung modelliert wird

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Wozu dieses Kapitel

Die Grammatik 0.9.3 hat **kein Semantikkapitel**. Sie liefert Bedeutung in Form von
Wörterbuchglossen (§24), Antonympaaren im Adjektivbestand (§24.7) und
Bedeutungsabgrenzungen an einzelnen Stellen (§24.6 zu *salv-* und *vaşn-*). Ein Modell,
das diese Angaben ordnet, gehört zur **Datenebene** des Projekts, nicht zur Sprache selbst.

Beschrieben wird hier also der Aufbau der Sprachdaten unter `language/lexicon/`, wie er in
`lexicon.schema.json` und `concept.schema.json` festgelegt ist. Für den **Inhalt** jeder
einzelnen Bedeutung bleibt allein die Grammatik 0.9.3 maßgeblich; das Datenmodell bildet
sie ab und ergänzt sie nicht.

Zwei Grundsätze rahmen alles Weitere:

- **Deutsch ist semantische Autorität** (TRANSLATION_POLICY §1, ORBIS_CONSTITUTION Art. 1).
  Englische Felder sind abgeleitet und dürfen den Bedeutungsumfang weder erweitern noch
  verengen noch präzisieren.
- **Keine stillen Bedeutungsänderungen** (Art. 6). Auch eine Präzisierung ist eine Änderung
  und braucht eine dokumentierte Entscheidung.

---

## 2. Zwei Ebenen: Konzept und Lexem

Das Modell trennt, **was** gemeint ist, von dem **Wort**, das es ausdrückt.

| Ebene | ID-Muster | Datei | Bestand |
|---|---|---|---|
| **Konzept** — sprachunabhängige Bedeutungseinheit | `ORB-CON-000000` | `language/lexicon/concepts/concepts.json` | 131 |
| **Lexem** — Wort der Sprache Orbis | `ORB-LEX-000000` | `language/lexicon/entries/<lemma>.json` | 281 |

Die Verbindung läuft in beide Richtungen: Das Lexem nennt unter `semantik.concept_ids` die
Konzepte, die es realisiert; das Konzept führt unter `lexeme` die Rückverweise (laut
`concept.schema.json` redundant, aus den Einträgen erzeugbar).

Der Sinn der Trennung: Mehrere Lexeme können dasselbe oder ein überlappendes Konzept
tragen — genau daran setzt die Synonymdifferenzierung an (Abschnitt 4). Umgekehrt kann ein
Lexem mehrere Konzepte tragen, wenn es mehrdeutig ist. IDs wechseln nie, auch nicht bei
einer Umbenennung des Lemmas (`lexicon.schema.json`, Feld `lexeme_id`;
ORBIS_CONSTITUTION Art. 7).

### 2.1 Felder eines Konzepts

| Feld | Inhalt |
|---|---|
| `concept_id` | stabile ID `ORB-CON-*` |
| `de.label` | Kurzbezeichnung, z. B. „Erinnerung" |
| `de.hauptdefinition` | kanonische Definition (Pflichtfeld) |
| `de.abgrenzung` | wogegen sich das Konzept abgrenzt |
| `en.label`, `en.definition`, `en.status` | abgeleitete englische Fassung |
| `domaene` | semantische Domäne, z. B. `natur`, `zeit`, `familie` (Pflichtfeld) |
| `oberbegriffe`, `unterbegriffe`, `verwandte`, `gegensaetze` | Verweise auf andere `ORB-CON-*` |
| `lexeme` | realisierende `ORB-LEX-*` |
| `status` | `draft` / `canonical` / `experimental` / `deprecated` |
| `quelle` | Fundstelle, hier durchgehend „Orbis-Grammatik-0.9.3.md §24" |

### 2.2 Welche Lexeme ein Konzept tragen

Nicht jedes Lexem ist ein Bedeutungsträger im Sinne des Konzeptmodells. Von den 281
Einträgen verweisen 131 auf ein Konzept:

| Wortart | mit Konzept | ohne Konzept |
|---|---|---|
| nomen | 71 | — |
| verb | 34 | — |
| adjektiv | 20 | — |
| pronomen | 6 (*kem, kelt, kur, kan, grais, kolm*) | 52 |
| artikel | — | 36 |
| partikel | — | 20 |
| präposition | — | 16 |
| zahl | — | 15 |
| konjunktion | — | 11 |
| **Summe** | **131** | **150** |

Die 150 konzeptlosen Einträge sind Funktionswörter und Flexionsformen geschlossener
Klassen (etwa die 36 Artikelformen *xra … vnaş* aus §11 oder die 36 Personalpronomenformen
aus §13.1). Ihre Bedeutung ist grammatisch, nicht lexikalisch. Die sechs Fragepronomen
tragen ein Konzept, weil sie einen abfragbaren Bedeutungsinhalt haben („wer", „was",
„wo/wohin", „wann", „warum", „wie", §18.2).

### 2.3 Domänen

Jedes Konzept liegt in genau einer Domäne. Der Bestand verteilt sich auf 26 Domänen:

| Domäne | Konzepte | Domäne | Konzepte |
|---|---|---|---|
| grammatik | 13 | mensch | 5 |
| natur | 11 | wetter | 5 |
| kommunikation | 10 | familie | 3 |
| abstrakta | 10 | beziehungen | 3 |
| zeit | 9 | tiere | 3 |
| raum | 8 | gesellschaft | 3 |
| bewegung | 8 | essen | 3 |
| existenz | 6 | bewertung | 3 |
| wahrnehmung | 6 | kultur | 2 |
| koerper | 6 | arbeit | 2 |
| denken | 6 | gefuehle | 2 |
| | | wohnen · pflanzen · transport · werkzeug | je 1 |

Die Domänen sind eine Ordnungshilfe der Datenebene, keine Kategorie der Grammatik 0.9.3.

### 2.4 Stand des Bestands

Alle 131 Konzepte tragen `status: draft`. Ihre `hauptdefinition` ist die migrierte
Wörterbuchglosse der Grammatik in Satzform; `abgrenzung`, `oberbegriffe`,
`unterbegriffe`, `verwandte` und `gegensaetze` sind durchgehend leer, ebenso jede
englische `definition`. Das Konzeptregister hält ausdrücklich fest: „Ein Konzept je
dokumentierter Glosse. Feinere semantische Differenzierung ist Designerarbeit."

Auf Lexemebene entspricht dem der Befund **W-04** (Dokumentationslücke), der an allen 281
Einträgen vermerkt ist: Sie tragen Glosse und Strukturangaben, aber keine ausformulierte
Definition, keine Bedeutungsnuancen, keine Kollokationen. Das ist offene Redaktionsarbeit
der Sprachdesigner — Werkzeuge dürfen Definitionen nicht selbst erfinden
(ORBIS_CONSTITUTION Art. 6, Art. 16).

---

## 3. Relationstypen

Bedeutungsbeziehungen stehen an zwei Stellen des Lexemschemas. Das ist kein Zufall,
sondern eine Konsequenz von Artikel 12 der Verfassung: Synonymie verlangt mehr Felder als
jede andere Relation und bekommt deshalb einen eigenen Block.

### 3.1 semantik.synonyme — Synonymie mit Pflichtangabe

| Feld | Werte / Inhalt |
|---|---|
| `lexeme_id` | Zielwort `ORB-LEX-*` (Pflicht) |
| `staerke` | **`synonym`** · **`near_synonym`** · `lose_verwandt` (Pflicht) |
| `austauschbar` | `ja` · `nein` · `teilweise` |
| `bedeutungsunterschied_de` | worin sich die beiden Wörter unterscheiden |
| `registerunterschied` | Stil-/Registerunterschied |
| `konnotationsunterschied` | Wertungsunterschied |
| `typische_kontexte` | Kontexte, in denen das eine Wort steht und das andere nicht |

Das Schema sagt dazu ausdrücklich: „Synonymrelation MIT Bedeutungsunterschied. Eine bloße
Liste genügt nicht."

### 3.2 semantik.relationen — alle übrigen Beziehungen

Ein Eintrag besteht aus `typ` (Pflicht), `ziel` (`ORB-LEX-*` oder `ORB-CON-*`, Pflicht)
und `anmerkung_de`.

| Typ | Bedeutung | Beispielrichtung |
|---|---|---|
| **antonym** | Gegensatz | *vlaid* (groß) ↔ *nirm* (klein) |
| **hypernym** | Oberbegriff des Eintragswortes | ein Wort → seine übergeordnete Kategorie |
| **hyponym** | Unterbegriff | ein Wort → ein spezielleres Wort |
| **part_of** | Teil-Ganzes-Beziehung | Teil → Ganzes |
| **related** | thematisch verwandt, ohne engere Festlegung | — |
| **derived_from** | morphologisch abgeleitet von | *meluma* → *mel-* (§21.1) |
| **historical_relation** | lautgeschichtlich verwandt | *taiv* → \*tal-iv (§22) |
| **metaphorical_extension** | übertragene Bedeutung | — |

Die letzten beiden Typen bilden ab, was die Grammatik selbst an
Bedeutungsentwicklung dokumentiert: §21.1 nennt *taiv* und *melva* als Angehörige der
Familien *tal-* und *mel-*, §22 liefert die Lautgesetze dazu.

**Zum Stand:** Im Bestand 0.1 sind ausschließlich `antonym`-Relationen belegt — 18 Stück,
also die neun Paare aus §24.7 in beiden Richtungen. `synonyme` ist bei allen 281 Einträgen
leer, ebenso `konnotation` und `bedeutungsnuancen`. Es gibt in 0.9.3 kein dokumentiertes
Synonympaar, das zu unterscheiden wäre; die Felder sind vorbereitet, nicht ungenutzt
liegengelassen.

---

## 4. Die Pflicht zur Synonymdifferenzierung

> **ORBIS_CONSTITUTION Art. 12 — Synonyme müssen semantisch unterschieden werden.**
> „Zwei kanonische Lexeme dürfen nicht dieselbe Bedeutung tragen. Jedes Synonympaar erhält
> im Lexikon eine ausdrückliche Unterscheidung (Bedeutungsnuance, Register, Kollokation
> oder Verwendungsbereich). […] Lässt sich kein Unterschied angeben, ist eine der Formen
> kein eigenes Lexem."

Die Begründung ist prüftechnisch: Ununterschiedene Synonyme machen Übersetzungen
unentscheidbar. Weder Mensch noch Werkzeug kann begründen, welche Form richtig ist, und
ein Testkorpus wird mehrdeutig bewertbar. Die Unterscheidung darf schmal sein, muss aber
benannt und prüfbar sein.

**Das Vorbild steht in der Grammatik selbst.** §24.6 unterscheidet zwei Wurzeln, die im
Deutschen leicht zusammenfallen:

| Wurzel | Bedeutung | Valenz | Beleg §24.6 |
|---|---|---|---|
| **salv-** | verlieren | **transitiv** — jemand verliert etwas | *Vim salvam xnan vreston.* — Ich verliere das Buch. |
| **vaşn-** | vergehen, schwinden | **intransitiv** — etwas vergeht von selbst | *Xla soruma vaşnat.* — Die Erinnerung vergeht. |

§24.6 schließt ausdrücklich: „Sie sind nicht austauschbar." Genau diese Art von Aussage
verlangt Art. 12 für jedes künftige Synonympaar — im Datenmodell abgelegt als
`austauschbar: nein` plus `bedeutungsunterschied_de`.

---

## 5. Antonymie: die neun belegten Paare (§24.7)

§24.7 listet 20 Adjektive als Grundformen. Achtzehn davon stehen paarweise; die Paarung
ergibt sich aus der Reihenfolge und den Glossen der Liste:

| Nr. | Wort | Bedeutung | Gegenwort | Bedeutung |
|---|---|---|---|---|
| 1 | **vlaid** | groß | **nirm** | klein |
| 2 | **selv** | gut | **morn** | schlecht |
| 3 | **granz** | alt | **zirv** | neu |
| 4 | **trelm** | lang | **misn** | kurz |
| 5 | **velm** | warm | **girn** | kalt |
| 6 | **luid** | hell | **şaln** | dunkel |
| 7 | **xarn** | stark | **vresn** | schwach |
| 8 | **zilv** | schnell | **tolm** | langsam |
| 9 | **klaun** | wahr | **norv** | falsch |

Ohne Partner bleiben die beiden übrigen Adjektive der Liste: **loşn** (schön) und **xan**
(kein). *xan* ist ohnehin ein Sonderfall — es dient nach §18.3 als attributive Negation
(*xanra valru*, „kein Mann") und nicht als beschreibendes Adjektiv.

Im Lexikon sind diese neun Paare als je zwei `antonym`-Relationen abgelegt, mit der
Anmerkung „Gegensatzpaar aus dem Adjektivbestand §24.7". Sie sind der einzige Teil des
Relationsnetzes, der aus der Grammatik direkt belegbar war.

**Belege im Satz** (Testkorpus / §25):

| Paar | Beleg | Übersetzung |
|---|---|---|
| granz ↔ zirv | *Xna breun granz stanat, klas xla kavla zirv vurt.* (§25.1) | Das Haus bleibt alt, aber die Stadt wird neu. |
| luid ↔ girn/velm | *Xla luiv luid vot, xla kirva girn vot.* (§25.2) | Die Sonne war hell, die Nacht war kalt. |
| zilv ↔ tolm | *Xla soruma xlas nauşes vran tolm vaşnat.* (§25.1) | Die Erinnerung der Zeit vergeht sehr langsam. |

Der letzte Satz ist zugleich Gegenstand von **K-04**: Er verwendet *tolm* adverbial ohne
das nach §12.4 erforderliche *-un*. Das betrifft die Adjektivmorphologie, nicht die
Antonymie (siehe `ADJEKTIVE.md`).

---

## 6. Homonymie: wenn eine Form zwei Bedeutungen trägt

Homonymie ist im Modell kein Relationstyp, sondern ein **Befund**: zwei Lexeme mit
getrennten IDs, aber gleicher Lautform. Das Datenmodell trennt sie sauber (zwei Einträge,
zwei `lexeme_id`); die Frage, ob die Kollision hinnehmbar ist, entscheiden die
Sprachdesigner.

### 6.1 [WORTSCHATZKOLLISION W-02] — velkran

> **W-02 (P2, offen): Formkollision *velkran*.**
> *velkran* „Freundschaft" (Nominativ, 10-Prozent-Gruppe §10.1) ist formgleich mit dem
> **Akkusativ** von *velkra* „Freund" (M-A, §24.2). Beide gehören zum selben semantischen
> Feld; artikellose Kontexte sind mehrdeutig.

Das ist die einzige **harte Flexionskollision** im gesamten Bestand: Nicht zwei
Wörterbuchformen fallen zusammen, sondern eine Wörterbuchform und eine Flexionsform.
Der Wortschatz-Freeze (§24) erlaubt Änderungen ausdrücklich bei „problematischer Kollision
mit einem anderen Wort" — eine Umbenennung wurde jedoch nicht vorgenommen; die
Entscheidung ist als ADR vorbereitet und steht aus.

### 6.2 [WORTSCHATZKOLLISION W-03] — weitere Homonyme

> **W-03 (P3, offen): Weitere Homonyme und Verwechselbarkeiten.**

| Form | Bedeutung 1 | Bedeutung 2 | Quellen |
|---|---|---|---|
| **fai** | Konjunktion „dass" | Relativpronomen | §20 / §13.4 (dazu L-02) |
| **kaun** | Kernwort „Mensch" | Indefinitpronomen „man" | §24.1 / §13.4 |
| **vran** | unbestimmter Artikel M Akk | Partikel „sehr" | §11 / §24.9 |
| **xa** | Negationspartikel „nicht" | Vorsilbe „Gegenteil, Fehlen" | §18.3 / §21.2 |

Dazu registriert W-03 ähnliche, nicht identische Paare, bei denen Verwechslung droht:
*nest-* (wollen) / *nast-* (essen), *tolm* (langsam) / *dolm-* (müssen), *şaln* (dunkel) /
*şlan* (trotz), *kalm* (vier) / *kolm* (wie), *xer* (denn) / *xerp* (Feuer).

Im Lexikon erscheinen die echten Homonyme als getrennte Dateien mit angehängter Ziffer
(*fai.json* und *fai__2.json*, *kaun.json* und *kaun__2.json*, *vran.json* und
*vran__2.json*); vier Einträge tragen `W-03` in `qualitaet.offene_befunde`.

ORBIS_CONSTITUTION Art. 6 nennt gerade den Fall *fai* als Beispiel dafür, was **nicht**
geschehen darf: Die Homonymie „darf nicht durch eine beiläufige Umformulierung aufgelöst
werden; sie ist Gegenstand der offenen Entscheidung zu Befund L-02."

---

## 7. Was das Modell nicht tut

| Nicht erlaubt | Grund |
|---|---|
| Bedeutungen ergänzen, präzisieren oder verschieben | Art. 6 — keine stillen Bedeutungsänderungen |
| Relationen erfinden, für die kein Beleg existiert | Art. 16 — keine eigenständigen Sprachentscheidungen |
| Englische Felder abweichend von der deutschen Fassung füllen | TRANSLATION_POLICY §1 — Deutsch ist Autorität |
| Homonyme durch Umbenennung auflösen | Art. 7 — keine stillen Umbenennungen; Wortschatz eingefroren (§24) |
| Fehlende Wörter selbst bilden | W-01 bleibt offen, bis entschieden ist |

---

## 8. Befundübersicht zu diesem Kapitel

| ID | Typ | Betrifft | Kurzfassung |
|---|---|---|---|
| **W-02** | WORTSCHATZKOLLISION | §10.1, §24.2 | *velkran* = Nominativ „Freundschaft" und Akkusativ von *velkra* |
| **W-03** | WORTSCHATZKOLLISION | §11, §13.4, §18.3, §20, §21.2, §24 | *fai*, *kaun*, *vran*, *xa* und ähnliche Paare |
| **W-04** | DOKUMENTATIONSLÜCKE | §24 | 281 Einträge ohne ausformulierte Definition |
| **W-01** | WORTSCHATZLÜCKE | §24 | „sagen", „zeigen", „suchen", „es gibt" fehlen |

Quellen dieses Kapitels: `language/lexicon/lexicon.schema.json`,
`language/lexicon/concept.schema.json`, `language/lexicon/concepts/concepts.json`,
`language/findings/findings.json`, `ORBIS_CONSTITUTION.md`, `TRANSLATION_POLICY.md` sowie
für alle Sprachinhalte `Orbis-Grammatik-0.9.3.md`.
