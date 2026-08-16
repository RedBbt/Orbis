# ORBIS — Das Nomen

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Grundprinzip (§6)

Orbis kennt drei Geschlechter: **Maskulin, Feminin, Neutrum**. Das Geschlecht ist am
Wort selbst sichtbar; bei etwa 90 % aller Nomen ist es sofort an der Endung erkennbar
(§6).

> **Klassenkonsonant + Themavokal**

Der **Klassenkonsonant** trägt das Geschlecht, der **Themavokal** gehört fest zum Wort
und sorgt für Klangvielfalt (§6). *valru* ist maskulin, weil *-r-* maskulin ist; das *-u-*
ist reine Wortidentität und hat keine grammatische Funktion.

Merksatz der Grammatik (§7.3): **r-k-d männlich · l-v-m weiblich · n-s-t sächlich.**

---

## 2. Die 45 regulären Geschlechtsendungen (§7)

Neun Klassenkonsonanten × fünf Themavokale ergeben 45 Endungen.

| Geschlecht | Unterklasse A | Unterklasse B | Unterklasse C |
|---|---|---|---|
| Maskulin | **r** | **k** | **d** |
| Feminin | **l** | **v** | **m** |
| Neutrum | **n** | **s** | **t** |

### 2.1 Die vollständige Endungstabelle

Die Spalten sind die fünf Themavokale (§7.1–§7.3). In Klammern steht ein im Wortschatz
0.9.3 belegtes Wort; „—" heißt: Die Endung ist regulär, aber im eingefrorenen Wortschatz
(§24.2–§24.4) von keinem Wort belegt.

| Klasse | -a | -e | -i | -o | -u |
|---|---|---|---|---|---|
| **M-A** (r) | -ra (*velkra* Freund) | -re (*zaldre* Tag) | -ri — | -ro — | -ru (*valru* Mann) |
| **M-B** (k) | -ka — | -ke — | -ki (*larki* Stein) | -ko (*vlaiko* Wind) | -ku (*narku* Hund) |
| **M-C** (d) | -da (*morda* Sturm) | -de — | -di (*luvandi* Fluss) | -do (*vrondo* Berg) | -du — |
| **F-A** (l) | -la (*sarla* Frau) | -le — | -li — | -lo (*zenlo* Blume) | -lu — |
| **F-B** (v) | -va (*kirva* Nacht) | -ve — | -vi (*gluvi* Flamme) | -vo — | -vu — |
| **F-C** (m) | -ma (*soruma* Erinnerung) | -me — | -mi — | -mo — | -mu — |
| **N-A** (n) | -na (*melna* Weg) | -ne (*milne* Auge) | -ni — | -no (*verno* Herz) | -nu (*skelnu* Himmel) |
| **N-B** (s) | -sa (*taisa* Wort) | -se — | -si (*brasi* Brot) | -so (*pliso* Feder) | -su — |
| **N-C** (t) | -ta — | -te (*vlaidte* das Große, §12.5) | -ti — | -to (*vresto* Buch) | -tu (*veltu* Jahr) |

Auszählung gegen §24.2–§24.4 und §12.5: 24 der 45 Endungen sind durch mindestens ein
Wort belegt, 21 sind regulär, aber unbelegt. Das ist eine Beobachtung am eingefrorenen
Wortschatz, keine Regel — alle 45 Endungen sind nach §7 gleichermaßen gültig. Der
Testkorpus 0.1 prüft sie vollständig am ausdrücklich markierten Teststamm *pren-*
(Anhang 1, 45 Formenreihen; diese Formen sind keine Wörter des Wortschatzes).

### 2.2 Bedeutung der Unterklassen (§7.4)

| Unterklasse | Tendenz laut §7.4 |
|---|---|
| **A** (r / l / n) | grundlegende, häufige, alte Alltagswörter |
| **B** (k / v / s) | konkrete, abgeleitete, jüngere Wörter |
| **C** (d / m / t) | abstrakte, traditionelle, gehobene Wörter |

§7.4 bezeichnet das ausdrücklich als Tendenz, nicht als feste Regel; die endgültige
Funktion der Unterklassen ist in §7.4 und §30 als **[NOCH ZU ENTSCHEIDEN]** markiert.

---

## 3. Die vier Fälle (§8)

> **Stamm + Klassenkonsonant + Themavokal + Kasusmarker**

| Fall | Marker |
|---|---|
| Nominativ | — |
| Akkusativ | **-n** |
| Dativ | **-ş** |
| Genitiv | **-s** |

### 3.1 Volltabelle *valru* „Mann" (M-A)

