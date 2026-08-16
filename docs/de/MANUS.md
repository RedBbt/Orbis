# Orbis — Orbis Manus, die Alltagsschrift

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Gegenstand

Dieses Kapitel beschreibt §26 der Grammatik vollständig: die Silbenformel (§26.1), die
20 Kernformen in 8 Familien (§26.2), den zweiten Anfangskonsonanten (§26.3), die
Vokalpunkte und die Zusammensetzung der Diphthonge (§26.4), die Platzierung von einem und
zwei Endkonsonanten (§26.5–26.6), die Trennung von Coda und Satzabschluss samt den sechs
Abschlusszeichen (§26.7), die Tastatureingabe (§26.8) und die Schreibregeln (§26.9).

Orbis Manus ist eine **Silbenschrift**: geschrieben wird nicht Buchstabe für Buchstabe,
sondern Silbenblock für Silbenblock. Schrift und Grammatik sind getrennte Ebenen und
werden getrennt versioniert; ein Schriftbefund ist kein Grammatikbefund.

Drei Vorbehalte gelten für das ganze Kapitel und werden hier benannt, nicht behoben:

| Vorbehalt | Wirkung |
|---|---|
| **[REGELLÜCKE L-09]** | Es gibt keine Silbifizierungsregel. 77 von 281 Grundformen haben mehr als eine regelkonforme Manus-Schreibung (Abschnitt 11 dieser Datei) |
| **[REGELLÜCKE L-10]** | Für *f s ş x v z j ç* ist keine Strichstärke definiert (Abschnitt 10 dieser Datei) |
| **[REGELUNKLARHEIT U-10]** | §26.8 nennt „20 Konsonantentasten"; Orbis hat 19 Konsonanten (Abschnitt 9 dieser Datei) |

---

## 2. Die vollständige Silbenformel (§26.1)

§26.1 gibt genau eine Formel für den Silbenblock:

> **Kernkonsonant + optionaler zweiter Anfangskonsonant + Vokalzeichen + 0–2 Endkonsonanten + (Satzabschluss)**

Die fünf Positionen im Einzelnen:

| Position | Pflicht | Regelt | Ort |
|---|---|---|---|
| Kernkonsonant | ja — ersatzweise der Vokalträger | eine der 20 Kernformen | Silbenkörper |
| zweiter Anfangskonsonant | nein | verkleinertes Beizeichen, ohne eigenes Vokalzeichen | unter der Kernform (§26.3) |
| Vokalzeichen | ja — *a* ist inhärent und wird nicht geschrieben | Punktposition, bei Diphthongen zwei Punkte | am Silbenkörper (§26.4) |
| Endkonsonant 1–2 | nein | verkleinerte Konsonantenform | unten rechts (§26.5–26.6) |
| Satzabschluss | nein | eines von sechs Zeichen | frei nach der Silbe (§26.7) |

Die Formel deckt sich in ihren Grenzen mit der Phonotaktik: höchstens zwei
Anfangskonsonanten (§5.2) und höchstens zwei Endkonsonanten (§5.3). Der Manus-Schreibtest
0.1 hält dazu ausdrücklich fest, dass Silbenformel, Vokalpunktsystem, Coda-Platzierung und
Abschlusszeichen **in sich vollständig** sind und alle zerlegbaren Silben abdecken —
**kein Befund** (`Orbis-Manus-Schreibtest-0_1.md`, Abschnitt 4.4).

Belegte Anwendung der Formel gibt §26 selbst in seinen Zerlegungstabellen: *mel*, *kaun*,
*breun*, *tel* (§26.5) sowie *moks*, *virn*, *xerp*, *teln* (§26.6).

---

## 3. Die 20 Kernformen in 8 Familien (§26.2)

§26.2 formuliert die Zahl ausdrücklich als Summe:

> **8 Zeichenfamilien, 20 Kernformen: 19 Konsonanten + 1 Vokalträger.**

