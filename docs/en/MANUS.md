# Orbis — Orbis Manus, the everyday script

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md).
Describes Orbis Grammar 0.9.3; the reference grammar itself is Orbis-Grammatik-0.9.3.md.*

---

## 1. Subject

This chapter describes §26 of the grammar in full: the syllable formula (§26.1), the
20 core forms in 8 families (§26.2), the second initial consonant (§26.3), the
vowel dots and the composition of the diphthongs (§26.4), the placement of one and
two final consonants (§26.5–26.6), the separation of coda and sentence closure together with the six
closing marks (§26.7), keyboard input (§26.8) and the writing rules (§26.9).

Orbis Manus is a **syllabic script**: one does not write letter by letter,
but syllable block by syllable block. Script and grammar are separate levels and
are versioned separately; a script finding is not a grammar finding.

Three reservations apply to the whole chapter and are named here, not resolved:

| Reservation | Effect |
|---|---|
| **[REGELLÜCKE L-09]** (rule gap) | There is no syllable-division rule. 77 of 281 base forms have more than one rule-conforming Manus spelling (section 11 of this file) |
| **[REGELLÜCKE L-10]** (rule gap) | For *f s ş x v z j ç* no stroke weight is defined (section 10 of this file) |
| **[REGELUNKLARHEIT U-10]** (rule ambiguity) | §26.8 says "20 consonant keys"; Orbis has 19 consonants (section 9 of this file) |

---

## 2. The complete syllable formula (§26.1)

§26.1 gives exactly one formula for the syllable block:

> **Core consonant + optional second initial consonant + vowel mark + 0–2 final consonants + (sentence closure)**

The five positions in detail:

| Position | Obligatory | Governs | Place |
|---|---|---|---|
| Core consonant | yes — or, as substitute, the vowel carrier | one of the 20 core forms | syllable body |
| Second initial consonant | no | reduced subsidiary mark, without its own vowel mark | beneath the core form (§26.3) |
| Vowel mark | yes — *a* is inherent and is not written | dot position, with diphthongs two dots | on the syllable body (§26.4) |
| Final consonant 1–2 | no | reduced consonant form | lower right (§26.5–26.6) |
| Sentence closure | no | one of six marks | free-standing after the syllable (§26.7) |

In its limits the formula coincides with phonotactics: at most two
initial consonants (§5.2) and at most two final consonants (§5.3). The Manus writing test
0.1 expressly records that the syllable formula, the vowel-dot system, coda placement and
closing marks are **complete in themselves** and cover all divisible syllables —
**no finding** (`Orbis-Manus-Schreibtest-0_1.md`, section 4.4).

Attested application of the formula is given by §26 itself in its decomposition tables: *mel*, *kaun*,
*breun*, *tel* (§26.5) as well as *moks*, *virn*, *xerp*, *teln* (§26.6).

---

## 3. The 20 core forms in 8 families (§26.2)

§26.2 states the number expressly as a sum:

> **8 sign families, 20 core forms: 19 consonants + 1 vowel carrier.**

The 20th core form is therefore **not a consonant**, but the carrier that makes a syllable without
an initial consonant writable (syllable shape V or VK, §5.1). This reading is the
touchstone for §26.8 (see §9, U-10).

| Family | Meaning | Sounds | Forms | Attested words with these sounds |
|---|---|---|---|---|
| **NER** | origin | m · n · ñ | 3 | *mela* (§24.3) · *nauş* (§24.1) · *oñ* (§13.1) |
| **TAL** | river | l · r | 2 | *luiv* (§24.1) · *ro* (§13.1) |
| **SOR** | angle | p · t · k | 3 | *prila* (§24.3) · *taiv* (§24.1) · *kaun* (§24.1) |
| **VEL** | arc | b · d · g | 3 | *breun* (§24.1) · *draun* (§24.1) · *grein* (§24.1) |
| **MOR** | turn | f · s · ş · x | 4 | *fai* (§13.4) · *sarla* (§24.3) · *şirn* (§24.1) · *xerp* (§24.1) |
| **ISH** | spiral | v · z · j | 3 | *virn* (§24.1) · *zva* (§19) · *j* **unattested** |
| **KAI** | path | ç | 1 | *ç* **unattested** |
| **RUUN** | shell | vowel carrier | 1 | *aul*, *eird*, *oñ* (§24.1, §13.1) — vowel-initial |