Singular nach §8, Plural nach §9:

| Fall | Singular | Plural |
|---|---|---|
| Nominativ | **valru** | **valruñ** |
| Akkusativ | **valrun** | **valruñun** |
| Dativ | **valruş** | **valruñuş** |
| Genitiv | **valrus** | **valruñus** |

Alle acht Formen stehen wörtlich in §8 und §9.

### 3.2 Dieselbe Reihe feminin und neutral (§8, §9)

| Fall | *sarla* (F-A) Sg | *sarla* Pl | *milne* (N-A) Sg | *milne* Pl |
|---|---|---|---|---|
| Nominativ | sarla | sarlañ | milne | milneñ |
| Akkusativ | sarlan | sarlañan | milnen | milneñen |
| Dativ | sarlaş | sarlañaş | milneş | milneñeş |
| Genitiv | sarlas | sarlañas | milnes | milneñes |

Der Kasusmarker ist in allen drei Geschlechtern und allen neun Unterklassen derselbe;
das Geschlecht steckt allein im Klassenkonsonanten.

Belegte Sätze: *Xra valru milkat xran narkun.* (Nom + Akk, §25.1) ·
*Xla veiş dolvet xnaş şirneş xnan brasin.* (Dat + Akk, §25.1) ·
*Xla soruma xlas nauşes vran tolm vaşnat.* (Genitiv, §25.1).

**[REGELLÜCKE] L-01:** Die **Stellung** des Genitivattributs ist nicht festgelegt. §8
definiert den Genitiv nur morphologisch, §17 schweigt zur Attributstellung. Sämtliche
Beispiele stellen das Genitivattribut nach (*xla soruma xlas nauşes*, *xlan luiven xlas
eirdes*, §25.1/§25.2); eine Regel ist das nicht. Ebenfalls offen ist die Reihenfolge bei
Stapelung von Genitiv und Possessiv.

---

## 4. Plural (§9)

> Marker **-ñ-** zwischen Themavokal und Kasusmarker, in den obliquen Fällen mit
> **Echovokal**.

Der Nominativ Plural hat keinen Echovokal (*valruñ*), die drei obliquen Fälle haben ihn
(*valruñun, valruñuş, valruñus*).

**[REGELUNKLARHEIT] U-09:** Der Begriff „Echovokal" ist in 0.9.3 nirgends definiert. Aus
den Tabellen ergibt sich, dass er der Themavokal des Nomens ist (u→u, a→a, e→e) und bei
Artikel und Adjektiv immer *a* lautet — als Regel formuliert ist das nicht; die Tabellen
tragen die Definition allein.

Belegte Echovokale:

| Themavokal | belegte Pluralform | Beleg |
|---|---|---|
| u | *valruñun, valruñuş, valruñus* | §9 |
| a | *sarlañan, sarlañaş, sarlañas* | §9 |
| e | *milneñen, milneñeş, milneñes*; *zaldreñen* | §9; §25.2 |
| i | *larkiñiş* | §25.2 („şlim xrañaş larkiñiş") |
| o | *vrestoñon* | Testkorpus 0.1, Test 067 |

Die Formen mit *i* und *o* sind belegt, aber nur per Analogie zu den Tabellen erklärbar
(U-09).

**Historische Nebenform (§9):** Die 15 alten Kernwörter bewahren den Plural auf **-ei**
(siehe Abschnitt 5).

---

## 5. Die 15 Kernwörter (§10.2, §10.3, §24.1)

Fünfzehn echte Ausnahmen, abschließend aufgezählt. Ihr Geschlecht ist nicht an der Form
ablesbar, sondern Wörterbuchwissen.

| Wort | Bedeutung | Geschlecht | Proto-Orbis | Plural (§24.1) |
|---|---|---|---|---|
| **kaun** | Mensch | m | \*kau-nu | kaunei |
| **veiş** | Mutter | f | \*veş-iv | veişei |
| **draun** | Vater | m | \*drau-nu | draunei |
| **şirn** | Kind | n | \*şir-ni | şirnei |
| **aul** | Wasser | n | \*au-lu | aulei |
| **xerp** | Feuer | m | \*xer-pa | xerpei |
| **luiv** | Sonne | f | \*luv-iv | luivei |
| **grein** | Erde, Boden | f | \*gre-ina | greinei |
| **nauş** | Zeit | f | \*nau-şa | nauşei |
| **virn** | Leben | n | \*vir-na | virnei |
| **moks** | Tod | m | \*mok-sa | moksei |
| **eird** | Welt | f | \*e-irda | eirdei |
| **şaul** | Name | m | \*şa-ulo | şaulei |
| **taiv** | Sprache | f | \*tal-iv | taivei |
| **breun** | Haus | n | \*breu-na | breunei |

### 5.1 Deklination (§10.3)

> **Singular: Wort + Bindevokal -e- + Kasusmarker. Plural: Wort + -ei + Kasusmarker.**

| Fall | *kaun* (m) | *aul* (n) | *eird* (f) |
|---|---|---|---|
| Nom Sg | kaun | aul | eird |
| Akk Sg | kaunen | aulen | eirden |
| Dat Sg | kauneş | auleş | eirdeş |
| Gen Sg | kaunes | aules | eirdes |
| Nom Pl | kaunei | aulei | eirdei |
| Akk Pl | kaunein | aulein | eirdein |
| Dat Pl | kauneiş | auleiş | eirdeiş |
| Gen Pl | kauneis | auleis | eirdeis |

Der Nominativ Singular ist endungslos. Der Bindevokal ist **immer -e-**; §10.3 erklärt
Formen wie \**aulan* oder \**eirdas* ausdrücklich für falsch.

Belegte Sätze: *Xla veiş dolvet xnaş şirneş xnan brasin.* (§25.1) ·
*Nunda melam vim dun xnaş breuneş vis.* (§25.1) ·
*mai traivam vim xlan eirden* (§16.2) ·
*Tel xraş navildoş milkot ro xlan luiven xlas eirdes.* (§25.2).

### 5.2 Betonung und Silbenstruktur

Die 15 Kernwörter tragen die Betonung auf der **letzten** Silbe (§23: *kaUN, breUN,
taIV*) und weichen damit von der Normalregel „vorletzte Silbe" ab.

Anmerkung zu **K-01**: *aul* und *eird* (samt allen flektierten Formen) haben vokalischen
Anlaut mit geschlossener Silbe (VK bzw. VKK). §5.1 führt diese Silbenformen nicht auf.
Das ist ein Befund an der Grammatik, kein Fehler der Wörter.

---

## 6. Die 10-Prozent-Gruppe (§10.1)

Bei diesen Wörtern ist der Endvokal historisch geschwunden; das Geschlecht bleibt am
Restkonsonanten erkennbar.

| Modern | Bedeutung | Proto-Orbis | Erklärung | Geschlecht |
|---|---|---|---|---|
| **velkran** | Freundschaft | \*velkra-na | Endvokal geschwunden | *-n-* → neutral |
| **soralm** | Denkmal | \*soral-mu | Endvokal geschwunden | *-m-* → feminin |
| **prilm** | Handwerk | \*prila-mu | Verschmelzung | *-m-* → feminin |

### 6.1 Deklination Singular

Wie bei den Kernwörtern mit Bindevokal **-e-** (§10.1), belegt an *velkran*:

| Fall | Form |
|---|---|
| Nominativ | velkran |
| Akkusativ | velkranen |
| Dativ | velkraneş |
| Genitiv | velkranes |

Für die drei Wörter gibt es in 0.9.3 keinen Beispielsatz; belegt ist allein die
Formenreihe *velkran, velkranen, velkraneş, velkranes* in §10.1. Auch der Testkorpus 0.1
enthält keinen Satz mit *velkran*, *soralm* oder *prilm*. Das im Satzbeispiel §17.3
verwendete *velkraş* gehört zum regulären Nomen *velkra* „Freund" (M-A), nicht zu
*velkran*.

### 6.2 Plural

**[REGELLÜCKE] L-07:** §10.1 regelt nur den Singular. Der reguläre Plural (*-ñ-* nach
dem Themavokal) ist mangels Themavokal nicht anwendbar (\**velkranñ*), und der
Kernwortplural **-ei** ist laut §9 ausdrücklich den 15 Kernwörtern vorbehalten. „Die
Freundschaften", „die Denkmäler", „die Handwerke" sind in 0.9.3 **nicht bildbar**. Hier
wird nichts geraten und nichts ergänzt.

---

## 7. Der Artikel (§11)

> Bestimmtheitszeichen (**x-** bestimmt, **v-** unbestimmt) + Geschlechtskonsonant der
> **A-Reihe** (r / l / n) + **-a**, danach die üblichen Marker.

### 7.1 Bestimmter Artikel (§11.1)

| Fall | Maskulin | Feminin | Neutrum |
|---|---|---|---|
| Nom Sg | **xra** | **xla** | **xna** |
| Akk Sg | xran | xlan | xnan |
| Dat Sg | xraş | xlaş | xnaş |
| Gen Sg | xras | xlas | xnas |
| Nom Pl | xrañ | xlañ | xnañ |
| Akk Pl | xrañan | xlañan | xnañan |
| Dat Pl | xrañaş | xlañaş | xnañaş |
| Gen Pl | xrañas | xlañas | xnañas |

Der Echovokal des Artikels ist immer **a** — auch dort, wo das Nomen einen anderen
Themavokal hat: *xrañaş larkiñiş* (§25.2), *xnañan vrestoñon* (Testkorpus 0.1, Test 067).

### 7.2 Unbestimmter Artikel (§11.2)

**vra** (m) · **vla** (f) · **vna** (n), mit denselben Markern: *vran, vraş, vras* usw.

> **Im Plural steht kein unbestimmter Artikel** (§11.2).

Belege: *Vra melru molet dral xrañan trelmrañan zaldreñen.* (§25.2) ·
*Vraş zaldreş traivot ro vnan aulen şlim xrañaş larkiñiş.* (§25.2) ·
*Tund vim vra vlaidra valru mai em …* (§16.2).

### 7.3 Der Artikel zeigt nur das Geschlecht (§11.3)

Der Artikel verwendet **immer** die A-Reihe. Es gibt keine Artikel mit *k, d, v, m, s, t*.

| Nomen | Unterklasse | Geschlecht | Artikel |
|---|---|---|---|
| valru | M-A | maskulin | **xra** valru |
| narku | M-B | maskulin | **xra** narku |
| vrondo | M-C | maskulin | **xra** vrondo — *nicht* †xda |
| kirva | F-B | feminin | **xla** kirva |
| soruma | F-C | feminin | **xla** soruma |
| taisa | N-B | neutral | **xna** taisa |
| vresto | N-C | neutral | **xna** vresto |

Bei den 15 Kernwörtern folgt der Artikel dem Wörterbuchgeschlecht (§11.3):
*xnaş şirneş* (dem Kind) · *xlan eirden* (die Welt, Akk.) · *xnan aulen* (das Wasser, Akk.).

### 7.4 Formale Randnotiz

*vran* ist zugleich unbestimmter Artikel Maskulin Akkusativ (§11.2) und die Partikel
„sehr" (§24.9). Diese Homonymie ist kein Regelbefund; sie wird in Phase 7 des
`Orbis-Testbericht-0_1.md` geführt.

---

## 8. Zusammensetzungen mit nominalem Kopf (§21.3)

Bestimmungswort vorn, Grundwort hinten; Geschlecht und Klasse richten sich nach dem
letzten Glied.

| Kompositum | Bildung | Geschlecht |
|---|---|---|
| *taivbreun* Schule | taiv + breun | n |
| *aulmelna* Kanal | aul + melna | n |
| *luivresto* Kalender | luiv + vresto (Fugenregel §21.4) | n |

**[REGELUNKLARHEIT] U-08:** *taivbreun* hat als Kopf das Kernwort *breun*. Ob die
Zusammensetzung wie ein Kernwort dekliniert (Bindevokal *-e-*, Plural *-ei*) oder
regulär, sagt §21.3 nicht — die Kernwörter haben keine Klasse. *aulmelna* und
*luivresto* mit regulären Köpfen sind unproblematisch.

---

## 9. Offene Punkte zum Nomen

| ID | Typ | Betrifft | Kurz |
|---|---|---|---|
| L-01 | Lücke | §8, §17 | Stellung des Genitivattributs |
| L-07 | Lücke | §10.1 | Plural der 10-Prozent-Gruppe |
| L-08 | Lücke | §24.8 | Syntax der Kardinalzahlen: Kongruenz und Numerus des gezählten Nomens |
| U-05 | Unklarheit | §17 | Objektreihenfolge Dativ vor Akkusativ nur Beispielpraxis |
| U-08 | Unklarheit | §21.3 | Deklination von Komposita mit Kernwort-Kopf |
| U-09 | Unklarheit | §9 | „Echovokal" nur durch die Tabellen definiert |
| U-11 | Unklarheit | §25.2 | temporaler Dativ ohne Präposition (*Vraş zaldreş*) |
| U-14 | Unklarheit | §18.3 ↔ §8/§10.3/§11 | *Vim xa num vna breun* lässt Artikel und Kernwort unmarkiert |
| K-01 | Konflikt | §5.1 | Silbenformen VK/VKK fehlen, *aul*/*eird* brauchen sie |

Vollständige Beschreibung aller Befunde: `Orbis-Audit-0_1.md` §A.

---

*Dokumentation zur Grammatik 0.9.3. Bei Abweichung gilt `Orbis-Grammatik-0.9.3.md`.*
