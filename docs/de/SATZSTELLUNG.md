# ORBIS — Satzstellung: die Konstruktionen im Einzelnen

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

Dieses Kapitel führt jede belegbare Satzkonstruktion von Orbis einzeln vor. `SYNTAX.md`
gibt den Überblick über §17–§20; hier steht die Umstellprobe.

## Aufbau eines Abschnitts

Jeder Abschnitt hat dieselben acht Felder:

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | der deutsche Satz — Deutsch ist die semantische Autorität (`TRANSLATION_POLICY.md`) |
| **(b) Orbis** | der **belegte** Orbis-Satz mit Fundstelle (§n der Grammatik oder Testnummer des Korpus) |
| **(c) Englisch** | aus dem Deutschen abgeleitet, nie aus dem Orbis-Wort erraten |
| **(d) Muster** | abstraktes Satzmuster in der Notation von `language/corpus/sentence.schema.json` |
| **(e) Erklärung** | welche Regel die Stellung erzwingt |
| **(f) Gültige Umstellungen** | was die Regeln zulassen |
| **(g) Ungültige Umstellungen** | was die Regeln ausschließen |
| **(h) Regel-ID** | `ORB-GRAM-SYN-*` aus `language/syntax/rules.json` |

## Konventionen

- **Kein Satz unter (b) ist erfunden.** Jede Orbis-Zeile trägt ihre Fundstelle. Wo kein
  Beleg existiert, steht das ausdrücklich da und der Abschnitt beschreibt nur die Lage.
- Unter (f) und (g) sind Umstellungen nötigerweise konstruiert. Sie tragen die Marke
  **[Beleg …]**, wenn die umgestellte Form selbst belegt ist, sonst **[regelabgeleitet]**.
- **†** markiert eine nach 0.9.3 ungültige Form — so wie die Grammatik selbst in §12.2
  (*†Lo loşna est*).
- **Diese Datei entscheidet nichts.** Wo die Grammatik schweigt oder sich widerspricht,
  steht die Befund-ID aus `Orbis-Audit-0_1.md` §A.

## Musternotation

| Kürzel | Bedeutung |
|---|---|
| NP | Nominalgruppe (Artikel + ggf. Adjektiv + Nomen) |
| PRON | Pronomen |
| V | finites Verb oder Infinitiv |
| ADJ | prädikatives oder attributives Adjektiv |
| PART | Partikel (*xa*, *mai*) oder Adverb |
| P | Präposition |
| W | Fragewort |
| KONJ | Konjunktion |
| SUBJ | Beginn eines Nebensatzes |

---

## Übersicht

| # | Konstruktion | Muster | Regel-ID | Befund |
|---|---|---|---|---|
| 1 | Grundstellung | NP-V-NP | ORB-GRAM-SYN-010 | — |
| 2 | Topikalisierung | X-V-… | ORB-GRAM-SYN-010 | — |
| 3 | Objekt im Vorfeld | NP-V-NP | ORB-GRAM-SYN-010 | — |
| 4 | Zeit im Vorfeld | PART-V-NP-NP | ORB-GRAM-SYN-010 | U-11 |
| 5 | Adverb/Adverbiale im Vorfeld | P-NP-V-PRON-NP | ORB-GRAM-SYN-010 | — |
| 6 | Ja/Nein-Frage | V-PRON-PART | ORB-GRAM-SYN-016 | U-04 |
| 7 | W-Frage | W-V(-PRON) | ORB-GRAM-SYN-017 | L-03, U-04 |
| 8 | Negation | PRON-PART-V | ORB-GRAM-SYN-018 | U-14 |
| 9 | Modalverb | PRON-V-NP-V | ORB-GRAM-SYN-013 | U-03 |
| 10 | Modalverb + Negation | NP-PART-V-V | ORB-GRAM-SYN-013 / -018 | K-05 |
| 11 | Nebensatz | PRON-V-SUBJ-KONJ-PRON-V | ORB-GRAM-SYN-011 | K-05 |
| 12 | Nebensatz vor Hauptsatz | SUBJ-KONJ-PRON-V-V-PRON | ORB-GRAM-SYN-012 | — |
| 13 | Relativsatz | nicht bestimmbar | ORB-GRAM-SYN-022 | **L-02** |
| 14 | Passiv | NP-V | ORB-GRAM-SYN-019 | **L-05** |
| 15 | Dativ + Akkusativ | NP-V-NP-NP | ORB-GRAM-SYN-023 | U-05 |
| 16 | Genitivattribute | NP-NP-V | ORB-GRAM-SYN-021 | **L-01** |
| 17 | Prädikative Konstruktionen | PRON-ADJ-V | ORB-GRAM-SYN-015 | U-13 |
| 18 | Konditional (*mai*) | SUBJ-KONJ-…-PART-V, PART-V-PRON | ORB-GRAM-SYN-020 | — |
| 19 | Mehrfach-Nebensätze | kein Beleg | ORB-GRAM-SYN-011 / -012 | K-05 |
| 20 | Koordination | [HS] KONJ-[HS] | §20 / ORB-GRAM-SYN-002 | — |
| 21 | Kontrast | [HS] KONJ-[HS] | §20 / ORB-GRAM-SYN-002 | U-13 |
| 22 | Informationsstruktur | — | ORB-GRAM-SYN-010 / -014 | — |

---

## 1. Grundstellung

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Der Mann sieht den Hund. |
| **(b) Orbis** | *Xra valru milkat xran narkun.* — **Beleg §17.1**, wortgleich in §25.1 |
| **(c) Englisch** | The man sees the dog. |
| **(d) Muster** | NP-V-NP |
| **(h) Regel-ID** | ORB-GRAM-SYN-010 (§17.1) |

**(e) Erklärung.** Die Grundstellung ist Subjekt – finites Verb – Objekt. Sie ist kein
eigenes Gesetz, sondern der Fall, in dem das Subjekt das Vorfeld füllt: §17.1 verlangt allein,
dass das finite Verb an **Position 2** steht. Das Objekt trägt den Akkusativ (*xran narkun*),
nicht die Stellung; Kasus und Kongruenz machen den Satz auch bei anderer Folge eindeutig.

Minimalform ohne Objekt: Test 001 *Xra valru melat.* — Der Mann geht. (NP-V) ·
Test 021 *Vim milkam xran narkun.* — Ich sehe den Hund. (PRON-V-NP)

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| *Xran narkun milkat xra valru.* — Den Hund sieht der Mann. | **[Beleg §17.1]** |
| *Nunda milkat xra valru xran narkun.* — Heute sieht der Mann den Hund. | **[Beleg §17.1]** — ein Zeitausdruck tritt hinzu und besetzt das Vorfeld |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Xra valru xran narkun milkat.* | Verb an Position 3 — §17.1 [regelabgeleitet] |
| †*Xran narkun xra valru milkat.* | Verb an Position 3 — §17.1 [regelabgeleitet] |
| †*Milkat xra valru xran narkun.* (als Aussage) | Verb an Position 1; das ist nach §18.1 die Ja/Nein-Frage, nicht der Aussagesatz [regelabgeleitet] |

---

## 2. Topikalisierung

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Den Hund sieht der Mann. / Heute sieht der Mann den Hund. |
| **(b) Orbis** | *Xran narkun milkat xra valru.* · *Nunda milkat xra valru xran narkun.* — **Beleg §17.1** |
| **(c) Englisch** | The dog, the man sees. / Today the man sees the dog. |
| **(d) Muster** | X-V-… (X = ein beliebiges Satzglied) |
| **(h) Regel-ID** | ORB-GRAM-SYN-010 (§17.1) |

**(e) Erklärung.** §17.1 belegt die V2-Regel gerade dadurch, dass es **dieselbe Aussage in
drei Stellungen** vorführt. Daraus folgt das Grundprinzip der Orbis-Satzstellung: Das Vorfeld
ist **ein einziges freies Feld**, in dem genau **ein** Satzglied steht; das finite Verb folgt
unmittelbar. Welches Satzglied das ist, entscheidet keine Regel der Grammatik.

Belegte Vorfeldbesetzungen:

| Vorfeld | Beleg |
|---|---|
| Subjekt-NP | *Xra valru milkat xran narkun.* (§17.1) |
| Objekt-NP (Akk) | *Xran narkun milkat xra valru.* (§17.1) · *Xnan melnan traivamen viñ, tund …* (§25.1) |
| Zeitadverb | *Nunda milkat …* (§17.1) · *Nunda melam vim dun xnaş breuneş vis.* (§25.1) · Test 132 *Zirna ruskaim vim.* |
| Dativ-Zeitangabe | *Vraş zaldreş traivot ro vnan aulen şlim xrañaş larkiñiş.* (§25.2) — **U-11** |
| Präpositionalgruppe | *Tel xraş navildoş milkot ro xlan luiven xlas eirdes.* (§25.2) |
| Demonstrativpronomen | *Kilna est xna traivute.* (§25.2) |
| Nebensatz | *Tund vim vra vlaidra valru mai em, mai traivam vim xlan eirden.* (§25.1) |

Steht ein anderes Satzglied als das Subjekt im Vorfeld, rückt das Subjekt hinter das Verb.
Das ist keine eigene Regel, sondern die Folge der V2-Stellung.

**(f) Gültige Umstellungen.** Jede der obigen Zeilen ist die Umstellung einer anderen. Die
Grammatik nennt keine Beschränkung, welches Satzglied topikalisiert werden darf.

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Nunda xra valru milkat xran narkun.* | zwei Satzglieder im Vorfeld, Verb an Position 3 — §17.1 [regelabgeleitet] |
| †*Xran narkun nunda milkat xra valru.* | dito [regelabgeleitet] |

Der einzige belegte Fall, in dem das finite Verb **nicht** an zweiter Wortstelle steht, ist
das Prädikativ (*Lo loşn est*, §12.2) — genau darum geht es in **U-13**, Abschnitt 17.

---

## 3. Objekt im Vorfeld

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Den Hund sieht der Mann. |
| **(b) Orbis** | *Xran narkun milkat xra valru.* — **Beleg §17.1** |
| **(c) Englisch** | The dog, the man sees. — sinngleich mit *The man sees the dog*; das Englische bildet die Vorfeldbesetzung nicht ab, weil Stellung dort kein Kasusmittel ist |
| **(d) Muster** | NP-V-NP (Akk-V-Nom) |
| **(h) Regel-ID** | ORB-GRAM-SYN-010 (§17.1) |

**(e) Erklärung.** Das Objekt ist durch den Akkusativ markiert (*xran narkun*), das Subjekt
durch den Nominativ (*xra valru*). Die Vorfeldstellung des Objekts erzeugt darum **keine
Mehrdeutigkeit**: Die Rollen hängen an der Endung, nicht am Platz. Das ist der strukturelle
Grund, warum §17.1 das Vorfeld freigeben kann.

Zweiter Beleg, §25.1: *Xnan melnan traivamen viñ, tund xla luiv luid est.* — Wir finden den
Weg, wenn die Sonne hell ist. Hier steht das Akkusativobjekt *Xnan melnan* im Vorfeld, das
Subjektpronomen *viñ* hinter dem Verb.

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| *Xra valru milkat xran narkun.* | **[Beleg §17.1]** — Subjekt im Vorfeld |
| *Nunda milkat xra valru xran narkun.* | **[Beleg §17.1]** — Zeit im Vorfeld, beide Nominalgruppen im Mittelfeld |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Xran narkun xra valru milkat.* | Verb an Position 3 — §17.1 [regelabgeleitet] |
| †*Xra narku milkat xra valru.* | kein Stellungs-, sondern ein Kasusfehler: das Vorfeldobjekt muss den Akkusativ tragen (§8) [regelabgeleitet] |

---

## 4. Zeit im Vorfeld

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Heute gehe ich zu meinem Haus. |
| **(b) Orbis** | *Nunda melam vim dun xnaş breuneş vis.* — **Beleg §25.1** |
| **(c) Englisch** | Today I go to my house. |
| **(d) Muster** | PART-V-PRON-P-NP |
| **(h) Regel-ID** | ORB-GRAM-SYN-010 (§17.1), Mittelfeld ORB-GRAM-SYN-014 (§17.4) |

**(e) Erklärung.** Zeitausdrücke stehen im Vorfeld besonders häufig; §17.4 nennt **Zeit** auch
als erstes Glied der Mittelfeldtendenz. Beides ist dieselbe Beobachtung aus zwei Blickwinkeln:
Die Zeitangabe steht früh. Erzwungen ist nichts — §17.4 sagt ausdrücklich „Tendenz, keine
harte Regel".

Weitere Belege: *Nunda milkat xra valru xran narkun.* (§17.1) · Test 132 *Zirna ruskaim vim.*
— Morgen werde ich schreiben. (PART-V-PRON)

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| Zeitangabe im Mittelfeld: *Şet dolmaş nunda vandex.* — Du musst heute kommen. | **[Beleg §16.1]**, ebenso Test 107 |
| Zeitangabe im Mittelfeld nach Modalverb: *Vim valnam nunda zva xraş velkraş dun xlaş kavlaş melex.* | **[Beleg §17.3]** |
| Zeitangabe im Mittelfeld eines Nebensatzes: *Vim zavam, fai xra vlaidra valru zirna xnaş şirneş xnan brasin dalvait.* | **[Beleg Test 146]** |
| Zeitangabe als Dativgruppe im Vorfeld: *Vraş zaldreş traivot ro vnan aulen şlim xrañaş larkiñiş.* | **[Beleg §25.2]** — aber **U-11**: eine bloße Dativ-Zeitangabe ohne Präposition sehen §8, §17 und §19 nicht vor |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Nunda vim melam dun xnaş breuneş vis.* | Verb an Position 3 — §17.1 [regelabgeleitet] |
| †*Zirna vim ruskaim.* | dito [regelabgeleitet] |

---

## 5. Adverb und Adverbiale im Vorfeld

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | In dem Traum sah er die Sonne der Welt. |
| **(b) Orbis** | *Tel xraş navildoş milkot ro xlan luiven xlas eirdes.* — **Beleg §25.2** |
| **(c) Englisch** | In the dream he saw the sun of the world. |
| **(d) Muster** | P-NP-V-PRON-NP-NP |
| **(h) Regel-ID** | ORB-GRAM-SYN-010 (§17.1) |

**(e) Erklärung.** Eine Präpositionalgruppe füllt das Vorfeld als **eine** Position, gleich
wie viele Wörter sie umfasst: *Tel xraş navildoş* zählt als 1, *milkot* steht auf 2, das
Subjekt *ro* folgt. *tel* + Dativ bezeichnet hier den Ort (§19).

**Zum Adverb im engeren Sinn.** §12.4 bildet Adverbien aus Adjektiven mit **-un**
(*vlaidun, zilvun, loşnun*). Für ein solches Adverb im Vorfeld gibt es **keinen Beleg** —
weder in 0.9.3 noch im Testkorpus 0.1. Belegt ist nur die Stellung nach dem Verb:
Test 059 *Lo melat zilvun.* — Sie geht schnell. (PRON-V-ADJ)

Belegt im Vorfeld sind ausschließlich die Partikeladverbien aus §24.9 (*nunda*, *zirna*;
siehe Abschnitt 4) und Präpositionalgruppen wie oben.

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| Präpositionalgruppe im Mittelfeld: *Vim maldam kru xlaş melvaş.* — Ich warte auf der Straße. | **[Beleg Test 031]** |
| dieselbe im Mittelfeld eines Nebensatzes: *…, grali xra morda span xlaş kavlaş vran xarn est.* | **[Beleg Test 150]** |
| Richtungsangabe im Mittelfeld: *Viñ xa melamen tel xlan kavlan.* | **[Beleg Test 089]** |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Tel xraş navildoş ro milkot xlan luiven xlas eirdes.* | Verb an Position 3 — §17.1 [regelabgeleitet] |
| †*Tel xraş navildon milkot ro …* | Kasusfehler: *tel* + Dativ bezeichnet den Ort, der Akkusativ die Richtung (§19) [regelabgeleitet] |

---

