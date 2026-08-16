# ORBIS — Syntax: Satzbau, Fragen, Negation, Präpositionen, Konjunktionen

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

Dieses Kapitel gibt den Überblick über **§17 bis §20**: die beiden Verbstellungen, die
Verbklammer, die Satzgliedfolge, die Fragetypen, die Negation, das Präpositionssystem und
die Konjunktionen. Die ausführliche Behandlung der einzelnen Stellungsmuster mit
Umstellproben steht in `SATZSTELLUNG.md`.

**Belegpflicht.** Jede Regel dieses Kapitels ist mit mindestens einem Satz belegt, der
wörtlich in `Orbis-Grammatik-0.9.3.md` oder in `Orbis-Testkorpus-0_1.md` steht. Wo kein
Beleg existiert, steht das ausdrücklich da. Ungrammatische Formen sind mit **†** markiert —
so wie die Grammatik selbst es in §12.2 tut (*†Lo loşna est*).

**Diese Datei entscheidet nichts.** Wo die Grammatik schweigt oder sich widerspricht, steht
die Befund-ID aus `Orbis-Audit-0_1.md` §A. Die Regel-IDs `ORB-GRAM-SYN-*` verweisen auf
`language/syntax/rules.json`.

---

## 1. Der Rahmen: zwei Verbstellungen (§17)

Orbis kennt genau zwei Stellungen des finiten Verbs. Welche gilt, hängt allein am Satztyp:

| Satztyp | Stellung des finiten Verbs | Paragraph | Regel-ID |
|---|---|---|---|
| Aussagehauptsatz | Position 2 | §17.1 | ORB-GRAM-SYN-010 |
| Ja/Nein-Frage | Position 1 | §18.1 | ORB-GRAM-SYN-016 |
| W-Frage | Position 2 (Fragewort auf 1) | §18.2 | ORB-GRAM-SYN-017 |
| Nebensatz | Satzende | §17.2 | ORB-GRAM-SYN-011 |

Ein drittes Muster gibt es nicht. Der Imperativ ist in §14 nur morphologisch beschrieben
(*Mel!*, *Meleñ!*, *Melaten!*); eine Stellungsregel für den Imperativsatz steht weder in
§14 noch in §17.

---

## 2. Hauptsatz — Verb auf Position 2 (§17.1)

> **ORB-GRAM-SYN-010** — Das finite Verb steht im Aussagehauptsatz an zweiter Position.

Die Grammatik belegt die Regel mit drei Stellungen derselben Aussage. Position 1 wechselt,
das Verb bleibt auf 2:

| Position 1 | Verb (2) | Rest | Deutsch |
|---|---|---|---|
| *Xra valru* | *milkat* | *xran narkun.* | Der Mann sieht den Hund. |
| *Xran narkun* | *milkat* | *xra valru.* | Den Hund sieht der Mann. |
| *Nunda* | *milkat* | *xra valru xran narkun.* | Heute sieht der Mann den Hund. |

Alle drei Zeilen stehen wörtlich in §17.1; die erste zusätzlich in §25.1.

Position 1 ist **eine** Satzposition, gleich wie viele Wörter sie füllt: *Xra valru* ist ein
Feld, *Nunda* ebenso. Zwei Sonderfälle sind ausdrücklich geregelt:

- **Partikel *mai* zählt nicht eigenständig.** §16.2: „*mai* und das finite Verb bilden
  **eine** Satzposition." Beleg §25.1: *Tund vim vra vlaidra valru mai em, mai traivam vim
  xlan eirden.* — der Nachsatz beginnt mit *mai traivam*, und das ist Position 2.
- **Ein vorangestellter Nebensatz besetzt Position 1** (siehe Abschnitt 4).

Für die Negationspartikel *xa* trifft §18.3 **keine** entsprechende Aussage über das
Positionszählen; §18.3 legt nur die Nachbarschaft fest (*xa* unmittelbar vor dem finiten
Verb). Der Audit verzeichnet zur Negation keinen Befund (`Orbis-Audit-0_1.md` §13).

---

## 3. Nebensatz — Verb am Ende (§17.2)

> **ORB-GRAM-SYN-011** — Im Nebensatz steht das finite Verb am Ende.