Check sum: 3 + 2 + 3 + 3 + 4 + 3 + 1 = **19 consonants**, plus RUUN = **20 core forms**.
The families thereby group exactly the sound classes from §2.1 (nasals, liquids,
voiceless and voiced stops, voiceless and voiced fricatives, affricate).

**Distinction rule.** §26.2 requires: "Every core form must differ from every other in
**at least two** features." Which features are meant (stroke count,
direction, aperture, height …) is not spelled out by §26; reference forms of the signs are not
depicted in the grammar. The audit assigns no finding ID for this — recorded here only,
not interpreted. The glyph set with sign IDs and reference forms is a
work package of the still-open Manus version 1.0 (`ROADMAP.md`, phase F).

**Observation without finding ID.** For the affricate **ç** (family KAI) and the voiced
fricative **j** (family ISH) the frozen vocabulary 0.9.3 contains **not a single
word** (281 base forms, `language/lexicon/entries/`). Both sounds are regular parts of the inventory
through §2.1 and §3.3 and have their own core forms in Manus — they are
merely unattested, like the diphthong *oi* (§2.3). See `PHONOLOGY.md` §6.

---

## 4. The second initial consonant (§26.3)

> **Reduced subsidiary mark beneath the core form, without its own vowel mark.**

The second initial consonant is thus subordinated to the syllable body, not coordinated with it:
it carries no vowel of its own and forms no block of its own. Which pairs can occur at all
is governed not by §26 but by the closed list of 25 initial clusters
in §5.2 (*tr dr kr gr pr br pl bl fl vl fr vr vn sl şl şr sk st sp xr xl xn zv gl kl*).

§26.3 itself gives no example. The only syllable block with a
second initial consonant written out in §26 stands in the coda table §26.5:

| Syllable | Core form | Subsidiary mark | Vowel | Coda |
|---|---|---|---|---|
| **breun** house (§24.1) | b | r | eu (double dot) | n |

Further initial clusters attested by §5.2 — *xra · xla · xna* (article, §11.1), *vra · vla · vna*
(§11.2), *zva* with, *kru* on (§19), *trelm* long, *vresto* book (§24) — are writable by
the same formula; a written-out Manus decomposition of these words is not contained in the
grammar.

---

## 5. Vowel dots and diphthong composition (§26.4)

### 5.1 The four written vowel marks

Orbis has five vowels (§2.2), but only **four vowel marks**: *a* is inherent and is
not written.

| Vowel | Position | Attested monosyllabic words |
|---|---|---|
| **a** | (not written) | *xra* (§11.1) · *zva* (§19) · *xa* (§18.3) |
| **e** | dot **in front** | *mel* (§26.5) · *tel* (§19) · *se* (§13.4) |
| **i** | dot **above** | *vim* (§13.1) · *şlim* (§19) · *zil* (§24.9) |
| **o** | dot **behind** | *moks* (§24.1) · *ro*, *lo*, *no* (§13.1) |
| **u** | dot **below** | *kru* (§19) · *nul* (§19) · *xun* (§19) |

A syllable block without a visible vowel dot is therefore an *a* block — not a block without
a vowel. Vowelless syllables are not provided for by §5.1.

### 5.2 The composition of the diphthongs

A diphthong is **not a sign of its own**, but a composition:

> **Mark of the first vowel + small second dot in the position of the second vowel.**

