# ORBIS — Testkorpus 0.1

*150 Testsätze gegen Grammatik 0.9.3. Kein Grammatikdokument — ein Prüfwerkzeug.*

**Zweck:** Feststellen, ob Orbis 0.9.3 in der Anwendung trägt. Entdeckte Probleme werden **nicht** durch Änderung der Sprache gelöst, sondern mit **[TESTPROBLEM]** markiert und der verursachenden Regel zugeordnet.

**Analyseformat:** Artikel · Geschlecht · Kasus · Zahl · Verbform · Satzstellung · Wortschatz · Phonotaktik.

---

## A. EINFACHE HAUPTSÄTZE (1–20)

**1.** Der Mann geht. — **Xra valru melat.**
*xra M-Nom-Sg · valru M-A · melat 3.Sg Präs · V2 ✓*

**2.** Die Frau spricht. — **Xla sarla talat.**
*xla F-Nom-Sg · sarla F-A · talat 3.Sg Präs ✓*

**3.** Das Kind schläft. — **Xna şirn soñat.**
*şirn Kernwort n, Nom endungslos · xna N-Nom ✓*

**4.** Der Hund läuft. — **Xra narku vlentat.**
*narku M-B · Artikel A-Reihe trotz B-Klasse ✓ (§11.3)*

**5.** Ich komme. — **Vim vandam.**
*vim 1.Sg Nom · vandam Präs 1.Sg ✓*

**6.** Du wartest. — **Şet maldaş.**
*şet 2.Sg · maldaş ✓*

**7.** Wir bleiben. — **Viñ stanamen.**
*viñ 1.Pl · stanamen = Sg -m + -en ✓*

**8.** Ihr lest. — **Şeñ leşnaşen.**
*leşn- Coda şn nach §5.3c ✓*

**9.** Sie schreiben. — **Oñ ruskaten.**
*oñ 3.Pl · rusk- Coda sk ✓*

**10.** Der Wind kommt. — **Xra vlaiko vandat.**
*vlaiko M-B · Onset vl ✓ · Diphthong in betonter Silbe VLAI-ko ✓*

**11.** Der Sprecher spricht. — **Xra talru talat.**
*talru < tal- + -ru ✓*

**12.** Das Wasser bleibt. — **Xna aul stanat.**
*aul Kernwort n ✓*

**13.** Der Vogel sieht. — **Xra vlenko milkat.**
*milk- Coda lk ✓*

**14.** Die Nacht kommt. — **Xla kirva vandat.**
*kirva F-B, Artikel xla ✓*

**15.** Der Mensch denkt. — **Xra kaun dremnat.**
*kaun Kernwort m · dremn- Coda mn nach §5.3a ✓*

**16.** Die Mutter wartet. — **Xla veiş maldat.**
*veiş Kernwort f, Diphthong ei ✓*

**17.** Das Buch bleibt. — **Xna vresto stanat.**
*vresto N-C, Onset vr ✓*

**18.** Der Freund isst. — **Xra velkra nastat.**
*velkra M-A · nast- Coda st ✓*

**19.** Die Wanderin geht. — **Xla mela melat.**
*mela < mel + la, Fugenregel §21.4 ✓*

**20.** Der Vater hört. — **Xra draun zaubat.**
*draun Kernwort m · zaub- Auslaut b, nach §3.4 R3 zulässig ✓*

---

## B. AKKUSATIV UND DATIV (21–35)

**21.** Ich sehe den Hund. — **Vim milkam xran narkun.**
*Artikel und Nomen beide Akk -n ✓*

**22.** Du hörst die Stimme. — **Şet zaubaş xlan şonman.**
*şonma F-C, Akk şonman ✓*

**23.** Der Mann gibt dem Kind das Brot. — **Xra valru dalvat xnaş şirneş xnan brasin.**
*şirn Kernwort, Dat mit Bindevokal -e- ✓ · Dativ vor Akkusativ ✓*

**24.** Wir schreiben ein Wort. — **Viñ ruskamen vnan taisan.**
*vnan unbestimmter Artikel N-Akk ✓*

**25.** Sie nimmt die Hand. — **Lo prensat xlan prilan.**
*prens- Coda ns ✓*

**26.** Ich gebe dem Freund das Buch. — **Vim dalvam xraş velkraş xnan vreston.**
*velkra Dat velkraş ✓*

