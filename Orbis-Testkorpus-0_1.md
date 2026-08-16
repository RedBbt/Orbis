# ORBIS — Testkorpus 0.1 (Prüffassung)

*150 Testsätze gegen die eingefrorene Referenzgrammatik `Orbis-Grammatik-0.9.3.md`. Die Grammatik wurde nicht verändert. Diese Prüffassung ersetzt den Chat-Entwurf `Orbis-Testkorpus-0.1.md` (der als Referenz erhalten bleibt) und korrigiert dort gefundene Fehler (u. a. Satz 48: \*loşna → loşnla).*

**Ergebniswerte:** [OK] · [TESTPROBLEM] · [REGELLÜCKE] · [REGELKONFLIKT] · [REGELUNKLARHEIT]

**Zählkonvention:** Ein offener Punkt der Grammatik wird als Ergebnis-Marker bei den Tests gezählt, die ihn **gezielt prüfen** (dort steht der Satz ausdrücklich als „nicht eindeutig bildbar" oder „nicht eindeutig entscheidbar"). Tests, die dieselbe offene Stelle nur **berühren**, aber der einheitlichen Beispielpraxis der Grammatik folgen (z. B. nachgestelltes Genitivattribut), erhalten [OK] mit Verweis auf die Befund-ID. Die Statistik misst so die Zahl der offenen Stellen, nicht die Häufigkeit ihrer Berührung. Befund-IDs (K-xx/L-xx/U-xx): siehe `Orbis-Audit-0_1.md` §A.

**Hinweis K-01:** Formen wie *est, em, granz, trelm, aul, eird* sind vom Silbenformen-Konflikt K-01 (§5.1) betroffen. Das ist ein zentraler Befund der Grammatik, kein Fehler einzelner Sätze; die Phonotaktik-Zeile vermerkt ihn als „K-01 (…)", das Ergebnis bleibt davon unberührt.

**Verteilung:** A 001–020 einfache Hauptsätze · B 021–035 Akkusativ/Dativ (inkl. Reflexiv-Stresstests) · C 036–045 Genitiv · D 046–060 Adjektive · E 061–070 Plural · F 071–080 Fragen · G 081–090 Negation · H 091–105 Nebensätze (inkl. Relativ- und Modal-Stresstests) · I 106–115 Modalverben · J 116–125 Vergangenheit · K 126–135 Zukunft · L 136–140 Passiv · M 141–145 mai/Konditional · N 146–150 komplex. Anhang: 45-Endungen-Prüftabelle [TESTFORM] und Verbparadigmen.

**Automatische Prüfung:** Jede Orbis-Zeile wurde mit `orbis_validator.py --corpus Orbis-Testkorpus-0_1.md` geprüft (Lexik, Morphologie, Phonotaktik, NP-Kongruenz, Präposition→Kasus). Nicht algorithmisch entscheidbar und daher manuell geprüft (MANUELLE_PRÜFUNG): V2-Stellung, Verbklammer, Nebensatz-Endstellung, Kongruenz über Distanz, Semantik.

---

## A. EINFACHE HAUPTSÄTZE (001–020)

## Test 001
Deutsch:
Der Mann geht.
Orbis:
Xra valru melat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xra valru
- Verb: melat (mel-, unregelm., Präsens regulär)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart (-a-)
- Nomen: valru (Mann)
- Artikel: xra (best., M, Nom Sg)
- Geschlecht: M (M-A)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓ (§17.1)
- Phonotaktik: §5-konform
- verwendete Regeln: §7, §8, §11, §14, §15, §17.1
- Ergebnis: [OK]

## Test 002
Deutsch:
Die Frau spricht.
Orbis:
Xla sarla talat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xla sarla
- Verb: talat (tal-, regelmäßig)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: sarla (Frau)
- Artikel: xla (best., F, Nom Sg)
- Geschlecht: F (F-A)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §7, §11, §14, §15, §17.1
- Ergebnis: [OK]

## Test 003
Deutsch:
Das Kind schläft.
Orbis:
Xna şirn soñat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xna şirn
- Verb: soñat (soñ-, regelmäßig)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: şirn (Kind, Kernwort)
- Artikel: xna (best., N, Nom Sg)
- Geschlecht: N (Kernwort, Wörterbuchgeschlecht §11.3)
- Kasus: Nom (Kernwort Nom endungslos §10.3)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (şirn KVKK)
- verwendete Regeln: §10.2–10.3, §11.3, §14, §17.1
- Ergebnis: [OK]

## Test 004
Deutsch:
Der Hund läuft.
Orbis:
Xra narku vlentat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xra narku
- Verb: vlentat (vlent-, regelmäßig)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: narku (Hund)
- Artikel: xra (best., M, Nom Sg)
- Geschlecht: M (M-B; Artikel zeigt nur Geschlecht, §11.3)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (Wurzel vlent- selbst → K-01 KKVKK; die flektierte Form vlen-tat ist unauffällig)
- verwendete Regeln: §7, §11, §14, §17.1
- Ergebnis: [OK]

## Test 005
Deutsch:
Ich komme.
Orbis:
Vim vandam.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: vim
- Verb: vandam (vand-, unregelm., Präsens regulär)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom (Pronomen)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §13.1, §14, §15.2, §17.1
- Ergebnis: [OK]

## Test 006
Deutsch:
Du wartest.
Orbis:
Şet maldaş.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: şet
- Verb: maldaş (mald-, regelmäßig)
- Person/Numerus: 2. Sg (-ş)
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom (Pronomen)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (mald- Coda ld §5.3a)
- verwendete Regeln: §13.1, §14, §17.1
- Ergebnis: [OK]

## Test 007
Deutsch:
Wir bleiben.
Orbis:
Viñ stanamen.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: viñ
- Verb: stanamen (stan-, regelmäßig)
- Person/Numerus: 1. Pl (-men)
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom (Pronomen)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (st- Onset §5.2)
- verwendete Regeln: §13.1, §14, §17.1
- Ergebnis: [OK]

## Test 008
Deutsch:
Ihr lest.
Orbis:
Şeñ leşnaşen.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: şeñ
- Verb: leşnaşen (leşn-, regelmäßig)
- Person/Numerus: 2. Pl (-şen)
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom (Pronomen)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (leşn- Coda şn §5.3c)
- verwendete Regeln: §13.1, §14, §17.1
- Ergebnis: [OK]

## Test 009
Deutsch:
Sie schreiben.
Orbis:
Oñ ruskaten.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: oñ
- Verb: ruskaten (rusk-, regelmäßig)
- Person/Numerus: 3. Pl (-ten)
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom (Pronomen)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: oñ → K-01 (VK); ruskaten §5-konform (sk §5.3c/rus-ka-ten)
- verwendete Regeln: §13.1, §14, §17.1
- Ergebnis: [OK]