| Diphthong | Spelling | Status (§2.3) | Attestation |
|---|---|---|---|
| **ai** | inherent *a* + small dot **above** | attested | *taiv* (§24.1) · *mai* (§16.2) |
| **au** | inherent *a* + small dot **below** | attested | *kaun* (§26.5) · *şaul* (§24.1) |
| **ei** | dot in front + small dot **above** | attested | *grein*, *eird* (§24.1) |
| **ui** | dot below + small dot **above** | attested | *luiv*, *luid* (§24.1, §24.7) |
| **eu** | dot in front + small dot **below** | attested | *breun* (§26.5) |
| **oi** | dot behind + small dot **above** | **writable, currently unattested** | no word of the lexicon (§2.3) |

The difference in size between first and second dot carries the reading order: *ai* is a
large *a* field with a small *i* dot, not the same as a hypothetical *ia*. Because the
four dot positions are already present, §26.4 records:

> "The system needs not a single new sign."

*oi* is therefore the practical proof of the system's productivity: the diphthong is
fully writable in Manus although no word uses it. §30, by contrast, expressly keeps the diphthong *ou*
open as **[NOCH ZU ENTSCHEIDEN]** (to be decided) — it is currently not
part of the inventory and may not be written.

---

## 6. One final consonant (§26.5)

> **Reduced form of the consonant's own sign, at the lower right of the syllable, resting on
> the baseline.**

The coda uses no sign inventory of its own: it is the reduced core form of the same
consonant. Decisive is solely the **place**, because it distinguishes the coda from the
second initial consonant, which is likewise reduced:

| Sign | Place | Meaning |
|---|---|---|
| Subsidiary mark (§26.3) | beneath the **middle** | second initial consonant |
| Coda (§26.5) | lower **right** | final consonant |

The four examples written out in §26.5:

| Syllable | Structure | Meaning / source |
|---|---|---|
| **mel** | m core form + e dot in front + l coda at lower right | root *mel-* to go (§24.5) |
| **kaun** | k core form + au double dot + n coda at lower right | human being (§24.1) |
| **breun** | b core form + r subsidiary mark + eu double dot + n coda at lower right | house (§24.1) |
| **tel** | t core form + e dot in front + l coda at lower right | *tel* in (§19) |

---

## 7. Two final consonants (§26.6)

> **First coda at the lower right, second beside it, one step lower. Reading order left to
> right, top to bottom.**

The staggering is therefore not decorative but carries the order: *ks* and *sk* are
distinguished in the written image. Which two-member clusters may occur at all is governed by §5.3
(first sound liquid or nasal · second sound *s* · or the list *şn sn sk st*).

| Syllable | First coda | Second coda | Meaning / source | §5.3 condition |
|---|---|---|---|---|
| **moks** | k | s | death (§24.1) | (b) second sound *s* |
| **virn** | r | n | life (§24.1) | (a) first sound liquid |
| **xerp** | r | p | fire (§24.1) | (a) first sound liquid |
| **teln** | l | n | 3 (§24.8) | (a) first sound liquid |

More than two coda signs are provided for by neither §26.6 nor §5.3.

---

## 8. Coda and sentence closure are two levels (§26.7)

### 8.1 The three distinguishing criteria

§26.7 separates the syllable sign from sentence punctuation by three criteria holding
simultaneously:

| No. | Coda | Closing mark |
|---|---|---|
| 1 | hangs on the syllable body | stands **free** after it |
| 2 | **reduced** | **full size** |
| 3 | on or below the baseline | on the writing line |

A closing mark can therefore never be misread as a third coda, and a coda never
as an end of sentence — not even when a word ends in two consonants.

### 8.2 The six closing marks

| Closure | Function (§26.7) | Attested sentence type of the grammar |
|---|---|---|
| **soft** | statement | *Xra valru milkat xran narkun.* — The man sees the dog (§25.1) |
| **held** | continuation follows | no example sentence in the grammar |
| **drawn** | contrast | *Xna breun granz stanat, klas xla kavla zirv vurt.* (§25.1; *klas* but, §20) |
| **open** | question | *Melaş nunda?* (§18.1) · *Valnaten şevar vin zaubex?* (§25.1) |
| **fading** | possibility, uncertainty (corresponds to *mai*) | *Vim mai melam.* — I would go (§16.2) |
| **bound** | end, completion | no example sentence in the grammar |