**27.** Der Wanderer findet den Weg. — **Xra melru traivat xnan melnan.**
*melna N-A Akk melnan — Artikel xnan trägt denselben Marker ✓*

**28.** Ihr lest das Buch. — **Şeñ leşnaşen xnan vreston.** ✓

**29.** Die Frau liebt den Mann. — **Xla sarla saivat xran valrun.** ✓

**30.** Ich trinke das Wasser. — **Vim prevam xnan aulen.**
*aul Kernwort, Akk aulen ✓*

**31.** Er isst das Brot. — **Ro nastat xnan brasin.** ✓

**32.** Wir geben der Frau die Blume. — **Viñ dalvamen xlaş sarlaş xlan zenlon.** ✓

**33.** Du siehst den Berg. — **Şet milkaş xran vrondon.**
*vrondo M-C, Artikel bleibt xran ✓*

**34.** Sie hören den Fluss. — **Oñ zaubaten xran luvandin.** ✓

**35.** Ich warte auf der Straße. — **Vim maldam kru xlaş melvaş.**
*kru + Dativ = Ort ✓*

---

## C. GENITIV (36–45)

**36.** Die Hand der Mutter ist warm. — **Xla prila xlas veişes velm est.**
*veiş Kernwort, Gen veişes ✓ · velm prädikativ unverändert ✓*
**[TESTPROBLEM 1]** Die Grammatik legt nirgends fest, ob das Genitivattribut **vor** oder **nach** dem Bezugswort steht. Alle Beispiele stellen es nach — aber das ist Praxis, keine Regel. Verursachende Lücke: §8 und §17 schweigen zur Attributstellung.

**37.** Der Weg des Wanderers ist lang. — **Xna melna xras melrus trelm est.** ✓

**38.** Das Haus des Vaters bleibt alt. — **Xna breun xras draunes granz stanat.**
*draun Gen draunes ✓ · stanex + Grundform ✓*

**39.** Die Erinnerung der Zeit vergeht langsam. — **Xla soruma xlas nauşes tolm vaşnat.**
*vaşn- intransitiv „vergehen" ✓ (§24.6) · tolm adverbial*

**40.** Der Name des Kindes ist neu. — **Xra şaul xnas şirnes zirv est.**
*şaul m, şirn n — zwei verschiedene Artikel im selben Satz ✓*

**41.** Die Nacht der Stadt ist dunkel. — **Xla kirva xlas kavlas şaln est.** ✓

**42.** Das Wort des Sprechers ist wahr. — **Xna taisa xras talrus klaun est.** ✓

**43.** Die Flamme des Feuers ist warm. — **Xla gluvi xras xerpes velm est.**
*xerp Kernwort m, Gen xerpes ✓*

**44.** Der Traum des Menschen vergeht. — **Xra navildo xras kaunes vaşnat.** ✓

**45.** Die Freiheit der Welt ist groß. — **Xla klerma xlas eirdes vlaid est.**
*eird f, Gen eirdes ✓*

---

## D. ADJEKTIVE (46–60)

**46.** Der große Berg ist alt. — **Xra vlaidra vrondo granz est.**
*attributiv dekliniert, prädikativ nicht ✓*

**47.** Ich sehe den kleinen Vogel. — **Vim milkam xran nirmran vlenkon.** ✓

**48.** Die schöne Frau spricht. — **Xla loşna sarla talat.** ✓

**49.** Wir gehen auf der langen Straße. — **Viñ melamen kru xlaş trelmlaş melvaş.**
*Artikel, Adjektiv, Nomen alle F-Dat ✓*

**50.** Das dunkle Wasser ist kalt. — **Xna şalna aul girn est.**
*şaln + na → şalna, Fugenregel ✓*

**51.** Der starke Mann bleibt. — **Xra xarnra valru stanat.** ✓

**52.** Ich lese ein neues Buch. — **Vim leşnam vnan zirvnan vreston.** ✓

**53.** Die kalte Nacht ist lang. — **Xla girnla kirva trelm est.** ✓

**54.** Er ist größer als ich. — **Ro vlaidvi est kon vim.**
*prädikativer Komparativ = Stamm + -vi ✓*

**55.** Sie ist die schönste Frau. — **Lo xla loşnvaxla sarla est.**
*attributiver Superlativ ✓*