## 6. Ja/Nein-Frage

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Gehst du heute? |
| **(b) Orbis** | *Melaş nunda?* — **Beleg §18.1**; mit gesetztem Subjekt *Melaş şet nunda?* — **Beleg Test 071** |
| **(c) Englisch** | Are you going today? |
| **(d) Muster** | V-PART (§18.1) · V-PRON-PART (Test 071) |
| **(h) Regel-ID** | ORB-GRAM-SYN-016 (§18.1) |

**(e) Erklärung.** §18.1 verlangt das finite Verb auf **Position 1**. Das Vorfeld bleibt leer;
alles Übrige folgt. Die Antwortpartikeln sind **ain** (ja) und **xaus** (nein) (§18.1).

Weitere Belege: Test 072 *Vandat xra draun?* — Kommt der Vater? (V-NP) · Test 114 *Valnaten
şevar vin zaubex?* — Können Sie mich hören? (V-PRON-PRON-V; Höflichkeitsform §13.2 mit 3. Pl,
zugleich Verbklammer §16.1; wortgleich in §25.1).

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| ohne Subjektpronomen: *Melaş nunda?* | **[Beleg §18.1]** |
| mit Subjektpronomen: *Melaş şet nunda?* | **[Beleg Test 071]** |
| mit nominalem Subjekt: *Vandat xra draun?* | **[Beleg Test 072]** |

Dass beide ersten Formen gelten, ist Beispielpraxis, keine Regel — **U-04**: Wann das
Subjektpronomen wegfallen darf, sagt §18 nicht.

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Şet melaş nunda?* als Ja/Nein-Frage | Verb an Position 2 — §18.1 verlangt Position 1. §18 sagt nichts über eine Intonationsfrage mit V2; belegt ist sie nicht [regelabgeleitet] |
| †*Nunda melaş?* als Ja/Nein-Frage | dito: das Vorfeld ist besetzt, das Verb steht auf 2 [regelabgeleitet] |

---

## 7. W-Frage

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Wer spricht? |
| **(b) Orbis** | *Kem talat?* — **Beleg Test 073** |
| **(c) Englisch** | Who speaks? |
| **(d) Muster** | W-V |
| **(h) Regel-ID** | ORB-GRAM-SYN-017 (§18.2) |

**(e) Erklärung.** Das Fragewort besetzt Position 1, das finite Verb Position 2. Ist das
Fragewort selbst das Subjekt (*Kem talat?*), fällt das Muster mit dem Aussagesatz zusammen;
nur das Fragezeichen unterscheidet.

Belege der Grammatik (§18.2, ohne Übersetzung im Text): *Kan melaş?* · *Grais xa vandat?* ·
*Kellan sarlan milkoş?*

Belege mit Übersetzung aus dem Testkorpus:

| Test | Orbis | Deutsch | Muster |
|---|---|---|---|
| 077 | *Kur maldaşen şeñ?* | Wo wartet ihr? | W-V-PRON |
| 078 | *Kolm est xla kirva?* | Wie ist die Nacht? | W-V-NP |
| 079 | *Kelnan vreston leşnaş şet?* | Welches Buch liest du? | ADJ-N-V-PRON |
| 080 | *Kelnaş şirneş dalvaş şet xnan brasin?* | Welchem Kind gibst du das Brot? | ADJ-N-V-PRON-NP |

*kelra / kella / kelna* kongruieren adjektivisch mit ihrem Nomen und bilden mit ihm **eine**
Vorfeldposition (*Kelnan vreston*, *Kellan sarlan*).

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| Subjekt hinter das Verb: *Kur maldaşen şeñ?* | **[Beleg Test 077]** |
| Subjekt weggelassen: *Kan melaş?*, *Grais xa vandat?* | **[Beleg §18.2]** — **U-04** |
| weitere Ergänzung am Satzende: *Kelnaş şirneş dalvaş şet xnan brasin?* | **[Beleg Test 080]** |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Talat kem?* | Fragewort nicht auf Position 1 — §18.2 [regelabgeleitet] |
| †*Kem şet milkaş?* | Verb an Position 3 — §18.2/§17.1 [regelabgeleitet] |

> **[REGELLÜCKE L-03]** *kem* und *kelt* sind nur in der Grundform gelistet. „Wen siehst du?"
> (Test 074), „Wem gibst du das Buch?" (Test 075) und „Wessen Buch liest du?" (Test 076) sind
> **nicht bildbar**: Weder Kasusformen noch Indeklinabilität sind definiert. Test 076 hängt
> zusätzlich an L-01. Diese Dokumentation entscheidet nicht.

---

## 8. Negation

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Ich gehe nicht. |
| **(b) Orbis** | *Vim xa melam.* — **Beleg §18.3**, ebenso Test 081 |
| **(c) Englisch** | I do not go. |
| **(d) Muster** | PRON-PART-V |
| **(h) Regel-ID** | ORB-GRAM-SYN-018 (§18.3) |

**(e) Erklärung.** §18.3 kennt **eine einzige** Negationspartikel: **xa**, unmittelbar vor dem
finiten Verb. Die Partikel wandert mit dem Verb, nicht mit dem negierten Begriff. Attributiv
tritt an ihre Stelle das deklinierte Adjektiv **xan-** (*xanra valru* — kein Mann, §18.3;
Test 086 *Xanra valru maldat.*), pronominal die Indefinita **xakaun** / **xakelte** (§13.4;
Test 088 *Xakaun vandat.* — Niemand kommt).

Die Adjazenz hält in jeder Umgebung:

| Umgebung | Beleg |
|---|---|
| Subjekt im Vorfeld | Test 085 *Xna şirn xa soñat.* |
| Objekt hinter dem Verb | Test 084 *Lo xa milkat xran narkun.* |
| Kopf + Genitivattribut im Vorfeld | Test 045 *Xla taiv xlas eirdes xa vaşnat.* |
| Verbklammer | Test 115 *Xna şirn xa vlekat melex.* — *xa* vor dem **finiten** Verb |
| Nebensatz | Test 090 *Vim zavam, fai ro xa vandat.* |
| W-Frage | §18.2 *Grais xa vandat?* |
| Richtungsangabe | Test 089 *Viñ xa melamen tel xlan kavlan.* |

**(f) Gültige Umstellungen.** Alle Zeilen der obigen Tabelle sind Umstellungen desselben
Musters: Das Vorfeld ist frei besetzbar, *xa* bleibt am finiten Verb.

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Vim melam xa.* | *xa* nicht unmittelbar vor dem finiten Verb — §18.3 [regelabgeleitet] |
| †*Xa vim melam.* | dito: *xa* ist vom Verb getrennt [regelabgeleitet] |
| †*Xna şirn vlekat xa melex.* | *xa* vor dem Infinitiv statt vor dem finiten Verb — §18.3 [regelabgeleitet] |