The assignments in the right-hand column are **attestations for the sentence type**, not for the
spelling: the grammar shows no sentence in Manus. §26.7 expressly links only a
single mark to a language form, namely *fading* with the possibility particle
*mai* (§16.2). For the remaining five, §26.7 names function labels without an
assignment procedure and without an example; whether, say, every subordinate clause with *klas* requires the drawn
mark is left unsaid. The Manus writing test lists the six closing marks as
**complete in themselves** and assigns no finding; here the observation is only
recorded, not built up into a rule.

---

## 9. Keyboard input (§26.8)

### 9.1 The input rule

> Input as with Korean Hangul: type sounds **in the order spoken**, the system
> assembles the syllable block.
>
> **Core consonant → second initial consonant → vowel → coda 1 → coda 2**

Together with two stipulations:

- **A new core consonant closes the previous block.**
- **The closing mark lies on a key of its own.**

### 9.2 The key-count calculation

§26.8 calculates:

> **20 consonant keys + 4 vowel keys + 1 diphthong key + 6 closure keys = 31 key assignments.**

### 9.3 [REGELUNKLARHEIT U-10] (rule ambiguity) — "20 consonant keys" is terminologically wrong

**Finding ID: U-10** (`Orbis-Audit-0_1.md` §21 and §A; `Orbis-Manus-Schreibtest-0_1.md`
section 4.1). Concerns §26.8.

Orbis has **19** consonants (§2.1). The 20th core form is, according to §26.2, the **vowel carrier**
(family RUUN) and therefore not a consonant. §26.8 transfers the number 20 from §26.2 to a
term that §26.2 itself does not cover.

| | §26.8 (wording) | terminologically correct |
|---|---|---|
| Core-form keys | 20 consonant keys | 19 consonant keys + 1 vowel-carrier key |
| Vowel keys | 4 | 4 |
| Diphthong key | 1 | 1 |
| Closure keys | 6 | 6 |
| **Total** | **31** | **31** |

The **total of 31 key assignments remains correct**; the audit expressly classifies the point as a
**documentation error, not a system error**. The correction will appear in a
future grammar version, not through a change to 0.9.3 (`ROADMAP.md`, phase F). This
documentation quotes the wording and marks it; it does not correct the grammar.

**Not spelled out in §26.8:** how a single diphthong key produces the six diphthongs from
§26.4 (there every diphthong consists of a first-vowel mark plus a small second
dot). The audit assigns no finding ID for this; nothing is added here.

On keyboard planning as a whole see `KEYBOARD.md`.

---

## 10. Writing rules and stroke weight (§26.9)

§26.9 names three rules:

| Rule | Wording |
|---|---|
| **Stroke weight** | thin = vowel · medium = liquid and nasal · thick = stop |
| **Running direction** | words joined, sentences separated by gaps, left to right |
| **Transcription and titles** | Cormorant Garamond, Cinzel for capitals |

The running-direction rule means: in Manus text the word boundary is **not** a gap — the
gap marks the sentence boundary. Together with the free-standing closing mark (§26.7)
this yields two independent signals for the end of a sentence [inference from §26.9, not stated there].

### 10.1 [REGELLÜCKE L-10] (rule gap) — stroke weight undefined for eight consonants

**Finding ID: L-10** (`Orbis-Audit-0_1.md` §21 and §A; `Orbis-Manus-Schreibtest-0_1.md`
section 4.2). Concerns §26.9.

The stroke-weight rule names three classes and thereby covers only a part of the inventory:

| Stroke weight | Sounds covered | Families (§26.2) | Count |
|---|---|---|---|
| thin | vowel marks | — (diacritics) | — |
| medium | liquids *l r* and nasals *m n ñ* | TAL, NER | 5 |
| thick | stops *p t k b d g* | SOR, VEL | 6 |
| **not defined** | fricatives *f s ş x v z j* and affricate *ç* | **MOR, ISH, KAI** | **8** |