Beleg §17.2: *Vim zavam, fai şet nunda dun xnaş breuneş melaş.* (Die Grammatik gibt zu
diesem Satz keine Übersetzung.)

Beleg mit Übersetzung, §25.1: *Vim zavam, fai şet zirna vandaiş.* — Ich weiß, dass du
morgen kommen wirst. · *Vim xa valnam soñex, grali xla kirva vran luid est.* — Ich kann
nicht schlafen, weil die Nacht sehr hell ist.

Die Verbendstellung gilt für alle sieben unterordnenden Konjunktionen aus §20 (Abschnitt 9).
Sie gilt im Beleg auch für den **indirekten Fragesatz**: §25.2 *Ro xa zovet, kur xna melna
molet* — Er wusste nicht, wohin der Weg führte. §20 führt *kur* nicht in der Liste der
unterordnenden Konjunktionen; belegt ist die Konstruktion nur durch dieses Beispiel und
durch Test 098 (*Vim xa zavam, kur xna vresto est.*).

---

## 4. Der vorangestellte Nebensatz (§17.1)

> **ORB-GRAM-SYN-012** — Steht ein Nebensatz auf Position 1, folgt das finite Verb des
> Hauptsatzes unmittelbar.

§17.1 sagt es wörtlich: „Steht ein Nebensatz vor dem Hauptsatz, besetzt er Position 1 — das
finite Verb folgt direkt."

Beleg §25.1: *Xnan melnan traivamen viñ, tund xla luiv luid est.* (Nebensatz nachgestellt) ·
*Tund vim vra vlaidra valru mai em, mai traivam vim xlan eirden.* (Nebensatz vorangestellt,
danach *mai traivam*).

Belege aus dem Testkorpus: Test 093 *Tund şet melaş, stanam vim.* · Test 095 *Dremi viñ
maldamen, talat xra valru.* · Test 097 *Trausi ro nastot, soñot ro.*

Der Effekt ist regelmäßig: Weil der Nebensatz Position 1 füllt, steht das Subjekt des
Hauptsatzes **hinter** dem Verb.

---

## 5. Verbklammer (§17.3, §16.1)

> **ORB-GRAM-SYN-013** — Modalverb Position 2, Infinitiv am Satzende.

§16.1: „Konjugiertes Modalverb auf Position 2, Vollverb im **Infinitiv am Satzende**."

Beleg §17.3: *Vim valnam nunda zva xraş velkraş dun xlaş kavlaş melex.* (ohne Übersetzung
in der Grammatik) · Beleg §16.1: *Vim valnam xnan melnan milkex.* — Ich kann den Weg sehen.
· *Şet dolmaş nunda vandex.* — Du musst heute kommen.

Alles zwischen Modalverb und Infinitiv ist Mittelfeld. Die sechs Modalwurzeln sind *valn-*
(können), *dolm-* (müssen), *vlek-* (dürfen), *tirn-* (sollen), *nest-* (wollen), *suvr-*
(mögen) (§16.1).

> **[REGELKONFLIKT K-05] Verbklammer im Nebensatz.**
> §16.1 verlangt den Infinitiv „am Satzende", §17.2 das finite Verb am Nebensatzende. Im
> Nebensatz beanspruchen beide dieselbe Position. Kein Beispiel in 0.9.3 enthält ein
> Modalverb im Nebensatz; Test 103 und Test 105 prüfen den Fall gezielt und bleiben
> unentscheidbar. Diese Dokumentation entscheidet nicht.

> **[REGELUNKLARHEIT U-03] Modalverb ohne Infinitiv.**
> Ob ein Modalverb als Vollverb mit direktem Objekt stehen darf, regelt §16.1 nicht
> (Test 111).

---

## 6. Satzgliedfolge im Mittelfeld (§17.4)

> **ORB-GRAM-SYN-014** — Zeit – Grund – Art – Ort. Status: `provisional`.

§17.4 nennt die Folge **Zeit – Grund – Art – Ort** und sagt ausdrücklich dazu: „Tendenz,
keine harte Regel."

Beleg §17.4: *Vim melaim zirna gral xlas talumas zva xraş velkraş dun xlaş kavlaş.* (ohne
Übersetzung in der Grammatik)