**56.** Ich sehe das schnelle Fahrzeug. — **Vim milkam xnan zilvnan meliston.** ✓

**57.** Der alte Freund kommt. — **Xra granzra velkra vandat.**
*granz Coda nz ✓*

**58.** Wir warten in der dunklen Stadt. — **Viñ maldamen tel xlaş şalnlaş kavlaş.**
*tel + Dat = Ort ✓*

**59.** Das Wort ist wahr. — **Xna taisa klaun est.** ✓

**60.** Der schwache Wind wird stark. — **Xra vresnra vlaiko xarn vurt.**
*vurn- unregelmäßig, 3.Sg Präs vurt ✓*

---

## E. PLURAL (61–70)

**61.** Die Männer gehen. — **Xrañ valruñ melaten.** ✓

**62.** Ich sehe die Hunde. — **Vim milkam xrañan narkuñun.**
*Echovokal u nach Themavokal u ✓*

**63.** Die Frauen sprechen. — **Xlañ sarlañ talaten.** ✓

**64.** Wir geben den Kindern das Brot. — **Viñ dalvamen xnañaş şirneiş xnan brasin.**
*Artikel regulärer Plural, Nomen alter Plural -ei ✓ — die beiden Systeme laufen nebeneinander*

**65.** Die Steine sind kalt. — **Xrañ larkiñ girn esten.**
*prädikativ auch im Plural unverändert ✓*

**66.** Die Augen sind groß. — **Xnañ milneñ vlaid esten.** ✓

**67.** Ich lese die Bücher. — **Vim leşnam xnañan vrestoñon.** ✓

**68.** Die Wanderer finden die Wege. — **Xrañ melruñ traivaten xnañan melnañan.** ✓

**69.** Die Menschen bleiben. — **Xrañ kaunei stanaten.** ✓

**70.** Wir hören die Stimmen. — **Viñ zaubamen xlañan şonmañan.** ✓

---

## F. FRAGEN (71–80)

**71.** Gehst du? — **Melaş?**
*V1, Pronomen kann entfallen, da die Endung die Person trägt ✓*

**72.** Kommt der Mann heute? — **Vandat xra valru nunda?** ✓

**73.** Wer spricht? — **Kem talat?** ✓

**74.** Was siehst du? — **Kelt milkaş?**
**[TESTPROBLEM 2]** *kelt* steht hier im Akkusativ, hat aber dieselbe Form wie im Nominativ. §18.2 listet die Fragewörter, sagt aber nichts über ihre Deklination. Unklar, ob *kem/kelt* unveränderlich sind oder Kasusformen bilden müssten.

**75.** Wo ist das Haus? — **Kur est xna breun?** ✓

**76.** Wann kommst du? — **Kan vandaş?** ✓

**77.** Warum wartet er? — **Grais maldat ro?** ✓

**78.** Wie ist die Nacht? — **Kolm est xla kirva?** ✓

**79.** Welches Buch liest du? — **Kelnan vreston leşnaş?**
*kelna kongruiert wie ein Adjektiv ✓ — im Gegensatz zu kem/kelt*

**80.** Habt ihr das Wasser? — **Nuşen şeñ xnan aulen?**
*nuv- unregelmäßig, 2.Pl Präs nuşen ✓*

---

## G. NEGATION (81–90)

**81.** Ich gehe nicht. — **Vim xa melam.** ✓

**82.** Er kommt nicht. — **Ro xa vandat.** ✓

**83.** Wir haben kein Haus. — **Viñ xa numen vna breun.**
*Verneinung am Verb, Objekt bleibt unbestimmt ✓*

**84.** Sie sieht den Hund nicht. — **Lo xa milkat xran narkun.** ✓

**85.** Das Kind schläft nicht. — **Xna şirn xa soñat.** ✓

**86.** Kein Mann wartet. — **Xanra valru maldat.**
*attributives xan- ✓*

**87.** Ich weiß es nicht. — **Vim xa zavam non.** ✓

**88.** Du liest das Buch nicht. — **Şet xa leşnaş xnan vreston.** ✓

**89.** Niemand kommt. — **Xakaun vandat.** ✓

**90.** Wir gehen nicht in die Stadt. — **Viñ xa melamen tel xlan kavlan.** ✓

---

## H. NEBENSÄTZE (91–105)