**8 of the 19 consonants** remain without assignment — and not scattered, but as
three closed sign families: MOR (4), ISH (3) and KAI (1). Affected are, among
others, such high-frequency signs as *x* (article *xra/xla/xna*, negation *xa*), *s*, *ş*
(dative marker) and *v* (pronoun *vim*, indefinite article *vra/vla/vna*).

The gap is not closable through the sound groups of §3.2: there *v z s j* count among
the liquid sounds and *f x ş ç* among the hard sounds — an assignment that §26.9 does not
take up and that would cut straight across the families MOR and ISH. Whether the fricatives
receive their own, fourth stroke weight, are added to the existing classes, or
whether §3.2 should be authoritative, is a **designer decision** (`ROADMAP.md`, phase F) and
is not made here.

---

## 11. [REGELLÜCKE L-09] (rule gap) — there is no syllable-division rule

**Finding ID: L-09** (`Orbis-Audit-0_1.md` §2.4 and §A, priority P2). Concerns §5 and §26
jointly. In detail on the phonotactic side: `PHONOTACTICS.md` §7.

### 11.1 The mechanism

§5.1 lays down which syllables are **permitted**. Nowhere does the grammar lay down how a
sound chain is **divided** into syllables: there is no onset maximization, no
sonority rule, no diphthong priority, no lexically stored syllable boundaries.
For pronunciation this is without consequence — the stress rule §23 counts syllables from the end and
yields the same result for *mela* in both divisions.

For Manus it is not without consequence, because §26.1 writes **syllable by syllable**: every admissible
division yields a different written image. After a vowel the next consonant can be
one of three things — coda of the current syllable, core consonant of the next syllable or (after
a further consonant) second initial consonant.

### 11.2 The four example words

| Word | Divisions (all §5-conforming) | Manus consequence |
|---|---|---|
| **mela** wanderer (§24.3) | **me·la** or **mel·a** | m core form + e dot, then l core form + inherent *a* — **or** m core form + e dot + l coda, then RUUN vowel carrier with inherent *a* |
| **kavla** city (§24.3) | **kav·la** or **ka·vla** | *v* as coda of the first block — **or** *v* as core form with *l* as subsidiary mark beneath it (§26.3) |
| **drovna** forest (§24.4) | **drov·na** or **dro·vna** | *v* as coda — **or** *v* as core form with *n* subsidiary mark (initial cluster *vn*, §5.2) |
| **vresto** book (§24.4) | **vres·to** or **vre·sto** | two blocks with different distribution of *s* and *t*. A third reading *vrest·o* (vowel carrier at the end) would require the syllable shape KKVKK, which §5.1 does **not** list — see K-01; it is not counted here |

All variants named are correct according to §5 **and** according to §26. The grammar contains
no sentence that singles out one of them.

### 11.3 The quantification

`Orbis-Manus-Schreibtest-0_1.md` (phase 8, reproducible with
`python3 orbis_validator.py --manus`) checks the entire basic vocabulary:

| Category | Count |
|---|---|
| Base forms checked | 281 |
| unambiguously divisible | 203 |
| **[MANUS-AMBIGUITÄT] ambiguous** | **77** |
| not divisible (bare root *suvr-*, §14 supporting e) | 1 |

**77 of 281 base forms (27 %) have more than one rule-conforming Manus spelling.**
The proportion rises further for inflected forms, because every V-K-V sequence is ambiguous. The
range extends from two divisions (*mela*, *valru*, *kavla*) through three (*vlaiko*,
*taluma*, *taisa*) and five (*klaunuma*, *şauluma*, *saivuma*) up to eight divisions for
the compound *aulmelna* (canal, §21.3).