Die 20. Kernform ist also **kein Konsonant**, sondern der Träger, der eine Silbe ohne
Anfangskonsonant schreibbar macht (Silbenform V bzw. VK, §5.1). Diese Lesart ist der
Prüfstein für §26.8 (siehe §9, U-10).

| Familie | Bedeutung | Laute | Formen | Belegte Wörter mit diesen Lauten |
|---|---|---|---|---|
| **NER** | Ursprung | m · n · ñ | 3 | *mela* (§24.3) · *nauş* (§24.1) · *oñ* (§13.1) |
| **TAL** | Fluss | l · r | 2 | *luiv* (§24.1) · *ro* (§13.1) |
| **SOR** | Winkel | p · t · k | 3 | *prila* (§24.3) · *taiv* (§24.1) · *kaun* (§24.1) |
| **VEL** | Bogen | b · d · g | 3 | *breun* (§24.1) · *draun* (§24.1) · *grein* (§24.1) |
| **MOR** | Wendung | f · s · ş · x | 4 | *fai* (§13.4) · *sarla* (§24.3) · *şirn* (§24.1) · *xerp* (§24.1) |
| **ISH** | Spirale | v · z · j | 3 | *virn* (§24.1) · *zva* (§19) · *j* **unbelegt** |
| **KAI** | Pfad | ç | 1 | *ç* **unbelegt** |
| **RUUN** | Schale | Vokalträger | 1 | *aul*, *eird*, *oñ* (§24.1, §13.1) — vokalisch anlautend |

Rechenprobe: 3 + 2 + 3 + 3 + 4 + 3 + 1 = **19 Konsonanten**, plus RUUN = **20 Kernformen**.
Die Familien gruppieren dabei genau die Lautklassen aus §2.1 (Nasale, Fließlaute,
stimmlose und stimmhafte Verschlusslaute, stimmlose und stimmhafte Reibelaute, Affrikate).

**Unterscheidungsregel.** §26.2 verlangt: „Jede Kernform muss sich von jeder anderen in
**mindestens zwei** Merkmalen unterscheiden." Welche Merkmale gemeint sind (Strichzahl,
Richtung, Öffnung, Höhe …), führt §26 nicht aus; Referenzformen der Zeichen sind in der
Grammatik nicht abgebildet. Das Audit vergibt dafür keine Befund-ID — hier nur
festgehalten, nicht gedeutet. Der Glyphensatz mit Zeichen-IDs und Referenzformen ist ein
Arbeitspaket der noch offenen Manus-Fassung 1.0 (`ROADMAP.md`, Phase F).

**Beobachtung ohne Befund-ID.** Für die Affrikate **ç** (Familie KAI) und den stimmhaften
Reibelaut **j** (Familie ISH) enthält der eingefrorene Wortschatz 0.9.3 **kein einziges
Wort** (281 Grundformen, `language/lexicon/entries/`). Beide Laute sind durch §2.1 und
§3.3 reguläre Bestandteile des Inventars und haben in Manus eigene Kernformen — sie sind
lediglich unbelegt, wie der Diphthong *oi* (§2.3). Siehe `PHONOLOGIE.md` §6.

---

## 4. Der zweite Anfangskonsonant (§26.3)

> **Verkleinertes Beizeichen unter der Kernform, ohne eigenes Vokalzeichen.**

Der zweite Anfangskonsonant ist damit dem Silbenkörper untergeordnet, nicht nebengeordnet:
er trägt keinen eigenen Vokal und bildet keinen eigenen Block. Welche Paare überhaupt
auftreten können, regelt nicht §26, sondern die geschlossene 25er-Liste der Anfangsgruppen
in §5.2 (*tr dr kr gr pr br pl bl fl vl fr vr vn sl şl şr sk st sp xr xl xn zv gl kl*).

§26.3 selbst führt kein Beispiel. Der einzige in §26 ausgeschriebene Silbenblock mit
zweitem Anfangskonsonanten steht in der Coda-Tabelle §26.5:

| Silbe | Kernform | Beizeichen | Vokal | Coda |
|---|---|---|---|---|
| **breun** Haus (§24.1) | b | r | eu (Doppelpunkt) | n |

Weitere §5.2-belegte Anlautgruppen — *xra · xla · xna* (Artikel, §11.1), *vra · vla · vna*
(§11.2), *zva* mit, *kru* auf (§19), *trelm* lang, *vresto* Buch (§24) — sind nach
derselben Formel schreibbar; eine ausgeschriebene Manus-Zerlegung dieser Wörter enthält die
Grammatik nicht.

---

## 5. Vokalpunkte und Diphthongkomposition (§26.4)

### 5.1 Die vier geschriebenen Vokalzeichen

Orbis hat fünf Vokale (§2.2), aber nur **vier Vokalzeichen**: *a* ist inhärent und wird
nicht geschrieben.

| Vokal | Position | Belegte einsilbige Wörter |
|---|---|---|
| **a** | (nicht geschrieben) | *xra* (§11.1) · *zva* (§19) · *xa* (§18.3) |
| **e** | Punkt **vorn** | *mel* (§26.5) · *tel* (§19) · *se* (§13.4) |
| **i** | Punkt **oben** | *vim* (§13.1) · *şlim* (§19) · *zil* (§24.9) |
| **o** | Punkt **hinten** | *moks* (§24.1) · *ro*, *lo*, *no* (§13.1) |
| **u** | Punkt **unten** | *kru* (§19) · *nul* (§19) · *xun* (§19) |

Ein Silbenblock ohne sichtbaren Vokalpunkt ist damit ein *a*-Block — nicht ein Block ohne
Vokal. Vokallose Silben sieht §5.1 nicht vor.

### 5.2 Die Komposition der Diphthonge

Ein Diphthong ist **kein eigenes Zeichen**, sondern eine Zusammensetzung:

> **Zeichen des ersten Vokals + kleiner zweiter Punkt in der Position des zweiten Vokals.**

| Diphthong | Schreibung | Status (§2.3) | Beleg |
|---|---|---|---|
| **ai** | inhärentes *a* + kleiner Punkt **oben** | belegt | *taiv* (§24.1) · *mai* (§16.2) |
| **au** | inhärentes *a* + kleiner Punkt **unten** | belegt | *kaun* (§26.5) · *şaul* (§24.1) |
| **ei** | Punkt vorn + kleiner Punkt **oben** | belegt | *grein*, *eird* (§24.1) |
| **ui** | Punkt unten + kleiner Punkt **oben** | belegt | *luiv*, *luid* (§24.1, §24.7) |
| **eu** | Punkt vorn + kleiner Punkt **unten** | belegt | *breun* (§26.5) |
| **oi** | Punkt hinten + kleiner Punkt **oben** | **schreibbar, derzeit unbelegt** | kein Wort des Lexikons (§2.3) |

Der Größenunterschied zwischen erstem und zweitem Punkt trägt die Lesereihenfolge: *ai* ist
großes *a*-Feld mit kleinem *i*-Punkt, nicht dasselbe wie ein hypothetisches *ia*. Weil die
vier Punktpositionen bereits vorhanden sind, hält §26.4 fest:

> „Das System braucht kein einziges neues Zeichen."

*oi* ist deshalb der praktische Beleg für die Produktivität des Systems: Der Diphthong ist
in Manus vollständig schreibbar, obwohl ihn kein Wort benutzt. §30 hält den Diphthong *ou*
demgegenüber ausdrücklich als **[NOCH ZU ENTSCHEIDEN]** offen — er ist derzeit nicht
Bestandteil des Inventars und darf nicht geschrieben werden.

---

## 6. Ein Endkonsonant (§26.5)

> **Verkleinerte Form des eigenen Konsonantenzeichens, unten rechts an der Silbe, auf der
> Grundlinie anliegend.**