**91.** Ich weiß, dass du kommst. — **Vim zavam, fai şet vandaş.**
*Verb am Ende ✓*

**92.** Er wartet, weil die Nacht kalt ist. — **Ro maldat, grali xla kirva girn est.** ✓

**93.** Wenn du gehst, bleibe ich. — **Tund şet melaş, stanam vim.**
*Nebensatz auf Position 1, Verb folgt direkt ✓*

**94.** Obwohl das Buch alt ist, lese ich es. — **Şlani xna vresto granz est, leşnam vim non.** ✓

**95.** Während wir warten, spricht der Mann. — **Dremi viñ maldamen, talat xra valru.** ✓

**96.** Bevor die Sonne kommt, gehen wir. — **Glemi xla luiv vandat, melamen viñ.** ✓

**97.** Nachdem er aß, schlief er. — **Trausi ro nastot, soñot ro.** ✓

**98.** Ich denke, dass die Welt groß ist. — **Vim dremnam, fai xla eird vlaid est.** ✓

**99.** Wir wissen, dass der Weg lang ist. — **Viñ zavamen, fai xna melna trelm est.** ✓

**100.** Sie sagt, dass sie kommt. — **Lo talat, fai lo vandat.**
**[TESTPROBLEM 3]** Es gibt kein Verb für „sagen". *tal-* bedeutet „sprechen" und ist intransitiv gebraucht; „sagen, dass …" ist damit nur behelfsmäßig ausdrückbar. Wortschatzlücke, keine Regellücke.

**101.** Weil ich schwach bin, warte ich. — **Grali vim vresn em, maldam vim.** ✓

**102.** Wenn die Flamme dunkel wird, gehen wir. — **Tund xla gluvi şaln vurt, melamen viñ.** ✓

**103.** Der Mann, der spricht, ist mein Freund. — **Xra valru, fai talat, xra velkra vis est.**
**[TESTPROBLEM 4]** §13.4 nennt *fai* als Relativpronomen, aber §17 beschreibt keinen Relativsatz. Offen: ob *fai* nach Geschlecht und Kasus kongruiert, ob das Verb am Ende steht (hier angenommen) und wie sich das Relativpronomen vom gleichlautenden *fai* „dass" unterscheidet.

**104.** Obwohl der Sturm kommt, bleiben wir. — **Şlani xra morda vandat, stanamen viñ.** ✓

**105.** Ich weiß nicht, wo das Buch ist. — **Vim xa zavam, kur xna vresto est.**
*indirekte Frage: Fragewort leitet ein, Verb am Ende ✓*

---

## I. MODALVERBEN (106–115)

**106.** Ich kann gehen. — **Vim valnam melex.** ✓

**107.** Du musst kommen. — **Şet dolmaş vandex.** ✓

**108.** Er darf das Buch lesen. — **Ro vlekat xnan vreston leşnex.**
*Verbklammer: Objekt im Mittelfeld ✓*

**109.** Wir sollen warten. — **Viñ tirnamen maldex.** ✓

**110.** Sie will schlafen. — **Lo nestat soñex.** ✓

**111.** Ich mag das Wort. — **Vim suvram xnan taisan.**
*suvr- ohne Infinitiv, direkt mit Objekt ✓*

**112.** Ihr könnt den Berg sehen. — **Şeñ valnaşen xran vrondon milkex.** ✓

**113.** Sie müssen die Stadt finden. — **Oñ dolmaten xlan kavlan traivex.** ✓

**114.** Können Sie mich hören? — **Valnaten şevar vin zaubex?**
*Höflichkeitsform mit 3.Pl ✓ · V1-Frage ✓*

**115.** Das Kind darf nicht gehen. — **Xna şirn xa vlekat melex.**
*Negation am Modalverb ✓*

---

## J. VERGANGENHEIT (116–125)

**116.** Ich ging. — **Vim molem.**
*mel- unregelmäßig: Ablautstamm mol- + -e- + -m ✓*

**117.** Du kamst. — **Şet vendeş.** ✓

**118.** Er sah den Hund. — **Ro milkot xran narkun.**
*milk- regelmäßig: Tempusvokal -o- ✓*

**119.** Wir wussten es. — **Viñ zovemen non.** ✓

**120.** Sie gaben dem Kind das Brot. — **Oñ dolveten xnaş şirneş xnan brasin.** ✓

