# ORBIS — Wortbildung

*Beschreibt Orbis-Grammatik 0.9.3. Diese Datei ist Dokumentation, nicht die Referenz.*

---

## 1. Drei Verfahren

§21 kennt drei Wege, aus vorhandenem Material neue Wörter zu bilden:

| Verfahren | Ort | Abschnitt |
|---|---|---|
| **Ableitung mit Suffix** — Wortfamilie um eine Wurzel | §21.1 | 2 |
| **Ableitung mit Vorsilbe** | §21.2 | 3 |
| **Zusammensetzung** | §21.3 | 4 |

Über allen dreien steht die **Fugenregel** (§21.4, Abschnitt 5), die regelt, was an der
Nahtstelle zweier Morpheme geschieht.

**Wichtige Einschränkung.** Der Wortschatz ist ab 0.9.3 eingefroren (§24). §21 beschreibt,
wie Wörter gebaut **sind**; dass ein Muster produktiv ist, macht eine selbst gebildete
Form nicht zu einem Wort des Lexikons. Neue Lexeme entstehen nur durch eine Entscheidung
der Sprachdesigner (ORBIS_CONSTITUTION Art. 5, Art. 16). Alle Formen in diesem Kapitel
sind belegt — aus §21, §24 oder dem Testkorpus.

---

## 2. Wortfamilien und ihre Suffixe (§21.1)

Eine Wurzel plus Suffix ergibt ein Wort mit fester Funktion **und** fester Flexionsklasse.
Das Suffix bestimmt beides: die Bedeutungsrolle und die Klasse nach §7.

| Funktion | Suffix | Klasse |
|---|---|---|
| Verb (Infinitiv) | **-ex** | Infinitiv (§14) |
| Person männlich | **-ru** | M-A |
| Person weiblich | **-la** | F-A |
| Ort | **-na** | N-A |
| Werkzeug | **-isto** | N-C |
| Eigenschaft | **-vi** | Adjektiv-Grundform |
| Abstraktum | **-uma** | F-C |

### 2.1 Die beiden belegten Familien

§21.1 führt das Verfahren an genau zwei Wurzeln vollständig vor. Beide sind hier
nebeneinandergestellt; die Zeilen sind die sieben Suffixe der Tabelle oben.

| Suffix | Wurzel *mel-* (gehen) | Wurzel *tal-* (sprechen) |
|---|---|---|
| **-ex** | **melex** — gehen | **talex** — sprechen |
| **-ru** | **melru** — Wanderer (M-A) | **talru** — Sprecher (M-A) |
| **-la** | **mela** — Wanderin (F-A) | **tala** — Sprecherin (F-A) |
| **-na** | **melna** — Weg (N-A) | **talna** — Versammlungsort (N-A) |
| **-isto** | **melisto** — Fahrzeug (N-C) | **talisto** — Instrument (N-C) |
| **-vi** | **melvi** — reiselustig | **talvi** — gesprächig |
| **-uma** | **meluma** — Reise (F-C) | **taluma** — Rede (F-C) |

Beide Zeilen *-la* zeigen die Fugenregel im Kleinen: *mel + la* → **mela**, *tal + la* →
**tala** (§21.4). Die Formen sind also nicht \**mella*, \**talla*.

§21.1 nennt zwei weitere Angehörige der Familien, die nicht dem regelmäßigen Muster
folgen, sondern lautgeschichtlich entstanden sind:

| Wort | Bedeutung | Herleitung laut §21.1 / §22 |
|---|---|---|
| **taiv** | Sprache (Kernwort, f) | \*tal-iv, Diphthongierung durch Vokalverlust (§22, Gesetz 2) |
| **melva** | Straße (F-B) | „alter Ableger von *mel-*" (§21.1) — ohne Lautgesetz-Angabe |

Diese beiden zeigen, dass eine Wortfamilie mehr Mitglieder haben kann als das Suffixraster
hergibt. Ein Bildungsmuster für solche Altformen gibt §21.1 nicht — sie sind Bestand, nicht
Werkzeug.

### 2.2 Das Suffix -uma über die beiden Musterfamilien hinaus

**-uma** ist das einzige Suffix, für das §24.6 einen größeren belegten Bestand ausweist.
Die Spalte „Herkunft" dort zeigt, dass -uma nicht nur an Verbwurzeln tritt:

| Wort | Bedeutung | Basis | Wortart der Basis |
|---|---|---|---|
| **soruma** | Erinnerung | *sor-* bewahren | Verbwurzel |
| **nestuma** | Wille | *nest-* wollen | Modalwurzel |
| **salvuma** | Verlust | *salv-* verlieren | Verbwurzel |
| **vaşnuma** | Vergänglichkeit | *vaşn-* vergehen | Verbwurzel |
| **mirnuma** | Entscheidung | *mirn-* entscheiden | Verbwurzel |
| **tarnuma** | Konsequenz, Folge | *tarn-* folgen | Verbwurzel |
| **saivuma** | Liebe | *saiv-* lieben | Verbwurzel |
| **meluma** | Reise | *mel-* gehen | Verbwurzel |
| **taluma** | Rede | *tal-* sprechen | Verbwurzel |
| **klaunuma** | Wahrheit | *klaun* wahr | Adjektiv (§24.7) |
| **şauluma** | Identität | *şaul* Name | Nomen (Kernwort) |
| **virnuma** | Dasein, Existenz | *virn* Leben | Nomen (Kernwort) |

Alle diese Wörter sind F-C (Klassenkonsonant *m*, Themavokal *a*) und deklinieren regulär
nach §8: *soruma, soruman, sorumaş, sorumas*. Beleg im Satz: *Xla soruma xlas nauşes vran
tolm vaşnat* (§25.1).

Bemerkenswert an *şauluma* und *virnuma*: Die Basis ist ein **Kernwort** mit
unregelmäßiger Deklination (§10.3), die Ableitung ist trotzdem regelmäßig. Das ist
belegter Bestand, keine ausformulierte Regel — §21.1 sagt zur Basiswortart nichts.

### 2.3 Betonung der Ableitungen (§23)

| Fall | Regel | Beispiel §23 |
|---|---|---|
| Normalfall | vorletzte Silbe | *VAL-ru, SAR-la* |
| Wörter auf **-uma** und **-isto** | Betonung bleibt auf dem **Stamm** | **MEL**-uma, **TAL**-isto |
| Wörter mit Vorsilbe | Vorsilbe **unbetont** | şu-**NAR**-gat |
| Zusammensetzungen | erstes Glied | **LUIV**-resto |

Die beiden Suffixe -uma und -isto verhalten sich also betonungsmäßig anders als die
übrigen fünf. §23 gibt die Vorhersagbarkeit der Betonungsregel mit etwa 85 % an.

### 2.4 Verwandtes Bildungsmittel: die Nominalisierung (§12.5)

§12.5 verwendet dieselben Personensuffixe an einer anderen Basis — am **Adjektiv** statt
an der Wurzel — und ergänzt ein drittes für Sachen:

| Bedeutung | Suffix | Klasse | Beispiel §12.5 |
|---|---|---|---|
| männliche Person | **-ru** | M-A | *vlaidru* — der Große |
| weibliche Person | **-la** | F-A | *vlaidla* — die Große |
| Sache oder Begriff | **-te** | N-C | *vlaidte* — das Große |

Beim Partizip verschmilzt *-ut* mit *-te* zu **-ute**: *traivut* → **traivute** „das
Gefundene" (§12.5), belegt im Kurztext: *Kilna est xna traivute.* (§25.2).

---

## 3. Vorsilben (§21.2)

Fünf Vorsilben, jede mit genau einem belegten Beispiel:

| Vorsilbe | Bedeutung | Beispiel §21.2 | Zerlegung |
|---|---|---|---|
| **şu-** | Passiv | *şunargat* | şu- + *narg-* (machen) + -a- + -t (3. Sg Präs) |
| **xa-** | Gegenteil, Fehlen | *xaselvra* | xa- + *selv* (gut) + -ra (attributiv M, §12.1) |
| **re-** | wieder | *revandat* | re- + *vand-* (kommen) + -a- + -t |
| **dra-** | ganz, hindurch | *dramilkat* | dra- + *milk-* (sehen) + -a- + -t |
| **su-** | halb | *suluidra* | su- + *luid* (hell) + -ra |

Die Beispiele der Grammatik stehen in **flektierter Form**, nicht als Wörterbuchform.
Sie zeigen damit zugleich, dass die Vorsilbe **vor** dem gesamten flektierten Wort steht
und Konjugation wie Deklination unberührt lässt.

### 3.1 şu- und das Passiv (§16.3)

*şu-* ist die einzige Vorsilbe mit einer eigenen grammatischen Funktion außerhalb von §21:

| Form | Beleg | Übersetzung |
|---|---|---|
| Vorgangspassiv | *Xna breun şunargat.* (§16.3; Testkorpus 136) | Das Haus wird gebaut. |
| Zustandspassiv | *Xna breun şunargut est.* (§16.3) | Das Haus ist gebaut. |

> **[REGELLÜCKE L-05] — angrenzend.** §16.3 regelt nur die Vorsilbe. Wie das **Agens**
> ausgedrückt wird („vom Mann gebaut"), ist nicht festgelegt; keine Präposition aus §19 ist
> dafür ausgewiesen. Testkorpus 137 und 138 scheitern daran. Das ist ein Befund der
> Modalität/Passiv-Regel, nicht der Wortbildung — hier nur erwähnt, weil er an *şu-* hängt.

### 3.2 Abgrenzungen

| Paar | Verhältnis | Quelle |
|---|---|---|
| **dra-** (Vorsilbe) ↔ **dral** (Präposition „durch") | ausdrücklich **getrennte Kategorien**; *dral* ist nur Präposition, *dra-* nur Vorsilbe | §19 |
| **xa-** (Vorsilbe) ↔ **xa** (Negationspartikel „nicht") | formgleich, aber unterschiedliche Kategorie; registriert als Kollision **W-03** | §18.3, §21.2 |

Die Vorsilbe *xa-* ist über §21.2 hinaus in Wörtern des festen Bestands sichtbar:
*xakaun* (niemand), *xakelte* (nichts) in §13.4, *xanur* (nie) in §24.9. Diese Wörter sind
Lexikoneinträge, keine ad hoc gebildeten Formen.

---

## 4. Zusammensetzungen (§21.3)

> **Bestimmungswort vorn, Grundwort hinten. Geschlecht und Klasse richten sich nach dem
> letzten Glied.**

Der Kopf steht rechts. Das linke Glied verändert seine Form nicht und wird nicht
flektiert; dekliniert wird nur der Kopf.

| Kompositum | Zerlegung | Kopf | Geschlecht/Klasse | Bedeutung |
|---|---|---|---|---|
| **taivbreun** | *taiv* + *breun* | breun (Kernwort, n) | n — Klasse siehe U-08 | Schule |
| **aulmelna** | *aul* + *melna* | melna (N-A) | n, N-A | Kanal |
| **luivresto** | *luiv* + *vresto* | vresto (N-C) | n, N-C | Kalender |

*luivresto* zeigt zusätzlich die Fugenregel: *luiv + vresto* → **luivresto**, nicht
\**luivvresto* (§21.4).

Die Betonung liegt auf dem ersten Glied: **LUIV**-resto (§23).

### 4.1 [REGELUNKLARHEIT U-08] — Komposita mit Kernwort als Kopf

> **[REGELUNKLARHEIT U-08] Wie dekliniert ein Kompositum mit Kernwort-Kopf?**
> §21.3 sagt, „Geschlecht und Klasse" richten sich nach dem letzten Glied. Die 15
> Kernwörter (§10.2–§10.3) **haben** aber keine Klasse im Sinne von §7 — sie deklinieren
> mit Bindevokal *-e-* und bilden den Plural auf *-ei*. Ob *taivbreun* (Kopf: *breun*)
> deshalb wie ein Kernwort dekliniert (\**taivbreunen, taivbreunei*) oder regulär, sagt
> §21.3 nicht.

*aulmelna* und *luivresto* sind davon nicht betroffen: Ihre Köpfe *melna* und *vresto*
sind reguläre Nomen mit Klasse und Themavokal.

---

## 5. Die Fugenregel (§21.4)

> **Treffen an einer Morphemfuge zwei identische Konsonanten aufeinander, verschmelzen sie
> zu einem.** Das gilt für **Zusammensetzungen, Ableitungen und Endungen gleichermaßen.**

| Fuge | Ergebnis | Bereich |
|---|---|---|
| *luiv + vresto* | **luivresto** | Zusammensetzung |
| *mel + la* | **mela** | Ableitung (Suffix -la) |
| *tal + la* | **tala** | Ableitung (Suffix -la) |
| *şaln + na* | **şalna** | Endung (Adjektiv attributiv, §12.1) |
| *selv + vi* | **selvi** | Steigerung/Eigenschaft (§12.3, §21.1) |

Die Regel ist eng gefasst: Sie gilt **nur für identische Konsonanten**. Unterschiedliche
Konsonanten an der Fuge bleiben erhalten, sofern §5.2 und §5.3 sie zulassen (§21.4).
Vokale nennt die Regel nicht.

### 5.1 [REGELKONFLIKT K-02] — killa, dolla, kella

> **[REGELKONFLIKT K-02] Belegte Pronomenformen widersprechen der Fugenregel.**
> §13.4 führt **killa** (diese, f) und **dolla** (jene, f), §18.2 führt **kella / kellan**
> (welche) — jeweils mit unverschmolzener *l+l*-Fuge. Nach §21.4, die ausdrücklich auch für
> Endungen gilt, müssten die Formen *kila*, *dola*, *kela* lauten. Entweder sind die
> Pronomen Ausnahmen — das steht nirgends — oder die Formen sind falsch.

Belegt ist der Konflikt auch im Satz: *Kellan sarlan milkoş?* („Welche Frau hast du
gesehen?", §18.2). Die maskulinen und neutralen Formen (*kilra, kilna, dolra, dolna,
kelra, kelna*) sind nicht betroffen. Ausführlich in `PRONOMEN.md` §5.6.

### 5.2 [REGELKONFLIKT K-03] — telnxelmmern

> **[REGELKONFLIKT K-03] Die Zahl 35 widerspricht der Fugenregel.**
> §24.8 notiert 35 als **telnxelmmern** — zusammengesetzt aus *teln* (3), *xelm* (10) und
> *mern* (5), mit Doppel-*m* an der Fuge *xelm + mern*. Nach §21.4 müsste die Form
> *telnxelmern* lauten.

Die übrigen belegten Zahlkomposita sind unauffällig, weil an ihren Fugen keine identischen
Konsonanten zusammentreffen: *xelmnel* (11, *xelm + nel*), *dramxelm* (20, *dram + xelm*).

K-02 und K-03 sind derselbe Konflikttyp: **ein belegtes Wort gegen eine allgemein
formulierte Regel.** Da der Wortschatz eingefroren (§24) und die Grammatik READ ONLY ist,
bleiben beide offen; entschieden wird durch die Sprachdesigner, nicht durch Auslegung
(ORBIS_CONSTITUTION Art. 16, Art. 17).

Im maschinenlesbaren Lexikon sind die betroffenen Einträge markiert: *killa*, *dolla* und
*kella* tragen `K-02`, *telnxelmmern* trägt `K-03` im Feld `qualitaet.offene_befunde`.

---

## 6. Neue Wörter entstehen nicht hier (§22)

§22 beschreibt für den Fall, dass Sprachdesigner ein neues Wort beschließen, den Weg über
Proto-Orbis: Proto-Form ansetzen → Lautgesetze anwenden → Prüfung gegen §3.3 (verbindliche
Klangregeln) → Abgleich mit §3.4 (Klangrichtlinien). Die sieben Lautgesetze (§22) sind
ausdrücklich **Sprachgeschichte** (§4.3), keine Aussprachehinweise und kein
Wortbildungsverfahren der Gegenwartssprache.

Für Werkzeuge und Dokumentation gilt: Wortbildungsmuster werden beschrieben, nicht
angewendet. Die einzige Wortschatzlücke, die im Bestand registriert ist — **W-01**
(„sagen", „zeigen", „suchen", Existenzkonstruktion „es gibt") — bleibt offen und wird
nicht durch selbst gebildete Ableitungen geschlossen.

---

## 7. Befundübersicht zu diesem Kapitel

| ID | Typ | Betrifft | Kurzfassung |
|---|---|---|---|
| **K-02** | REGELKONFLIKT | §13.4, §18.2 ↔ §21.4 | *killa/dolla/kella* mit unverschmolzener l+l-Fuge |
| **K-03** | REGELKONFLIKT | §24.8 ↔ §21.4 | *telnxelmmern* mit m+m-Fuge |
| **U-08** | REGELUNKLARHEIT | §21.3 | Deklination von Komposita mit Kernwort-Kopf (*taivbreun*) |
| **L-05** | REGELLÜCKE | §16.3 | Agens im Passiv (angrenzend an die Vorsilbe *şu-*) |
| **W-01** | WORTSCHATZLÜCKE | §24 | „sagen", „zeigen", „suchen", „es gibt" fehlen |
| **W-03** | WORTSCHATZKOLLISION | §18.3, §21.2 | *xa* (Partikel) ↔ *xa-* (Vorsilbe) |

Die Suffix- und Vorsilbenlisten selbst (§21.1, §21.2) sind im Audit **ohne Befund**
geführt; die Konflikte liegen an den Fugen und an einzelnen belegten Wörtern.
