# ORBIS — Audit 0.1

*Strukturierte Prüfbasis der Referenzgrammatik `Orbis-Grammatik-0.9.3.md`. Kein Grammatikdokument — eine Bestandsaufnahme. Die Grammatik 0.9.3 bleibt unverändert (READ ONLY).*

**Methode:** Jede Regel ist so erfasst, wie sie in 0.9.3 steht, mit Paragraphenverweis. Nichts wurde ergänzt. Wo eine benötigte Regel fehlt: **[REGELLÜCKE]**. Wo zwei bestehende Regeln einander widersprechen: **[REGELKONFLIKT]**. Wo eine Regel nur unklar formuliert ist: **[REGELUNKLARHEIT]**.

**Befund-IDs:** Jeder Befund trägt eine ID (K = Konflikt, L = Lücke, U = Unklarheit). Testkorpus, Validator-Bericht und Testbericht verweisen auf diese IDs. Sammelregister am Ende dieses Dokuments (§A).

**Maschinenlesbare Fassung:** Alle hier erfassten Bestände (Phoneme, Cluster, Endungen, Lexikon, Paradigmen) sind 1:1 in `orbis_validator.py` (Teil 1, „Regeldaten") kodiert.

---

## 1. PHONEMINVENTAR (§2)

**19 Konsonanten (§2.1):**

| Gruppe | Laute |
|---|---|
| Stimmlose Verschlusslaute | p t k |
| Stimmhafte Verschlusslaute | b d g |
| Affrikate | ç |
| Stimmlose Reibelaute | f s ş x |
| Stimmhafte Reibelaute | v z j |
| Nasale | m n ñ |
| Fließlaute | l r |

Explizit nicht vorhanden: h, w, th, pf, ts, ng als eigener Laut.

**5 Vokale (§2.2):** a e i o u — voll, kein Schwa.

**Diphthonge (§2.3):**

| Diphthong | Status |
|---|---|
| ai au ei ui eu | belegt und notwendig |
| oi | regulär, schreibbar, derzeit unbelegt |
| ou | [NOCH ZU ENTSCHEIDEN] (kein Befund — in 0.9.3 ausdrücklich offen) |

Prüfregel: 6 zulässige Diphthonge (5 belegt + oi). *eu* ist nur durch **ein** Wort belegt (*breun*).

**Klanggruppen (§3.2):** Fließlaute l r n m ñ v z s j · Härtelaute p t k b d g f x ş ç. — §3.3 (verbindlich) vs. §3.4 (Richtlinien, nur lexikalischer Stamm, §3.5) ist sauber getrennt; kein Befund.

---

## 2. SILBENSTRUKTUR (§5)

### 2.1 Silbenformen (§5.1)

Wörtlich erlaubt: **V · KV · KVK · KKV · KKVK · KVKK** (letzteres selten). §3.3 verweist verbindlich auf genau diese Liste.

> **[REGELKONFLIKT K-01] §5.1 vs. eingefrorener Wortschatz und grammatikeigene Formen.**
> Die Liste enthält weder **VK/VKK** (vokalisch anlautende geschlossene Silben) noch **KKVKK** (Zweieronset + Zweiercoda). Beides wird vom Lexikon und von den eigenen Beispielen der Grammatik benötigt:
> - **VK/VKK:** *aul* (Kernwort), *eird* (Kernwort, alle Formen: *eirden, eirdes …*), *ain* (ja), *oñ* (sie Pl.), Verbformen *em, eş, est* (§15.2), Kompositum *aulmelna*, Wurzel *es-*.
> - **KKVKK:** *granz* (alt), *trelm* (lang), *vresn* (schwach), *skirm* (wenig), *prilm* (Handwerk), Wurzeln *prens-, dremn-, vlent-*; flektiert z. B. *trelmrañan* (§25.2). §5.3 nennt *granz* und *prens* sogar selbst als Coda-Beispiele — die Coda-Regel setzt also Silbenformen voraus, die §5.1 nicht führt.
> Automatischer Nachweis: `orbis_validator.py --lexicon` und `--examples` (Befundklasse „§5.1-BEFUND").

### 2.2 Anfangsgruppen (§5.2)

Maximal zwei Konsonanten, geschlossene Liste (25):
**tr dr kr gr pr br pl bl fl vl fr vr vn sl şl şr sk st sp xr xl xn zv gl kl**

Belegt im Lexikon: tr dr kr gr pr br vl vr vn sl→(unbelegt) şl sk st sp xr xl xn zv gl kl pl.
Unbelegt (aber zulässig): **sl, şr, fl, bl**; *fr* nur im §5.3-Beispielwort *frisk*, das nicht im Wortschatz steht (siehe Testbericht, Phase 7). Drei und mehr Konsonanten: ausnahmslos verboten. Kein Befund an der Liste selbst.

### 2.3 Endgruppen (§5.3)

Maximal zwei Konsonanten. Zweiergruppe erlaubt, wenn (a) erster Laut ∈ {l r m n}, oder (b) zweiter Laut = s, oder (c) Gruppe ∈ {şn, sn, sk, st}. — Regel ist eindeutig und maschinell prüfbar. Kein Befund an der Regel; zum Konflikt mit §5.1 siehe K-01.

### 2.4 Silbengrenzen

> **[REGELLÜCKE L-09] Keine Silbifizierungs-Präferenzregel.**
> §5 erlaubt Silbenformen, legt aber nirgends fest, wie eine Lautkette in Silben **zerlegt** wird (z. B. Onset-Maximierung). *mela* ist als *me-la* und *mel-a* regelkonform, *kavla* als *kav-la* und *ka-vla*, *drovna* als *drov-na* und *dro-vna*, *vresto* als *vres-to*, *vre-sto* und *vrest-o*. Für Aussprache und Betonung ist das folgenlos, für **Orbis Manus** (§26) und die Tastatur (§26.8) nicht: dieselbe Standardschreibung hat mehrere zulässige Manus-Schreibungen. Quantifizierung: 77 von 281 Grundformen des Lexikons sind mehrdeutig zerlegbar (`orbis_validator.py --manus`; Details im Manus-Schreibtest 0.1).

---

## 3. NOMEN: KLASSEN UND ENDUNGEN (§6–§7)

**Prinzip:** Klassenkonsonant (Geschlecht) + Themavokal. Ca. 90 % zeigen ihr Geschlecht an der Endung.

**Die 45 regulären Endungen (§7):** 9 Klassenkonsonanten × 5 Themavokale:

| Geschlecht | A | B | C |
|---|---|---|---|
| Maskulin | r | k | d |
| Feminin | l | v | m |
| Neutrum | n | s | t |

Je Konsonant: -Ca -Ce -Ci -Co -Cu. Merksatz: r-k-d männlich, l-v-m weiblich, n-s-t sächlich. Unterklassenbedeutung (§7.4): Tendenz, endgültige Funktion [NOCH ZU ENTSCHEIDEN] — offen, aber kein Prüfbefund.

---

## 4. DIE VIER FÄLLE (§8)

Stamm + Klassenkonsonant + Themavokal + Kasusmarker: **Nom — · Akk -n · Dat -ş · Gen -s**. Belegt durch Volltabellen (*valru, sarla, milne*). Eindeutig, maschinell prüfbar. Kein Befund.

---

## 5. PLURAL (§9)

Marker **-ñ-** zwischen Themavokal und Kasusmarker, oblique mit „Echovokal": *valruñ, valruñun, valruñuş, valruñus; sarlañan; milneñeş*.

> **[REGELUNKLARHEIT U-09] „Echovokal" ist nirgends definiert.**
> Aus den Tabellen ergibt sich: Echovokal = Themavokal des Nomens (u→u, a→a, e→e); beim Artikel und Adjektiv immer a. Als Regel formuliert ist das nicht — die Tabellen tragen die Definition allein. Für neue Wörter mit anderen Themavokalen (i, o) ist das Muster nur per Analogie ableitbar (*larkiñiş, vrestoñon* kommen so im Testkorpus vor und funktionieren).

Historische Nebenform: Kernwort-Plural **-ei** (§9/§10.3). Kein Konflikt zwischen beiden Systemen (getestet, s. Testkorpus E).

---

## 6. UNREGELMÄSSIGE NOMEN (§10)

### 6.1 10-Prozent-Gruppe (§10.1)

*velkran* (n, Freundschaft), *soralm* (f, Denkmal), *prilm* (f, Handwerk) — Endvokal geschwunden, Geschlecht am Restkonsonanten erkennbar. Deklination Singular mit Bindevokal **-e-**: *velkran, velkranen, velkraneş, velkranes*.

> **[REGELLÜCKE L-07] Plural der 10-Prozent-Gruppe undefiniert.**
> §10.1 regelt nur den Singular. Regulärer Plural (-ñ- nach Themavokal) ist mangels Themavokal unanwendbar (\**velkranñ*), der Kernwortplural **-ei** ist laut §9 ausdrücklich den 15 Kernwörtern vorbehalten. „Die Freundschaften", „die Denkmäler" sind derzeit nicht bildbar.

### 6.2 Die 15 Kernwörter (§10.2–10.3, §24.1)

kaun (m) · veiş (f) · draun (m) · şirn (n) · aul (n) · xerp (m) · luiv (f) · grein (f) · nauş (f) · virn (n) · moks (m) · eird (f) · şaul (m) · taiv (f) · breun (n)

Deklination: Singular **+ -e- + Marker** (Nom endungslos), Plural **+ -ei + Marker**. Bindevokal immer -e- (*aulan, eirdas* ausdrücklich falsch). Vollständig geregelt, maschinell prüfbar. Kein Befund an der Deklination. (*aul, eird* betrifft K-01 auf Silbenebene.)

---

## 7. ARTIKEL (§11)

Bestimmtheitszeichen (x- bestimmt, v- unbestimmt) + Geschlechtskonsonant der A-Reihe (r/l/n) + -a + Marker.

| | M | F | N |
|---|---|---|---|
| bestimmt | xra… | xla… | xna… |
| unbestimmt | vra… | vla… | vna… |

Plural nur beim bestimmten Artikel (xrañ, xrañan, xrañaş, xrañas usw. mit Echovokal a); **im Plural steht kein unbestimmter Artikel** (§11.2). Der Artikel zeigt **nur das Geschlecht, nie die Unterklasse** (§11.3, immer A-Reihe). Bei Kernwörtern gilt das Wörterbuchgeschlecht. Vollständig geregelt; kein Befund.

Randnotiz Phase 7: **vran** (unbest. Artikel M Akk) ist formgleich mit **vran** „sehr" (§24.9) — Homonymie, siehe Testbericht.

---

## 8. ADJEKTIVE (§12)

### 8.1 Attributiv (§12.1)

Stamm + r/l/n + a + Kasus-/Pluralmarker (Muster identisch mit Artikel-A-Reihe). Fugenregel bei identischem Stammauslaut: *şaln+na → şalna, girn+na → girna*. Eindeutig, maschinell erzeugbar. Kein Befund.

### 8.2 Prädikativ (§12.2)

Nach **esex, vurnex, stanex**: Grundform, unverändert, auch im Plural. Eindeutig. Kein Befund. (Ob die Liste der Kopulaverben abschließend ist — z. B. bei Wahrnehmungsverben — ist nicht gesagt, für den Testumfang aber ohne Folge.)

### 8.3 Steigerung (§12.3)

Komparativ -vi-, Superlativ -vax-, attributiv dekliniert, prädikativ endungslos; Fugenregel bei v-Stämmen (*selvi, zilvira*). Vergleichswörter **kon** (als), **zil** (wie).

> **[REGELUNKLARHEIT U-06] Kasus nach kon/zil nicht festgelegt.**
> Beide Beispiele (*kon vim*, *zil luiv*) zeigen Nominativ; eine Regel dazu fehlt. Bei „Ich sehe ihn wie einen Freund" wäre der Kasus offen.

### 8.4 Adverbien (§12.4)

Grundform + **-un**: *vlaidun, zilvun, loşnun*.

> **[REGELKONFLIKT K-04] §12.4 vs. §25.1.**
> Der grammatikeigene Beispielsatz *„Xla soruma xlas nauşes vran tolm vaşnat"* (§25.1) verwendet **tolm** ohne -un in adverbialer Funktion („vergeht sehr langsam"). Nach §12.4 müsste dort *tolmun* stehen. Entweder ist der Beispielsatz fehlerhaft oder es gibt eine ungeschriebene Ausnahme (prädikativähnliche Verwendung); beides ist in 0.9.3 nicht auflösbar. (Der Satz wurde in Testkorpus 0.1 der Chat-Fassung als ✓ übernommen — der Konflikt blieb dort unentdeckt.)

### 8.5 Nominalisierung (§12.5)

-ru (M-A Person m) · -la (F-A Person f) · -te (N-C Sache); Partizip -ut + -te → **-ute** (*traivute*). Eindeutig. Kein Befund.

> **[REGELUNKLARHEIT U-02] Partizip als attributives Adjektiv ungeregelt.**
> §14 definiert das Partizip (-ut), §16.3 nutzt es prädikativ (*şunargut est*), §12.5 nominalisiert es. Ob es wie ein Adjektiv attributiv dekliniert werden kann („das gefundene Wasser" → *xna traivutna aul*?), sagt keine Regel.

---

## 9. PRONOMEN (§13)

### 9.1 Personalpronomen (§13.1)

Voll dekliniert (Nom/Akk/Dat/Gen × 9 Formenreihen): vim/şet/şevar/ro/lo/no/viñ/şeñ/oñ. Höflichkeitsform şevar + 3. Person Plural (§13.2). Possessiv = Genitiv des Personalpronomens, **nachgestellt** (§13.3). Vollständig geregelt. Kein Befund. (*oñ* betrifft K-01 auf Silbenebene.)

### 9.2 Übrige Pronomen (§13.4)

| Art | Bestand | Befund |
|---|---|---|
| Demonstrativ | kilra/killa/kilna, dolra/dolla/dolna | **[REGELLÜCKE L-06]** Deklination nicht definiert (nur Grundformen gelistet; Verwendung als Attribut oder Pronomen ungeregelt) |
| Reflexiv | se | **[REGELLÜCKE L-04]** keine Kasusformen; unklar, ob indeklinabel und für welche Personen se gilt (1./2. Person über Personalpronomen wie im Deutschen?) |
| Relativ | fai | **[REGELLÜCKE L-02]** Relativsatzbau fehlt vollständig (Kasus, Kongruenz, Verbstellung); zusätzlich Homonymie mit fai „dass" (§20) |
| Indefinit | kaun, kelsu, xakaun, kelte, xakelte | **[REGELLÜCKE L-06]** Deklination nicht definiert; kaun homonym mit Kernwort kaun „Mensch" |

> **[REGELKONFLIKT K-02] killa/dolla/kella vs. Fugenregel §21.4.**
> §21.4 gilt ausdrücklich „für Zusammensetzungen, Ableitungen und Endungen gleichermaßen" und verschmilzt identische Konsonanten an jeder Fuge (*mel+la → mela*, *tal+la → tala*). Die belegten Formen **killa** (§13.4), **dolla** (§13.4) und **kella/kellan** (§18.2, inkl. Beispielsatz *Kellan sarlan milkoş?*) enthalten aber die unverschmolzene Fuge *l+l*. Entweder sind die Pronomenformen Ausnahmen (nirgends gesagt) oder sie müssten *kila/dola/kela* lauten. Automatischer Nachweis: Geminaten-Check des Validators.

---

## 10. VERBEN (§14–§15)

### 10.1 Bildung (§14)

Wurzel + Tempusvokal + Personendung. Personen: -m -ş -t / -men -şen -ten. Infinitiv -ex, Partizip -ut. Imperative: bloße Wurzel (du), -eñ (ihr), 3. Pl. Präsens (höflich); Stütz-e bei nach §5.3 unzulässiger Endgruppe (*Suvre!*). Modalverben bilden im Normalfall keinen Imperativ.

> **[REGELUNKLARHEIT U-12] Imperativ-Stütz-e prüft §5.3, nicht §5.1.**
> Die Wurzeln *dremn-, prens-, vlent-* haben §5.3-konforme Codas (mn, ns, nt), ihre Imperative *Dremn!, Prens!, Vlent!* hätten aber die Silbenform KKVKK, die §5.1 nicht führt (→ K-01). Ob hier das Stütz-e greifen soll, ist nicht entscheidbar.

### 10.2 Zeitformen (§15)

Gegenwart -a-, Vergangenheit -o-, Zukunft -ai-. Regelmäßiges Paradigma vollständig belegt (*milkex*). Eindeutig, maschinell erzeugbar (Volltabellen: `orbis_validator.py --tables`). Kein Befund.

### 10.3 Die 8 unregelmäßigen Verben (§15.2)

esex, nuvex, vurnex, melex, vandex, nargex, zavex, dalvex.

> **[REGELUNKLARHEIT U-01] Beschreibung und Tabellen decken sich nicht.**
> Der Text sagt: „bewahren **in der Vergangenheit** eine ältere Vokalstufe" und gibt die Formel „Ablautstamm + Bindevokal -e- + Personendung". Die eigenen Tabellen zeigen mehr bzw. anderes:
> 1. **esex** ist durchgängig suppletiv: Präsens *em/eş/est/…* (3. Sg. *est* passt in keine Formel), Vergangenheit *vo+Endung* **ohne** Bindevokal -e- (*vot*, nicht \**vovet*), Zukunft Stamm *vai-*.
> 2. **nuvex** und **vurnex** haben zusätzlich kontrahierte **Präsens**-Stämme (*nu-*, *vur-*: *num, nut, vurt* statt \**nuvam, nuvat, vurnat*).
> 3. Nur mel-/vand-/narg-/zav-/dalv- entsprechen der Textbeschreibung exakt.
> Die Formen selbst sind vollständig belegt und damit prüfbar — unklar ist allein die Regelbeschreibung.

Aspekt (§15.3): [NOCH ZU ENTSCHEIDEN] — offen, kein Prüfbefund.

---

## 11. MODALITÄT (§16)

### 11.1 Modalverben (§16.1)

valn- können · dolm- müssen · vlek- dürfen · tirn- sollen · nest- wollen · suvr- mögen. Konjugiertes Modalverb auf Position 2, Vollverb im **Infinitiv am Satzende** (Verbklammer). Im Hauptsatz eindeutig; Beispiele belegt.

> **[REGELUNKLARHEIT U-03] Modalverb ohne Infinitiv.**
> Ob ein Modalverb mit direktem Objekt stehen darf („Ich mag das Wort" → *Vim suvram xnan taisan*), ist nicht geregelt. §16.1 beschreibt nur die Klammerkonstruktion mit Infinitiv. (Testkorpus 0.1 der Chat-Fassung hatte diese Konstruktion als ✓ gewertet — dafür gibt es keine Regelgrundlage.)

> **[REGELKONFLIKT K-05] Modalverb im Nebensatz: zwei Regeln beanspruchen das Satzende.**
> §16.1: Vollverb-Infinitiv „am Satzende". §17.2: im Nebensatz steht das **finite Verb** am Ende. In „…, dass der Mann morgen in die Stadt gehen muss" konkurrieren Infinitiv und finites Modalverb um die Endposition; die Reihenfolge (*melex dolmat* oder *dolmat melex*) ist durch keine Regel entscheidbar. Kein Beispiel in 0.9.3 enthält ein Modalverb im Nebensatz.

### 11.2 Möglichkeitsform (§16.2)

Partikel **mai** unmittelbar vor dem finiten Verb; mai + Verb = eine Satzposition. Belegt im Haupt- und (per §16.2-Beispiel) im Nebensatz. Eindeutig. Kein Befund.

### 11.3 Passiv (§16.3)

Vorsilbe **şu-** (*şunargat*); Zustandspassiv Partizip + esex (*şunargut est*).

> **[REGELLÜCKE L-05] Agens im Passiv undefiniert.**
> „Das Haus wird **vom Mann** gebaut" ist nicht bildbar; §16.3 regelt nur die Vorsilbe. *ven* + Dativ läge nahe, ist aber nirgends festgelegt.

---

## 12. SATZBAU (§17)

| Regel | Bestand | Befund |
|---|---|---|
| Hauptsatz V2 (§17.1) | belegt mit drei Stellungsvarianten | kein Befund |
| Nebensatz Verbendstellung (§17.2) | belegt | kein Befund |
| Nebensatz auf Position 1 → finites Verb direkt danach (§17.1) | belegt | kein Befund |
| Verbklammer (§17.3) | belegt (Hauptsatz) | im Nebensatz → K-05 |
| Satzgliedfolge Zeit–Grund–Art–Ort (§17.4) | ausdrücklich Tendenz | kein Befund |
| Keine Kopula-Auslassung (§17.5) | verbindlich; dichterisch [NZE] | kein Befund |

> **[REGELLÜCKE L-01] Stellung des Genitivattributs nicht festgelegt.**
> §8 definiert den Genitiv nur morphologisch, §17 schweigt zur Attributstellung. Sämtliche Beispiele stellen das Genitivattribut nach (*xla soruma xlas nauşes*, *xlan luiven xlas eirdes*), und §13.3 schreibt für den verwandten Fall des Possessivs „nachgestellt" vor — eine Regel für Nomen-Genitive ist das nicht. Zusätzlich offen: die Reihenfolge bei Stapelung („das Buch meines Freundes" = Kopf + Genitiv + dessen Possessiv: *xna vresto xras velkras vis*?).

> **[REGELUNKLARHEIT U-05] Objektreihenfolge Dativ vor Akkusativ nur Praxis.**
> Alle Doppelobjekt-Beispiele zeigen Dat vor Akk (*dolvet xnaş şirneş xnan brasin*); geregelt ist die Reihenfolge nicht.

> **[REGELUNKLARHEIT U-04] Subjektauslassung (Pro-Drop) nur Praxis.**
> §18-Beispiele lassen das Subjektpronomen in Fragen weg (*Melaş nunda?*, *Kan melaş?*, *Grais xa vandat?*), alle Aussagesatz-Beispiele behalten es. Wann Weglassen zulässig ist, sagt keine Regel.

> **[REGELUNKLARHEIT U-11] Temporaler Dativ ohne Präposition.**
> §25.2 verwendet *Vraş zaldreş* („an einem Tag") als bloße Dativ-Zeitangabe. Diese Konstruktion ist in §8/§17/§19 nicht vorgesehen.

---

## 13. FRAGEN UND NEGATION (§18)

**Ja/Nein-Frage:** Verb Position 1; Antworten ain/xaus. Eindeutig. Kein Befund.
**W-Fragen:** kem, kelt, kur, kan, grais, kolm, kelra/kella/kelna.

> **[REGELLÜCKE L-03] Deklination von kem/kelt undefiniert.**
> §18.2 listet nur Grundformen. „Wen?", „Wem?", „Wessen?" sind nicht bildbar (kemn? kemen? keme­ş?) — weder Kasusformen noch Indeklinabilität sind festgelegt. *kelra/kella/kelna* kongruieren dagegen laut Beispiel (*Kellan sarlan milkoş?*) adjektivisch — belegt allerdings nur im Akkusativ; die übrigen Kasus sind Analogie. (*kella* → Fugenkonflikt K-02.)

**Negation:** Partikel **xa** vor dem finiten Verb; attributiv **xan-** (dekliniert). Eindeutig, auch in Kombination mit Modalverb und Nebensatz komponierbar. Kein Befund.

---

## 14. PRÄPOSITIONEN (§19)

| Kasus | Präpositionen |
|---|---|
| Dativ | zva, dun, ven, nul |
| Akkusativ | xun, prai, dral |
| Genitiv | gral, şlan |
| Dat=Ort / Akk=Richtung | tel, kru, span, drel, glem, traus, şlim |

Vollständig und eindeutig; maschinell prüfbar (Kasusheuristik im Validator). *dral* (Präposition) vs. *dra-* (Vorsilbe) ausdrücklich getrennt. Kein Befund.

---

## 15. KONJUNKTIONEN (§20)

Nebenordnend: ze, vu, klas, xer (Hauptsatzstellung). Unterordnend (Verbendstellung): fai, grali, tund, şlani, dremi, glemi, trausi.

> **[REGELUNKLARHEIT U-07] „Systematisch aus den Präpositionen abgeleitet, Suffix -i" stimmt nur teilweise.**
> Belegbar: grali < gral, şlani < şlan, glemi < glem, trausi < traus. Nicht herleitbar: **dremi** (keine Präposition \*drem; *drel* „unter" ergäbe *dreli*), **tund** (kein -i, keine Basis), **fai** (keine Basis). Die Regelbehauptung ist damit für 3 von 7 Formen falsch bzw. leer.

---

## 16. WORTBILDUNG (§21)

**Familien-Suffixe (§21.1):** -ex Verb · -ru/-la Person · -na Ort · -isto Werkzeug · -vi Eigenschaft · -uma Abstraktum. Belegt an mel- und tal-. Kein Befund.

**Vorsilben (§21.2):** şu- Passiv · xa- Gegenteil · re- wieder · dra- ganz/hindurch · su- halb. Kein Befund. (Homonymie xa-/xa „nicht": Phase 7.)

**Zusammensetzungen (§21.3):** Bestimmungswort + Grundwort; Geschlecht/Klasse nach letztem Glied.

> **[REGELUNKLARHEIT U-08] Deklination von Komposita mit Kernwort-Kopf.**
> *taivbreun* (Schule) hat als Kopf das Kernwort *breun*. Ob die Zusammensetzung wie ein Kernwort dekliniert (Bindevokal -e-, Plural -ei) oder regulär, sagt §21.3 nicht („Geschlecht und Klasse" — die Kernwörter haben keine Klasse). *aulmelna* und *luivresto* mit regulären Köpfen sind unproblematisch.

**Fugenregel (§21.4):** Identische Konsonanten an der Morphemfuge verschmelzen; gilt für Zusammensetzungen, Ableitungen und Endungen gleichermaßen. Regel selbst klar.

> **[REGELKONFLIKT K-03] telnxelmmern (§24.8) vs. Fugenregel.**
> Die Zahl 35 ist als *telnxelmmern* mit Doppel-m an der Fuge xelm+mern notiert — nach §21.4 müsste sie *telnxelmern* lauten. (Gleicher Konflikttyp wie K-02 killa/dolla/kella.)

---

## 17. PROTO-ORBIS UND LAUTGESCHICHTE (§22)

Sieben Gesetze, ausdrücklich rein diachron (§4.3): Endvokalschwund, Diphthongierung, Erweichung, Assimilation, Verlust vor Nasal, Ablaut, Reduktion. Arbeitsanweisung für neue Wörter (Proto-Form → Gesetze → §3.3 → §3.4). Für den Stabilitätstest folgenlos; kein Befund. (Stichprobe: die angegebenen Herleitungen der Kernwörter sind mit den Gesetzen konsistent.)

---

## 18. BETONUNG (§23)

Regel: vorletzte Silbe; Ausnahmen: -uma/-isto (Stammbetonung), 15 Kernwörter (letzte Silbe), Zusammensetzungen (erstes Glied), Vorsilben unbetont. Ca. 85 % vorhersagbar (Eigenangabe). Eindeutig genug für den Testumfang; kein Befund. Wechselwirkung mit Klangrichtlinie 4 (Diphthong bevorzugt in betonter Silbe) ist Richtlinie, kein Gesetz.

---

## 19. ZAHLEN (§24.8)

nel dram teln kalm mern vesn zerm glon pirn xelm · munar 100 · kraven 1000. Kompositbildung: xelmnel 11, dramxelm 20, telnxelmmern 35 (→ K-03). Ordnungszahlen: Zahl + -ost- + Geschlechtsendung (*nelostra*).

> **[REGELLÜCKE L-08] Syntax der Kardinalzahlen undefiniert.**
> Weder Kongruenz (deklinieren Zahlen?) noch der Numerus/Kasus des gezählten Nomens („zwei Männer" = *dram valruñ*? *dram valru*?) sind geregelt. Kein einziges Beispiel verwendet eine Zahl attributiv.

---

## 20. GRUNDWORTSCHATZ (§24) — PRÜFBESTAND

Eingefroren ab 0.9.3; Änderung nur bei Phonotaktikverstoß, grammatischer Inkonsistenz, Kollision oder widersprüchlicher Bedeutung.

| Bestand | Anzahl | Quelle |
|---|---|---|
| Kernwörter (unregelmäßig) | 15 | §24.1 |
| 10-Prozent-Gruppe | 3 | §10.1 |
| Reguläre Nomen M/F/N | 13 + 15 + 13 | §24.2–24.4 |
| Abstrakta auf -uma (zusätzlich) | 9 | §24.6 |
| Zusammensetzungen | 3 | §21.3 |
| Verbwurzeln (davon 8 unregelmäßig) | 28 | §24.5 |
| Modalwurzeln | 6 | §16.1/§24.5 |
| Adjektive | 20 | §24.7 |
| Zahlen | 12 + Komposita | §24.8 |
| Adverbien/Partikeln | 20 | §24.9 |
| Grußformeln | 4 | §13.2 |
| Pronomen/Artikel/Funktionswörter | geschlossene Klassen | §11, §13, §18–20 |

Vollständige Liste maschinenlesbar in `orbis_validator.py` (Funktion `full_lexeme_inventory`, 281 Grundformen inkl. Funktionswörter und Flexionsklassen-Grundformen). Kollisionsbefunde: Phase 7 im Testbericht.

---

## 21. ORBIS MANUS (§26) — SILBENSTRUKTUR DER SCHRIFT

**Silbenformel (§26.1):** Kernkonsonant + optionaler zweiter Anfangskonsonant + Vokalzeichen + 0–2 Endkonsonanten + (Satzabschluss).
**Kernformen (§26.2):** 8 Familien, **20 Kernformen = 19 Konsonanten + 1 Vokalträger**; je zwei Unterscheidungsmerkmale.
**Vokale (§26.4):** a inhärent; e/i/o/u als Punktpositionen; Diphthonge = Erstvokalzeichen + kleiner Zweitpunkt (6, inkl. oi schreibbar).
**Coda (§26.5–26.6):** verkleinert unten rechts; zweite Coda daneben, eine Stufe tiefer. **Abschlusszeichen (§26.7):** 6 Stück, eigene Ebene, drei Unterscheidungskriterien zur Coda.

Befunde:

> **[REGELLÜCKE L-09]** (siehe §2.4): Ohne Silbifizierungs-Präferenzregel ist die Manus-Schreibung vieler Wörter mehrdeutig (*mela* = m-Kern+e+l-Coda | a-Träger **oder** m-Kern+e | l-Kern+a). Details und Quantifizierung: Orbis-Manus-Schreibtest 0.1.

> **[REGELUNKLARHEIT U-10] §26.8 „20 Konsonantentasten" ist terminologisch falsch.**
> Orbis hat 19 Konsonanten; die 20. Kernform ist der **Vokalträger** (§26.2), der kein Konsonant ist. Korrekt wäre „19 Konsonantentasten + 1 Vokalträgertaste" (Summe 31 Belegungen bleibt richtig). Reiner Dokumentationsfehler.

> **[REGELLÜCKE L-10] Strichstärkenregel deckt nicht alle 19 Konsonanten.**
> §26.9: „dünn = Vokal, mittel = Fließlaut und Nasal, dick = Verschlusslaut". Damit sind nur l r (Fließlaute), m n ñ (Nasale) und p t k b d g (Verschlusslaute) erfasst — für die **8 Reibelaute f s ş x v z j** und die **Affrikate ç** ist keine Strichstärke definiert.

**Orbis Magna (§27):** stilistische Schicht über denselben Kernformen; Spiralregeln [NOCH ZU ENTSCHEIDEN] — offen, kein Prüfbefund.

---

## A. SAMMELREGISTER ALLER BEFUNDE

| ID | Typ | Betrifft | Kurzbeschreibung |
|---|---|---|---|
| K-01 | [REGELKONFLIKT] | §5.1 ↔ §5.3, §10.2, §15.2, §24, §25 | Silbenformenliste ohne VK/VKK/KKVKK, aber aul, eird, ain, oñ, em/eş/est, granz, trelm, vresn, skirm, prilm, prens-, dremn-, vlent- brauchen sie |
| K-02 | [REGELKONFLIKT] | §13.4, §18.2 ↔ §21.4 | killa/dolla/kella(n) mit unverschmolzener l+l-Fuge gegen die Fugenregel |
| K-03 | [REGELKONFLIKT] | §24.8 ↔ §21.4 | telnxelmmern mit m+m-Fuge gegen die Fugenregel |
| K-04 | [REGELKONFLIKT] | §25.1 ↔ §12.4 | Beispielsatz nutzt tolm adverbial statt tolmun |
| K-05 | [REGELKONFLIKT] | §16.1 ↔ §17.2 | Modalverb im Nebensatz: Infinitiv und finites Verb konkurrieren um das Satzende |
| L-01 | [REGELLÜCKE] | §8, §17 | Stellung des Genitivattributs (inkl. Stapelung mit Possessiv) |
| L-02 | [REGELLÜCKE] | §13.4, §17 | Relativsatzbau (Kasus/Kongruenz/Verbstellung von fai; Homonymie fai „dass") |
| L-03 | [REGELLÜCKE] | §18.2 | Deklination von kem/kelt (wen/wem/wessen) |
| L-04 | [REGELLÜCKE] | §13.4 | Kasusformen des Reflexivpronomens se; Personenbereich |
| L-05 | [REGELLÜCKE] | §16.3 | Agens im Passiv |
| L-06 | [REGELLÜCKE] | §13.4 | Deklination der Demonstrativa und Indefinita |
| L-07 | [REGELLÜCKE] | §10.1 | Plural der 10-Prozent-Gruppe (velkran, soralm, prilm) |
| L-08 | [REGELLÜCKE] | §24.8 | Syntax der Kardinalzahlen (Kongruenz, Numerus des Nomens) |
| L-09 | [REGELLÜCKE] | §5, §26 | Silbifizierungs-Präferenzregel fehlt → Manus-/Tastatur-Mehrdeutigkeit |
| L-10 | [REGELLÜCKE] | §26.9 | Strichstärke für f s ş x v z j ç undefiniert |
| U-01 | [REGELUNKLARHEIT] | §15.2 | Formel „Ablautstamm + -e- + Endung" deckt es-/nuv-/vurn- nicht |
| U-02 | [REGELUNKLARHEIT] | §12, §14 | Partizip attributiv verwendbar? |
| U-03 | [REGELUNKLARHEIT] | §16.1 | Modalverb ohne Infinitiv (Vollverbgebrauch) |
| U-04 | [REGELUNKLARHEIT] | §18 | Pro-Drop nur Beispiels-Praxis |
| U-05 | [REGELUNKLARHEIT] | §17 | Objektreihenfolge Dat vor Akk nur Praxis |
| U-06 | [REGELUNKLARHEIT] | §12.3 | Kasus nach kon/zil |
| U-07 | [REGELUNKLARHEIT] | §20 | Ableitungsbehauptung passt nicht zu dremi/tund/fai |
| U-08 | [REGELUNKLARHEIT] | §21.3 | Deklination von Komposita mit Kernwort-Kopf (taivbreun) |
| U-09 | [REGELUNKLARHEIT] | §9 | „Echovokal" nur durch Tabellen definiert |
| U-10 | [REGELUNKLARHEIT] | §26.8 | „20 Konsonantentasten" — Terminologie-/Dokumentationsfehler |
| U-11 | [REGELUNKLARHEIT] | §25.2 | Temporaler Dativ ohne Präposition (Vraş zaldreş) |
| U-12 | [REGELUNKLARHEIT] | §14 | Imperativ-Stütz-e prüft §5.3, nicht §5.1 (Dremn!/Prens!/Vlent!) |
| U-13 | [REGELUNKLARHEIT] | §12.2 ↔ §17.1 | Prädikativ steht in allen Beispielen VOR dem Verb (Lo loşn est = Verb an Position 3) — reibt sich an der V2-Regel; ob Prädikativ+Kopula als eine Position zählt, ist ungesagt *(gefunden im Korpuslauf, Test 055)* |
| U-14 | [REGELUNKLARHEIT] | §18.3 ↔ §8/§10.3/§11 | Beispiel „Vim xa num vna breun" lässt Artikel und Kernwort im Objekt unmarkiert (regelkonform wäre vnan breunen) *(gefunden im Korpuslauf, Test 083)* |

Wortschatz-Kollisionen (Homonyme, Verwechselbarkeiten, fehlende Alltagswörter) sind keine Regelbefunde und werden in Phase 7 des Testberichts geführt.

---

*Orbis-Audit 0.1 — erstellt gegen Grammatik 0.9.3, ohne Änderung an der Referenz.*