## Test 010
Deutsch:
Der Wind kommt.
Orbis:
Xra vlaiko vandat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xra vlaiko
- Verb: vandat (vand-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: vlaiko (Wind)
- Artikel: xra (best., M, Nom Sg)
- Geschlecht: M (M-B)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (vl- Onset, ai Diphthong)
- verwendete Regeln: §2.3, §5.2, §7, §11, §14, §17.1
- Ergebnis: [OK]

## Test 011
Deutsch:
Der Sprecher spricht.
Orbis:
Xra talru talat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xra talru
- Verb: talat (tal-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: talru (Sprecher; Ableitung tal- + -ru §21.1)
- Artikel: xra (best., M, Nom Sg)
- Geschlecht: M (M-A)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §7, §11, §14, §17.1, §21.1
- Ergebnis: [OK]

## Test 012
Deutsch:
Das Wasser bleibt.
Orbis:
Xna aul stanat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xna aul
- Verb: stanat (stan-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: aul (Wasser, Kernwort)
- Artikel: xna (best., N, Nom Sg)
- Geschlecht: N (Kernwort)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: K-01 (aul = VK — Silbenform fehlt in §5.1)
- verwendete Regeln: §10.2, §11.3, §14, §17.1
- Ergebnis: [OK]

## Test 013
Deutsch:
Der Vogel sieht.
Orbis:
Xra vlenko milkat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xra vlenko
- Verb: milkat (milk-, regelmäßig)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: vlenko (Vogel)
- Artikel: xra (best., M, Nom Sg)
- Geschlecht: M (M-B)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (vlen-ko; milk- Coda lk §5.3a)
- verwendete Regeln: §7, §11, §14, §17.1
- Ergebnis: [OK]

## Test 014
Deutsch:
Die Nacht kommt.
Orbis:
Xla kirva vandat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xla kirva
- Verb: vandat (vand-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: kirva (Nacht)
- Artikel: xla (best., F, Nom Sg)
- Geschlecht: F (F-B)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (kir-va)
- verwendete Regeln: §7, §11, §14, §17.1
- Ergebnis: [OK]

## Test 015
Deutsch:
Der Mensch denkt.
Orbis:
Xra kaun dremnat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xra kaun
- Verb: dremnat (dremn-, regelmäßig)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: kaun (Mensch, Kernwort; Homonymie mit kaun „man" §13.4 — hier durch Artikel eindeutig)
- Artikel: xra (best., M, Nom Sg)
- Geschlecht: M (Kernwort)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (drem-nat; Wurzel dremn- selbst → K-01 KKVKK)
- verwendete Regeln: §10.2, §11.3, §14, §17.1
- Ergebnis: [OK]

## Test 016
Deutsch:
Die Mutter wartet.
Orbis:
Xla veiş maldat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xla veiş
- Verb: maldat (mald-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: veiş (Mutter, Kernwort)
- Artikel: xla (best., F, Nom Sg)
- Geschlecht: F (Kernwort)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (veiş KVK mit ei)
- verwendete Regeln: §10.2, §11.3, §14, §17.1
- Ergebnis: [OK]

## Test 017
Deutsch:
Das Buch bleibt.
Orbis:
Xna vresto stanat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xna vresto
- Verb: stanat (stan-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: vresto (Buch)
- Artikel: xna (best., N, Nom Sg)
- Geschlecht: N (N-C)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (vres-to / vre-sto — Zerlegung mehrdeutig, L-09; Wort selbst zulässig)
- verwendete Regeln: §7, §11, §14, §17.1
- Ergebnis: [OK]

## Test 018
Deutsch:
Der Freund isst.
Orbis:
Xra velkra nastat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xra velkra
- Verb: nastat (nast-, regelmäßig)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: velkra (Freund)
- Artikel: xra (best., M, Nom Sg)
- Geschlecht: M (M-A)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (vel-kra; nast- Coda st §5.3c)
- verwendete Regeln: §7, §11, §14, §17.1
- Ergebnis: [OK]

## Test 019
Deutsch:
Die Wanderin geht.
Orbis:
Xla mela melat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xla mela
- Verb: melat (mel-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: mela (Wanderin; mel- + -la → Fugenregel §21.4: l+l verschmilzt zu mela)
- Artikel: xla (best., F, Nom Sg)
- Geschlecht: F (F-A)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §7, §11, §14, §17.1, §21.1, §21.4
- Ergebnis: [OK]

## Test 020
Deutsch:
Der Vater hört.
Orbis:
Xra draun zaubat.
Analyse:
- Satztyp: Hauptsatz, Aussage
- Subjekt: xra draun
- Verb: zaubat (zaub-, regelmäßig)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: draun (Vater, Kernwort)
- Artikel: xra (best., M, Nom Sg)
- Geschlecht: M (Kernwort)
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (draun KKVK mit au)
- verwendete Regeln: §10.2, §11.3, §14, §17.1
- Ergebnis: [OK]

---

## B. AKKUSATIV- / DATIV-KONSTRUKTIONEN (021–035)

## Test 021
Deutsch:
Ich sehe den Hund.
Orbis:
Vim milkam xran narkun.
Analyse:
- Satztyp: Hauptsatz, transitiv
- Subjekt: vim
- Verb: milkam (milk-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: narku
- Artikel: xran (best., M, Akk Sg)
- Geschlecht: M
- Kasus: Nom (vim), Akk (xran narkun, Marker -n §8)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓, Objekt im Feld
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §14, §17.1
- Ergebnis: [OK]

## Test 022
Deutsch:
Du siehst dich.
Orbis:
Şet milkaş şen.
Analyse:
- Satztyp: Hauptsatz, reflexiv (2. Person)
- Subjekt: şet
- Verb: milkaş (milk-)
- Person/Numerus: 2. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom + Akk (şen = Personalpronomen 2. Sg Akk §13.1)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §13.1, §14, §17.1
- Anmerkung: Reflexivität der 1./2. Person über das Personalpronomen (deutsches Modell, §1 „Satzbau folgt eng dem Deutschen"); ob se auch hier gelten soll, ist Teil von L-04. Formal bildbar.
- Ergebnis: [OK]

## Test 023
Deutsch:
Die Mutter gibt dem Kind das Brot.
Orbis:
Xla veiş dalvat xnaş şirneş xnan brasin.
Analyse:
- Satztyp: Hauptsatz, Doppelobjekt (Stresstest G: Nom + Dat + Akk)
- Subjekt: xla veiş
- Verb: dalvat (dalv-, unregelm., Präsens regulär)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: veiş (Kernwort), şirn (Kernwort), brasi
- Artikel: xla (F Nom), xnaş (N Dat), xnan (N Akk)
- Geschlecht: F / N / N
- Kasus: Nom + Dat (şirneş, Bindevokal -e- §10.3) + Akk (brasin)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓; Dat vor Akk nach Beispielpraxis (U-05, ungeregelt)
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §10.3, §11, §14, §17.1; strukturgleich mit dem §25.1-Beispiel (das dort im Präteritum dolvet steht, hier korrekt Präsens dalvat)
- Ergebnis: [OK]

## Test 024
Deutsch:
Wir schreiben ein Wort.
Orbis:
Viñ ruskamen vnan taisan.
Analyse:
- Satztyp: Hauptsatz, transitiv
- Subjekt: viñ
- Verb: ruskamen (rusk-)
- Person/Numerus: 1. Pl
- Tempus: Gegenwart
- Nomen: taisa (Wort)
- Artikel: vnan (unbest., N, Akk Sg)
- Geschlecht: N (N-B)
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (tai-san)
- verwendete Regeln: §8, §11.2, §14, §17.1
- Ergebnis: [OK]

## Test 025
Deutsch:
Die Frau gibt dem Vater das Wasser.
Orbis:
Xla sarla dalvat xraş drauneş xnan aulen.
Analyse:
- Satztyp: Hauptsatz, Doppelobjekt (Stresstest G; Kernwörter oblique)
- Subjekt: xla sarla
- Verb: dalvat (dalv-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: sarla, draun (Kernwort), aul (Kernwort)
- Artikel: xla (F Nom), xraş (M Dat), xnan (N Akk)
- Geschlecht: F / M / N
- Kasus: Nom + Dat (drauneş, -e- §10.3) + Akk (aulen)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓; Dat vor Akk (U-05)
- Phonotaktik: K-01 (aulen: au-len unauffällig; Nom aul wäre VK); sonst §5-konform
- verwendete Regeln: §8, §10.3, §11, §14, §17.1
- Ergebnis: [OK]

## Test 026
Deutsch:
Ich gebe dem Freund das Buch.
Orbis:
Vim dalvam xraş velkraş xnan vreston.
Analyse:
- Satztyp: Hauptsatz, Doppelobjekt
- Subjekt: vim
- Verb: dalvam (dalv-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: velkra, vresto
- Artikel: xraş (M Dat), xnan (N Akk)
- Geschlecht: M / N
- Kasus: Dat (velkraş) + Akk (vreston)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓; Dat vor Akk (U-05)
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §14, §17.1
- Ergebnis: [OK]

## Test 027
Deutsch:
Ich trinke das Wasser.
Orbis:
Vim prevam xnan aulen.
Analyse:
- Satztyp: Hauptsatz, transitiv (Stresstest H: Kernwort oblique)
- Subjekt: vim
- Verb: prevam (prev-, regelmäßig)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: aul (Kernwort)
- Artikel: xnan (best., N, Akk Sg)
- Geschlecht: N
- Kasus: Akk (aulen = aul + -e- + -n §10.3)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (au-len)
- verwendete Regeln: §8, §10.3, §11, §14, §17.1
- Ergebnis: [OK]

## Test 028
Deutsch:
Ich weiß den Namen.
Orbis:
Vim zavam xran şaulen.
Analyse:
- Satztyp: Hauptsatz, transitiv (Kernwort şaul oblique)
- Subjekt: vim
- Verb: zavam (zav-, unregelm., Präsens regulär)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: şaul (Name, Kernwort)
- Artikel: xran (best., M, Akk Sg)
- Geschlecht: M
- Kasus: Akk (şaulen)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (şau-len)
- verwendete Regeln: §8, §10.3, §11, §15.2, §17.1
- Ergebnis: [OK]

## Test 029
Deutsch:
Sie liebt die Sprache.
Orbis:
Lo saivat xlan taiven.
Analyse:
- Satztyp: Hauptsatz, transitiv (Kernwort taiv oblique)
- Subjekt: lo
- Verb: saivat (saiv-, regelmäßig)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: taiv (Sprache, Kernwort)
- Artikel: xlan (best., F, Akk Sg)
- Geschlecht: F
- Kasus: Akk (taiven)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (tai-ven)
- verwendete Regeln: §8, §10.3, §11, §14, §17.1
- Ergebnis: [OK]

## Test 030
Deutsch:
Wir sehen die Sonne.
Orbis:
Viñ milkamen xlan luiven.
Analyse:
- Satztyp: Hauptsatz, transitiv (Kernwort luiv oblique)
- Subjekt: viñ
- Verb: milkamen (milk-)
- Person/Numerus: 1. Pl
- Tempus: Gegenwart
- Nomen: luiv (Sonne, Kernwort)
- Artikel: xlan (best., F, Akk Sg)
- Geschlecht: F
- Kasus: Akk (luiven)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (lui-ven, ui Diphthong)
- verwendete Regeln: §2.3, §8, §10.3, §11, §14, §17.1
- Ergebnis: [OK]

## Test 031
Deutsch:
Ich warte auf der Straße.
Orbis:
Vim maldam kru xlaş melvaş.
Analyse:
- Satztyp: Hauptsatz mit Ortsangabe
- Subjekt: vim
- Verb: maldam (mald-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: melva (Straße)
- Artikel: xlaş (best., F, Dat Sg)
- Geschlecht: F (F-B)
- Kasus: Dat (Ort, kein Richtungswechsel → Dativ §19)
- Adjektive: —
- Präpositionen: kru (auf, Dat=Ort/Akk=Richtung)
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (mel-vaş)
- verwendete Regeln: §8, §11, §14, §17.1, §19
- Ergebnis: [OK]

## Test 032
Deutsch:
Ich sehe mich.
Orbis:
Vim milkam vin.
Analyse:
- Satztyp: Hauptsatz, reflexiv (1. Person; Stresstest D)
- Subjekt: vim
- Verb: milkam (milk-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom + Akk (vin = 1. Sg Akk §13.1)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §13.1, §14, §17.1
- Anmerkung: Formal bildbar über das Personalpronomen. Ob 1./2. Person stattdessen se verwenden sollen, regelt §13.4 nicht — Personenbereich von se ist Teil von L-04.
- Ergebnis: [OK]

## Test 033
Deutsch:
Er sieht sich.
Orbis:
— nicht eindeutig bildbar: Ro milkat se(?) — se hat keine Kasusformen; *sen ist nirgends definiert. Ro milkat ron hieße „er sieht ihn (einen anderen)".
Analyse:
- Satztyp: Hauptsatz, reflexiv (3. Person; Stresstest D)
- Subjekt: ro
- Verb: milkat (milk-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: benötigt Akk des Reflexivs — nicht definiert
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 wäre erfüllbar
- Phonotaktik: unkritisch
- verwendete Regeln: §13.1, §13.4 (se ohne Formen), §14, §17.1
- Befund: L-04 — se ist ohne Kasusformen gelistet; ob es indeklinabel als Akk/Dat dienen kann, ist nicht gesagt. NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 034
Deutsch:
Ich gebe mir Zeit.
Orbis:
Vim dalvam viş xlan nauşen.
Analyse:
- Satztyp: Hauptsatz, reflexives Dativobjekt (1. Person; Stresstest D)
- Subjekt: vim
- Verb: dalvam (dalv-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: nauş (Zeit, Kernwort)
- Artikel: xlan (best., F, Akk Sg; im Deutschen artikellos, in Orbis ist Artikellosigkeit nicht geregelt → bestimmter Artikel gewählt)
- Geschlecht: F
- Kasus: Dat (viş = 1. Sg Dat) + Akk (nauşen)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓; Dat vor Akk (U-05)
- Phonotaktik: §5-konform (nau-şen)
- verwendete Regeln: §8, §10.3, §11, §13.1, §14, §17.1
- Anmerkung: 1. Person über Personalpronomen bildbar (vgl. Test 032); L-04 berührt.
- Ergebnis: [OK]

## Test 035
Deutsch:
Sie spricht über sich.
Orbis:
— nicht eindeutig bildbar: Lo talat span se(?) — span verlangt Dat oder Akk (§19); se hat weder Dativ- noch Akkusativform, und ob es unverändert nach Präpositionen stehen darf, ist nicht definiert.
Analyse:
- Satztyp: Hauptsatz, Präpositionalobjekt reflexiv (Stresstest D)
- Subjekt: lo
- Verb: talat (tal-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: span + Dat/Akk — Kasusform von se fehlt
- Adjektive: —
- Präpositionen: span (über)
- Wortstellung: V2 wäre erfüllbar
- Phonotaktik: unkritisch
- verwendete Regeln: §13.4, §17.1, §19
- Befund: L-04 — Reflexiv nach Präposition nicht bildbar. NICHT geraten.
- Ergebnis: [REGELLÜCKE]

---

## C. GENITIVKONSTRUKTIONEN (036–045) — Stresstest A

## Test 036
Deutsch:
Das Haus des Mannes ist alt.
Orbis:
— nicht eindeutig bildbar: Xna breun xras valrus granz est (nachgestellt) ODER Xras valrus xna breun granz est (vorangestellt) — beide morphologisch korrekt; die Stellung des Genitivattributs ist nirgends festgelegt.
Analyse:
- Satztyp: Hauptsatz mit Genitivattribut (gezielter Stellungstest)
- Subjekt: xna breun (+ Genitivattribut xras valrus)
- Verb: est (es-, 3. Sg Präsens)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: breun (Kernwort), valru
- Artikel: xna (N Nom), xras (M Gen)
- Geschlecht: N / M
- Kasus: Nom + Gen (valrus, Marker -s §8)
- Adjektive: granz (prädikativ, Grundform §12.2)
- Präpositionen: —
- Wortstellung: Attributstellung ungeregelt — §8 definiert den Genitiv nur morphologisch, §17 schweigt; alle Beispiele (§25.1/§25.2) stellen nach, §13.3 regelt nur das Possessiv
- Phonotaktik: K-01 (breun-Nom, est, granz); Formen sonst §5-konform
- verwendete Regeln: §8, §10.3, §11, §12.2, §15.2, §17.1
- Befund: L-01. NICHT geraten — beide Stellungen bleiben unentschieden.
- Ergebnis: [REGELLÜCKE]

## Test 037
Deutsch:
Die Erinnerung der Zeit vergeht.
Orbis:
Xla soruma xlas nauşes vaşnat.
Analyse:
- Satztyp: Hauptsatz mit Genitivattribut
- Subjekt: xla soruma
- Verb: vaşnat (vaşn-, intransitiv „vergehen" §24.6)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: soruma (Erinnerung), nauş (Zeit, Kernwort)
- Artikel: xla (F Nom), xlas (F Gen)
- Geschlecht: F / F
- Kasus: Nom + Gen (nauşes = nauş + -e- + -s §10.3)
- Adjektive: —
- Präpositionen: —
- Wortstellung: Genitiv nachgestellt nach Beispielpraxis (§25.1 wörtlich so); normativ offen → L-01
- Phonotaktik: §5-konform (vaşn- Coda şn §5.3c)
- verwendete Regeln: §8, §10.3, §11, §17.1, §24.6
- Ergebnis: [OK]

## Test 038
Deutsch:
Der Name der Frau ist schön.
Orbis:
Xra şaul xlas sarlas loşn est.
Analyse:
- Satztyp: Hauptsatz mit Genitivattribut, prädikatives Adjektiv
- Subjekt: xra şaul
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: şaul (Kernwort), sarla
- Artikel: xra (M Nom), xlas (F Gen)
- Geschlecht: M / F
- Kasus: Nom + Gen (sarlas)
- Adjektive: loşn (prädikativ)
- Präpositionen: —
- Wortstellung: Genitiv nachgestellt (Beispielpraxis → L-01); Prädikativ vor est wie §12.2-Beispiele
- Phonotaktik: K-01 (est); sonst §5-konform
- verwendete Regeln: §8, §10.3, §11, §12.2, §15.2, §17.1
- Ergebnis: [OK]

## Test 039
Deutsch:
Das Buch meines Freundes ist neu.
Orbis:
— nicht eindeutig bildbar: Xna vresto xras velkras vis zirv est(?) — Stapelung Genitivattribut + nachgestelltes Possessiv (§13.3): ob vis hinter velkras oder hinter vresto steht und ob die Folge Kopf + Gen + Poss überhaupt so gebaut wird, ist ungeregelt.
Analyse:
- Satztyp: Hauptsatz, Genitivattribut mit Possessiv (gezielter Stapelungstest)
- Subjekt: xna vresto (+ xras velkras vis)
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: vresto, velkra
- Artikel: xna (N Nom), xras (M Gen)
- Geschlecht: N / M
- Kasus: Nom + Gen + Possessiv (vis = Gen 1. Sg, nachgestellt §13.3)
- Adjektive: zirv (prädikativ)
- Präpositionen: —
- Wortstellung: Bezug und Position des Possessivs in der Genitivkette ungeregelt
- Phonotaktik: K-01 (est); sonst §5-konform
- verwendete Regeln: §8, §11, §12.2, §13.3, §15.2, §17.1
- Befund: L-01 (Stapelungsfall). NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 040
Deutsch:
Die Flamme des Feuers ist warm.
Orbis:
Xla gluvi xras xerpes velm est.
Analyse:
- Satztyp: Hauptsatz mit Genitivattribut
- Subjekt: xla gluvi
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: gluvi (Flamme), xerp (Feuer, Kernwort)
- Artikel: xla (F Nom), xras (M Gen)
- Geschlecht: F / M
- Kasus: Nom + Gen (xerpes = xerp + -e- + -s)
- Adjektive: velm (prädikativ)
- Präpositionen: —
- Wortstellung: Genitiv nachgestellt (→ L-01)
- Phonotaktik: K-01 (est); xerp KVKK zulässig („selten")
- verwendete Regeln: §8, §10.3, §11, §12.2, §15.2, §17.1
- Ergebnis: [OK]

## Test 041
Deutsch:
Der Weg des Lebens ist lang.
Orbis:
Xna melna xnas virnes trelm est.
Analyse:
- Satztyp: Hauptsatz mit Genitivattribut
- Subjekt: xna melna
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: melna (Weg; mel- + -na §21.1), virn (Leben, Kernwort)
- Artikel: xna (N Nom), xnas (N Gen)
- Geschlecht: N / N
- Kasus: Nom + Gen (virnes)
- Adjektive: trelm (prädikativ)
- Präpositionen: —
- Wortstellung: Genitiv nachgestellt (→ L-01)
- Phonotaktik: K-01 (est, trelm KKVKK); sonst §5-konform
- verwendete Regeln: §8, §10.3, §11, §12.2, §15.2, §17.1, §21.1
- Ergebnis: [OK]

## Test 042
Deutsch:
Der Tag des Todes kommt.
Orbis:
Xra zaldre xras mokses vandat.
Analyse:
- Satztyp: Hauptsatz mit Genitivattribut
- Subjekt: xra zaldre
- Verb: vandat (vand-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: zaldre (Tag), moks (Tod, Kernwort)
- Artikel: xra (M Nom), xras (M Gen)
- Geschlecht: M / M
- Kasus: Nom + Gen (mokses = moks + -e- + -s)
- Adjektive: —
- Präpositionen: —
- Wortstellung: Genitiv nachgestellt (→ L-01)
- Phonotaktik: §5-konform (moks KVKK zulässig; mok-ses)
- verwendete Regeln: §8, §10.3, §11, §17.1
- Ergebnis: [OK]

## Test 043
Deutsch:
Das Wasser der Erde ist kalt.
Orbis:
Xna aul xlas greines girn est.
Analyse:
- Satztyp: Hauptsatz mit Genitivattribut
- Subjekt: xna aul
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: aul (Kernwort), grein (Erde, Kernwort)
- Artikel: xna (N Nom), xlas (F Gen)
- Geschlecht: N / F
- Kasus: Nom + Gen (greines)
- Adjektive: girn (prädikativ)
- Präpositionen: —
- Wortstellung: Genitiv nachgestellt (→ L-01)
- Phonotaktik: K-01 (aul VK, est); grei-nes §5-konform
- verwendete Regeln: §8, §10.3, §11, §12.2, §15.2, §17.1
- Ergebnis: [OK]

## Test 044
Deutsch:
Die Stimme des Menschen ist stark.
Orbis:
Xla şonma xras kaunes xarn est.
Analyse:
- Satztyp: Hauptsatz mit Genitivattribut
- Subjekt: xla şonma
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: şonma (Stimme), kaun (Mensch, Kernwort)
- Artikel: xla (F Nom), xras (M Gen)
- Geschlecht: F / M
- Kasus: Nom + Gen (kaunes)
- Adjektive: xarn (prädikativ)
- Präpositionen: —
- Wortstellung: Genitiv nachgestellt (→ L-01)
- Phonotaktik: K-01 (est); şon-ma, kau-nes §5-konform
- verwendete Regeln: §8, §10.3, §11, §12.2, §15.2, §17.1
- Ergebnis: [OK]

## Test 045
Deutsch:
Die Sprache der Welt vergeht nicht.
Orbis:
Xla taiv xlas eirdes xa vaşnat.
Analyse:
- Satztyp: Hauptsatz, Genitivattribut + Negation (Kategorienüberschneidung)
- Subjekt: xla taiv
- Verb: vaşnat (vaşn-), negiert
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: taiv (Kernwort), eird (Kernwort)
- Artikel: xla (F Nom), xlas (F Gen)
- Geschlecht: F / F
- Kasus: Nom + Gen (eirdes)
- Adjektive: —
- Präpositionen: —
- Wortstellung: Genitiv nachgestellt (→ L-01); xa unmittelbar vor dem finiten Verb §18.3
- Phonotaktik: K-01 (eirdes VKK-Anlautsilbe); sonst §5-konform
- verwendete Regeln: §8, §10.3, §11, §17.1, §18.3
- Ergebnis: [OK]

---

## D. ADJEKTIVKONSTRUKTIONEN (046–060)

## Test 046
Deutsch:
Der große Berg ist alt.
Orbis:
Xra vlaidra vrondo granz est.
Analyse:
- Satztyp: Hauptsatz, attributives + prädikatives Adjektiv
- Subjekt: xra vlaidra vrondo
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: vrondo (Berg)
- Artikel: xra (M Nom)
- Geschlecht: M (M-C; Adjektiv immer A-Reihe r/l/n §12.1)
- Kasus: Nom
- Adjektive: vlaidra (attributiv M Nom), granz (prädikativ)
- Präpositionen: —
- Wortstellung: V2 ✓; Kongruenz Artikel–Adjektiv–Nomen ✓
- Phonotaktik: K-01 (granz, est); sonst §5-konform
- verwendete Regeln: §11, §12.1, §12.2, §15.2, §17.1
- Ergebnis: [OK]

## Test 047
Deutsch:
Ich sehe den kleinen Vogel.
Orbis:
Vim milkam xran nirmran vlenkon.
Analyse:
- Satztyp: Hauptsatz, attributives Adjektiv im Akkusativ
- Subjekt: vim
- Verb: milkam (milk-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: vlenko (Vogel)
- Artikel: xran (M Akk)
- Geschlecht: M
- Kasus: Akk (Kongruenz xran–nirmran–vlenkon ✓)
- Adjektive: nirmran (nirm + -ra + -n, attributiv M Akk)
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (nirm-ran)
- verwendete Regeln: §8, §11, §12.1, §17.1
- Ergebnis: [OK]

## Test 048
Deutsch:
Die schöne Frau spricht.
Orbis:
Xla loşnla sarla talat.
Analyse:
- Satztyp: Hauptsatz, attributives Adjektiv
- Subjekt: xla loşnla sarla
- Verb: talat (tal-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: sarla
- Artikel: xla (F Nom)
- Geschlecht: F
- Kasus: Nom
- Adjektive: loşnla (loşn + -la; KEINE Fusion, n ≠ l — Fugenregel §21.4 greift nur bei identischen Konsonanten)
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (loşn-la, Coda şn §5.3c)
- verwendete Regeln: §11, §12.1, §17.1, §21.4
- Anmerkung: Korrigiert gegenüber Chat-Korpus 0.1 Satz 48, der fälschlich *loşna* (= Neutrum-Form) schrieb — dort unentdeckter Kongruenzfehler.
- Ergebnis: [OK]

## Test 049
Deutsch:
Wir gehen auf der langen Straße.
Orbis:
Viñ melamen kru xlaş trelmlaş melvaş.
Analyse:
- Satztyp: Hauptsatz, Adjektiv im Präpositionalgefüge
- Subjekt: viñ
- Verb: melamen (mel-)
- Person/Numerus: 1. Pl
- Tempus: Gegenwart
- Nomen: melva (Straße)
- Artikel: xlaş (F Dat)
- Geschlecht: F
- Kasus: Dat (Ort §19)
- Adjektive: trelmlaş (trelm + -la + -ş, F Dat)
- Präpositionen: kru (auf) + Dat
- Wortstellung: V2 ✓; Kongruenz xlaş–trelmlaş–melvaş ✓
- Phonotaktik: K-01 (trelm KKVKK); trelm-laş Fuge zulässig
- verwendete Regeln: §8, §11, §12.1, §17.1, §19
- Ergebnis: [OK]

## Test 050
Deutsch:
Das dunkle Wasser ist kalt.
Orbis:
Xna şalna aul girn est.
Analyse:
- Satztyp: Hauptsatz, attributives Adjektiv mit Fugenregel
- Subjekt: xna şalna aul
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: aul (Kernwort)
- Artikel: xna (N Nom)
- Geschlecht: N
- Kasus: Nom
- Adjektive: şalna (şaln + -na → Fusion n+n §12.1/§21.4, wörtliches Grammatikbeispiel), girn (prädikativ)
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: K-01 (aul, est); şal-na §5-konform
- verwendete Regeln: §11, §12.1, §12.2, §15.2, §21.4
- Ergebnis: [OK]

## Test 051
Deutsch:
Das gefundene Buch ist alt.
Orbis:
— nicht eindeutig bildbar: Xna traivutna vresto granz est(?) — das Partizip traivut (§14) müsste dafür wie ein Adjektiv dekliniert werden (traivut + -na); ob Partizipien attributiv stehen dürfen, regelt weder §12 noch §14.
Analyse:
- Satztyp: Hauptsatz, Partizip als Attribut (gezielter Test)
- Subjekt: xna (traivutna?) vresto
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: vresto
- Artikel: xna (N Nom)
- Geschlecht: N
- Kasus: Nom
- Adjektive: Partizip traivut in Adjektivfunktion — Status ungeregelt
- Präpositionen: —
- Wortstellung: V2 wäre erfüllbar
- Phonotaktik: unkritisch (trai-vut-na)
- verwendete Regeln: §12.1, §14 (Partizip -ut), §16.3 (nur prädikativ belegt), §12.5 (nur Nominalisierung -ute)
- Befund: U-02 — attributiver Partizipgebrauch nicht definiert. NICHT geraten.
- Ergebnis: [REGELUNKLARHEIT]

## Test 052
Deutsch:
Ich lese ein neues Buch.
Orbis:
Vim leşnam vnan zirvnan vreston.
Analyse:
- Satztyp: Hauptsatz, Adjektiv nach unbestimmtem Artikel
- Subjekt: vim
- Verb: leşnam (leşn-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: vresto
- Artikel: vnan (unbest., N, Akk Sg)
- Geschlecht: N
- Kasus: Akk (Kongruenz vnan–zirvnan–vreston ✓; Adjektivendung nach unbest. Artikel unverändert — §12.1 kennt nur ein Muster)
- Adjektive: zirvnan (zirv + -na + -n)
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (zirv-nan)
- verwendete Regeln: §8, §11.2, §12.1, §17.1
- Ergebnis: [OK]

## Test 053
Deutsch:
Die kalte Nacht ist lang.
Orbis:
Xla girnla kirva trelm est.
Analyse:
- Satztyp: Hauptsatz, attributiv + prädikativ
- Subjekt: xla girnla kirva
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: kirva
- Artikel: xla (F Nom)
- Geschlecht: F
- Kasus: Nom
- Adjektive: girnla (girn + -la, keine Fusion n≠l), trelm (prädikativ)
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: K-01 (trelm, est); girn-la §5-konform
- verwendete Regeln: §11, §12.1, §12.2, §15.2
- Ergebnis: [OK]

## Test 054
Deutsch:
Er ist größer als ich.
Orbis:
Ro vlaidvi est kon vim.
Analyse:
- Satztyp: Hauptsatz, Komparativ prädikativ
- Subjekt: ro
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom; Vergleichsglied vim im Nom (nur Beispielpraxis → U-06)
- Adjektive: vlaidvi (vlaid + -vi-, prädikativ endungslos §12.3)
- Präpositionen: — (kon = Vergleichswort)
- Wortstellung: V2 ✓ (wörtliches Grammatikbeispiel §12.3)
- Phonotaktik: K-01 (est); vlaid-vi §5-konform
- verwendete Regeln: §12.3, §15.2, §17.1
- Ergebnis: [OK]

## Test 055
Deutsch:
Sie ist die schönste Frau.
Orbis:
Lo xla loşnvaxla sarla est.
Analyse:
- Satztyp: Hauptsatz, Superlativ attributiv im Prädikatsnomen
- Subjekt: lo
- Verb: est (es-, Satzende hier zulässig? — V2 verlangt Position 2: siehe Wortstellung)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: sarla
- Artikel: xla (F Nom, Prädikatsnomen im Nominativ nach Beispielpraxis §16.2)
- Geschlecht: F
- Kasus: Nom
- Adjektive: loşnvaxla (loşn + -vax- + -la §12.3)
- Präpositionen: —
- Wortstellung: est steht hier satzfinal; §17.1 verlangt V2 → korrekt wäre „Lo est xla loşnvaxla sarla." Die Grammatik §12.2 stellt aber Prädikative VOR est (Lo loşn est) — bei nominalen Prädikaten ist die Abfolge nicht geregelt; gewählt wurde die §12.2-Analogie
- Phonotaktik: K-01 (est); loşn-vax-la §5-konform
- verwendete Regeln: §11, §12.2, §12.3, §15.2, §17.1
- Anmerkung: Spannung zwischen §12.2-Muster (Prädikativ vor est) und §17.1 (V2) besteht schon in der Grammatik selbst (Lo loşn est = Verb an Position 3); als Beispielpraxis gewertet, Ergebnis unberührt. Wird im Testbericht unter U-13 geführt.
- Ergebnis: [OK]

## Test 056
Deutsch:
Sie ist warm wie die Sonne.
Orbis:
Lo velm est zil luiv.
Analyse:
- Satztyp: Hauptsatz, Positiv-Vergleich
- Subjekt: lo
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: luiv (Kernwort)
- Artikel: — (nach zil artikellos wie im Grammatikbeispiel)
- Geschlecht: F
- Kasus: Nom nach zil (Beispielpraxis → U-06)
- Adjektive: velm (prädikativ)
- Präpositionen: — (zil = Vergleichswort)
- Wortstellung: nach §12.3-Beispiel (Lo loşn est zil luiv)
- Phonotaktik: K-01 (est); sonst §5-konform
- verwendete Regeln: §12.2, §12.3, §15.2
- Ergebnis: [OK]

## Test 057
Deutsch:
Der Mann wird stark.
Orbis:
Xra valru xarn vurt.
Analyse:
- Satztyp: Hauptsatz, prädikatives Adjektiv mit vurnex
- Subjekt: xra valru
- Verb: vurt (vurn-, unregelm. Präsens 3. Sg — kontrahierter Stamm vur-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: valru
- Artikel: xra (M Nom)
- Geschlecht: M
- Kasus: Nom
- Adjektive: xarn (prädikativ, Grundform nach vurnex §12.2; wörtliches Grammatikbeispiel)
- Präpositionen: —
- Wortstellung: Prädikativ vor Verb nach §12.2-Muster (vgl. Anmerkung Test 055)
- Phonotaktik: §5-konform (xarn KVKK)
- verwendete Regeln: §12.2, §15.2
- Ergebnis: [OK]

## Test 058
Deutsch:
Wir warten in der dunklen Stadt.
Orbis:
Viñ maldamen tel xlaş şalnlaş kavlaş.
Analyse:
- Satztyp: Hauptsatz, Adjektiv im Dativ-Präpositionalgefüge
- Subjekt: viñ
- Verb: maldamen (mald-)
- Person/Numerus: 1. Pl
- Tempus: Gegenwart
- Nomen: kavla (Stadt)
- Artikel: xlaş (F Dat)
- Geschlecht: F
- Kasus: Dat (Ort §19: tel + Dat)
- Adjektive: şalnlaş (şaln + -la + -ş; keine Fusion n≠l)
- Präpositionen: tel (in)
- Wortstellung: V2 ✓; Kongruenz xlaş–şalnlaş–kavlaş ✓
- Phonotaktik: §5-konform (şaln-laş)
- verwendete Regeln: §8, §11, §12.1, §17.1, §19
- Ergebnis: [OK]

## Test 059
Deutsch:
Sie geht schnell.
Orbis:
Lo melat zilvun.
Analyse:
- Satztyp: Hauptsatz mit Adverb
- Subjekt: lo
- Verb: melat (mel-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: —
- Adjektive: zilvun (Adverb: Grundform zilv + -un §12.4)
- Präpositionen: —
- Wortstellung: V2 ✓, Adverb im Feld
- Phonotaktik: §5-konform (zil-vun)
- verwendete Regeln: §12.4, §14, §17.1
- Ergebnis: [OK]

## Test 060
Deutsch:
Die Erinnerung vergeht langsam.
Orbis:
— nicht eindeutig entscheidbar: Nach §12.4 muss es „Xla soruma tolmun vaşnat" heißen (Adverb = Grundform + -un). Der Referenzsatz §25.1 schreibt aber wörtlich „Xla soruma xlas nauşes vran tolm vaşnat" — tolm OHNE -un in adverbialer Funktion. Zwei Belege, zwei Formen.
Analyse:
- Satztyp: Hauptsatz mit Adverb (gezielter Konflikttest)
- Subjekt: xla soruma
- Verb: vaşnat (vaşn-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: soruma
- Artikel: xla (F Nom)
- Geschlecht: F
- Kasus: Nom
- Adjektive: tolm/tolmun — strittige Adverbform
- Präpositionen: —
- Wortstellung: V2 ✓ in beiden Varianten
- Phonotaktik: beide Formen §5-konform
- verwendete Regeln: §12.4 ↔ §25.1
- Befund: K-04 — Regel und Referenzbeispiel widersprechen sich. (Chat-Korpus 0.1 Satz 39 übernahm §25.1 unmarkiert.)
- Ergebnis: [REGELKONFLIKT]

---

## E. PLURALKONSTRUKTIONEN (061–070)

## Test 061
Deutsch:
Die Männer gehen.
Orbis:
Xrañ valruñ melaten.
Analyse:
- Satztyp: Hauptsatz, Plural Nominativ
- Subjekt: xrañ valruñ
- Verb: melaten (mel-)
- Person/Numerus: 3. Pl
- Tempus: Gegenwart
- Nomen: valru → valruñ (Plural -ñ §9)
- Artikel: xrañ (best., M, Nom Pl)
- Geschlecht: M
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓; Kongruenz Subjekt Pl – Verb 3. Pl ✓
- Phonotaktik: §5-konform (Coda ñ einfach)
- verwendete Regeln: §9, §11, §14, §17.1
- Ergebnis: [OK]

## Test 062
Deutsch:
Ich sehe die Hunde.
Orbis:
Vim milkam xrañan narkuñun.
Analyse:
- Satztyp: Hauptsatz, Plural Akkusativ
- Subjekt: vim
- Verb: milkam (milk-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: narku → narkuñun (Akk Pl: -ñ- + Echovokal u + -n §9)
- Artikel: xrañan (M Akk Pl, Echovokal a)
- Geschlecht: M
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (nar-ku-ñun)
- verwendete Regeln: §9 (Echovokal = Themavokal, nur tabellarisch definiert → U-09), §11, §17.1
- Ergebnis: [OK]

## Test 063
Deutsch:
Die Frauen sprechen.
Orbis:
Xlañ sarlañ talaten.
Analyse:
- Satztyp: Hauptsatz, Plural Nominativ
- Subjekt: xlañ sarlañ
- Verb: talaten (tal-)
- Person/Numerus: 3. Pl
- Tempus: Gegenwart
- Nomen: sarla → sarlañ
- Artikel: xlañ (F Nom Pl)
- Geschlecht: F
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §9, §11, §14, §17.1
- Ergebnis: [OK]

## Test 064
Deutsch:
Wir geben den Kindern das Brot.
Orbis:
Viñ dalvamen xnañaş şirneiş xnan brasin.
Analyse:
- Satztyp: Hauptsatz, Kernwort-Plural im Dativ + Akkusativobjekt
- Subjekt: viñ
- Verb: dalvamen (dalv-)
- Person/Numerus: 1. Pl
- Tempus: Gegenwart
- Nomen: şirn → şirneiş (Dat Pl: -ei- + -ş §10.3), brasi
- Artikel: xnañaş (N Dat Pl, reguläres Artikelsystem), xnan (N Akk Sg)
- Geschlecht: N / N
- Kasus: Dat Pl + Akk Sg
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓; Dat vor Akk (U-05)
- Phonotaktik: §5-konform (şir-neiş)
- verwendete Regeln: §9, §10.3, §11, §17.1 — Mischung Artikel-Regelplural + Kernwort-ei-Plural funktioniert
- Ergebnis: [OK]

## Test 065
Deutsch:
Die Steine sind kalt.
Orbis:
Xrañ larkiñ girn esten.
Analyse:
- Satztyp: Hauptsatz, Plural + prädikatives Adjektiv
- Subjekt: xrañ larkiñ
- Verb: esten (es-, 3. Pl Präsens)
- Person/Numerus: 3. Pl
- Tempus: Gegenwart
- Nomen: larki → larkiñ
- Artikel: xrañ (M Nom Pl)
- Geschlecht: M
- Kasus: Nom
- Adjektive: girn (prädikativ, im Plural unverändert §12.2 — wörtliches Grammatikbeispiel)
- Präpositionen: —
- Wortstellung: Prädikativ vor esten (§12.2-Muster)
- Phonotaktik: §5-konform
- verwendete Regeln: §9, §11, §12.2, §15.2
- Ergebnis: [OK]

## Test 066
Deutsch:
Die Mütter warten.
Orbis:
Xlañ veişei maldaten.
Analyse:
- Satztyp: Hauptsatz, Kernwort-Plural
- Subjekt: xlañ veişei
- Verb: maldaten (mald-)
- Person/Numerus: 3. Pl
- Tempus: Gegenwart
- Nomen: veiş → veişei (Nom Pl -ei §10.3)
- Artikel: xlañ (F Nom Pl)
- Geschlecht: F
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (vei-şei)
- verwendete Regeln: §9, §10.3, §11, §17.1
- Ergebnis: [OK]

## Test 067
Deutsch:
Ich lese die Bücher.
Orbis:
Vim leşnam xnañan vrestoñon.
Analyse:
- Satztyp: Hauptsatz, Plural Akkusativ (Echovokal o)
- Subjekt: vim
- Verb: leşnam (leşn-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: vresto → vrestoñon (Akk Pl, Echovokal = Themavokal o)
- Artikel: xnañan (N Akk Pl)
- Geschlecht: N
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §9 (U-09: Echovokal-Analogie), §11, §17.1
- Ergebnis: [OK]

## Test 068
Deutsch:
Die Menschen bleiben.
Orbis:
Xrañ kaunei stanaten.
Analyse:
- Satztyp: Hauptsatz, Kernwort-Plural
- Subjekt: xrañ kaunei
- Verb: stanaten (stan-)
- Person/Numerus: 3. Pl
- Tempus: Gegenwart
- Nomen: kaun → kaunei
- Artikel: xrañ (M Nom Pl)
- Geschlecht: M
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (kau-nei)
- verwendete Regeln: §9, §10.3, §11, §17.1
- Ergebnis: [OK]

## Test 069
Deutsch:
Wir hören die Sprachen.
Orbis:
Viñ zaubamen xlañan taivein.
Analyse:
- Satztyp: Hauptsatz, Kernwort-Plural Akkusativ
- Subjekt: viñ
- Verb: zaubamen (zaub-)
- Person/Numerus: 1. Pl
- Tempus: Gegenwart
- Nomen: taiv → taivein (Akk Pl: -ei- + -n §10.3)
- Artikel: xlañan (F Akk Pl)
- Geschlecht: F
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (tai-vein)
- verwendete Regeln: §9, §10.3, §11, §17.1
- Ergebnis: [OK]

## Test 070
Deutsch:
Zwei Männer kommen.
Orbis:
— nicht eindeutig bildbar: Dram valruñ vandaten(?) — ob das gezählte Nomen im Plural steht, ob die Zahl kongruiert und ob ein Artikel nötig ist, regelt §24.8 nicht; kein Beispiel verwendet eine Kardinalzahl attributiv.
Analyse:
- Satztyp: Hauptsatz mit Kardinalzahl (gezielter Test)
- Subjekt: dram + valru(ñ?)
- Verb: vandaten (vand-)
- Person/Numerus: 3. Pl (falls Plural)
- Tempus: Gegenwart
- Nomen: valru
- Artikel: keiner? (ungeregelt)
- Geschlecht: M
- Kasus: Nom
- Adjektive: — (dram = Kardinalzahl, Flexionsstatus offen)
- Präpositionen: —
- Wortstellung: V2 wäre erfüllbar
- Phonotaktik: unkritisch
- verwendete Regeln: §9, §24.8
- Befund: L-08 — Syntax der Kardinalzahlen fehlt. NICHT geraten.
- Ergebnis: [REGELLÜCKE]

---

## F. FRAGEN (071–080) — Stresstest C

## Test 071
Deutsch:
Gehst du heute?
Orbis:
Melaş şet nunda?
Analyse:
- Satztyp: Ja/Nein-Frage (V1 §18.1)
- Subjekt: şet
- Verb: melaş (mel-)
- Person/Numerus: 2. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: Verb an Position 1 ✓; Subjekt ausgeschrieben (das §18.1-Beispiel „Melaş nunda?" lässt es weg → Pro-Drop ungeregelt, U-04)
- Phonotaktik: §5-konform
- verwendete Regeln: §13.1, §18.1
- Ergebnis: [OK]

## Test 072
Deutsch:
Kommt der Vater?
Orbis:
Vandat xra draun?
Analyse:
- Satztyp: Ja/Nein-Frage
- Subjekt: xra draun
- Verb: vandat (vand-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: draun (Kernwort)
- Artikel: xra (M Nom)
- Geschlecht: M
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V1 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §10.2, §11, §18.1
- Ergebnis: [OK]

## Test 073
Deutsch:
Wer spricht?
Orbis:
Kem talat?
Analyse:
- Satztyp: W-Frage, Fragewort als Subjekt
- Subjekt: kem
- Verb: talat (tal-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom (Grundform kem belegt §18.2)
- Adjektive: —
- Präpositionen: —
- Wortstellung: Fragewort Position 1, Verb Position 2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §18.2
- Ergebnis: [OK]

## Test 074
Deutsch:
Wen siehst du?
Orbis:
— nicht bildbar: §18.2 listet nur die Grundform kem. Ein Akkusativ (*kemen? *kemn?) ist nirgends definiert, Indeklinabilität ebenso wenig.
Analyse:
- Satztyp: W-Frage, Fragewort als Akkusativobjekt (gezielter Test)
- Subjekt: şet
- Verb: milkaş (milk-)
- Person/Numerus: 2. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Akk des Frageworts — nicht definiert
- Adjektive: —
- Präpositionen: —
- Wortstellung: wäre W-Wort + V2
- Phonotaktik: unkritisch
- verwendete Regeln: §18.2
- Befund: L-03. NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 075
Deutsch:
Wem gibst du das Buch?
Orbis:
— nicht bildbar: Dativ von kem (*kemeş?) ist nicht definiert.
Analyse:
- Satztyp: W-Frage, Fragewort als Dativobjekt (gezielter Test)
- Subjekt: şet
- Verb: dalvaş (dalv-)
- Person/Numerus: 2. Sg
- Tempus: Gegenwart
- Nomen: vresto
- Artikel: xnan (N Akk)
- Geschlecht: N
- Kasus: Dat des Frageworts — nicht definiert; Akk (vreston) regulär
- Adjektive: —
- Präpositionen: —
- Wortstellung: wäre W-Wort + V2
- Phonotaktik: unkritisch
- verwendete Regeln: §8, §18.2
- Befund: L-03. NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 076
Deutsch:
Wessen Buch liest du?
Orbis:
— nicht bildbar: Genitiv von kem (*kemes?) ist nicht definiert; auch die attributive Verwendung eines Fragewort-Genitivs ist ungeregelt (hängt zusätzlich an L-01).
Analyse:
- Satztyp: W-Frage, Fragewort als Genitivattribut (gezielter Test)
- Subjekt: şet
- Verb: leşnaş (leşn-)
- Person/Numerus: 2. Sg
- Tempus: Gegenwart
- Nomen: vresto
- Artikel: — (Artikelgebrauch bei Fragewort-Genitiv ungeklärt)
- Geschlecht: N
- Kasus: Gen des Frageworts — nicht definiert
- Adjektive: —
- Präpositionen: —
- Wortstellung: wäre W-Wort + V2
- Phonotaktik: unkritisch
- verwendete Regeln: §8, §18.2
- Befund: L-03 (+ L-01 berührt). NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 077
Deutsch:
Wo wartet ihr?
Orbis:
Kur maldaşen şeñ?
Analyse:
- Satztyp: W-Frage, Ortsadverb
- Subjekt: şeñ
- Verb: maldaşen (mald-)
- Person/Numerus: 2. Pl
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: —
- Adjektive: —
- Präpositionen: —
- Wortstellung: W-Wort Position 1, Verb Position 2, Subjekt Position 3 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §18.2, §13.1
- Ergebnis: [OK]

## Test 078
Deutsch:
Wie ist die Nacht?
Orbis:
Kolm est xla kirva?
Analyse:
- Satztyp: W-Frage nach Eigenschaft
- Subjekt: xla kirva
- Verb: est (es-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: kirva
- Artikel: xla (F Nom)
- Geschlecht: F
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: W-Wort + V2 ✓
- Phonotaktik: K-01 (est); sonst §5-konform
- verwendete Regeln: §15.2, §18.2
- Ergebnis: [OK]

## Test 079
Deutsch:
Welches Buch liest du?
Orbis:
Kelnan vreston leşnaş şet?
Analyse:
- Satztyp: W-Frage mit kongruierendem Fragewort
- Subjekt: şet
- Verb: leşnaş (leşn-)
- Person/Numerus: 2. Sg
- Tempus: Gegenwart
- Nomen: vresto
- Artikel: — (kelna übernimmt die Attributrolle)
- Geschlecht: N
- Kasus: Akk (kelnan + vreston kongruent — Muster des §18.2-Beispiels „Kellan sarlan milkoş?")
- Adjektive: — (kelna dekliniert adjektivisch)
- Präpositionen: —
- Wortstellung: Fragephrase Position 1, Verb Position 2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §12.1 (Muster), §18.2
- Ergebnis: [OK]

## Test 080
Deutsch:
Welchem Kind gibst du das Brot?
Orbis:
Kelnaş şirneş dalvaş şet xnan brasin?
Analyse:
- Satztyp: W-Frage, kongruierendes Fragewort im Dativ
- Subjekt: şet
- Verb: dalvaş (dalv-)
- Person/Numerus: 2. Sg
- Tempus: Gegenwart
- Nomen: şirn (Kernwort), brasi
- Artikel: — / xnan (N Akk)
- Geschlecht: N / N
- Kasus: Dat (kelnaş şirneş) + Akk (brasin)
- Adjektive: — (kelna adjektivisch dekliniert)
- Präpositionen: —
- Wortstellung: Fragephrase Position 1, Verb Position 2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §10.3, §12.1, §18.2
- Anmerkung: Belegt ist nur der Akkusativ (kellan §18.2); der Dativ folgt dem Adjektivparadigma §12.1 per Analogie. Grenzfall zu L-03 — als tragfähige Analogie [OK] gewertet, im Testbericht vermerkt.
- Ergebnis: [OK]

---

## G. NEGATIONEN (081–090)

## Test 081
Deutsch:
Ich gehe nicht.
Orbis:
Vim xa melam.
Analyse:
- Satztyp: Hauptsatz, negiert
- Subjekt: vim
- Verb: melam (mel-), negiert durch xa
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: xa unmittelbar vor dem finiten Verb (§18.3, wörtliches Beispiel)
- Phonotaktik: §5-konform
- verwendete Regeln: §13.1, §18.3
- Ergebnis: [OK]

## Test 082
Deutsch:
Er kommt nicht.
Orbis:
Ro xa vandat.
Analyse:
- Satztyp: Hauptsatz, negiert
- Subjekt: ro
- Verb: vandat (vand-), negiert
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: xa vor finitem Verb ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §13.1, §18.3
- Ergebnis: [OK]

## Test 083
Deutsch:
Wir haben kein Haus.
Orbis:
Viñ xa numen vnan breunen.
Analyse:
- Satztyp: Hauptsatz, Verbnegation mit unbestimmtem Objekt
- Subjekt: viñ
- Verb: numen (nuv-, kontrahierter Präsensstamm nu- §15.2)
- Person/Numerus: 1. Pl
- Tempus: Gegenwart
- Nomen: breun (Kernwort)
- Artikel: vnan (unbest., N, Akk Sg §11.2)
- Geschlecht: N
- Kasus: Akk (breunen = breun + -e- + -n §10.3)
- Adjektive: —
- Präpositionen: —
- Wortstellung: xa vor finitem Verb ✓
- Phonotaktik: §5-konform (breu-nen)
- verwendete Regeln: §8, §10.3, §11.2, §15.2, §18.3
- Anmerkung: Regelbasierte Form. Das Grammatikbeispiel §18.3 „Vim xa num **vna breun**" lässt Artikel UND Kernwort im Objekt unmarkiert — das widerspricht §8/§10.3/§11 und wird als Befund U-14 im Testbericht geführt (Beispiel fehlerhaft oder ungeschriebene Regel). Der Testsatz selbst folgt den Paragraphen und ist eindeutig.
- Ergebnis: [OK]

## Test 084
Deutsch:
Sie sieht den Hund nicht.
Orbis:
Lo xa milkat xran narkun.
Analyse:
- Satztyp: Hauptsatz, Verbnegation mit bestimmtem Objekt
- Subjekt: lo
- Verb: milkat (milk-), negiert
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: narku
- Artikel: xran (M Akk)
- Geschlecht: M
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: xa vor finitem Verb; Objekt im Feld dahinter
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §18.3
- Ergebnis: [OK]

## Test 085
Deutsch:
Das Kind schläft nicht.
Orbis:
Xna şirn xa soñat.
Analyse:
- Satztyp: Hauptsatz, negiert
- Subjekt: xna şirn
- Verb: soñat (soñ-), negiert
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: şirn (Kernwort)
- Artikel: xna (N Nom)
- Geschlecht: N
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: xa vor finitem Verb ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §10.2, §11, §18.3
- Ergebnis: [OK]

## Test 086
Deutsch:
Kein Mann wartet.
Orbis:
Xanra valru maldat.
Analyse:
- Satztyp: Hauptsatz, attributive Negation
- Subjekt: xanra valru
- Verb: maldat (mald-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: valru
- Artikel: — (xan- übernimmt die Attributrolle; §18.3 „xanra valru")
- Geschlecht: M
- Kasus: Nom
- Adjektive: xanra (xan „kein" §24.7, adjektivisch dekliniert §18.3)
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §12.1, §18.3, §24.7
- Ergebnis: [OK]

## Test 087
Deutsch:
Ich weiß es nicht.
Orbis:
Vim xa zavam non.
Analyse:
- Satztyp: Hauptsatz, negiert, pronominales Objekt
- Subjekt: vim
- Verb: zavam (zav-), negiert
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: N (Pronomen no)
- Kasus: Akk (non = 3. Sg n Akk §13.1)
- Adjektive: —
- Präpositionen: —
- Wortstellung: xa vor finitem Verb ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §13.1, §18.3
- Ergebnis: [OK]

## Test 088
Deutsch:
Niemand kommt.
Orbis:
Xakaun vandat.
Analyse:
- Satztyp: Hauptsatz, negatives Indefinitpronomen als Subjekt
- Subjekt: xakaun (niemand §13.4; xa- Gegenteilsvorsilbe §21.2 + kaun)
- Verb: vandat (vand-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: — (m per Basis kaun; ungeregelt)
- Kasus: Nom (Grundform belegt; oblique Formen → L-06)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (xa-kaun)
- verwendete Regeln: §13.4, §17.1, §21.2
- Ergebnis: [OK]

## Test 089
Deutsch:
Wir gehen nicht in die Stadt.
Orbis:
Viñ xa melamen tel xlan kavlan.
Analyse:
- Satztyp: Hauptsatz, negiert, Richtungsangabe
- Subjekt: viñ
- Verb: melamen (mel-), negiert
- Person/Numerus: 1. Pl
- Tempus: Gegenwart
- Nomen: kavla
- Artikel: xlan (F Akk)
- Geschlecht: F
- Kasus: Akk (Richtung §19: tel + Akk)
- Adjektive: —
- Präpositionen: tel (in)
- Wortstellung: xa vor finitem Verb; Präpositionalgefüge im Feld
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §18.3, §19
- Ergebnis: [OK]

## Test 090
Deutsch:
Ich weiß, dass er nicht kommt.
Orbis:
Vim zavam, fai ro xa vandat.
Analyse:
- Satztyp: Hauptsatz + Nebensatz, Negation im Nebensatz
- Subjekt: vim / ro
- Verb: zavam (zav-) / vandat (vand-), negiert
- Person/Numerus: 1. Sg / 3. Sg
- Tempus: Gegenwart / Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom / Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: Nebensatz-Endstellung ✓ (§17.2); xa unmittelbar vor dem finiten Verb auch am Satzende — Komposition beider Regeln eindeutig
- Phonotaktik: §5-konform
- verwendete Regeln: §17.2, §18.3, §20
- Ergebnis: [OK]

---

## H. NEBENSÄTZE (091–105) — Stresstests B und F

## Test 091
Deutsch:
Ich weiß, dass du kommst.
Orbis:
Vim zavam, fai şet vandaş.
Analyse:
- Satztyp: Hauptsatz + fai-Nebensatz
- Subjekt: vim / şet
- Verb: zavam / vandaş
- Person/Numerus: 1. Sg / 2. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: Verbendstellung im Nebensatz ✓ (§17.2)
- Phonotaktik: §5-konform
- verwendete Regeln: §17.2, §20
- Ergebnis: [OK]

## Test 092
Deutsch:
Er wartet, weil die Nacht kalt ist.
Orbis:
Ro maldat, grali xla kirva girn est.
Analyse:
- Satztyp: Hauptsatz + grali-Nebensatz
- Subjekt: ro / xla kirva
- Verb: maldat / est
- Person/Numerus: 3. Sg / 3. Sg
- Tempus: Gegenwart
- Nomen: kirva
- Artikel: xla (F Nom)
- Geschlecht: F
- Kasus: Nom
- Adjektive: girn (prädikativ, vor dem finiten Verb am Nebensatzende)
- Präpositionen: —
- Wortstellung: Verbendstellung ✓; Muster identisch mit §25.1 („grali xla kirva vran luid est")
- Phonotaktik: K-01 (est); sonst §5-konform
- verwendete Regeln: §12.2, §17.2, §20
- Ergebnis: [OK]

## Test 093
Deutsch:
Wenn du gehst, bleibe ich.
Orbis:
Tund şet melaş, stanam vim.
Analyse:
- Satztyp: vorangestellter Nebensatz + Hauptsatz
- Subjekt: şet / vim
- Verb: melaş / stanam
- Person/Numerus: 2. Sg / 1. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: Nebensatz = Position 1, finites Verb des Hauptsatzes direkt danach (§17.1) ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §17.1, §17.2, §20
- Ergebnis: [OK]

## Test 094
Deutsch:
Obwohl das Buch alt ist, lese ich es.
Orbis:
Şlani xna vresto granz est, leşnam vim non.
Analyse:
- Satztyp: vorangestellter şlani-Nebensatz + Hauptsatz
- Subjekt: xna vresto / vim
- Verb: est / leşnam
- Person/Numerus: 3. Sg / 1. Sg
- Tempus: Gegenwart
- Nomen: vresto
- Artikel: xna (N Nom)
- Geschlecht: N
- Kasus: Nom / Akk (non)
- Adjektive: granz (prädikativ)
- Präpositionen: —
- Wortstellung: Nebensatz Position 1, Hauptsatzverb direkt danach ✓
- Phonotaktik: K-01 (granz, est); sonst §5-konform
- verwendete Regeln: §12.2, §13.1, §17.1, §17.2, §20
- Ergebnis: [OK]

## Test 095
Deutsch:
Während wir warten, spricht der Mann.
Orbis:
Dremi viñ maldamen, talat xra valru.
Analyse:
- Satztyp: vorangestellter dremi-Nebensatz + Hauptsatz
- Subjekt: viñ / xra valru
- Verb: maldamen / talat
- Person/Numerus: 1. Pl / 3. Sg
- Tempus: Gegenwart
- Nomen: valru
- Artikel: xra (M Nom)
- Geschlecht: M
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: Nebensatz Position 1, Hauptsatzverb danach ✓
- Phonotaktik: §5-konform (dre-mi)
- verwendete Regeln: §17.1, §17.2, §20 (dremi: Ableitungsbehauptung → U-07, Funktion selbst klar)
- Ergebnis: [OK]

## Test 096
Deutsch:
Bevor die Sonne kommt, gehen wir.
Orbis:
Glemi xla luiv vandat, melamen viñ.
Analyse:
- Satztyp: vorangestellter glemi-Nebensatz + Hauptsatz
- Subjekt: xla luiv / viñ
- Verb: vandat / melamen
- Person/Numerus: 3. Sg / 1. Pl
- Tempus: Gegenwart
- Nomen: luiv (Kernwort)
- Artikel: xla (F Nom)
- Geschlecht: F
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: ✓ wie Test 093
- Phonotaktik: §5-konform
- verwendete Regeln: §10.2, §17.1, §17.2, §20
- Ergebnis: [OK]

## Test 097
Deutsch:
Nachdem er aß, schlief er.
Orbis:
Trausi ro nastot, soñot ro.
Analyse:
- Satztyp: vorangestellter trausi-Nebensatz + Hauptsatz, Vergangenheit
- Subjekt: ro / ro
- Verb: nastot / soñot (regelmäßige Vergangenheit -o-)
- Person/Numerus: 3. Sg
- Tempus: Vergangenheit
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: ✓ wie Test 093
- Phonotaktik: §5-konform
- verwendete Regeln: §15, §17.1, §17.2, §20
- Ergebnis: [OK]

## Test 098
Deutsch:
Ich weiß nicht, wo das Buch ist.
Orbis:
Vim xa zavam, kur xna vresto est.
Analyse:
- Satztyp: Hauptsatz (negiert) + indirekte Frage
- Subjekt: vim / xna vresto
- Verb: zavam (negiert) / est
- Person/Numerus: 1. Sg / 3. Sg
- Tempus: Gegenwart
- Nomen: vresto
- Artikel: xna (N Nom)
- Geschlecht: N
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: indirekte Frage mit W-Wort + Verbendstellung (Muster §25.2: „Ro xa zovet, kur xna melna molet")
- Phonotaktik: K-01 (est); sonst §5-konform
- verwendete Regeln: §17.2, §18.2, §18.3
- Ergebnis: [OK]

## Test 099
Deutsch:
Ich warte, denn die Nacht ist kalt.
Orbis:
Vim maldam, xer xla kirva girn est.
Analyse:
- Satztyp: zwei nebengeordnete Hauptsätze (xer §20)
- Subjekt: vim / xla kirva
- Verb: maldam / est
- Person/Numerus: 1. Sg / 3. Sg
- Tempus: Gegenwart
- Nomen: kirva
- Artikel: xla (F Nom)
- Geschlecht: F
- Kasus: Nom
- Adjektive: girn (prädikativ vor est, §12.2-Muster → U-13)
- Präpositionen: —
- Wortstellung: nach xer Hauptsatzstellung (nebenordnend §20) ✓
- Phonotaktik: K-01 (est); sonst §5-konform
- verwendete Regeln: §12.2, §17.1, §20
- Ergebnis: [OK]

## Test 100
Deutsch:
Der Mann, der kommt, ist mein Freund.
Orbis:
— nicht bildbar: §13.4 nennt fai als Relativpronomen, aber es existiert keine Regel für Relativsätze: weder Verbstellung noch Kasus-/Genus-Kongruenz von fai sind definiert; zusätzlich kollidiert fai „der/die/das" mit fai „dass" (§20). *Xra valru, fai vandat, xra velkra vis est* wäre reine Spekulation.
Analyse:
- Satztyp: Relativsatz zum Subjekt (gezielter Test, Stresstest B)
- Subjekt: xra valru (+ Relativsatz)
- Verb: vandat / est
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: valru, velkra
- Artikel: xra / xra
- Geschlecht: M
- Kasus: fai müsste Nominativ tragen — Formen fehlen
- Adjektive: —
- Präpositionen: —
- Wortstellung: Relativsatz-Verbstellung ungeregelt
- Phonotaktik: unkritisch
- verwendete Regeln: §13.4, §17.2, §20
- Befund: L-02. NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 101
Deutsch:
Die Frau, die ich sehe, spricht.
Orbis:
— nicht bildbar: fai müsste hier als Akkusativobjekt des Relativsatzes fungieren (*fain?*); keine Kasusformen, keine Struktur definiert (L-02).
Analyse:
- Satztyp: Relativsatz mit Relativpronomen als Objekt (gezielter Test)
- Subjekt: xla sarla / vim (im Relativsatz)
- Verb: milkam / talat
- Person/Numerus: 1. Sg / 3. Sg
- Tempus: Gegenwart
- Nomen: sarla
- Artikel: xla
- Geschlecht: F
- Kasus: Akk des Relativpronomens — nicht definiert
- Adjektive: —
- Präpositionen: —
- Wortstellung: ungeregelt
- Phonotaktik: unkritisch
- verwendete Regeln: §13.4, §17.2
- Befund: L-02. NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 102
Deutsch:
Der Mann, dem ich das Buch gebe, wartet.
Orbis:
— nicht bildbar: Dativ des Relativpronomens (*faiş?*) nicht definiert (L-02).
Analyse:
- Satztyp: Relativsatz mit Relativpronomen im Dativ (gezielter Test)
- Subjekt: xra valru / vim (im Relativsatz)
- Verb: dalvam / maldat
- Person/Numerus: 1. Sg / 3. Sg
- Tempus: Gegenwart
- Nomen: valru, vresto
- Artikel: xra, xnan
- Geschlecht: M / N
- Kasus: Dat des Relativpronomens — nicht definiert; Akk (vreston) regulär
- Adjektive: —
- Präpositionen: —
- Wortstellung: ungeregelt
- Phonotaktik: unkritisch
- verwendete Regeln: §8, §13.4, §17.2
- Befund: L-02. NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 103
Deutsch:
Ich weiß, dass der Mann morgen in die Stadt gehen muss.
Orbis:
— nicht eindeutig bildbar: Vim zavam, fai xra valru zirna tel xlan kavlan melex dolmat ODER … dolmat melex. §16.1 verlangt den Infinitiv „am Satzende", §17.2 verlangt das finite Verb am Nebensatzende — beide Regeln beanspruchen dieselbe Position; kein Beispiel entscheidet.
Analyse:
- Satztyp: fai-Nebensatz mit Modalverb + Verbklammer (gezielter Test, Stresstest F)
- Subjekt: vim / xra valru
- Verb: zavam / dolmat + melex
- Person/Numerus: 1. Sg / 3. Sg
- Tempus: Gegenwart
- Nomen: valru, kavla
- Artikel: xra (M Nom), xlan (F Akk)
- Geschlecht: M / F
- Kasus: Nom / Akk (Richtung, tel + Akk §19)
- Adjektive: —
- Präpositionen: tel
- Wortstellung: Endfeld-Reihenfolge Infinitiv↔Modalverb ungeregelt
- Phonotaktik: unkritisch
- verwendete Regeln: §16.1 ↔ §17.2, §19, §20
- Befund: K-05. NICHT entschieden.
- Ergebnis: [REGELKONFLIKT]

## Test 104
Deutsch:
Sie sagt, dass sie kommt.
Orbis:
— nicht ohne Behelf bildbar: Es gibt kein Verb „sagen". tal- ist als „sprechen" definiert (§24.5); „Lo talat, fai lo vandat" verschiebt die Bedeutung ohne Wörterbuchgrundlage. Kein Grammatikproblem, sondern eine Wortschatzlücke des Testkorpus.
Analyse:
- Satztyp: Hauptsatz + fai-Nebensatz (Redeeinleitung)
- Subjekt: lo / lo
- Verb: „sagen" fehlt / vandat
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: Nebensatzmuster wäre regulär (§17.2)
- Phonotaktik: unkritisch
- verwendete Regeln: §17.2, §20, §24.5
- Befund: W-01 (Wortschatzlücke „sagen"; ebenso fehlen z. B. „zeigen", „suchen", „es gibt"). Kein Regelverstoß.
- Ergebnis: [TESTPROBLEM]

## Test 105
Deutsch:
Er weiß, dass sie das Buch nicht lesen kann.
Orbis:
— nicht eindeutig bildbar: Ro zavat, fai lo xnan vreston … — für das Endfeld konkurrieren xa + valnat (finit, §18.3+§17.2) und leşnex (§16.1): „… xa leşnex valnat"? „… leşnex xa valnat"? „… xa valnat leşnex"? Reihenfolge ungeregelt (K-05), Position von xa relativ zum Infinitiv ebenfalls.
Analyse:
- Satztyp: fai-Nebensatz mit Modalverb + Negation (gezielter Test, Stresstest F)
- Subjekt: ro / lo
- Verb: zavat / valnat + leşnex, negiert
- Person/Numerus: 3. Sg / 3. Sg
- Tempus: Gegenwart
- Nomen: vresto
- Artikel: xnan (N Akk)
- Geschlecht: N
- Kasus: Nom / Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: Endfeld ungeregelt (Modal + Infinitiv + xa)
- Phonotaktik: unkritisch
- verwendete Regeln: §16.1 ↔ §17.2 ↔ §18.3, §20
- Befund: K-05 (verschärft durch Negation). NICHT entschieden.
- Ergebnis: [REGELKONFLIKT]

---

## I. MODALVERBKONSTRUKTIONEN (106–115)

## Test 106
Deutsch:
Ich kann gehen.
Orbis:
Vim valnam melex.
Analyse:
- Satztyp: Hauptsatz mit Modalverb + Infinitiv
- Subjekt: vim
- Verb: valnam (valn-, Modal) + melex (Infinitiv)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: Modal Position 2, Infinitiv am Satzende (§16.1) ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §14, §16.1
- Ergebnis: [OK]

## Test 107
Deutsch:
Du musst heute kommen.
Orbis:
Şet dolmaş nunda vandex.
Analyse:
- Satztyp: Hauptsatz, Modalverb + Zeitangabe + Infinitiv (Verbklammer)
- Subjekt: şet
- Verb: dolmaş (dolm-) + vandex
- Person/Numerus: 2. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: Klammer Modal…Infinitiv ✓ (wörtliches Grammatikbeispiel §16.1)
- Phonotaktik: §5-konform
- verwendete Regeln: §16.1, §17.3
- Ergebnis: [OK]

## Test 108
Deutsch:
Er darf das Buch lesen.
Orbis:
Ro vlekat xnan vreston leşnex.
Analyse:
- Satztyp: Hauptsatz, Modalverb + Objekt + Infinitiv
- Subjekt: ro
- Verb: vlekat (vlek-) + leşnex
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: vresto
- Artikel: xnan (N Akk)
- Geschlecht: N
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: Objekt in der Klammer, Infinitiv am Ende ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §16.1, §17.3
- Ergebnis: [OK]

## Test 109
Deutsch:
Wir sollen warten.
Orbis:
Viñ tirnamen maldex.
Analyse:
- Satztyp: Hauptsatz, Modalverb + Infinitiv
- Subjekt: viñ
- Verb: tirnamen (tirn-) + maldex
- Person/Numerus: 1. Pl
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: ✓ §16.1
- Phonotaktik: §5-konform
- verwendete Regeln: §16.1
- Ergebnis: [OK]

## Test 110
Deutsch:
Sie will schlafen.
Orbis:
Lo nestat soñex.
Analyse:
- Satztyp: Hauptsatz, Modalverb + Infinitiv
- Subjekt: lo
- Verb: nestat (nest-) + soñex
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: ✓ §16.1
- Phonotaktik: §5-konform (nest- Coda st §5.3c)
- verwendete Regeln: §16.1
- Ergebnis: [OK]

## Test 111
Deutsch:
Ich mag das Wort.
Orbis:
— nicht eindeutig bildbar: Vim suvram xnan taisan(?) — §16.1 definiert Modalverben nur in der Klammerkonstruktion mit Infinitiv. Ob sie als Vollverb mit direktem Objekt stehen dürfen, ist ungeregelt. (Chat-Korpus 0.1 Satz 111 wertete dies unmarkiert als ✓.)
Analyse:
- Satztyp: Modalverb als Vollverb (gezielter Test)
- Subjekt: vim
- Verb: suvram (suvr-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart
- Nomen: taisa
- Artikel: xnan (N Akk)
- Geschlecht: N
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 wäre erfüllbar
- Phonotaktik: unkritisch (suv-ram; bloße Wurzel suvr- → Imperativ-Stütz-e §14)
- verwendete Regeln: §16.1
- Befund: U-03 — Vollverbgebrauch der Modalverben nicht definiert. NICHT geraten.
- Ergebnis: [REGELUNKLARHEIT]

## Test 112
Deutsch:
Ihr könnt den Berg sehen.
Orbis:
Şeñ valnaşen xran vrondon milkex.
Analyse:
- Satztyp: Hauptsatz, Modal + Objekt + Infinitiv
- Subjekt: şeñ
- Verb: valnaşen (valn-) + milkex
- Person/Numerus: 2. Pl
- Tempus: Gegenwart
- Nomen: vrondo
- Artikel: xran (M Akk)
- Geschlecht: M
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: Klammer ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §16.1, §17.3
- Ergebnis: [OK]

## Test 113
Deutsch:
Sie müssen die Stadt finden.
Orbis:
Oñ dolmaten xlan kavlan traivex.
Analyse:
- Satztyp: Hauptsatz, Modal + Objekt + Infinitiv
- Subjekt: oñ
- Verb: dolmaten (dolm-) + traivex
- Person/Numerus: 3. Pl
- Tempus: Gegenwart
- Nomen: kavla
- Artikel: xlan (F Akk)
- Geschlecht: F
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: Klammer ✓
- Phonotaktik: K-01 (oñ VK); sonst §5-konform
- verwendete Regeln: §8, §11, §16.1, §17.3
- Ergebnis: [OK]

## Test 114
Deutsch:
Können Sie mich hören?
Orbis:
Valnaten şevar vin zaubex?
Analyse:
- Satztyp: Ja/Nein-Frage, Höflichkeitsform, Modal + Infinitiv
- Subjekt: şevar (Höflichkeitspronomen)
- Verb: valnaten (valn-, 3. Pl wegen şevar §13.2) + zaubex
- Person/Numerus: 3. Pl (höflich)
- Tempus: Gegenwart
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom (şevar) + Akk (vin)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V1-Frage + Klammer ✓ (wörtliches §25.1-Beispiel)
- Phonotaktik: §5-konform
- verwendete Regeln: §13.1, §13.2, §16.1, §18.1
- Ergebnis: [OK]

## Test 115
Deutsch:
Das Kind darf nicht gehen.
Orbis:
Xna şirn xa vlekat melex.
Analyse:
- Satztyp: Hauptsatz, negiertes Modalverb + Infinitiv
- Subjekt: xna şirn
- Verb: vlekat (vlek-, negiert) + melex
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: şirn (Kernwort)
- Artikel: xna (N Nom)
- Geschlecht: N
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: xa vor dem finiten Modalverb (§18.3), Infinitiv am Ende (§16.1) — Komposition im Hauptsatz eindeutig ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §16.1, §18.3
- Ergebnis: [OK]

---

## J. VERGANGENHEIT (116–125) — Stresstest J (alle 8 unregelmäßigen Verben)

## Test 116
Deutsch:
Ich ging.
Orbis:
Vim molem.
Analyse:
- Satztyp: Hauptsatz, Vergangenheit
- Subjekt: vim
- Verb: molem (mel-, Ablautstamm mole- §15.2)
- Person/Numerus: 1. Sg
- Tempus: Vergangenheit
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §15.2
- Ergebnis: [OK]

## Test 117
Deutsch:
Du kamst.
Orbis:
Şet vendeş.
Analyse:
- Satztyp: Hauptsatz, Vergangenheit
- Subjekt: şet
- Verb: vendeş (vand-, Ablautstamm vende- §15.2)
- Person/Numerus: 2. Sg
- Tempus: Vergangenheit
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §15.2
- Ergebnis: [OK]

## Test 118
Deutsch:
Er sah den Hund.
Orbis:
Ro milkot xran narkun.
Analyse:
- Satztyp: Hauptsatz, Vergangenheit, regelmäßiges Verb
- Subjekt: ro
- Verb: milkot (milk-, regulär -o- §15)
- Person/Numerus: 3. Sg
- Tempus: Vergangenheit
- Nomen: narku
- Artikel: xran (M Akk)
- Geschlecht: M
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §15
- Ergebnis: [OK]

## Test 119
Deutsch:
Wir wussten es.
Orbis:
Viñ zovemen non.
Analyse:
- Satztyp: Hauptsatz, Vergangenheit
- Subjekt: viñ
- Verb: zovemen (zav-, Ablautstamm zove- §15.2)
- Person/Numerus: 1. Pl
- Tempus: Vergangenheit
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Akk (non)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §13.1, §15.2
- Ergebnis: [OK]

## Test 120
Deutsch:
Sie gaben dem Kind das Brot.
Orbis:
Oñ dolveten xnaş şirneş xnan brasin.
Analyse:
- Satztyp: Hauptsatz, Vergangenheit, Doppelobjekt (Stresstest G)
- Subjekt: oñ
- Verb: dolveten (dalv-, Ablautstamm dolve- §15.2)
- Person/Numerus: 3. Pl
- Tempus: Vergangenheit
- Nomen: şirn (Kernwort), brasi
- Artikel: xnaş (N Dat), xnan (N Akk)
- Geschlecht: N / N
- Kasus: Dat + Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓; Dat vor Akk (U-05)
- Phonotaktik: K-01 (oñ); sonst §5-konform
- verwendete Regeln: §8, §10.3, §11, §15.2
- Ergebnis: [OK]

## Test 121
Deutsch:
Die Nacht war kalt.
Orbis:
Xla kirva girn vot.
Analyse:
- Satztyp: Hauptsatz, Vergangenheit von esex
- Subjekt: xla kirva
- Verb: vot (es-, Vergangenheitsstamm vo- OHNE Bindevokal — §15.2-Formel deckt das nicht, U-01)
- Person/Numerus: 3. Sg
- Tempus: Vergangenheit
- Nomen: kirva
- Artikel: xla (F Nom)
- Geschlecht: F
- Kasus: Nom
- Adjektive: girn (prädikativ, §12.2-Muster → U-13)
- Präpositionen: —
- Wortstellung: wörtliches Grammatikbeispiel §12.2/§25.2
- Phonotaktik: §5-konform
- verwendete Regeln: §12.2, §15.2
- Ergebnis: [OK]

## Test 122
Deutsch:
Ich hatte ein Haus.
Orbis:
Vim novem vnan breunen.
Analyse:
- Satztyp: Hauptsatz, Vergangenheit von nuvex
- Subjekt: vim
- Verb: novem (nuv-, Ablautstamm nove- §15.2)
- Person/Numerus: 1. Sg
- Tempus: Vergangenheit
- Nomen: breun (Kernwort)
- Artikel: vnan (unbest., N, Akk)
- Geschlecht: N
- Kasus: Akk (breunen; regelbasiert — zum abweichenden §18.3-Beispiel siehe Test 083/U-14)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §10.3, §11.2, §15.2
- Ergebnis: [OK]

## Test 123
Deutsch:
Der Mann machte das Fahrzeug.
Orbis:
Xra valru norget xnan meliston.
Analyse:
- Satztyp: Hauptsatz, Vergangenheit von nargex
- Subjekt: xra valru
- Verb: norget (narg-, Ablautstamm norge- §15.2)
- Person/Numerus: 3. Sg
- Tempus: Vergangenheit
- Nomen: melisto (Fahrzeug; mel- + -isto §21.1)
- Artikel: xnan (N Akk)
- Geschlecht: N
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §15.2, §21.1
- Ergebnis: [OK]

## Test 124
Deutsch:
Ihr wartetet.
Orbis:
Şeñ maldoşen.
Analyse:
- Satztyp: Hauptsatz, Vergangenheit, regelmäßig
- Subjekt: şeñ
- Verb: maldoşen (mald-, -o- + -şen)
- Person/Numerus: 2. Pl
- Tempus: Vergangenheit
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §15
- Ergebnis: [OK]

## Test 125
Deutsch:
Wir wurden stark.
Orbis:
Viñ voremen xarn.
Analyse:
- Satztyp: Hauptsatz, Vergangenheit von vurnex + Prädikativ
- Subjekt: viñ
- Verb: voremen (vurn-, Ablautstamm vore- §15.2)
- Person/Numerus: 1. Pl
- Tempus: Vergangenheit
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: xarn (prädikativ nach vurnex §12.2; hier nach dem Verb — Stellung des Prädikativs ist ungeregelt, vgl. U-13)
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §12.2, §15.2
- Ergebnis: [OK]

---

## K. ZUKUNFT (126–135) — Stresstest J (alle 8 unregelmäßigen Futurformen)

## Test 126
Deutsch:
Ich werde gehen.
Orbis:
Vim melaim.
Analyse:
- Satztyp: Hauptsatz, Zukunft (synthetisch)
- Subjekt: vim
- Verb: melaim (mel- + -ai- + -m)
- Person/Numerus: 1. Sg
- Tempus: Zukunft
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (me-laim)
- verwendete Regeln: §15
- Ergebnis: [OK]

## Test 127
Deutsch:
Du wirst kommen.
Orbis:
Şet vandaiş.
Analyse:
- Satztyp: Hauptsatz, Zukunft
- Subjekt: şet
- Verb: vandaiş (vand-, Futur regulär §15.2)
- Person/Numerus: 2. Sg
- Tempus: Zukunft
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §15.2
- Ergebnis: [OK]

## Test 128
Deutsch:
Er wird das Buch lesen.
Orbis:
Ro leşnait xnan vreston.
Analyse:
- Satztyp: Hauptsatz, Zukunft, transitiv
- Subjekt: ro
- Verb: leşnait (leşn-)
- Person/Numerus: 3. Sg
- Tempus: Zukunft
- Nomen: vresto
- Artikel: xnan (N Akk)
- Geschlecht: N
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓ (synthetisches Futur — keine Klammer nötig)
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §15
- Ergebnis: [OK]

## Test 129
Deutsch:
Wir werden warten.
Orbis:
Viñ maldaimen.
Analyse:
- Satztyp: Hauptsatz, Zukunft
- Subjekt: viñ
- Verb: maldaimen (mald-)
- Person/Numerus: 1. Pl
- Tempus: Zukunft
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §15
- Ergebnis: [OK]

## Test 130
Deutsch:
Sie werden das Fahrzeug machen.
Orbis:
Oñ nargaiten xnan meliston.
Analyse:
- Satztyp: Hauptsatz, Zukunft von nargex
- Subjekt: oñ
- Verb: nargaiten (narg-, Futur regulär)
- Person/Numerus: 3. Pl
- Tempus: Zukunft
- Nomen: melisto
- Artikel: xnan (N Akk)
- Geschlecht: N
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: K-01 (oñ); nar-gai-ten §5-konform
- verwendete Regeln: §8, §11, §15.2
- Ergebnis: [OK]

## Test 131
Deutsch:
Das Kind wird stark werden.
Orbis:
Xna şirn vurnait xarn.
Analyse:
- Satztyp: Hauptsatz, Zukunft von vurnex + Prädikativ
- Subjekt: xna şirn
- Verb: vurnait (vurn-, Futur regulär §15.2)
- Person/Numerus: 3. Sg
- Tempus: Zukunft
- Nomen: şirn (Kernwort)
- Artikel: xna (N Nom)
- Geschlecht: N
- Kasus: Nom
- Adjektive: xarn (prädikativ; Stellung nach dem Verb — U-13)
- Präpositionen: —
- Wortstellung: V2 ✓ (das deutsche „wird werden" fällt in Orbis mit dem synthetischen Futur von vurnex zusammen)
- Phonotaktik: §5-konform (vur-nait)
- verwendete Regeln: §12.2, §15.2
- Ergebnis: [OK]

## Test 132
Deutsch:
Morgen werde ich schreiben.
Orbis:
Zirna ruskaim vim.
Analyse:
- Satztyp: Hauptsatz, Zukunft, Zeitangabe auf Position 1
- Subjekt: vim (nach dem Verb — Inversion)
- Verb: ruskaim (rusk-)
- Person/Numerus: 1. Sg
- Tempus: Zukunft
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: Zeitangabe Position 1 → Verb Position 2 → Subjekt Position 3 (§17.1, Muster „Nunda melam vim" §25.1) ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §15, §17.1, §24.9
- Ergebnis: [OK]

## Test 133
Deutsch:
Ihr werdet stark sein.
Orbis:
Şeñ vaişen xarn.
Analyse:
- Satztyp: Hauptsatz, Zukunft von esex + Prädikativ
- Subjekt: şeñ
- Verb: vaişen (es-, Futurstamm vai- §15.2 — suppletiv, U-01)
- Person/Numerus: 2. Pl
- Tempus: Zukunft
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: xarn (prädikativ; U-13)
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (vai-şen)
- verwendete Regeln: §12.2, §15.2
- Ergebnis: [OK]

## Test 134
Deutsch:
Ich werde ein Haus haben.
Orbis:
Vim nuvaim vnan breunen.
Analyse:
- Satztyp: Hauptsatz, Zukunft von nuvex
- Subjekt: vim
- Verb: nuvaim (nuv-, Futur regulär §15.2)
- Person/Numerus: 1. Sg
- Tempus: Zukunft
- Nomen: breun (Kernwort)
- Artikel: vnan (unbest., N, Akk)
- Geschlecht: N
- Kasus: Akk (regelbasiert, vgl. U-14)
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §10.3, §11.2, §15.2
- Ergebnis: [OK]

## Test 135
Deutsch:
Sie wird die Wahrheit wissen.
Orbis:
Lo zavait xlan klaunuman.
Analyse:
- Satztyp: Hauptsatz, Zukunft von zavex, Abstraktum als Objekt
- Subjekt: lo
- Verb: zavait (zav-, Futur regulär)
- Person/Numerus: 3. Sg
- Tempus: Zukunft
- Nomen: klaunuma (Wahrheit, F-C Abstraktum §24.6; klaun + -uma mit Fusion n+? — keine: klaun+uma = klaunuma, Vokal folgt)
- Artikel: xlan (F Akk)
- Geschlecht: F
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (klau-nu-man)
- verwendete Regeln: §8, §11, §15.2, §21.1, §24.6
- Ergebnis: [OK]

---

## L. PASSIV (136–140) — Stresstest E

## Test 136
Deutsch:
Das Haus wird gebaut.
Orbis:
Xna breun şunargat.
Analyse:
- Satztyp: Hauptsatz, Vorgangspassiv
- Subjekt: xna breun (Patiens)
- Verb: şunargat (şu- + narg- §16.3; „bauen" über narg- „machen" — wörtliches Grammatikbeispiel)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: breun (Kernwort)
- Artikel: xna (N Nom)
- Geschlecht: N
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓
- Phonotaktik: §5-konform (şu-nar-gat)
- verwendete Regeln: §16.3, §21.2
- Ergebnis: [OK]

## Test 137
Deutsch:
Das Haus wird vom Mann gebaut.
Orbis:
— nicht bildbar: Xna breun şunargat … (ven xraş valruş?) — wie der Agens ausgedrückt wird, definiert §16.3 nicht; keine Präposition ist dafür ausgewiesen.
Analyse:
- Satztyp: Vorgangspassiv mit Agens (gezielter Test)
- Subjekt: xna breun (Patiens)
- Verb: şunargat
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: breun, valru
- Artikel: xna (N Nom); Agensphrase offen
- Geschlecht: N / M
- Kasus: Agens-Kasus unbestimmt
- Adjektive: —
- Präpositionen: keine für Agens definiert (ven „mit" läge nahe — wäre aber Festlegung)
- Wortstellung: —
- Phonotaktik: unkritisch
- verwendete Regeln: §16.3, §19
- Befund: L-05. NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 138
Deutsch:
Das Buch wurde von der Frau gelesen.
Orbis:
— nicht bildbar: Xna vresto şuleşnot … — die Passiv-Vergangenheit selbst ist regulär bildbar (şu- + leşn- + -o- + -t), aber der Agens „von der Frau" hat keine definierte Form (L-05).
Analyse:
- Satztyp: Vorgangspassiv Vergangenheit mit Agens (gezielter Test)
- Subjekt: xna vresto (Patiens)
- Verb: şuleşnot (şu- + leşn- + Vergangenheit)
- Person/Numerus: 3. Sg
- Tempus: Vergangenheit
- Nomen: vresto, sarla
- Artikel: xna (N Nom); Agensphrase offen
- Geschlecht: N / F
- Kasus: Agens-Kasus unbestimmt
- Adjektive: —
- Präpositionen: keine für Agens definiert
- Wortstellung: —
- Phonotaktik: unkritisch
- verwendete Regeln: §15, §16.3
- Befund: L-05. NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 139
Deutsch:
Das Wort ist gesprochen.
Orbis:
Xna taisa şutalut est.
Analyse:
- Satztyp: Zustandspassiv (Partizip + esex §16.3)
- Subjekt: xna taisa
- Verb: est (es-) + şutalut (Partizip von şu-tal-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart
- Nomen: taisa
- Artikel: xna (N Nom)
- Geschlecht: N
- Kasus: Nom
- Adjektive: — (Partizip prädikativ, belegtes Muster „şunargut est")
- Präpositionen: —
- Wortstellung: Muster §16.3 ✓
- Phonotaktik: K-01 (est); şu-ta-lut §5-konform
- verwendete Regeln: §14, §16.3
- Ergebnis: [OK]

## Test 140
Deutsch:
Die Bücher werden gelesen.
Orbis:
Xnañ vrestoñ şuleşnaten.
Analyse:
- Satztyp: Vorgangspassiv Plural
- Subjekt: xnañ vrestoñ
- Verb: şuleşnaten (şu- + leşn-, 3. Pl)
- Person/Numerus: 3. Pl
- Tempus: Gegenwart
- Nomen: vresto → vrestoñ
- Artikel: xnañ (N Nom Pl)
- Geschlecht: N
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓; Kongruenz Patiens-Plural ↔ Verb 3. Pl ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §9, §11, §16.3
- Ergebnis: [OK]

---

## M. MAI / KONDITIONAL (141–145)

## Test 141
Deutsch:
Ich würde gehen.
Orbis:
Vim mai melam.
Analyse:
- Satztyp: Hauptsatz, Möglichkeitsform
- Subjekt: vim
- Verb: mai melam (mai + finites Verb = eine Einheit §16.2)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart (+ mai)
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 ✓ (mai+Verb als eine Satzposition; wörtliches Grammatikbeispiel)
- Phonotaktik: §5-konform
- verwendete Regeln: §16.2
- Ergebnis: [OK]

## Test 142
Deutsch:
Wenn ich ein Haus hätte, würde ich bleiben.
Orbis:
Tund vim vnan breunen mai num, mai stanam vim.
Analyse:
- Satztyp: Konditionalgefüge (tund-Nebensatz + Hauptsatz, beide mit mai)
- Subjekt: vim / vim
- Verb: mai num (nuv-) / mai stanam (stan-)
- Person/Numerus: 1. Sg
- Tempus: Gegenwart (+ mai beidseitig, Muster §16.2/§25.1)
- Nomen: breun (Kernwort)
- Artikel: vnan (unbest., N, Akk)
- Geschlecht: N
- Kasus: Akk (breunen — regelbasiert; das §16.2-Beispiel „vra vlaidra valru mai em" betrifft ein Prädikatsnomen im Nominativ, keinen Objektfall)
- Adjektive: —
- Präpositionen: —
- Wortstellung: Nebensatz: mai+Verb am Ende ✓; Hauptsatz: Nebensatz Position 1, mai+Verb Position 2, Subjekt danach ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §10.3, §11.2, §15.2, §16.2, §17.1, §17.2
- Ergebnis: [OK]

## Test 143
Deutsch:
Wenn die Nacht kalt wäre, würden wir warten.
Orbis:
Tund xla kirva girn mai est, mai maldamen viñ.
Analyse:
- Satztyp: Konditionalgefüge
- Subjekt: xla kirva / viñ
- Verb: mai est (es-) / mai maldamen (mald-)
- Person/Numerus: 3. Sg / 1. Pl
- Tempus: Gegenwart (+ mai)
- Nomen: kirva
- Artikel: xla (F Nom)
- Geschlecht: F
- Kasus: Nom
- Adjektive: girn (prädikativ vor mai+Verb am Nebensatzende)
- Präpositionen: —
- Wortstellung: ✓ Muster §16.2
- Phonotaktik: K-01 (est); sonst §5-konform
- verwendete Regeln: §12.2, §15.2, §16.2, §17.2
- Ergebnis: [OK]

## Test 144
Deutsch:
Er würde das Buch lesen.
Orbis:
Ro mai leşnat xnan vreston.
Analyse:
- Satztyp: Hauptsatz, Möglichkeitsform, transitiv
- Subjekt: ro
- Verb: mai leşnat (leşn-)
- Person/Numerus: 3. Sg
- Tempus: Gegenwart (+ mai)
- Nomen: vresto
- Artikel: xnan (N Akk)
- Geschlecht: N
- Kasus: Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: V2 (mai+Verb Position 2) ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §16.2
- Ergebnis: [OK]

## Test 145
Deutsch:
Ich könnte gehen.
Orbis:
Vim mai valnam melex.
Analyse:
- Satztyp: Hauptsatz, mai + Modalverb + Infinitiv (Kombinationstest)
- Subjekt: vim
- Verb: mai valnam (valn-) + melex
- Person/Numerus: 1. Sg
- Tempus: Gegenwart (+ mai)
- Nomen: —
- Artikel: —
- Geschlecht: —
- Kasus: Nom
- Adjektive: —
- Präpositionen: —
- Wortstellung: mai unmittelbar vor dem finiten Modalverb (§16.2), Infinitiv am Satzende (§16.1) — Komposition im Hauptsatz eindeutig ✓ (Kombination in 0.9.3 nicht belegt, aber widerspruchsfrei ableitbar)
- Phonotaktik: §5-konform
- verwendete Regeln: §16.1, §16.2
- Ergebnis: [OK]

---

## N. KOMPLEXE SÄTZE (146–150)

## Test 146
Deutsch:
Ich weiß, dass der große Mann dem Kind morgen das Brot geben wird.
Orbis:
Vim zavam, fai xra vlaidra valru zirna xnaş şirneş xnan brasin dalvait.
Analyse:
- Satztyp: fai-Nebensatz mit Adjektiv, Doppelobjekt, Zeitangabe, Zukunft
- Subjekt: vim / xra vlaidra valru
- Verb: zavam / dalvait (dalv-, Futur — synthetisch, daher KEINE Klammerkollision im Nebensatz)
- Person/Numerus: 1. Sg / 3. Sg
- Tempus: Gegenwart / Zukunft
- Nomen: valru, şirn (Kernwort), brasi
- Artikel: xra (M Nom), xnaş (N Dat), xnan (N Akk)
- Geschlecht: M / N / N
- Kasus: Nom + Dat + Akk (Stresstest G im Nebensatz)
- Adjektive: vlaidra (attributiv M Nom)
- Präpositionen: —
- Wortstellung: Verbendstellung ✓; Zeit vor Objekten (§17.4-Tendenz); Dat vor Akk (U-05)
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §10.3, §11, §12.1, §15.2, §17.2, §17.4, §20
- Ergebnis: [OK]

## Test 147
Deutsch:
Obwohl die Nacht kalt war, gingen die Wanderer über den Berg.
Orbis:
Şlani xla kirva girn vot, moleten xrañ melruñ span xran vrondon.
Analyse:
- Satztyp: şlani-Nebensatz (Vergangenheit) + Hauptsatz mit Richtungsangabe
- Subjekt: xla kirva / xrañ melruñ
- Verb: vot (es-) / moleten (mel-)
- Person/Numerus: 3. Sg / 3. Pl
- Tempus: Vergangenheit / Vergangenheit
- Nomen: kirva, melru → melruñ, vrondo
- Artikel: xla (F Nom), xrañ (M Nom Pl), xran (M Akk)
- Geschlecht: F / M / M
- Kasus: Nom / Nom Pl / Akk (Richtung: span + Akk §19)
- Adjektive: girn (prädikativ)
- Präpositionen: span (über)
- Wortstellung: Nebensatz Position 1 → Hauptsatzverb direkt danach ✓; Hauptsatzteil = §25.1-Muster („Xrañ melruñ moleten span xran vrondon")
- Phonotaktik: K-01 (vot regulär, kein Befund; girn ok); §5-konform
- verwendete Regeln: §9, §11, §12.2, §15.2, §17.1, §17.2, §19, §20
- Ergebnis: [OK]

## Test 148
Deutsch:
Wenn du das Buch des Freundes liest, wirst du die Wahrheit finden.
Orbis:
Tund şet xnan vreston xras velkras leşnaş, traivaiş şet xlan klaunuman.
Analyse:
- Satztyp: tund-Nebensatz mit Genitivattribut + Hauptsatz Zukunft
- Subjekt: şet / şet
- Verb: leşnaş / traivaiş (traiv-, Futur)
- Person/Numerus: 2. Sg / 2. Sg
- Tempus: Gegenwart / Zukunft
- Nomen: vresto, velkra, klaunuma
- Artikel: xnan (N Akk), xras (M Gen), xlan (F Akk)
- Geschlecht: N / M / F
- Kasus: Akk + Gen (Attribut, nachgestellt nach Beispielpraxis → L-01) + Akk
- Adjektive: —
- Präpositionen: —
- Wortstellung: Nebensatz-Endstellung ✓; Nebensatz Position 1 → Hauptsatzverb danach ✓
- Phonotaktik: §5-konform
- verwendete Regeln: §8, §11, §15, §17.1, §17.2, §20, §24.6
- Ergebnis: [OK]

## Test 149
Deutsch:
Der Mann, der gestern kam, gab dem Kind das Brot des Hauses.
Orbis:
— nicht bildbar: Der eingebettete Relativsatz („der gestern kam") scheitert an L-02 (kein Relativsatzbau); der Rest (Xra valru … dolvet xnaş şirneş xnan brasin xnas breunes) wäre regulär, hängt beim Genitivattribut zusätzlich an L-01.
Analyse:
- Satztyp: Relativsatz eingebettet + Doppelobjekt + Genitivattribut (Maximaltest)
- Subjekt: xra valru (+ Relativsatz)
- Verb: (Relativsatz:) vendet / (Hauptsatz:) dolvet
- Person/Numerus: 3. Sg
- Tempus: Vergangenheit
- Nomen: valru, şirn, brasi, breun
- Artikel: xra, xnaş, xnan, xnas
- Geschlecht: M / N / N / N
- Kasus: Nom + Dat + Akk + Gen
- Adjektive: —
- Präpositionen: —
- Wortstellung: Relativsatz ungeregelt (L-02)
- Phonotaktik: unkritisch
- verwendete Regeln: §8, §10.3, §13.4, §15.2, §17.2
- Befund: L-02 (primär), L-01 (berührt). NICHT geraten.
- Ergebnis: [REGELLÜCKE]

## Test 150
Deutsch:
Wir können nicht schlafen, weil der Sturm über der Stadt sehr stark ist.
Orbis:
Viñ xa valnamen soñex, grali xra morda span xlaş kavlaş vran xarn est.
Analyse:
- Satztyp: negiertes Modalverb + Infinitiv + grali-Nebensatz mit Präpositionalattribut und Gradpartikel
- Subjekt: viñ / xra morda
- Verb: valnamen (negiert) + soñex / est
- Person/Numerus: 1. Pl / 3. Sg
- Tempus: Gegenwart
- Nomen: morda (Sturm), kavla
- Artikel: xra (M Nom), xlaş (F Dat)
- Geschlecht: M / F
- Kasus: Nom / Dat (Ort: span + Dat §19)
- Adjektive: xarn (prädikativ), verstärkt durch vran (sehr §24.9; Muster „vran luid est" §25.1)
- Präpositionen: span (über)
- Wortstellung: Hauptsatz: xa + Modal, Infinitiv am Ende ✓ (Muster §25.1 „Vim xa valnam soñex, grali …"); Nebensatz: Verbendstellung ✓
- Phonotaktik: K-01 (est); sonst §5-konform
- verwendete Regeln: §12.2, §16.1, §17.2, §18.3, §19, §20, §24.9
- Ergebnis: [OK]

---

## ANHANG 1 — PRÜFTABELLE: ALLE 45 NOMENENDUNGEN (Stresstest I)

Träger ist der ausdrücklich markierte [TESTFORM]-Stamm **pren-** (phonotaktisch zulässig: pren = KKVK). Diese 45 Formen sind KEINE Wörter des Wortschatzes — sie existieren ausschließlich zum morphologischen Test von §7–§9. Erzeugt und geprüft mit `orbis_validator.py --tables`.

| Klasse | Endung | Nom Sg | Akk Sg | Dat Sg | Gen Sg | Nom Pl | Akk Pl | Dat Pl | Gen Pl |
|---|---|---|---|---|---|---|---|---|---|
| M-A | -ra | prenra | prenran | prenraş | prenras | prenrañ | prenrañan | prenrañaş | prenrañas |
| M-A | -re | prenre | prenren | prenreş | prenres | prenreñ | prenreñen | prenreñeş | prenreñes |
| M-A | -ri | prenri | prenrin | prenriş | prenris | prenriñ | prenriñin | prenriñiş | prenriñis |
| M-A | -ro | prenro | prenron | prenroş | prenros | prenroñ | prenroñon | prenroñoş | prenroños |
| M-A | -ru | prenru | prenrun | prenruş | prenrus | prenruñ | prenruñun | prenruñuş | prenruñus |
| M-B | -ka | prenka | prenkan | prenkaş | prenkas | prenkañ | prenkañan | prenkañaş | prenkañas |
| M-B | -ke | prenke | prenken | prenkeş | prenkes | prenkeñ | prenkeñen | prenkeñeş | prenkeñes |
| M-B | -ki | prenki | prenkin | prenkiş | prenkis | prenkiñ | prenkiñin | prenkiñiş | prenkiñis |
| M-B | -ko | prenko | prenkon | prenkoş | prenkos | prenkoñ | prenkoñon | prenkoñoş | prenkoños |
| M-B | -ku | prenku | prenkun | prenkuş | prenkus | prenkuñ | prenkuñun | prenkuñuş | prenkuñus |
| M-C | -da | prenda | prendan | prendaş | prendas | prendañ | prendañan | prendañaş | prendañas |
| M-C | -de | prende | prenden | prendeş | prendes | prendeñ | prendeñen | prendeñeş | prendeñes |
| M-C | -di | prendi | prendin | prendiş | prendis | prendiñ | prendiñin | prendiñiş | prendiñis |
| M-C | -do | prendo | prendon | prendoş | prendos | prendoñ | prendoñon | prendoñoş | prendoños |
| M-C | -du | prendu | prendun | prenduş | prendus | prenduñ | prenduñun | prenduñuş | prenduñus |
| F-A | -la | prenla | prenlan | prenlaş | prenlas | prenlañ | prenlañan | prenlañaş | prenlañas |
| F-A | -le | prenle | prenlen | prenleş | prenles | prenleñ | prenleñen | prenleñeş | prenleñes |
| F-A | -li | prenli | prenlin | prenliş | prenlis | prenliñ | prenliñin | prenliñiş | prenliñis |
| F-A | -lo | prenlo | prenlon | prenloş | prenlos | prenloñ | prenloñon | prenloñoş | prenloños |
| F-A | -lu | prenlu | prenlun | prenluş | prenlus | prenluñ | prenluñun | prenluñuş | prenluñus |
| F-B | -va | prenva | prenvan | prenvaş | prenvas | prenvañ | prenvañan | prenvañaş | prenvañas |
| F-B | -ve | prenve | prenven | prenveş | prenves | prenveñ | prenveñen | prenveñeş | prenveñes |
| F-B | -vi | prenvi | prenvin | prenviş | prenvis | prenviñ | prenviñin | prenviñiş | prenviñis |
| F-B | -vo | prenvo | prenvon | prenvoş | prenvos | prenvoñ | prenvoñon | prenvoñoş | prenvoños |
| F-B | -vu | prenvu | prenvun | prenvuş | prenvus | prenvuñ | prenvuñun | prenvuñuş | prenvuñus |
| F-C | -ma | prenma | prenman | prenmaş | prenmas | prenmañ | prenmañan | prenmañaş | prenmañas |
| F-C | -me | prenme | prenmen | prenmeş | prenmes | prenmeñ | prenmeñen | prenmeñeş | prenmeñes |
| F-C | -mi | prenmi | prenmin | prenmiş | prenmis | prenmiñ | prenmiñin | prenmiñiş | prenmiñis |
| F-C | -mo | prenmo | prenmon | prenmoş | prenmos | prenmoñ | prenmoñon | prenmoñoş | prenmoños |
| F-C | -mu | prenmu | prenmun | prenmuş | prenmus | prenmuñ | prenmuñun | prenmuñuş | prenmuñus |
| N-A | -na | prenna | prennan | prennaş | prennas | prennañ | prennañan | prennañaş | prennañas |
| N-A | -ne | prenne | prennen | prenneş | prennes | prenneñ | prenneñen | prenneñeş | prenneñes |
| N-A | -ni | prenni | prennin | prenniş | prennis | prenniñ | prenniñin | prenniñiş | prenniñis |
| N-A | -no | prenno | prennon | prennoş | prennos | prennoñ | prennoñon | prennoñoş | prennoños |
| N-A | -nu | prennu | prennun | prennuş | prennus | prennuñ | prennuñun | prennuñuş | prennuñus |
| N-B | -sa | prensa | prensan | prensaş | prensas | prensañ | prensañan | prensañaş | prensañas |
| N-B | -se | prense | prensen | prenseş | prenses | prenseñ | prenseñen | prenseñeş | prenseñes |
| N-B | -si | prensi | prensin | prensiş | prensis | prensiñ | prensiñin | prensiñiş | prensiñis |
| N-B | -so | prenso | prenson | prensoş | prensos | prensoñ | prensoñon | prensoñoş | prensoños |
| N-B | -su | prensu | prensun | prensuş | prensus | prensuñ | prensuñun | prensuñuş | prensuñus |
| N-C | -ta | prenta | prentan | prentaş | prentas | prentañ | prentañan | prentañaş | prentañas |
| N-C | -te | prente | prenten | prenteş | prentes | prenteñ | prenteñen | prenteñeş | prenteñes |
| N-C | -ti | prenti | prentin | prentiş | prentis | prentiñ | prentiñin | prentiñiş | prentiñis |
| N-C | -to | prento | prenton | prentoş | prentos | prentoñ | prentoñon | prentoñoş | prentoños |
| N-C | -tu | prentu | prentun | prentuş | prentus | prentuñ | prentuñun | prentuñuş | prentuñus |
Befund: Alle 45 Endungen deklinieren mechanisch fehlerfrei über alle vier Fälle und den Plural (Echovokal = Themavokal, U-09). Alle 360 erzeugten Formen (45 Endungen × 8 = volle Kasus-/Numerus-Matrix) sind §5-konform (maschinell geprüft); keine Kollision zwischen Endung und Marker.

## ANHANG 2 — VERBPARADIGMEN (Stresstest J)

### Regelmäßiges Verb milk- „sehen“: 6 Personen x 3 Zeiten

| Person | Gegenwart | Vergangenheit | Zukunft |
|---|---|---|---|
| 1. Sg | milkam | milkom | milkaim |
| 2. Sg | milkaş | milkoş | milkaiş |
| 3. Sg | milkat | milkot | milkait |
| 1. Pl | milkamen | milkomen | milkaimen |
| 2. Pl | milkaşen | milkoşen | milkaişen |
| 3. Pl | milkaten | milkoten | milkaiten |

### Die 8 unregelmäßigen Verben (vollständig, alle 6 Personen x 3 Zeiten)

**esex** (sein):

| Person | Gegenwart | Vergangenheit | Zukunft |
|---|---|---|---|
| 1. Sg | em | vom | vaim |
| 2. Sg | eş | voş | vaiş |
| 3. Sg | est | vot | vait |
| 1. Pl | emen | vomen | vaimen |
| 2. Pl | eşen | voşen | vaişen |
| 3. Pl | esten | voten | vaiten |

**nuvex** (haben):

| Person | Gegenwart | Vergangenheit | Zukunft |
|---|---|---|---|
| 1. Sg | num | novem | nuvaim |
| 2. Sg | nuş | noveş | nuvaiş |
| 3. Sg | nut | novet | nuvait |
| 1. Pl | numen | novemen | nuvaimen |
| 2. Pl | nuşen | noveşen | nuvaişen |
| 3. Pl | nuten | noveten | nuvaiten |

**vurnex** (werden):

| Person | Gegenwart | Vergangenheit | Zukunft |
|---|---|---|---|
| 1. Sg | vurm | vorem | vurnaim |
| 2. Sg | vurş | voreş | vurnaiş |
| 3. Sg | vurt | voret | vurnait |
| 1. Pl | vurmen | voremen | vurnaimen |
| 2. Pl | vurşen | voreşen | vurnaişen |
| 3. Pl | vurten | voreten | vurnaiten |

**melex** (gehen):

| Person | Gegenwart | Vergangenheit | Zukunft |
|---|---|---|---|
| 1. Sg | melam | molem | melaim |
| 2. Sg | melaş | moleş | melaiş |
| 3. Sg | melat | molet | melait |
| 1. Pl | melamen | molemen | melaimen |
| 2. Pl | melaşen | moleşen | melaişen |
| 3. Pl | melaten | moleten | melaiten |

**vandex** (kommen):

| Person | Gegenwart | Vergangenheit | Zukunft |
|---|---|---|---|
| 1. Sg | vandam | vendem | vandaim |
| 2. Sg | vandaş | vendeş | vandaiş |
| 3. Sg | vandat | vendet | vandait |
| 1. Pl | vandamen | vendemen | vandaimen |
| 2. Pl | vandaşen | vendeşen | vandaişen |
| 3. Pl | vandaten | vendeten | vandaiten |

**nargex** (machen):

| Person | Gegenwart | Vergangenheit | Zukunft |
|---|---|---|---|
| 1. Sg | nargam | norgem | nargaim |
| 2. Sg | nargaş | norgeş | nargaiş |
| 3. Sg | nargat | norget | nargait |
| 1. Pl | nargamen | norgemen | nargaimen |
| 2. Pl | nargaşen | norgeşen | nargaişen |
| 3. Pl | nargaten | norgeten | nargaiten |

**zavex** (wissen):

| Person | Gegenwart | Vergangenheit | Zukunft |
|---|---|---|---|
| 1. Sg | zavam | zovem | zavaim |
| 2. Sg | zavaş | zoveş | zavaiş |
| 3. Sg | zavat | zovet | zavait |
| 1. Pl | zavamen | zovemen | zavaimen |
| 2. Pl | zavaşen | zoveşen | zavaişen |
| 3. Pl | zavaten | zoveten | zavaiten |

**dalvex** (geben):

| Person | Gegenwart | Vergangenheit | Zukunft |
|---|---|---|---|
| 1. Sg | dalvam | dolvem | dalvaim |
| 2. Sg | dalvaş | dolveş | dalvaiş |
| 3. Sg | dalvat | dolvet | dalvait |
| 1. Pl | dalvamen | dolvemen | dalvaimen |
| 2. Pl | dalvaşen | dolveşen | dalvaişen |
| 3. Pl | dalvaten | dolveten | dalvaiten |

Befund: Die Generatoren reproduzieren alle in §15.2 belegten Tabellenformen exakt; die Formelbeschreibung in §15.2 deckt es-/nuv-/vurn- nicht (U-01). Korpusabdeckung: alle 8 Vergangenheitsformen (Tests 116–125), alle 8 Futurformen (Tests 126–135, 146), Präsensformen verteilt über die Blöcke A–I (narg- Präsens nur als şunargat, Test 136).

---

## ERGEBNISÜBERSICHT

| Ergebnis | Anzahl | Tests |
|---|---|---|
| [OK] | 130 | alle übrigen |
| [REGELLÜCKE] | 14 | 033, 035 (L-04) · 036, 039 (L-01) · 070 (L-08) · 074, 075, 076 (L-03) · 100, 101, 102, 149 (L-02) · 137, 138 (L-05) |
| [REGELKONFLIKT] | 3 | 060 (K-04) · 103, 105 (K-05) |
| [REGELUNKLARHEIT] | 2 | 051 (U-02) · 111 (U-03) |
| [TESTPROBLEM] | 1 | 104 (W-01 — „sagen“ fehlt im Wortschatz) |

Statistik, Prioritäten und Gesamturteil: `Orbis-Testbericht-0_1.md`.