Die Coda benutzt kein eigenes Zeicheninventar: sie ist die verkleinerte Kernform desselben
Konsonanten. Entscheidend ist allein der **Ort**, denn er unterscheidet die Coda vom
zweiten Anfangskonsonanten, der ebenfalls verkleinert ist:

| Zeichen | Ort | Bedeutung |
|---|---|---|
| Beizeichen (§26.3) | unter der **Mitte** | zweiter Anfangskonsonant |
| Coda (§26.5) | unten **rechts** | Endkonsonant |

Die vier ausgeschriebenen Beispiele aus §26.5:

| Silbe | Aufbau | Bedeutung / Fundstelle |
|---|---|---|
| **mel** | m-Kernform + e-Punkt vorn + l-Coda unten rechts | Wurzel *mel-* gehen (§24.5) |
| **kaun** | k-Kernform + au-Doppelpunkt + n-Coda unten rechts | Mensch (§24.1) |
| **breun** | b-Kernform + r-Beizeichen + eu-Doppelpunkt + n-Coda unten rechts | Haus (§24.1) |
| **tel** | t-Kernform + e-Punkt vorn + l-Coda unten rechts | *tel* in (§19) |

---

## 7. Zwei Endkonsonanten (§26.6)

> **Erste Coda unten rechts, zweite daneben, eine Stufe tiefer. Lesereihenfolge links nach
> rechts, oben nach unten.**

Die Staffelung ist damit nicht dekorativ, sondern trägt die Reihenfolge: *ks* und *sk* sind
im Schriftbild unterschieden. Welche Zweiergruppen überhaupt vorkommen dürfen, regelt §5.3
(erster Laut Fließlaut oder Nasal · zweiter Laut *s* · oder die Liste *şn sn sk st*).

| Silbe | Erste Coda | Zweite Coda | Bedeutung / Fundstelle | §5.3-Bedingung |
|---|---|---|---|---|
| **moks** | k | s | Tod (§24.1) | (b) zweiter Laut *s* |
| **virn** | r | n | Leben (§24.1) | (a) erster Laut Fließlaut |
| **xerp** | r | p | Feuer (§24.1) | (a) erster Laut Fließlaut |
| **teln** | l | n | 3 (§24.8) | (a) erster Laut Fließlaut |

Mehr als zwei Codazeichen sieht weder §26.6 noch §5.3 vor.

---

## 8. Coda und Satzabschluss sind zwei Ebenen (§26.7)

### 8.1 Die drei Unterscheidungskriterien

§26.7 trennt das Silbenzeichen von der Satzinterpunktion durch drei gleichzeitig geltende
Kriterien:

| Nr. | Coda | Abschlusszeichen |
|---|---|---|
| 1 | hängt am Silbenkörper | steht **frei** danach |
| 2 | **verkleinert** | **volle Größe** |
| 3 | an oder unter der Grundlinie | auf der Schreiblinie |

Ein Abschlusszeichen kann deshalb nie als dritte Coda missgelesen werden, und eine Coda nie
als Satzende — auch dann nicht, wenn ein Wort auf zwei Konsonanten endet.

### 8.2 Die sechs Abschlusszeichen

| Abschluss | Funktion (§26.7) | Belegter Satztyp der Grammatik |
|---|---|---|
| **weich** | Aussage | *Xra valru milkat xran narkun.* — Der Mann sieht den Hund (§25.1) |
| **gehalten** | Fortsetzung folgt | kein Beispielsatz in der Grammatik |
| **gezogen** | Gegensatz | *Xna breun granz stanat, klas xla kavla zirv vurt.* (§25.1; *klas* aber, §20) |
| **offen** | Frage | *Melaş nunda?* (§18.1) · *Valnaten şevar vin zaubex?* (§25.1) |
| **verwehend** | Möglichkeit, Ungewissheit (entspricht *mai*) | *Vim mai melam.* — Ich würde gehen (§16.2) |
| **gebunden** | Ende, Vollendung | kein Beispielsatz in der Grammatik |