> **[REGELUNKLARHEIT U-14]** Der zweite Beleg von §18.3, *Vim xa num vna breun* („Ich habe
> kein Haus"), lässt Artikel und Kernwort im Objekt unmarkiert. Regelkonform nach §8, §10.3
> und §11 wäre *vnan breunen* — so schreibt es Test 083: *Viñ xa numen vnan breunen.*
> Die Stellung ist davon nicht betroffen.

---

## 9. Modalverb

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Ich kann den Weg sehen. |
| **(b) Orbis** | *Vim valnam xnan melnan milkex.* — **Beleg §16.1** |
| **(c) Englisch** | I can see the way. |
| **(d) Muster** | PRON-V-NP-V |
| **(h) Regel-ID** | ORB-GRAM-SYN-013 (§16.1, §17.3) |

**(e) Erklärung.** Die **Verbklammer**: Das konjugierte Modalverb steht auf Position 2, das
Vollverb im **Infinitiv am Satzende** (§16.1). Alles dazwischen ist Mittelfeld. Die sechs
Modalwurzeln sind *valn-* (können), *dolm-* (müssen), *vlek-* (dürfen), *tirn-* (sollen),
*nest-* (wollen), *suvr-* (mögen).

Belege mit wachsendem Mittelfeld:

| Mittelfeld | Beleg |
|---|---|
| leer | Test 106 *Vim valnam melex.* — Ich kann gehen. |
| Zeit | §16.1 *Şet dolmaş nunda vandex.* — Du musst heute kommen. (= Test 107) |
| Objekt | Test 108 *Ro vlekat xnan vreston leşnex.* — Er darf das Buch lesen. |
| Objekt | Test 112 *Şeñ valnaşen xran vrondon milkex.* · Test 113 *Oñ dolmaten xlan kavlan traivex.* |
| Zeit + Art + Ort | §17.3 *Vim valnam nunda zva xraş velkraş dun xlaş kavlaş melex.* |

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| Mittelfeldfolge Zeit – Art – Ort | **[Beleg §17.3]**, entspricht der Tendenz §17.4 — Abweichungen sind keine Verstöße, weil §17.4 sich selbst als Tendenz bezeichnet |
| Vorfeld anders besetzt | **[regelabgeleitet §17.1]**; ein Beleg mit topikalisiertem Objekt vor einem Modalverb existiert nicht |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Vim valnam milkex xnan melnan.* | Infinitiv nicht am Satzende — §16.1 [regelabgeleitet] |
| †*Vim xnan melnan valnam milkex.* | finites Verb an Position 3 — §17.1 [regelabgeleitet] |
| †*Vim milkex xnan melnan valnam.* | finites Verb am Ende: das ist die Nebensatzstellung §17.2, nicht der Hauptsatz [regelabgeleitet] |

> **[REGELUNKLARHEIT U-03]** Ob ein Modalverb ohne Infinitiv, also als Vollverb mit direktem
> Objekt stehen darf („Ich mag das Wort"), regelt §16.1 nicht. Test 111 prüft den Fall und
> bleibt offen.

---

## 10. Modalverb + Negation

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Das Kind darf nicht gehen. |
| **(b) Orbis** | *Xna şirn xa vlekat melex.* — **Beleg Test 115** |
| **(c) Englisch** | The child may not go. |
| **(d) Muster** | NP-PART-V-V |
| **(h) Regel-ID** | ORB-GRAM-SYN-013 (§16.1) + ORB-GRAM-SYN-018 (§18.3) |

**(e) Erklärung.** Beide Regeln greifen unabhängig und widerspruchsfrei: *xa* tritt vor das
**finite** Verb (§18.3), der Infinitiv bleibt am Satzende (§16.1). Die Klammer wird also von
außen negiert, nicht von innen.

Weitere Belege: §25.1 *Vim xa valnam soñex, grali xla kirva vran luid est.* — Ich kann nicht
schlafen, weil die Nacht sehr hell ist. · Test 150 *Viñ xa valnamen soñex, grali xra morda
span xlaş kavlaş vran xarn est.*

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| Subjektpronomen im Vorfeld: *Vim xa valnam soñex, …* | **[Beleg §25.1]** |
| Subjekt-NP im Vorfeld: *Xna şirn xa vlekat melex.* | **[Beleg Test 115]** |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Xna şirn vlekat xa melex.* | *xa* nicht am finiten Verb — §18.3 [regelabgeleitet] |
| †*Xna şirn xa melex vlekat.* | Infinitiv nicht am Satzende — §16.1 [regelabgeleitet] |

> **[REGELKONFLIKT K-05]** Sobald dieselbe Fügung in den **Nebensatz** tritt, ist sie nicht
> mehr entscheidbar: §16.1 will den Infinitiv am Satzende, §17.2 das finite Verb. Test 105
> („Er weiß, dass sie das Buch nicht lesen kann") führt die Kandidaten vor — *… xa leşnex
> valnat*? *… leşnex xa valnat*? *… xa valnat leşnex*? — und entscheidet nicht. Kein Beispiel
> der Grammatik enthält ein Modalverb im Nebensatz. Diese Dokumentation entscheidet nicht.

---

## 11. Nebensatz

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Ich weiß, dass du kommst. |
| **(b) Orbis** | *Vim zavam, fai şet vandaş.* — **Beleg Test 091** |
| **(c) Englisch** | I know that you are coming. |
| **(d) Muster** | PRON-V-SUBJ-KONJ-PRON-V |
| **(h) Regel-ID** | ORB-GRAM-SYN-011 (§17.2) |

**(e) Erklärung.** Der Hauptsatz behält V2, der Nebensatz stellt sein finites Verb ans
**Ende** (§17.2). Die unterordnende Konjunktion (§20) leitet ein und zählt nicht als
Satzglied des Nebensatzes.

Belege der Grammatik: §17.2 *Vim zavam, fai şet nunda dun xnaş breuneş melaş.* (ohne
Übersetzung im Text) · §25.1 *Vim zavam, fai şet zirna vandaiş.* — Ich weiß, dass du morgen
kommen wirst. · §25.1 *Vim xa valnam soñex, grali xla kirva vran luid est.*

Belege für alle sieben Konjunktionen von §20 stehen in `SYNTAX.md` §11.2.

Wächst das Mittelfeld, bleibt die Endstellung: Test 146 *Vim zavam, fai xra vlaidra valru
zirna xnaş şirneş xnan brasin dalvait.* — Subjekt, Zeit, Dativobjekt, Akkusativobjekt, dann
das finite Verb.

Auch das Fragewort **kur** leitet im Beleg einen Nebensatz mit Verbendstellung ein: §25.2
*Ro xa zovet, kur xna melna molet* · Test 098 *Vim xa zavam, kur xna vresto est.* §20 führt
*kur* nicht in der Liste der unterordnenden Konjunktionen; belegt ist die Konstruktion nur
durch diese beiden Sätze.

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| Nebensatz vorangestellt | siehe Abschnitt 12 — **[Beleg Test 093]** |
| Negation im Nebensatz: *Vim zavam, fai ro xa vandat.* | **[Beleg Test 090]** |
| Mittelfeld beliebig lang | **[Beleg Test 146]** |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Vim zavam, fai vandaş şet.* | finites Verb nicht am Nebensatzende — §17.2 [regelabgeleitet] |
| †*Vim zavam, fai şet vandaş nunda.* | dito: nach dem finiten Verb steht nichts mehr [regelabgeleitet] |
| †*Vim, fai şet vandaş, zavam.* | Hauptsatzverb an Position 3 — §17.1. Ob ein Nebensatz überhaupt in den Hauptsatz eingebettet werden darf, sagt §17 nicht; belegt ist es nicht [regelabgeleitet] |

---

## 12. Nebensatz vor dem Hauptsatz

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Wenn du gehst, bleibe ich. |
| **(b) Orbis** | *Tund şet melaş, stanam vim.* — **Beleg Test 093** |
| **(c) Englisch** | If you go, I stay. |
| **(d) Muster** | SUBJ-KONJ-PRON-V-V-PRON |
| **(h) Regel-ID** | ORB-GRAM-SYN-012 (§17.1) |

**(e) Erklärung.** §17.1 sagt es wörtlich: „Steht ein Nebensatz vor dem Hauptsatz, besetzt er
**Position 1** — das finite Verb folgt direkt." Der ganze Nebensatz ist also **ein** Vorfeld.
Daraus folgt zwingend: Das Subjekt des Hauptsatzes steht **hinter** dem Verb.

Belege:

| Test | Orbis | Deutsch |
|---|---|---|
| 093 | *Tund şet melaş, stanam vim.* | Wenn du gehst, bleibe ich. |
| 094 | *Şlani xna vresto granz est, leşnam vim non.* | Obwohl das Buch alt ist, lese ich es. |
| 095 | *Dremi viñ maldamen, talat xra valru.* | Während wir warten, spricht der Mann. |
| 096 | *Glemi xla luiv vandat, melamen viñ.* | Bevor die Sonne kommt, gehen wir. |
| 097 | *Trausi ro nastot, soñot ro.* | Nachdem er aß, schlief er. |
| 147 | *Şlani xla kirva girn vot, moleten xrañ melruñ span xran vrondon.* | Obwohl die Nacht kalt war, gingen die Wanderer über den Berg. |
| 148 | *Tund şet xnan vreston xras velkras leşnaş, traivaiş şet xlan klaunuman.* | Wenn du das Buch des Freundes liest, wirst du die Wahrheit finden. |

Grammatikbeleg mit *mai*: §25.1 *Tund vim vra vlaidra valru mai em, mai traivam vim xlan
eirden.* — hier füllt *mai traivam* die Position 2 (§16.2).

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| Nebensatz nachgestellt, Objekt im Vorfeld des Hauptsatzes: *Xnan melnan traivamen viñ, tund xla luiv luid est.* | **[Beleg §25.1]** |
| Nebensatz nachgestellt, Subjekt im Vorfeld: *Vim zavam, fai şet zirna vandaiş.* | **[Beleg §25.1]** |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Tund şet melaş, vim stanam.* | Hauptsatzverb an Position 3: der Nebensatz zählt bereits als Position 1 — §17.1 [regelabgeleitet] |
| †*Tund melaş şet, stanam vim.* | Nebensatzverb nicht am Ende — §17.2 [regelabgeleitet] |

---

## 13. Relativsatz

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Der Mann, der kommt, ist mein Freund. |
| **(b) Orbis** | **kein Beleg.** Test 100 ist als **[REGELLÜCKE]** gewertet und trägt `orbis = null` |
| **(c) Englisch** | The man who is coming is my friend. |
| **(d) Muster** | nicht bestimmbar |
| **(h) Regel-ID** | ORB-GRAM-SYN-022, Status `open`, Befund **L-02** |

**(e) Erklärung — die Lage, keine Regel.** §13.4 führt **fai** in der Tabelle „Übrige
Pronomen" unter „Relativ". Damit endet, was 0.9.3 zum Relativsatz sagt. Es fehlt:

| Was fehlt | Betrifft |
|---|---|
| Kasusformen von *fai* | Relativpronomen als Objekt (*fain*?), als Dativ (*faiş*?), als Genitiv (*fais*?) |
| Kongruenz | Geschlecht und Numerus des Bezugsworts |
| Verbstellung | ob der Relativsatz die Endstellung nach §17.2 nimmt |
| Position | ob der Relativsatz unmittelbar hinter dem Bezugswort steht oder ausgeklammert wird |
| Homonymie | *fai* „dass" (§20) gegen *fai* „der/die/das" (§13.4) — zusätzlich W-03 |

Die betroffenen Tests: 100 (Relativpronomen als Subjekt), 101 (als Akkusativobjekt), 102 (als
Dativobjekt), 149 (eingebettet, zusätzlich mit L-01 verschränkt). Alle vier tragen
`orbis = null`.

**(f)/(g) Umstellungen.** Nicht angebbar. Ohne definierten Satzbau gibt es weder gültige noch
ungültige Umstellungen; jede Form wäre Spekulation. Test 100 hält das ausdrücklich fest:
„*Xra valru, fai vandat, xra velkra vis est* wäre reine Spekulation."

> **[REGELLÜCKE L-02]** Der Relativsatzbau fehlt vollständig. **Diese Dokumentation
> entscheidet nicht.** Die Festlegung treffen die Sprachdesigner.

---

## 14. Passiv

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Das Haus wird gebaut. |
| **(b) Orbis** | *Xna breun şunargat.* — **Beleg §16.3**, ebenso Test 136 |
| **(c) Englisch** | The house is being built. |
| **(d) Muster** | NP-V |
| **(h) Regel-ID** | ORB-GRAM-SYN-019, Status `provisional`, Befund **L-05** |

**(e) Erklärung.** Das Vorgangspassiv ist **morphologisch**, nicht syntaktisch: Die Vorsilbe
**şu-** tritt an die Verbwurzel (§16.3). Die Satzstellung ändert sich dadurch nicht — das
Patiens steht als Subjekt im Nominativ, das Verb bleibt auf Position 2.

Das **Zustandspassiv** bildet Partizip + *esex*: §16.3 *Xna breun şunargut est.* — Das Haus
ist gebaut. Damit fällt es unter die prädikative Konstruktion (Abschnitt 17) und teilt deren
offene Frage **U-13**.

| Form | Beleg |
|---|---|
| Vorgangspassiv Präsens | §16.3 / Test 136 *Xna breun şunargat.* |
| Vorgangspassiv Plural | Test 140 *Xnañ vrestoñ şuleşnaten.* — Die Bücher werden gelesen. |
| Zustandspassiv | §16.3 *Xna breun şunargut est.* · Test 139 *Xna taisa şutalut est.* — Das Wort ist gesprochen. |

**(f) Gültige Umstellungen.** Belegt ist nur die Subjekt-Vorfeld-Stellung. Eine
Topikalisierung im Passivsatz ist nach §17.1 nicht ausgeschlossen, aber **nicht belegt**.

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Şunargat xna breun.* (als Aussage) | Verb an Position 1 — §17.1 [regelabgeleitet] |
| †*Xna breun est şunargut.* | Beim Zustandspassiv steht das Partizip in allen Belegen vor der Kopula; siehe U-13, Abschnitt 17 — die Umkehrung ist **nicht entscheidbar**, nicht belegt und darum hier nur als unbelegt vermerkt |

> **[REGELLÜCKE L-05] Agens im Passiv.** „Das Haus wird **vom Mann** gebaut" (Test 137) und
> „Das Buch wurde **von der Frau** gelesen" (Test 138) sind **nicht bildbar**. §16.3 regelt
> nur die Vorsilbe; keine Präposition ist für den Agens ausgewiesen. *ven* + Dativ läge nahe
> — §19 gibt *ven* „von" mit Dativ an —, ist aber nirgends festgelegt. **Diese Dokumentation
> entscheidet nicht.**

---

## 15. Dativ + Akkusativ

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Die Mutter gibt dem Kind das Brot. |
| **(b) Orbis** | *Xla veiş dalvat xnaş şirneş xnan brasin.* — **Beleg Test 023**; in der Vergangenheit wortgleich §25.1 *Xla veiş dolvet xnaş şirneş xnan brasin.* — Die Mutter gab dem Kind das Brot. |
| **(c) Englisch** | The mother gives the child the bread. |
| **(d) Muster** | NP-V-NP-NP |
| **(h) Regel-ID** | ORB-GRAM-SYN-023, Status `provisional`, Befund **U-05** |

**(e) Erklärung.** Beide Objekte stehen im Mittelfeld, der Dativ vor dem Akkusativ. Die
Rollen sind durch den Kasus markiert (*xnaş şirneş* Dativ, *xnan brasin* Akkusativ), nicht
durch die Stellung.

Belege in gleicher Folge:

| Test | Orbis | Deutsch |
|---|---|---|
| 025 | *Xla sarla dalvat xraş drauneş xnan aulen.* | Die Frau gibt dem Vater das Wasser. |
| 026 | *Vim dalvam xraş velkraş xnan vreston.* | Ich gebe dem Freund das Buch. |
| 034 | *Vim dalvam viş xlan nauşen.* | Ich gebe mir Zeit. (reflexiver Dativ, 1. Person) |
| 064 | *Viñ dalvamen xnañaş şirneiş xnan brasin.* | Wir geben den Kindern das Brot. |
| 120 | *Oñ dolveten xnaş şirneş xnan brasin.* | Sie gaben dem Kind das Brot. |
| 080 | *Kelnaş şirneş dalvaş şet xnan brasin?* | Welchem Kind gibst du das Brot? (Dativ im Vorfeld) |
| 146 | *Vim zavam, fai xra vlaidra valru zirna xnaş şirneş xnan brasin dalvait.* | im Nebensatz, Dativ vor Akkusativ |

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| Dativobjekt ins Vorfeld: *Kelnaş şirneş dalvaş şet xnan brasin?* | **[Beleg Test 080]** — dort als Fragewortgruppe |
| Akkusativ vor Dativ | **nicht belegt.** §17 stellt keine Regel auf; U-05 hält fest, dass Dat-vor-Akk **nur Beispielpraxis** ist. Verboten ist die Umkehrung damit nicht — belegt ist sie aber auch nicht. Diese Dokumentation entscheidet nicht |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Xla veiş xnaş şirneş dalvat xnan brasin.* | finites Verb an Position 3 — §17.1 [regelabgeleitet] |
| †*Xla veiş dalvat xnaş şirneş xna brasin.* | Kasusfehler, kein Stellungsfehler: das zweite Objekt muss den Akkusativ tragen (§8) [regelabgeleitet] |

> **[REGELUNKLARHEIT U-05]** Die Objektreihenfolge ist durchgehende Praxis der Beispiele,
> aber keine Regel.

---

## 16. Genitivattribute

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Die Erinnerung der Zeit vergeht. |
| **(b) Orbis** | *Xla soruma xlas nauşes vaşnat.* — **Beleg Test 037**; mit Gradpartikel und Adverbial §25.1 *Xla soruma xlas nauşes vran tolm vaşnat.* — Die Erinnerung der Zeit vergeht sehr langsam. |
| **(c) Englisch** | The memory of time passes away. |
| **(d) Muster** | NP-NP-V |
| **(h) Regel-ID** | ORB-GRAM-SYN-021, Status `open`, Befund **L-01** |

**(e) Erklärung.** In **allen** Belegen steht das Genitivattribut **hinter** seinem Kopf, und
Kopf + Attribut bilden zusammen **eine** Satzposition — sichtbar daran, dass das finite Verb
unmittelbar folgt (*Xla soruma xlas nauşes* = Position 1, *vaşnat* = Position 2).

Belege:

| Fundstelle | Orbis | Deutsch |
|---|---|---|
| §25.1 | *Xla soruma xlas nauşes vran tolm vaşnat.* | Die Erinnerung der Zeit vergeht sehr langsam. |
| §25.2 | *Tel xraş navildoş milkot ro xlan luiven xlas eirdes.* | In dem Traum sah er die Sonne der Welt. |
| Test 038 | *Xra şaul xlas sarlas loşn est.* | Der Name der Frau ist schön. |
| Test 040 | *Xla gluvi xras xerpes velm est.* | Die Flamme des Feuers ist warm. |
| Test 041 | *Xna melna xnas virnes trelm est.* | Der Weg des Lebens ist lang. |
| Test 042 | *Xra zaldre xras mokses vandat.* | Der Tag des Todes kommt. |
| Test 043 | *Xna aul xlas greines girn est.* | Das Wasser der Erde ist kalt. |
| Test 044 | *Xla şonma xras kaunes xarn est.* | Die Stimme des Menschen ist stark. |
| Test 045 | *Xla taiv xlas eirdes xa vaşnat.* | Die Sprache der Welt vergeht nicht. |
| Test 148 | *Tund şet xnan vreston xras velkras leşnaş, …* | im Nebensatz, Kopf + Genitiv im Mittelfeld |

Verwandt, aber nicht dasselbe: Das **Possessiv** ist nach §13.3 ausdrücklich **nachgestellt**
(*xna breun vis* — mein Haus · *xla sarla şes* · *xrañ valruñ oñas*). §13.3 regelt nur das
Possessivpronomen, nicht das nominale Genitivattribut.

**(f) Gültige Umstellungen.** Die Kopf-Attribut-Gruppe kann als Ganzes in jedes Feld treten:
Vorfeld (Test 037, 045), Mittelfeld (Test 148), Objektposition (§25.2). Das folgt aus §17.1.

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Xla soruma vaşnat xlas nauşes.* | Kopf und Attribut auseinandergerissen; keine Regel erlaubt die Ausklammerung, kein Beleg zeigt sie [regelabgeleitet] |
| Voranstellung *Xlas nauşes xla soruma vaşnat* | **nicht entscheidbar** — siehe L-01 |

> **[REGELLÜCKE L-01] Stellung des Genitivattributs.** §8 definiert den Genitiv nur
> morphologisch, §17 schweigt zur Attributstellung. Test 036 („Das Haus des Mannes ist alt")
> führt beide Kandidaten vor — *Xna breun xras valrus granz est* (nachgestellt) und *Xras
> valrus xna breun granz est* (vorangestellt) — und stellt fest: **beide sind morphologisch
> korrekt**, die Stellung ist nirgends festgelegt. Test 039 („Das Buch meines Freundes ist
> neu") zeigt zusätzlich die ungeregelte **Stapelung** von Genitivattribut und nachgestelltem
> Possessiv. Test 149 hängt neben L-02 ebenfalls an L-01. **Diese Dokumentation entscheidet
> nicht**; sie hält nur fest, dass die einheitliche Beispielpraxis nachstellt.

Am Rand betroffen: **K-04** — §25.1 verwendet in diesem Satz *tolm* adverbial ohne das nach
§12.4 verlangte *-un* (*tolmun*). Test 060 wertet das als [REGELKONFLIKT]. Die Stellung ist
davon nicht betroffen.

---

## 17. Prädikative Konstruktionen

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Sie ist schön. |
| **(b) Orbis** | *Lo loşn est.* — **Beleg §12.2** |
| **(c) Englisch** | She is beautiful. |
| **(d) Muster** | PRON-ADJ-V |
| **(h) Regel-ID** | ORB-GRAM-SYN-015 (§17.5), Befund **U-13** |

**(e) Erklärung.** Nach **esex** (sein), **vurnex** (werden) und **stanex** (bleiben) steht das
Adjektiv in der **Grundform**, ohne jede Endung (§12.2). Die Kopula darf **nicht** ausgelassen
werden (§17.5) — auch nicht dort, wo das Deutsche oder Englische sie tilgen könnte.

Belege §12.2: *Lo loşn est.* (*nicht:* †*Lo loşna est*) · *Xla kirva girn vot.* · *Xra valru
xarn vurt.* · *Xna breun granz stanat.* · Plural *Xrañ larkiñ girn esten.*
Beleg §17.5: *Xla luiv luid vot, xla kirva girn vot.* — Die Sonne war hell, die Nacht war
kalt.

**Die Stellungsfrage (U-13).** In **allen** Belegen der Grammatik steht das Prädikativ **vor**
dem Verb; das finite Verb steht damit an dritter **Wortstelle**: *Lo*(1) *loşn*(2) *est*(3).
Ob Prädikativ und Kopula zusammen eine Satzposition bilden — so wie es §16.2 für *mai* + Verb
ausdrücklich sagt —, ist nirgends gesagt. Das Testkorpus belegt **beide** Folgen, beide mit
[OK]:

| Folge | Beleg |
|---|---|
| Prädikativ **vor** dem Verb | Test 046 *Xra vlaidra vrondo granz est.* · Test 053 *Xla girnla kirva trelm est.* · Test 057 *Xra valru xarn vurt.* · Test 121 *Xla kirva girn vot.* · Test 065 *Xrañ larkiñ girn esten.* |
| Prädikativ **nach** dem Verb | Test 125 *Viñ voremen xarn.* — Wir wurden stark. · Test 131 *Xna şirn vurnait xarn.* · Test 133 *Şeñ vaişen xarn.* |

Auch ein **nominales** Prädikat ist belegt und steht vor der Kopula: Test 055 *Lo xla
loşnvaxla sarla est.* — Sie ist die schönste Frau. Ebenso die Vergleichsformen §12.3: *Ro
vlaidvi est kon vim.* — Er ist größer als ich. · *Lo loşn est zil luiv.* — Sie ist schön wie
die Sonne. (Testkorpus: Test 054, Test 056 *Lo velm est zil luiv.*)

**(f) Gültige Umstellungen.** Beide oben belegten Folgen. Welche Bedingungen die Wahl steuern,
sagt die Grammatik nicht.

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Lo loşna est.* | Prädikativ dekliniert statt Grundform — **§12.2, † der Grammatik selbst** |
| †*Lo loşn.* | Kopula ausgelassen — §17.5. Die Auslassung als dichterisches Stilmittel trägt in §17.5 die Marke **[NOCH ZU ENTSCHEIDEN]** [regelabgeleitet] |

> **[REGELUNKLARHEIT U-13]** Prädikativstellung gegen V2. Der Befund wurde im Korpuslauf an
> Test 055 gefunden. **Diese Dokumentation entscheidet nicht**, ob *Lo loşn est* eine
> Ausnahme von §17.1 ist oder ob Prädikativ + Kopula als eine Position zählen.

---

## 18. Konditional (*mai*)

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Wenn ich ein Haus hätte, würde ich bleiben. |
| **(b) Orbis** | *Tund vim vnan breunen mai num, mai stanam vim.* — **Beleg Test 142** |
| **(c) Englisch** | If I had a house, I would stay. |
| **(d) Muster** | SUBJ-KONJ-PRON-NP-PART-V-PART-V-PRON |
| **(h) Regel-ID** | ORB-GRAM-SYN-020 (§16.2), Rahmen ORB-GRAM-SYN-012 (§17.1) |

**(e) Erklärung.** §16.2 legt zweierlei fest: **mai** steht **unmittelbar vor dem finiten
Verb**, und *mai* + finites Verb bilden **eine** Satzposition. Beides zusammen erklärt das
Konditionalgefüge vollständig:

| Teil | Stellung | Grund |
|---|---|---|
| *Tund vim vnan breunen mai num* | *mai num* am Nebensatzende | §17.2 (Verbendstellung) + §16.2 (Adjazenz) |
| *mai stanam vim* | *mai stanam* auf Position 2 | §17.1 (der Nebensatz ist Position 1) + §16.2 (*mai* + Verb = eine Position) |

Grammatikbeleg, §16.2 und §25.1: *Vim mai melam.* — Ich würde gehen. · *Tund vim vra vlaidra
valru mai em, mai traivam vim xlan eirden.* — Wenn ich ein großer Mann wäre, würde ich die
Welt finden.

Weitere Belege:

| Test | Orbis | Deutsch |
|---|---|---|
| 141 | *Vim mai melam.* | Ich würde gehen. |
| 143 | *Tund xla kirva girn mai est, mai maldamen viñ.* | Wenn die Nacht kalt wäre, würden wir warten. |
| 144 | *Ro mai leşnat xnan vreston.* | Er würde das Buch lesen. |
| 145 | *Vim mai valnam melex.* | Ich könnte gehen. (*mai* vor dem **finiten** Modalverb) |

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| einfacher Hauptsatz ohne Nebensatz: *Vim mai melam.* | **[Beleg §16.2]** |
| mit Objekt im Mittelfeld: *Ro mai leşnat xnan vreston.* | **[Beleg Test 144]** |
| mit Verbklammer: *Vim mai valnam melex.* | **[Beleg Test 145]** |
| *mai* nur im Hauptsatz, nicht im Nebensatz | **nicht belegt**: alle drei Konditionalbelege (§25.1, Test 142, Test 143) setzen *mai* in beiden Teilen |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Vim melam mai.* | *mai* nicht unmittelbar vor dem finiten Verb — §16.2 [regelabgeleitet] |
| †*Mai vim melam.* | *mai* vom Verb getrennt — §16.2 [regelabgeleitet] |
| †*Vim valnam mai melex.* | *mai* vor dem Infinitiv statt vor dem finiten Verb — §16.2 [regelabgeleitet] |
| †*Tund vim vnan breunen mai num, vim mai stanam.* | Hauptsatz: *mai stanam* an Position 3, weil der Nebensatz bereits Position 1 füllt — §17.1 + §16.2 [regelabgeleitet] |

---

## 19. Mehrfach-Nebensätze

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Er wusste nicht, wohin der Weg führte, aber er ging. |
| **(b) Orbis** | *Ro xa zovet, kur xna melna molet, klas ro molet.* — **Beleg §25.2**. Ein Satz mit **zwei Nebensätzen** ist weder in 0.9.3 noch im Testkorpus 0.1 belegt |
| **(c) Englisch** | He did not know where the way led, but he went. |
| **(d) Muster** | PRON-PART-V — SUBJ-W-NP-V — KONJ-PRON-V |
| **(h) Regel-ID** | ORB-GRAM-SYN-011 (§17.2) + ORB-GRAM-SYN-012 (§17.1) |

**(e) Erklärung.** Die längste belegte Satzkette der Grammatik besteht aus **Hauptsatz +
indirektem Fragesatz + nebengeordnetem Hauptsatz**. Jeder Teil behält seine eigene
Verbstellung:

| Teil | Stellung | Regel |
|---|---|---|
| *Ro xa zovet* | Verb auf 2, *xa* davor | §17.1, §18.3 |
| *kur xna melna molet* | Verb am Ende | §17.2 |
| *klas ro molet* | Verb auf 2 des Konjunkts | §17.1, §20 |

**Was nicht belegt ist.** Kein Satz der Grammatik und kein Satz des Testkorpus 0.1 enthält
zwei Nebensätze — weder nebengeordnet („…, dass A, und dass B") noch verschachtelt („…, dass
A, weil B"). Test 149 wäre der Maximaltest gewesen, scheitert aber bereits am Relativsatz
(L-02). Damit sind **ungeregelt und unbelegt**:

- die Reihenfolge zweier gleichrangiger Nebensätze zueinander,
- die Einbettung eines Nebensatzes in einen anderen,
- ob mehrere vorangestellte Nebensätze gemeinsam Position 1 füllen dürfen.

Für keinen dieser Punkte ist im Audit eine Befund-ID vergeben; sie sind schlicht nicht
behandelt.

**(f) Gültige Umstellungen.** Belegt ist nur, dass ein einzelner Nebensatz vor- oder
nachgestellt werden darf (Abschnitte 11 und 12). Weiteres ist nicht ableitbar.

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Ro xa zovet, kur molet xna melna, klas ro molet.* | Nebensatzverb nicht am Ende — §17.2 [regelabgeleitet] |
| †*Ro xa zovet, kur xna melna molet, klas molet ro.* | Konjunktverb an Position 1 — §17.1 [regelabgeleitet] |

Sobald ein **Modalverb** in einem dieser Nebensätze steht, greift zusätzlich **K-05**.

---

## 20. Koordination

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Er aß, er trank, und er schlief. |
| **(b) Orbis** | *Ro nastot, ro prevot, ze ro soñot.* — **Beleg §25.2** |
| **(c) Englisch** | He ate, he drank, and he slept. |
| **(d) Muster** | [PRON-V] — [PRON-V] — KONJ-[PRON-V] |
| **(h) Regel-ID** | §20 / `ORB-GRAM-SYN-002`; die Verbstellung je Konjunkt nach ORB-GRAM-SYN-010. Der Block -010…-025 enthält **keine** eigene Regel-ID für die Koordination |

**(e) Erklärung.** §20 nennt vier nebenordnende Konjunktionen: **ze** (und) · **vu** (oder) ·
**klas** (aber) · **xer** (denn). Sie verbinden Hauptsätze, und jeder Teilsatz behält seine
V2-Stellung.

Entscheidend für die Stellung: Die nebenordnende Konjunktion zählt in allen Belegen **nicht**
als Position 1. Auf sie folgt das Subjekt, dann das Verb:

| Beleg | Zählung |
|---|---|
| §25.2 *ze ro soñot* | *ze* – *ro*(1) – *soñot*(2) |
| §25.2 *Ze ro dremnot: „Kilna est xna traivute."* | satzinitiales *ze*, danach V2 |
| §25.2 *klas ro molet* | *klas* – *ro*(1) – *molet*(2) |
| §25.1 *klas xla kavla zirv vurt* | *klas* – *xla kavla*(1) – *zirv* – *vurt* → siehe **U-13** |
| Test 099 *xer xla kirva girn est* | *xer* – *xla kirva*(1) – *girn* – *est* → siehe **U-13** |

§20 selbst sagt zur Positionszählung nichts; die Aussage stützt sich auf diese fünf Belege.

Ebenfalls belegt ist die **asyndetische** Reihung ohne Konjunktion: §25.2 *Ro nastot, ro
prevot, …* und *Xla luiv luid vot, xla kirva girn vot.* (§17.5). Eine Regel dazu steht nicht
in §20.

**vu** (oder) hat **keinen einzigen Beleg** — weder in 0.9.3 noch im Testkorpus 0.1.

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| *ze* satzintern: *…, ze ro soñot.* | **[Beleg §25.2]** |
| *ze* satzinitial: *Ze ro dremnot: …* | **[Beleg §25.2]** |
| asyndetisch, ohne Konjunktion | **[Beleg §25.2, §17.5]** |
| Vorfeld des zweiten Konjunkts anders besetzt | **[regelabgeleitet §17.1]**, kein Beleg |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Ro nastot, ze soñot ro.* | Konjunktverb an Position 1 — §17.1, gestützt auf die durchgehende Zählung der Belege [regelabgeleitet] |
| †*Ro nastot, ro soñot ze.* | nachgestellte Konjunktion; kein Beleg, keine Regel dafür [regelabgeleitet] |

---

## 21. Kontrast

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Das Haus bleibt alt, aber die Stadt wird neu. |
| **(b) Orbis** | *Xna breun granz stanat, klas xla kavla zirv vurt.* — **Beleg §25.1** |
| **(c) Englisch** | The house stays old, but the city becomes new. |
| **(d) Muster** | NP-ADJ-V — KONJ-NP-ADJ-V |
| **(h) Regel-ID** | §20 / `ORB-GRAM-SYN-002` + ORB-GRAM-SYN-010; konzessiv ORB-GRAM-SYN-011 / -012 |

**(e) Erklärung.** Orbis kennt zwei belegte Wege, Gegensatz auszudrücken:

| Weg | Mittel | Wirkung auf die Stellung | Beleg |
|---|---|---|---|
| **nebenordnend** | *klas* (aber) | beide Teilsätze bleiben Hauptsätze mit V2 | §25.1 *Xna breun granz stanat, klas xla kavla zirv vurt.* · §25.2 *…, klas ro molet.* |
| **unterordnend** | *şlani* (obwohl) | der konzessive Teil wird Nebensatz mit Verbendstellung und kann Position 1 besetzen | Test 094 *Şlani xna vresto granz est, leşnam vim non.* · Test 147 *Şlani xla kirva girn vot, moleten xrañ melruñ span xran vrondon.* |

Der Unterschied ist rein syntaktisch: Bei *klas* bleiben zwei gleichrangige Hauptsätze
stehen, bei *şlani* rückt der Nebensatz ins Vorfeld und zwingt das Hauptsatzsubjekt hinter
das Verb (*leşnam vim*, *moleten xrañ melruñ*).

Beide *klas*-Belege und der *xer*-Beleg (Test 099) enthalten ein **Prädikativ vor dem Verb**
und fallen damit unter **U-13**.

**(f) Gültige Umstellungen.**

| Form | Status |
|---|---|
| konzessiver Nebensatz vorangestellt | **[Beleg Test 094, Test 147]** |
| konzessiver Nebensatz nachgestellt | **[regelabgeleitet §17.1]** — für *şlani* nicht belegt; für *grali* und *tund* nachgestellt belegt (§25.1) |
| Kausalkontrast mit *xer*: *Vim maldam, xer xla kirva girn est.* | **[Beleg Test 099]** |

**(g) Ungültige Umstellungen.**

| Form | Bruch |
|---|---|
| †*Xna breun granz stanat, klas vurt xla kavla zirv.* | Konjunktverb an Position 1 — §17.1 [regelabgeleitet] |
| †*Xna breun granz stanat, xla kavla klas zirv vurt.* | *klas* satzintern statt am Kopf des Konjunkts; alle Belege stellen die nebenordnende Konjunktion voran, §20 legt die Position nicht ausdrücklich fest [regelabgeleitet] |
| †*Şlani xna vresto granz est, vim leşnam non.* | Hauptsatzverb an Position 3, weil der Nebensatz Position 1 füllt — §17.1 [regelabgeleitet] |

---

## 22. Informationsstruktur

| Feld | Inhalt |
|---|---|
| **(a) Deutsch** | Der Mann sieht den Hund. / Den Hund sieht der Mann. / Heute sieht der Mann den Hund. |
| **(b) Orbis** | *Xra valru milkat xran narkun.* · *Xran narkun milkat xra valru.* · *Nunda milkat xra valru xran narkun.* — **Beleg §17.1** |
| **(c) Englisch** | The man sees the dog. / The dog, the man sees. / Today the man sees the dog. |
| **(d) Muster** | X-V-… |
| **(h) Regel-ID** | ORB-GRAM-SYN-010 (§17.1) für das Vorfeld, ORB-GRAM-SYN-014 (§17.4) für das Mittelfeld. Eine Regel-ID zur Informationsstruktur gibt es im Block -010…-025 **nicht** |

**(e) Erklärung — nur so weit belegt.** Die Grammatik 0.9.3 trifft **keine Aussage darüber,
was die Vorfeldbesetzung bedeutet**. Belegt ist ausschließlich:

1. **Das Vorfeld ist frei.** §17.1 führt drei Stellungen derselben Aussage nebeneinander auf,
   ohne eine davon als Normalfall, betont oder markiert zu kennzeichnen.
2. **Das Mittelfeld hat eine Tendenz.** §17.4 nennt Zeit – Grund – Art – Ort und sagt
   ausdrücklich „Tendenz, keine harte Regel".
3. **Der Kasus trägt die Rollen.** Weil Subjekt und Objekt morphologisch markiert sind
   (§8), ist keine Stellung zur Disambiguierung nötig — die Freiheit des Vorfelds ist
   strukturell möglich.

Was **nicht** in 0.9.3 steht: Fokuspartikeln, Spaltsätze, Topikmarker, eine Regel für
Kontrastbetonung, eine Aussage über Bekanntes vor Neuem. Die Gradpartikeln *vran* (sehr) und
*skirm* (wenig) aus §24.9 sind Grad-, nicht Informationsmittel — belegt in §25.1 *vran tolm
vaşnat*, *vran luid est* und Test 150 *vran xarn est*.

**(f) Gültige Umstellungen.** Alle drei Zeilen unter (b), gleichrangig.

**(g) Ungültige Umstellungen.** Nur die allgemeinen Stellungsbrüche (Verb nicht auf Position 2,
zwei Satzglieder im Vorfeld). Ein informationsstruktureller Fehler ist in 0.9.3 nicht
definierbar, weil keine Regel existiert, gegen die er verstoßen könnte.

> **Kein Befund vergeben.** Der Audit führt zur Informationsstruktur keine ID. Das ist kein
> Widerspruch der Grammatik, sondern ein unbeschriebenes Gebiet. **Diese Dokumentation füllt
> es nicht.**

---

## Offene Punkte der Satzstellung

| ID | Typ | Abschnitt | Kurz |
|---|---|---|---|
| **L-01** | Lücke | 16 | Stellung des Genitivattributs, inkl. Stapelung mit Possessiv |
| **L-02** | Lücke | 13 | Relativsatzbau vollständig undefiniert |
| **L-05** | Lücke | 14 | Agens im Passiv |
| **K-05** | Konflikt | 10, 11, 19 | Modalverb im Nebensatz: Infinitiv gegen finites Verb am Satzende |
| **U-13** | Unklarheit | 17, 20, 21 | Prädikativ vor dem Verb gegen die V2-Regel |
| **U-05** | Unklarheit | 15 | Objektreihenfolge Dativ vor Akkusativ nur Praxis |
| **U-04** | Unklarheit | 6, 7 | Subjektauslassung in Fragen nur Praxis |
| **U-11** | Unklarheit | 4 | temporaler Dativ ohne Präposition (*Vraş zaldreş*) |
| **U-03** | Unklarheit | 9 | Modalverb ohne Infinitiv |
| **L-03** | Lücke | 7 | Deklination von *kem/kelt* |
| **U-14** | Unklarheit | 8 | *Vim xa num vna breun* lässt Artikel und Kernwort unmarkiert |
| **K-04** | Konflikt | 16 | *tolm* adverbial ohne *-un* in §25.1 |

Unbelegt, aber nicht als Befund geführt: Adverb auf *-un* im Vorfeld (Abschnitt 5),
zwei Nebensätze in einem Satz (Abschnitt 19), *vu* als Konjunktion (Abschnitt 20),
acht der sechzehn Präpositionen (`SYNTAX.md` §10).

Vollständige Beschreibung aller Befunde: `Orbis-Audit-0_1.md` §A; maschinenlesbar in
`language/findings/findings.json`.

---

*Dokumentation zur Grammatik 0.9.3. Bei Abweichung gilt `Orbis-Grammatik-0.9.3.md`.*