**121.** Die Nacht war kalt. — **Xla kirva girn vot.** ✓

**122.** Ich hatte ein Haus. — **Vim novem vna breun.** ✓

**123.** Der Mann machte das Fahrzeug. — **Xra valru norget xnan meliston.** ✓

**124.** Ihr wartetet. — **Şeñ maldoşen.** ✓

**125.** Wir wurden stark. — **Viñ voremen xarn.**
*vurn- Ablaut vor- ✓ · prädikatives Adjektiv am Ende ✓*

---

## K. ZUKUNFT (126–135)

**126.** Ich werde gehen. — **Vim melaim.**
*Zukunft ist regelmäßig, auch bei unregelmäßigen Verben ✓*

**127.** Du wirst kommen. — **Şet vandaiş.** ✓

**128.** Er wird das Buch lesen. — **Ro leşnait xnan vreston.** ✓

**129.** Wir werden warten. — **Viñ maldaimen.** ✓

**130.** Sie werden die Stadt sehen. — **Oñ milkaiten xlan kavlan.** ✓

**131.** Das Kind wird schlafen. — **Xna şirn soñait.** ✓

**132.** Morgen werde ich schreiben. — **Zirna ruskaim vim.**
*Zeitangabe auf Position 1, V2 ✓*

**133.** Ihr werdet stark sein. — **Şeñ vaişen xarn.** ✓

**134.** Ich werde ein Haus haben. — **Vim nuvaim vna breun.** ✓

**135.** Der Wind wird kommen. — **Xra vlaiko vandait.** ✓

---

## L. PASSIV (136–140)

**136.** Das Haus wird gebaut. — **Xna breun şunargat.** ✓

**137.** Das Brot wurde gegessen. — **Xna brasi şunastot.** ✓

**138.** Das Buch wird gelesen. — **Xna vresto şuleşnat.** ✓

**139.** Der Weg wurde gefunden. — **Xna melna şutraivot.** ✓