Die Zuordnungen in der rechten Spalte sind **Belege für den Satztyp**, nicht für die
Schreibung: Die Grammatik zeigt keinen Satz in Manus. Ausdrücklich verknüpft §26.7 nur ein
einziges Zeichen mit einer Sprachform, nämlich *verwehend* mit der Möglichkeitspartikel
*mai* (§16.2). Für die übrigen fünf nennt §26.7 Funktionsbezeichnungen ohne
Zuordnungsverfahren und ohne Beispiel; ob etwa jeder Nebensatz mit *klas* das gezogene
Zeichen verlangt, ist ungesagt. Der Manus-Schreibtest führt die sechs Abschlusszeichen als
**in sich vollständig** und vergibt keinen Befund; hier wird die Beobachtung nur
festgehalten, nicht zu einer Regel ausgebaut.

---

## 9. Tastatureingabe (§26.8)

### 9.1 Die Eingaberegel

> Eingabe wie beim koreanischen Hangul: Laute **in Sprechreihenfolge** tippen, das System
> setzt den Silbenblock zusammen.
>
> **Kernkonsonant → zweiter Anfangskonsonant → Vokal → Coda 1 → Coda 2**

Dazu zwei Festlegungen:

- **Ein neuer Kernkonsonant schließt den vorherigen Block ab.**
- **Das Abschlusszeichen liegt auf einer eigenen Taste.**

### 9.2 Die Belegungsrechnung

§26.8 rechnet:

> **20 Konsonantentasten + 4 Vokaltasten + 1 Diphthongtaste + 6 Abschlusstasten = 31 Belegungen.**

### 9.3 [REGELUNKLARHEIT U-10] — „20 Konsonantentasten" ist terminologisch falsch

**Befund-ID: U-10** (`Orbis-Audit-0_1.md` §21 und §A; `Orbis-Manus-Schreibtest-0_1.md`
Abschnitt 4.1). Betrifft §26.8.

Orbis hat **19** Konsonanten (§2.1). Die 20. Kernform ist nach §26.2 der **Vokalträger**
(Familie RUUN) und damit kein Konsonant. §26.8 überträgt die Zahl 20 aus §26.2 auf einen
Begriff, den §26.2 selbst nicht deckt.

| | §26.8 (Wortlaut) | terminologisch korrekt |
|---|---|---|
| Kernformtasten | 20 Konsonantentasten | 19 Konsonantentasten + 1 Vokalträgertaste |
| Vokaltasten | 4 | 4 |
| Diphthongtaste | 1 | 1 |
| Abschlusstasten | 6 | 6 |
| **Summe** | **31** | **31** |

Die **Summe von 31 Belegungen bleibt richtig**; das Audit stuft den Punkt ausdrücklich als
**Dokumentationsfehler, nicht als Systemfehler** ein. Die Korrektur erscheint in einer
künftigen Grammatikversion, nicht durch Änderung der 0.9.3 (`ROADMAP.md`, Phase F). Diese
Dokumentation zitiert den Wortlaut und markiert ihn; sie korrigiert die Grammatik nicht.

**Nicht ausgeführt in §26.8:** wie eine einzige Diphthongtaste die sechs Diphthonge aus
§26.4 erzeugt (jeder Diphthong besteht dort aus Erstvokalzeichen plus kleinem zweitem
Punkt). Das Audit vergibt dafür keine Befund-ID; hier wird nichts ergänzt.

Zur Tastaturplanung insgesamt siehe `TASTATUR.md`.

---

## 10. Schreibregeln und Strichstärke (§26.9)

§26.9 nennt drei Regeln:

| Regel | Wortlaut |
|---|---|
| **Strichstärke** | dünn = Vokal · mittel = Fließlaut und Nasal · dick = Verschlusslaut |
| **Laufrichtung** | Wörter verbunden, Sätze durch Lücken getrennt, links nach rechts |
| **Umschrift und Titel** | Cormorant Garamond, Cinzel für Versalien |