| Feld | Ausdruck | Typ |
|---|---|---|
| Vorfeld | *Vim* | Subjekt |
| Verb (2) | *melaim* | 1. Sg Zukunft |
| Zeit | *zirna* | Adverb |
| Grund | *gral xlas talumas* | *gral* + Genitiv |
| Art | *zva xraş velkraş* | *zva* + Dativ |
| Ort | *dun xlaş kavlaş* | *dun* + Dativ |

Weil §17.4 die Folge selbst als Tendenz kennzeichnet, ist eine Abweichung **kein Verstoß**.
Ein Beleg für eine abweichende Folge steht in §17.3: dort geht *nunda* (Zeit) der Art- und
Ortsangabe voran, ein Grund fehlt — die Reihenfolge bleibt gewahrt.

> **[REGELUNKLARHEIT U-05] Objektreihenfolge.** Dativ vor Akkusativ ist durchgehende
> Beispielpraxis (*dolvet xnaş şirneş xnan brasin*, §25.1), aber keine Regel
> (ORB-GRAM-SYN-023).

> **[REGELUNKLARHEIT U-11] Temporaler Dativ.** §25.2 verwendet *Vraş zaldreş* („an einem
> Tag") als bloße Dativ-Zeitangabe ohne Präposition. §8, §17 und §19 sehen diese
> Konstruktion nicht vor (ORB-GRAM-SYN-025).

---

## 7. Keine Kopula-Auslassung (§17.5)

> **ORB-GRAM-SYN-015** — Die Kopula wird nicht ausgelassen.

Beleg §17.5: *Xla luiv luid vot, xla kirva girn vot.* — Die Sonne war hell, die Nacht war
kalt. Beide Teilsätze setzen *vot*; keiner lässt es weg.

§17.5 trägt zusätzlich die Marke **[NOCH ZU ENTSCHEIDEN]** für die Auslassung als
dichterisches Stilmittel. Bis dahin gilt die Regel ausnahmslos.

Das prädikative Adjektiv steht dabei in der **Grundform** (§12.2): *Lo loşn est.*,
*Xra valru xarn vurt.*, *Xna breun granz stanat.*, *Xrañ larkiñ girn esten.*

> **[REGELUNKLARHEIT U-13] Prädikativ und V2.**
> In allen Beispielen der Grammatik steht das Prädikativ **vor** dem Verb, das Verb also an
> dritter Wortposition (*Lo loşn est* = 1 *Lo*, 2 *loşn*, 3 *est*). Ob Prädikativ und Kopula
> zusammen eine Satzposition bilden, sagt die Grammatik nicht. Das Testkorpus belegt beide
> Folgen: Test 057 *Xra valru xarn vurt* (Prädikativ vor dem Verb) und Test 125 *Viñ voremen
> xarn* (Prädikativ nach dem Verb) sind beide mit [OK] bewertet.

---

## 8. Fragen (§18.1, §18.2)

### 8.1 Ja/Nein-Frage — Verb auf Position 1

> **ORB-GRAM-SYN-016** — Das finite Verb steht an Position 1.

Beleg §18.1: *Melaş nunda?* — Gehst du heute? Antwortpartikeln: **ain** (ja) · **xaus**
(nein).

Belege aus dem Testkorpus: Test 071 *Melaş şet nunda?* · Test 072 *Vandat xra draun?* ·
Test 114 *Valnaten şevar vin zaubex?* (Höflichkeitsform §13.2 + Verbklammer).

Der Grammatikbeleg *Melaş nunda?* lässt das Subjektpronomen weg, Test 071 setzt es. Beides
gilt als korrekt — siehe U-04 unten.

### 8.2 W-Frage — Fragewort auf 1, Verb auf 2

> **ORB-GRAM-SYN-017** — Fragewort Position 1, finites Verb Position 2.

| Orbis | Deutsch |
|---|---|
| **kem** | wer |
| **kelt** | was |
| **kur** | wo, wohin |
| **kan** | wann |
| **grais** | warum |
| **kolm** | wie |
| **kelra / kella / kelna** | welcher / welche / welches |

Belege §18.2: *Kan melaş?* · *Grais xa vandat?* · *Kellan sarlan milkoş?*
Belege Testkorpus: Test 073 *Kem talat?* · Test 077 *Kur maldaşen şeñ?* · Test 078 *Kolm est
xla kirva?* · Test 079 *Kelnan vreston leşnaş şet?* · Test 080 *Kelnaş şirneş dalvaş şet xnan
brasin?*

*kelra / kella / kelna* kongruieren adjektivisch mit ihrem Nomen — belegt durch *Kellan
sarlan* (Akkusativ, §18.2) und Test 079/080.

> **[REGELLÜCKE L-03] Deklination von *kem/kelt*.**
> §18.2 listet nur die Grundformen. „Wen?", „Wem?", „Wessen?" sind nicht bildbar; weder
> Kasusformen noch Indeklinabilität sind festgelegt (Tests 074, 075, 076).

> **[REGELUNKLARHEIT U-04] Subjektauslassung (Pro-Drop).**
> Die §18-Beispiele lassen das Subjektpronomen weg (*Melaş nunda?*, *Kan melaş?*, *Grais xa
> vandat?*), alle Aussagesatz-Beispiele behalten es. Wann Weglassen zulässig ist, sagt keine
> Regel (ORB-GRAM-SYN-024).

---

## 9. Negation (§18.3)

> **ORB-GRAM-SYN-018** — Partikel *xa* unmittelbar vor dem finiten Verb; attributiv *xan-*.

§18.3 kennt **eine einzige** Negationspartikel: **xa**, unmittelbar vor dem finiten Verb.

| Funktion | Mittel | Beleg |
|---|---|---|
| Satz-/Verbnegation | Partikel **xa** vor dem finiten Verb | *Vim xa melam.* (§18.3) — Ich gehe nicht. |
| attributive Negation | Adjektiv **xan-**, dekliniert wie §12.1 | *xanra valru* (§18.3) — kein Mann; Test 086 *Xanra valru maldat.* |
| negatives Indefinitpronomen | **xakaun** (niemand), **xakelte** (nichts), §13.4 | Test 088 *Xakaun vandat.* — Niemand kommt. |

Die Partikel bleibt auch dann direkt vor dem finiten Verb, wenn das Vorfeld gefüllt ist oder
eine Verbklammer vorliegt:

- Test 045 *Xla taiv xlas eirdes xa vaşnat.* — Vorfeld mit Genitivattribut, *xa* bleibt am
  Verb.
- Test 115 *Xna şirn xa vlekat melex.* — bei der Verbklammer steht *xa* vor dem **finiten**
  Verb, nicht vor dem Infinitiv.
- Test 090 *Vim zavam, fai ro xa vandat.* — im Nebensatz vor dem satzfinalen finiten Verb.
- §18.2 *Grais xa vandat?* — auch in der W-Frage.

> **[REGELUNKLARHEIT U-14] Unmarkiertes Objekt in §18.3.**
> Der Beleg *Vim xa num vna breun* („Ich habe kein Haus") lässt Artikel und Kernwort
> unmarkiert; regelkonform nach §8/§10.3/§11 wäre *vnan breunen* — so schreibt es Test 083
> (*Viñ xa numen vnan breunen.*).

---

## 10. Präpositionen (§19)

> **ORB-GRAM-SYN-001** (Datensatz `language/syntax/prepositions.json`)

Sechzehn Präpositionen, in drei feste Kasusgruppen und eine Wechselgruppe geteilt. Die
Spalte „Beleg" nennt eine belegte Fundstelle oder sagt, dass keine existiert.

### 10.1 Fester Kasus

| Orbis | Deutsch | Fall | Beleg |
|---|---|---|---|
| **zva** | mit | Dativ | *zva xraş velkraş* (§17.3, §17.4) |
| **dun** | zu, nach | Dativ | *dun xnaş breuneş vis* (§25.1); *dun xlaş kavlaş* (§17.3) |
| **ven** | von | Dativ | **kein Beleg** in Grammatik oder Testkorpus |
| **nul** | bei | Dativ | **kein Beleg** |
| **xun** | ohne | Akkusativ | **kein Beleg** |
| **prai** | für | Akkusativ | **kein Beleg** |
| **dral** | durch | Akkusativ | *dral xrañan trelmrañan zaldreñen* (§25.2) |
| **gral** | wegen | Genitiv | *gral xlas talumas* (§17.4) |
| **şlan** | trotz | Genitiv | **kein Beleg** |

### 10.2 Wechselpräpositionen — Dativ = Ort, Akkusativ = Richtung

| Orbis | Deutsch | Beleg |
|---|---|---|
| **tel** | in | *Vim melam tel xlan kavlan.* (Akk = Richtung, §19) · *Vim em tel xlaş kavlaş.* (Dat = Ort, §19) · *Tel xraş navildoş milkot ro …* (§25.2) |
| **kru** | auf | Test 031 *Vim maldam kru xlaş melvaş.* (Dat = Ort) |
| **span** | über | *span xran vrondon* (§25.1, Richtung) · Test 150 *span xlaş kavlaş* (Ort) |
| **drel** | unter | **kein Beleg** |
| **glem** | vor | **kein Beleg** |
| **traus** | hinter | **kein Beleg** |
| **şlim** | zwischen | *şlim xrañaş larkiñiş* (§25.2, Dativ) |

Acht der sechzehn Präpositionen haben in 0.9.3 und im Testkorpus 0.1 **keinen einzigen
Beispielsatz**: *ven, nul, xun, prai, şlan, drel, glem, traus*. Ihre Kasusangabe steht in der
Tabelle von §19 und ist damit geregelt; belegt ist sie nicht. (Test 137 erwägt *ven xraş
valruş* für das Passiv-Agens, verwirft die Form aber ausdrücklich als ungeregelt — siehe
L-05.)

### 10.3 Präposition und Vorsilbe

§19 hält ausdrücklich fest: **Präposition und Vorsilbe sind getrennte Kategorien.** *dral*
ist nur Präposition, *dra-* nur Vorsilbe (§21.2, *dramilkat*).

---

## 11. Konjunktionen (§20)

> **ORB-GRAM-SYN-002** (Datensatz `language/syntax/conjunctions.json`)

### 11.1 Nebenordnend — Hauptsatzstellung

| Orbis | Deutsch | Beleg |
|---|---|---|
| **ze** | und | §25.2 *Ro nastot, ro prevot, ze ro soñot.* · *Ze ro dremnot: „Kilna est xna traivute."* |
| **vu** | oder | **kein Beleg** in Grammatik oder Testkorpus |
| **klas** | aber | §25.1 *Xna breun granz stanat, klas xla kavla zirv vurt.* · §25.2 *…, klas ro molet.* |
| **xer** | denn | Test 099 *Vim maldam, xer xla kirva girn est.* |

Die nebenordnende Konjunktion zählt **nicht** als Position 1: In *ze ro soñot* und *klas ro
molet* folgt auf die Konjunktion das Subjekt, dann das Verb — das Verb steht also weiterhin
auf Position 2 des Teilsatzes. Das gilt auch satzinitial: *Ze ro dremnot …* (§25.2).

### 11.2 Unterordnend — Verbendstellung

| Orbis | Deutsch | Beleg |
|---|---|---|
| **fai** | dass | §25.1 *Vim zavam, fai şet zirna vandaiş.* |
| **grali** | weil | §25.1 *…, grali xla kirva vran luid est.* |
| **tund** | wenn | §25.1 *Xnan melnan traivamen viñ, tund xla luiv luid est.* |
| **şlani** | obwohl | Test 094 *Şlani xna vresto granz est, leşnam vim non.* |
| **dremi** | während | Test 095 *Dremi viñ maldamen, talat xra valru.* |
| **glemi** | bevor | Test 096 *Glemi xla luiv vandat, melamen viñ.* |
| **trausi** | nachdem | Test 097 *Trausi ro nastot, soñot ro.* |

### 11.3 Die Ableitungsbehauptung (U-07)

§20 schreibt: „Systematisch aus den Präpositionen abgeleitet, Suffix **-i**."

| Konjunktion | Präposition | Ableitung |
|---|---|---|
| grali | gral (wegen) | trägt |
| şlani | şlan (trotz) | trägt |
| glemi | glem (vor) | trägt |
| trausi | traus (hinter) | trägt |
| **dremi** | — | keine Präposition \*drem; *drel* „unter" ergäbe *dreli* |
| **tund** | — | kein *-i*, keine Basis |
| **fai** | — | keine Basis |

> **[REGELUNKLARHEIT U-07]** Die Behauptung trägt für vier von sieben Formen. Für *dremi*,
> *tund* und *fai* ist sie falsch bzw. leer. Diese Dokumentation korrigiert die Behauptung
> nicht; sie meldet den Befund.

Zusätzlich ist **fai** homonym: §13.4 führt es als Relativpronomen, §20 als Konjunktion
„dass" (siehe L-02 und W-03).

---

## 12. Vergleichspartikeln (§12.3)

Nicht zu den Konjunktionen von §20 gezählt, aber satzverbindend: **kon** (als) und **zil**
(wie).

Belege §12.3: *Ro vlaidvi est kon vim.* — Er ist größer als ich. · *Lo loşn est zil luiv.* —
Sie ist schön wie die Sonne. Testkorpus: Test 054 (*kon vim*), Test 056 (*Lo velm est zil
luiv.*).

> **[REGELUNKLARHEIT U-06]** Welcher Kasus nach *kon* und *zil* steht, ist nicht festgelegt;
> die Belege zeigen den Nominativ (*kon vim*, *zil luiv*), eine Regel dazu fehlt.

---

## 13. Offene Punkte der Syntax

Diese Dokumentation entscheidet nichts. Vollständige Beschreibung aller Befunde:
`Orbis-Audit-0_1.md` §A; maschinenlesbar in `language/findings/findings.json`.

| ID | Typ | Betrifft | Kurz | Regel-ID |
|---|---|---|---|---|
| L-01 | Lücke | §8, §17 | Stellung des Genitivattributs, inkl. Stapelung mit Possessiv | ORB-GRAM-SYN-021 |
| L-02 | Lücke | §13.4, §17 | Relativsatzbau: Kasus, Kongruenz, Verbstellung von *fai*; Homonymie mit *fai* „dass" | ORB-GRAM-SYN-022 |
| K-05 | Konflikt | §16.1 ↔ §17.2 | Modalverb im Nebensatz: Infinitiv und finites Verb beanspruchen dieselbe Endposition | ORB-GRAM-SYN-013 |
| U-04 | Unklarheit | §18 | Pro-Drop nur Beispielpraxis | ORB-GRAM-SYN-024 |
| U-05 | Unklarheit | §17 | Objektreihenfolge Dativ vor Akkusativ nur Praxis | ORB-GRAM-SYN-023 |
| U-11 | Unklarheit | §25.2 | temporaler Dativ ohne Präposition (*Vraş zaldreş*) | ORB-GRAM-SYN-025 |
| U-13 | Unklarheit | §12.2 ↔ §17.1 | Prädikativ steht in allen Grammatikbeispielen vor dem Verb; reibt sich an V2 | ORB-GRAM-SYN-015 |

Weitere Befunde berühren die Syntax mittelbar:

| ID | Typ | Betrifft | Kurz |
|---|---|---|---|
| L-03 | Lücke | §18.2 | Deklination von *kem/kelt* (wen/wem/wessen) |
| L-04 | Lücke | §13.4 | Kasusformen des Reflexivums *se* — trifft jedes reflexive Satzmuster |
| L-05 | Lücke | §16.3 | Agens im Passiv |
| L-08 | Lücke | §24.8 | Syntax der Kardinalzahlen |
| U-02 | Unklarheit | §12, §14 | Partizip attributiv verwendbar? |
| U-03 | Unklarheit | §16.1 | Modalverb ohne Infinitiv |
| U-06 | Unklarheit | §12.3 | Kasus nach *kon/zil* |
| U-07 | Unklarheit | §20 | Ableitungsbehauptung passt nicht zu *dremi/tund/fai* |
| U-14 | Unklarheit | §18.3 | *Vim xa num vna breun* lässt Artikel und Kernwort unmarkiert |

---

*Dokumentation zur Grammatik 0.9.3. Bei Abweichung gilt `Orbis-Grammatik-0.9.3.md`.*