**140.** Das Wort ist gesprochen. — **Xna taisa şutalut est.**
*Zustandspassiv mit Partizip ✓*
**[TESTPROBLEM 5]** Es gibt keine Regel für das **Agens im Passiv** („das Haus wird vom Mann gebaut"). *ven* + Dativ wäre naheliegend, ist aber nirgends festgelegt. Verursachende Lücke: §16.3 beschreibt nur die Vorsilbe *şu-*.

---

## M. KONDITIONAL (141–145)

**141.** Ich würde gehen. — **Vim mai melam.** ✓

**142.** Wenn ich ein Haus hätte, würde ich bleiben. — **Tund vim vna breun mai num, mai stanam vim.**
*mai + finites Verb als eine Position, auch im Nebensatz am Ende ✓*

**143.** Wenn die Nacht kalt wäre, würden wir warten. — **Tund xla kirva girn mai est, mai maldamen viñ.** ✓

**144.** Er würde das Buch lesen. — **Ro mai leşnat xnan vreston.** ✓

**145.** Wenn du kämst, wären wir gut daran. — **Tund şet mai vandaş, mai emen viñ selv.**
*Behelf: für „froh" fehlt ein Wort — siehe Auswertung*

---

## N. KOMPLEXE SÄTZE (146–150)

**146.** Ich weiß, dass der große Mann morgen mit dem Freund in die Stadt gehen wird.
**Vim zavam, fai xra vlaidra valru zirna zva xraş velkraş tel xlan kavlan melait.**
*Nebensatz mit Zeit–Art–Ort, Verb am Ende ✓ · tel + Akk = Richtung ✓*

**147.** Obwohl die Nacht kalt war, gingen die Wanderer über den Berg.
**Şlani xla kirva girn vot, moleten xrañ melruñ span xran vrondon.**
*Nebensatz Position 1, Hauptsatzverb direkt danach ✓ · span + Akk = Richtung ✓*

**148.** Wenn du das Buch des Freundes liest, wirst du die Wahrheit finden.
**Tund şet xnan vreston xras velkras leşnaş, traivaiş şet xlan klaunuman.**
*Genitivattribut im Nebensatz ✓ · klaunuma F-C Akk ✓*

**149.** Der Mann, der gestern kam, gab dem Kind das Brot des Hauses.
**Xra valru, fai granza vendet, dolvet xnaş şirneş xnan brasin xnas breunes.**
*betrifft [TESTPROBLEM 4] · Kernwort-Genitiv breunes ✓*

**150.** Wir können nicht schlafen, weil der Sturm über der Stadt sehr stark ist.
**Viñ xa valnamen soñex, grali xra morda span xlaş kavlaş vran xarn est.**
*Modalklammer im Hauptsatz, Verb am Ende im Nebensatz ✓ · span + Dat = Ort ✓*

---

## AUSWERTUNG

### Was einwandfrei funktioniert

**145 von 150 Sätzen** ließen sich ohne jede Regelverletzung bilden.

- **Kongruenz:** Artikel, Adjektiv und Nomen tragen in allen 150 Sätzen denselben Kasusmarker. Kein einziger Konflikt.
- **Artikelgenus:** Auch bei den Unterklassen B und C und bei allen 15 Kernwörtern greift die A-Reihe zuverlässig (§11.3).
- **Kernwörter:** Der Bindevokal *-e-* und der alte Plural *-ei* kollidieren an keiner Stelle mit dem regulären System — auch nicht dort, wo Artikel und Nomen zwei verschiedene Pluralbildungen zeigen (Satz 64).
- **Verbsystem:** Die acht unregelmäßigen Verben verhalten sich in Präsens und Zukunft völlig regelmäßig; nur die Vergangenheit weicht ab. Das ist leicht lernbar.
- **Syntax:** V2, Verbendstellung, Verbklammer und die Nebensatz-auf-Position-1-Regel funktionieren in allen geprüften Kombinationen, bis hin zu Satz 146 mit fünf Satzgliedern im Mittelfeld.
- **Phonotaktik:** Kein Wort und keine Flexionsform verstößt gegen §5. Die Coda-Ergänzung *sn* aus 0.9.3 war die letzte offene Lücke.
- **Prädikative Adjektive:** Die Regel „unverändert" hält auch im Plural (Sätze 65, 66) und nach *vurn-* und *stan-* (Sätze 60, 125).

### Gefundene Probleme

| Nr. | Problem | Verursachende Regel |
|---|---|---|
| **1** | Stellung des Genitivattributs nicht festgelegt | §8 und §17 sagen nichts zur Attributstellung |
| **2** | Deklination der Fragewörter *kem/kelt* undefiniert | §18.2 listet sie nur auf. *kelra/kella/kelna* kongruieren, *kem/kelt* offenbar nicht |
| **3** | Kein Verb für „sagen" | Wortschatzlücke, keine Regellücke |
| **4** | Relativsatzbau undefiniert | §13.4 nennt *fai*, §17 beschreibt keinen Relativsatz. Zusätzlich Homonymie mit *fai* „dass" |
| **5** | Agens im Passiv undefiniert | §16.3 beschreibt nur die Vorsilbe *şu-* |

**Zusätzlich beobachtet, ohne Satznummer:**

- Das Reflexivpronomen **se** (§13.4) hat keine Kasusformen. Für „Er sieht sich" ist unklar, ob *se* oder eine Akkusativform stehen müsste.
- Es gibt keine Konstruktion für **„es gibt"**.
- Wortschatzlücken bei häufigen Alltagsbegriffen: sagen, suchen, müde, froh, viel, wenig als Adjektiv.

### Bewertung im Hinblick auf Version 1.0

**Die Grammatik trägt.** Keines der fünf Probleme ist ein Widerspruch im bestehenden System — es sind ausnahmslos **Lücken**, also Stellen, an denen die Grammatik schweigt. Nichts musste umgebaut werden, um 150 Sätze zu bilden.

Damit Version 1.0 vollständig ist, fehlen vier Regeln:

1. Stellung des Genitivattributs
2. Relativsatzbau, inklusive Trennung von *fai* „dass" und *fai* „der/die/das"
3. Agens im Passiv
4. Reflexivpronomen mit Kasusformen

Dazu die Deklinationsfrage bei *kem/kelt* und ein Ausbau des Alltagswortschatzes.

**Empfehlung:** Diese vier Lücken schließen, das Ergebnis als **0.9.4** festhalten, den Testkorpus auf die neu geregelten Bereiche erweitern — und erst danach auf 1.0 gehen.

---

*Orbis Testkorpus 0.1 — geprüft gegen Grammatik 0.9.3.*