Die Laufrichtungsregel bedeutet: die Wortgrenze ist im Manus-Text **keine** Lücke — die
Lücke markiert die Satzgrenze. Zusammen mit dem freistehenden Abschlusszeichen (§26.7)
ergibt das zwei unabhängige Signale für das Satzende [Folgerung aus §26.9, nicht dort ausgesprochen].

### 10.1 [REGELLÜCKE L-10] — Strichstärke für acht Konsonanten undefiniert

**Befund-ID: L-10** (`Orbis-Audit-0_1.md` §21 und §A; `Orbis-Manus-Schreibtest-0_1.md`
Abschnitt 4.2). Betrifft §26.9.

Die Strichstärkenregel nennt drei Klassen und erfasst damit nur einen Teil des Inventars:

| Strichstärke | Erfasste Laute | Familien (§26.2) | Anzahl |
|---|---|---|---|
| dünn | Vokalzeichen | — (Diakritika) | — |
| mittel | Fließlaute *l r* und Nasale *m n ñ* | TAL, NER | 5 |
| dick | Verschlusslaute *p t k b d g* | SOR, VEL | 6 |
| **nicht definiert** | Reibelaute *f s ş x v z j* und Affrikate *ç* | **MOR, ISH, KAI** | **8** |

**8 der 19 Konsonanten** bleiben ohne Zuordnung — und zwar nicht verstreut, sondern als
drei geschlossene Zeichenfamilien: MOR (4), ISH (3) und KAI (1). Betroffen sind unter
anderem so hochfrequente Zeichen wie *x* (Artikel *xra/xla/xna*, Negation *xa*), *s*, *ş*
(Dativmarker) und *v* (Pronomen *vim*, unbestimmter Artikel *vra/vla/vna*).

Die Lücke ist nicht durch die Klanggruppen von §3.2 schließbar: dort zählen *v z s j* zu
den Fließlauten und *f x ş ç* zu den Härtelauten — eine Zuordnung, die §26.9 nicht
aufgreift und die die Familien MOR und ISH quer durchschneiden würde. Ob die Reibelaute
eine eigene, vierte Strichstärke erhalten, den bestehenden Klassen zugeschlagen werden oder
ob §3.2 maßgeblich sein soll, ist eine **Designerentscheidung** (`ROADMAP.md`, Phase F) und
wird hier nicht getroffen.

---

## 11. [REGELLÜCKE L-09] — es gibt keine Silbifizierungsregel

**Befund-ID: L-09** (`Orbis-Audit-0_1.md` §2.4 und §A, Priorität P2). Betrifft §5 und §26
gemeinsam. Ausführlich zur phonotaktischen Seite: `PHONOTAKTIK.md` §7.

### 11.1 Der Mechanismus

§5.1 legt fest, welche Silben **erlaubt** sind. Nirgends legt die Grammatik fest, wie eine
Lautkette in Silben **zerlegt** wird: es gibt keine Onset-Maximierung, keine
Sonoritätsregel, keine Diphthong-Priorität, keine lexikalisch gespeicherten Silbengrenzen.
Für die Aussprache ist das folgenlos — die Betonungsregel §23 zählt Silben von hinten und
liefert bei *mela* in beiden Zerlegungen dasselbe Ergebnis.

Für Manus ist es nicht folgenlos, weil §26.1 **Silbe für Silbe** schreibt: Jede zulässige
Zerlegung ergibt ein anderes Schriftbild. Nach einem Vokal kann der nächste Konsonant
dreierlei sein — Coda der laufenden Silbe, Kernkonsonant der nächsten Silbe oder (nach
einem weiteren Konsonanten) zweiter Anfangskonsonant.

### 11.2 Die vier Beispielwörter