A second, independent uncertainty factor is added: whether *aul*, *eird*, *ain* and *oñ*
are divisible at all depends on **[REGELKONFLIKT K-01]** (rule conflict) — §5.1 does not list the syllable
shapes VK/VKK/KKVKK although the vocabulary needs them (`PHONOTACTICS.md` §3). The
writing test therefore calculates in two rule sets (**strict** and **extended**); *aul* is
ambiguous in the extended mode (*a·ul* alongside *aul*).

### 11.4 The consequence: no deterministic composer

As long as no syllable-division rule applies, there is **no unambiguous mapping from the
standard spelling to a Manus written image**. The Manus writing test formulates the consequence
unmistakably:

> "A deterministic Manus composer is thereby blocked."

§26.8 does not solve this problem. The rule "A new core consonant closes the previous
block" orders the **input sequence** in typing, but does not decide the
**back-transfer** from the Latin spelling: the same letter chain remains ambiguous.
A program that is to set *mela* automatically in Manus must choose between *me·la* and
*mel·a* — and this choice is not a technical one but a language decision.

**What does not happen here.** No preference is laid down, not even an
obvious one. The repo contains a simulation (`python3 orbis_validator.py --sim-l09`)
that calculates four candidate strategies — onset maximization without diphthong precedence,
minimal onset with diphthong precedence, onset maximization with diphthong precedence as well as
lexically stored boundaries; the test report additionally names the possibility of declaring
free variation and leaving the script ambiguous. **These simulations are
analysis tools, not language rules, and may never be cited as a rule.** Which
division applies — including the special cases *suvr-* and the compositional seam in
*taivbreun* — is decided exclusively by the language designers.

---

## 12. Summary of rule status

| Rule | Paragraph | Status |
|---|---|---|
| Syllable formula of the block | §26.1 | complete, no finding |
| 8 families, 20 core forms = 19 consonants + 1 vowel carrier | §26.2 | complete; feature catalogue and reference forms not spelled out |
| Second initial consonant as subsidiary mark | §26.3 | complete, no example of its own |
| 4 vowel marks, *a* inherent, 6 diphthongs | §26.4 | complete, no finding; *oi* writable, unattested |
| Coda at lower right, reduced | §26.5 | complete, no finding |
| Second coda beside it, one step lower | §26.6 | complete, no finding |
| Coda and closure as two levels; 6 closing marks | §26.7 | complete, no finding; assignment sentence type → mark named only for *fading* / *mai* |
| Keyboard input, 31 key assignments | §26.8 | **[REGELUNKLARHEIT U-10]** — "20 consonant keys"; total 31 remains correct |
| Stroke weight | §26.9 | **[REGELLÜCKE L-10]** — *f s ş x v z j ç* undefined (8 of 19) |
| Syllable division | — | **[REGELLÜCKE L-09]** — not regulated; 77 of 281 base forms ambiguous |
| Syllable shapes VK/VKK/KKVKK | §5.1 | **[REGELKONFLIKT K-01]** — bears on divisibility in Manus |
| Spiral rules of Orbis Magna | §27, §30 | **[NOCH ZU ENTSCHEIDEN]** — see `MAGNA.md` |

---

## 13. Cross-references

| Topic | Place |
|---|---|
| Syllable shapes, initial clusters, coda conditions, L-09 phonotactically | `PHONOTACTICS.md` (section 5 of that file) |
| Sound inventory, sound groups, unattested sounds *j* and *ç* | `PHONOLOGY.md` (§2, §3) |
| Stress and sound realization | `PRONUNCIATION.md` (§23) |
| Solemn script form | `MAGNA.md` (§27) |
| State and architecture of keyboard planning | `KEYBOARD.md` (§26.8) |
| Decomposition table of all 281 base forms | `Orbis-Manus-Schreibtest-0_1.md` |
| Finding IDs L-09, L-10, U-10, K-01 | `Orbis-Audit-0_1.md`, `language/findings/findings.json` |
| Work packages Manus 1.0 | `ROADMAP.md` (phase F) |

---

*Source of all rule statements: `Orbis-Grammatik-0.9.3.md` (READ ONLY). In case of divergence
between this documentation and the grammar, the grammar applies.*