| Wort | Zerlegungen (alle §5-konform) | Manus-Folge |
|---|---|---|
| **mela** Wanderin (§24.3) | **me·la** oder **mel·a** | m-Kernform + e-Punkt, dann l-Kernform + inhärentes *a* — **oder** m-Kernform + e-Punkt + l-Coda, dann RUUN-Vokalträger mit inhärentem *a* |
| **kavla** Stadt (§24.3) | **kav·la** oder **ka·vla** | *v* als Coda des ersten Blocks — **oder** *v* als Kernform mit *l* als Beizeichen darunter (§26.3) |
| **drovna** Wald (§24.4) | **drov·na** oder **dro·vna** | *v* als Coda — **oder** *v* als Kernform mit *n*-Beizeichen (Anlautgruppe *vn*, §5.2) |
| **vresto** Buch (§24.4) | **vres·to** oder **vre·sto** | zwei Blöcke mit unterschiedlicher Verteilung von *s* und *t*. Eine dritte Lesart *vrest·o* (Vokalträger am Ende) wäre nur mit der Silbenform KKVKK möglich, die §5.1 **nicht** führt — siehe K-01; sie zählt hier nicht mit |

Alle **hier gezählten** Varianten sind nach §5.1 und nach §26 korrekt; Lesarten, die eine in §5.1 nicht geführte Silbenform bräuchten, sind ausgenommen (K-01). Die Grammatik enthält
keinen Satz, der eine davon auszeichnet.

### 11.3 Die Quantifizierung

`Orbis-Manus-Schreibtest-0_1.md` (Phase 8, reproduzierbar mit
`python3 orbis_validator.py --manus`) prüft den gesamten Grundwortschatz:

| Kategorie | Anzahl |
|---|---|
| Grundformen geprüft | 281 |
| eindeutig zerlegbar | 203 |
| **[MANUS-AMBIGUITÄT] mehrdeutig** | **77** |
| nicht zerlegbar (bloße Wurzel *suvr-*, §14-Stütz-e) | 1 |

**77 von 281 Grundformen (27 %) haben mehr als eine regelkonforme Manus-Schreibung.**
Der Anteil steigt bei flektierten Formen weiter, weil jede V-K-V-Folge zweideutig ist. Die
Spannbreite reicht von zwei Zerlegungen (*mela*, *valru*, *kavla*) über drei (*vlaiko*,
*taluma*, *taisa*) und fünf (*klaunuma*, *şauluma*, *saivuma*) bis zu acht Zerlegungen bei
der Zusammensetzung *aulmelna* (Kanal, §21.3).

Ein zweiter, unabhängiger Unsicherheitsfaktor kommt hinzu: Ob *aul*, *eird*, *ain* und *oñ*
überhaupt zerlegbar sind, hängt an **[REGELKONFLIKT K-01]** — §5.1 führt die Silbenformen
VK/VKK/KKVKK nicht, obwohl der Wortschatz sie braucht (`PHONOTAKTIK.md` §3). Der
Schreibtest rechnet deshalb in zwei Regelmengen (**strikt** und **erweitert**); *aul* ist
im erweiterten Modus mehrdeutig (*a·ul* neben *aul*).

### 11.4 Die Folge: kein deterministischer Composer

Solange keine Silbifizierungsregel gilt, gibt es **keine eindeutige Abbildung von der
Standardschreibung auf ein Manus-Schriftbild**. Der Manus-Schreibtest formuliert die Folge
unmissverständlich:

> „Ein deterministischer Manus-Composer ist damit blockiert."

§26.8 löst dieses Problem nicht. Die Regel „Ein neuer Kernkonsonant schließt den vorherigen
Block ab" ordnet die **Eingabereihenfolge** beim Tippen, entscheidet aber nicht die
**Rückübertragung** aus der Lateinschreibung: Dieselbe Buchstabenkette bleibt mehrdeutig.
Ein Programm, das *mela* automatisch in Manus setzen soll, muss zwischen *me·la* und
*mel·a* wählen — und diese Wahl ist keine technische, sondern eine Sprachentscheidung.

**Was hier nicht geschieht.** Es wird keine Präferenz festgelegt, auch keine
naheliegende. Das Repo enthält eine Simulation (`python3 orbis_validator.py --sim-l09`),
die vier Kandidatenstrategien durchrechnet — Onset-Maximierung ohne Diphthong-Vorrang,
Minimal-Onset mit Diphthong-Vorrang, Onset-Maximierung mit Diphthong-Vorrang sowie
lexikalisch gespeicherte Grenzen; der Testbericht nennt zusätzlich die Möglichkeit, freie
Varianz zu erklären und die Schrift mehrdeutig zu lassen. **Diese Simulationen sind
Analysewerkzeuge, keine Sprachregeln, und dürfen nie als Regel zitiert werden.** Welche
Zerlegung gilt — einschließlich der Sonderfälle *suvr-* und der Kompositionsfuge in
*taivbreun* —, entscheiden ausschließlich die Sprachdesigner.

---

## 12. Zusammenfassung des Regelstatus

| Regel | Paragraph | Status |
|---|---|---|
| Silbenformel des Blocks | §26.1 | vollständig, kein Befund |
| 8 Familien, 20 Kernformen = 19 Konsonanten + 1 Vokalträger | §26.2 | vollständig; Merkmalskatalog und Referenzformen nicht ausgeführt |
| Zweiter Anfangskonsonant als Beizeichen | §26.3 | vollständig, kein eigenes Beispiel |
| 4 Vokalzeichen, *a* inhärent, 6 Diphthonge | §26.4 | vollständig, kein Befund; *oi* schreibbar, unbelegt |
| Coda unten rechts, verkleinert | §26.5 | vollständig, kein Befund |
| Zweite Coda daneben, eine Stufe tiefer | §26.6 | vollständig, kein Befund |
| Coda und Abschluss als zwei Ebenen; 6 Abschlusszeichen | §26.7 | vollständig, kein Befund; Zuordnung Satztyp → Zeichen nur für *verwehend* / *mai* benannt |
| Tastatureingabe, 31 Belegungen | §26.8 | **[REGELUNKLARHEIT U-10]** — „20 Konsonantentasten"; Summe 31 bleibt richtig |
| Strichstärke | §26.9 | **[REGELLÜCKE L-10]** — *f s ş x v z j ç* undefiniert (8 von 19) |
| Silbentrennung | — | **[REGELLÜCKE L-09]** — nicht geregelt; 77 von 281 Grundformen mehrdeutig |
| Silbenformen VK/VKK/KKVKK | §5.1 | **[REGELKONFLIKT K-01]** — wirkt auf die Zerlegbarkeit in Manus |
| Spiralregeln von Orbis Magna | §27, §30 | **[NOCH ZU ENTSCHEIDEN]** — siehe `MAGNA.md` |

---

## 13. Querverweise

| Thema | Ort |
|---|---|
| Silbenformen, Anlautgruppen, Coda-Bedingungen, L-09 phonotaktisch | `PHONOTAKTIK.md`, Abschnitt 5 |
| Lautinventar, Klanggruppen, unbelegte Laute *j* und *ç* | `PHONOLOGIE.md` (§2, §3) |
| Betonung und Lautung | `AUSSPRACHE.md` (§23) |
| Feierliche Schriftform | `MAGNA.md` (§27) |
| Stand und Architektur der Tastaturplanung | `TASTATUR.md` (§26.8) |
| Zerlegungstabelle aller 281 Grundformen | `Orbis-Manus-Schreibtest-0_1.md` |
| Befund-IDs L-09, L-10, U-10, K-01 | `Orbis-Audit-0_1.md`, `language/findings/findings.json` |
| Arbeitspakete Manus 1.0 | `ROADMAP.md` (Phase F) |

---

*Quelle aller Regelaussagen: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Bei Abweichung
zwischen dieser Dokumentation und der Grammatik gilt die Grammatik.*
