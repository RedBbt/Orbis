# ORBIS — Word Order: the constructions one by one

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md).
Describes Orbis Grammar 0.9.3; the reference grammar itself is Orbis-Grammatik-0.9.3.md.*

---

This chapter presents every attestable sentence construction of Orbis one by one. `SYNTAX.md`
gives the overview of §17–§20; here stands the permutation test.

## Structure of a section

Every section has the same eight fields:

| Field | Content |
|---|---|
| **(a) German** | the German sentence — German is the semantic authority (`TRANSLATION_POLICY.md`) |
| **(b) Orbis** | the **attested** Orbis sentence with its source (§n of the grammar or test number of the corpus) |
| **(c) English** | derived from the German, never guessed from the Orbis word |
| **(d) Pattern** | abstract sentence pattern in the notation of `language/corpus/sentence.schema.json` |
| **(e) Explanation** | which rule forces the order |
| **(f) Valid permutations** | what the rules allow |
| **(g) Invalid permutations** | what the rules exclude |
| **(h) Rule ID** | `ORB-GRAM-SYN-*` from `language/syntax/rules.json` |

## Conventions

- **No sentence under (b) is invented.** Every Orbis line carries its source. Where no
  attestation exists, this is stated explicitly and the section only describes the situation.
- Under (f) and (g) the permutations are necessarily constructed. They carry the mark
  **[Attestation …]** when the permuted form is itself attested, otherwise **[rule-derived]**.
- **†** marks a form **invalid** under 0.9.3 — just as the grammar itself does in §12.2
  (*†Lo loşna est*).
- **?** marks a form that is **unattested but not excluded**: the rules do not decide the
  case, there is simply no attestation for it.
- **This file decides nothing.** Where the grammar is silent or contradicts itself, the
  finding ID from `Orbis-Audit-0_1.md` §A is given.

## Pattern notation

| Abbreviation | Meaning |
|---|---|
| NP | noun phrase (article + optional adjective + noun) |
| PRON | pronoun |
| V | finite verb or infinitive |
| ADJ | predicative or attributive adjective |
| PART | particle (*xa*, *mai*) or adverb |
| P | preposition |
| W | question word |
| KONJ | conjunction |
| SUBJ | beginning of a subordinate clause |

---

## Overview

| # | Construction | Pattern | Rule ID | Finding |
|---|---|---|---|---|
| 1 | Basic order | NP-V-NP | ORB-GRAM-SYN-010 | — |
| 2 | Topicalization | X-V-… | ORB-GRAM-SYN-010 | — |
| 3 | Object in the prefield | NP-V-NP | ORB-GRAM-SYN-010 | — |
| 4 | Time in the prefield | PART-V-NP-NP | ORB-GRAM-SYN-010 | U-11 |
| 5 | Adverb/adverbial in the prefield | P-NP-V-PRON-NP | ORB-GRAM-SYN-010 | — |
| 6 | Yes/no question | V-PRON-PART | ORB-GRAM-SYN-016 | U-04 |
| 7 | Wh-question | W-V(-PRON) | ORB-GRAM-SYN-017 | L-03, U-04 |
| 8 | Negation | PRON-PART-V | ORB-GRAM-SYN-018 | U-14 |
| 9 | Modal verb | PRON-V-NP-V | ORB-GRAM-SYN-013 | U-03 |
| 10 | Modal verb + negation | NP-PART-V-V | ORB-GRAM-SYN-013 / -018 | K-05 |
| 11 | Subordinate clause | PRON-V-SUBJ-KONJ-PRON-V | ORB-GRAM-SYN-011 | K-05 |
| 12 | Subordinate clause before main clause | SUBJ-KONJ-PRON-V-V-PRON | ORB-GRAM-SYN-012 | — |
| 13 | Relative clause | not determinable | ORB-GRAM-SYN-022 | **L-02** |
| 14 | Passive | NP-V | ORB-GRAM-SYN-019 | **L-05** |
| 15 | Dative + accusative | NP-V-NP-NP | ORB-GRAM-SYN-023 | U-05 |
| 16 | Genitive attributes | NP-NP-V | ORB-GRAM-SYN-021 | **L-01** |
| 17 | Predicative constructions | PRON-ADJ-V | ORB-GRAM-SYN-015 | U-13 |
| 18 | Conditional (*mai*) | SUBJ-KONJ-…-PART-V, PART-V-PRON | ORB-GRAM-SYN-020 | — |
| 19 | Multiple subordinate clauses | no attestation | ORB-GRAM-SYN-011 / -012 | K-05 |
| 20 | Coordination | [MC] KONJ-[MC] | §20 / ORB-GRAM-SYN-002 | — |
| 21 | Contrast | [MC] KONJ-[MC] | §20 / ORB-GRAM-SYN-002 | U-13 |
| 22 | Information structure | — | ORB-GRAM-SYN-010 / -014 | — |

---

## 1. Basic order

| Field | Content |
|---|---|
| **(a) German** | Der Mann sieht den Hund. |
| **(b) Orbis** | *Xra valru milkat xran narkun.* — **Attestation §17.1**, word for word the same in §25.1 |
| **(c) English** | The man sees the dog. |
| **(d) Pattern** | NP-V-NP |
| **(h) Rule ID** | ORB-GRAM-SYN-010 (§17.1) |

**(e) Explanation.** The basic order is subject – finite verb – object. It is not a law of its
own but the case in which the subject fills the prefield: §17.1 requires only that the finite
verb stand in **position 2**. The object carries the accusative (*xran narkun*), not the
position; case and agreement keep the sentence unambiguous under any other order as well.

Minimal form without object: test 001 *Xra valru melat.* — The man walks. (NP-V) ·
test 021 *Vim milkam xran narkun.* — I see the dog. (PRON-V-NP)

**(f) Valid permutations.**

| Form | Status |
|---|---|
| *Xran narkun milkat xra valru.* — The dog, the man sees. | **[Attestation §17.1]** |
| *Nunda milkat xra valru xran narkun.* — Today the man sees the dog. | **[Attestation §17.1]** — a time expression is added and occupies the prefield |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Xra valru xran narkun milkat.* | verb in position 3 — §17.1 [rule-derived] |
| †*Xran narkun xra valru milkat.* | verb in position 3 — §17.1 [rule-derived] |
| †*Milkat xra valru xran narkun.* (as a statement) | verb in position 1; under §18.1 that is the yes/no question, not the declarative sentence [rule-derived] |

---

## 2. Topicalization

| Field | Content |
|---|---|
| **(a) German** | Den Hund sieht der Mann. / Heute sieht der Mann den Hund. |
| **(b) Orbis** | *Xran narkun milkat xra valru.* · *Nunda milkat xra valru xran narkun.* — **Attestation §17.1** |
| **(c) English** | The dog, the man sees. / Today the man sees the dog. |
| **(d) Pattern** | X-V-… (X = any sentence element) |
| **(h) Rule ID** | ORB-GRAM-SYN-010 (§17.1) |

**(e) Explanation.** §17.1 attests the V2 rule precisely by presenting **the same statement in
three orders**. From this follows the basic principle of Orbis word order: the prefield is
**a single free field** holding exactly **one** sentence element; the finite verb follows
immediately. Which element that is, no rule of the grammar decides.

Attested prefield fillers:

| Prefield | Attestation |
|---|---|
| subject NP | *Xra valru milkat xran narkun.* (§17.1) |
| object NP (acc) | *Xran narkun milkat xra valru.* (§17.1) · *Xnan melnan traivamen viñ, tund …* (§25.1) |
| time adverb | *Nunda milkat …* (§17.1) · *Nunda melam vim dun xnaş breuneş vis.* (§25.1) · test 132 *Zirna ruskaim vim.* |
| dative time expression | *Vraş zaldreş traivot ro vnan aulen şlim xrañaş larkiñiş.* (§25.2) — **U-11** |
| prepositional phrase | *Tel xraş navildoş milkot ro xlan luiven xlas eirdes.* (§25.2) |
| demonstrative pronoun | *Kilna est xna traivute.* (§25.2) |
| subordinate clause | *Tund vim vra vlaidra valru mai em, mai traivam vim xlan eirden.* (§25.1) |

If an element other than the subject stands in the prefield, the subject moves behind the
verb. That is not a rule of its own but the consequence of the V2 order.

**(f) Valid permutations.** Each of the lines above is the permutation of another. The
grammar names no restriction on which element may be topicalized.

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Nunda xra valru milkat xran narkun.* | two elements in the prefield, verb in position 3 — §17.1 [rule-derived] |
| †*Xran narkun nunda milkat xra valru.* | likewise [rule-derived] |

The only attested case in which the finite verb does **not** stand in second word position is
the predicative (*Lo loşn est*, §12.2) — which is exactly what **U-13**, section 17, is about.

---

## 3. Object in the prefield

| Field | Content |
|---|---|
| **(a) German** | Den Hund sieht der Mann. |
| **(b) Orbis** | *Xran narkun milkat xra valru.* — **Attestation §17.1** |
| **(c) English** | The dog, the man sees. — same in meaning as *The man sees the dog*; English does not reproduce the prefield filling, because word order there is not a device of case |
| **(d) Pattern** | NP-V-NP (acc-V-nom) |
| **(h) Rule ID** | ORB-GRAM-SYN-010 (§17.1) |

**(e) Explanation.** The object is marked by the accusative (*xran narkun*), the subject by the
nominative (*xra valru*). Placing the object in the prefield therefore creates **no ambiguity**:
the roles hang on the ending, not on the slot. That is the structural reason why §17.1 can
release the prefield.

Second attestation, §25.1: *Xnan melnan traivamen viñ, tund xla luiv luid est.* — We find the
way when the sun is bright. Here the accusative object *Xnan melnan* stands in the prefield,
the subject pronoun *viñ* after the verb.

**(f) Valid permutations.**

| Form | Status |
|---|---|
| *Xra valru milkat xran narkun.* | **[Attestation §17.1]** — subject in the prefield |
| *Nunda milkat xra valru xran narkun.* | **[Attestation §17.1]** — time in the prefield, both noun phrases in the middle field |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Xran narkun xra valru milkat.* | verb in position 3 — §17.1 [rule-derived] |
| †*Xra narku milkat xra valru.* | not an order error but a case error: the prefield object must carry the accusative (§8) [rule-derived] |

---

## 4. Time in the prefield

| Field | Content |
|---|---|
| **(a) German** | Heute gehe ich zu meinem Haus. |
| **(b) Orbis** | *Nunda melam vim dun xnaş breuneş vis.* — **Attestation §25.1** |
| **(c) English** | Today I go to my house. |
| **(d) Pattern** | PART-V-PRON-P-NP |
| **(h) Rule ID** | ORB-GRAM-SYN-010 (§17.1), middle field ORB-GRAM-SYN-014 (§17.4) |

**(e) Explanation.** Time expressions stand in the prefield particularly often; §17.4 also
names **time** as the first member of the middle-field tendency. Both are the same observation
from two angles: the time expression stands early. Nothing is forced — §17.4 says explicitly
"tendency, not a hard rule".

Further attestations: *Nunda milkat xra valru xran narkun.* (§17.1) · test 132 *Zirna ruskaim
vim.* — Tomorrow I will write. (PART-V-PRON)

**(f) Valid permutations.**

| Form | Status |
|---|---|
| time expression in the middle field: *Şet dolmaş nunda vandex.* — You must come today. | **[Attestation §16.1]**, likewise test 107 |
| time expression in the middle field after a modal verb: *Vim valnam nunda zva xraş velkraş dun xlaş kavlaş melex.* | **[Attestation §17.3]** |
| time expression in the middle field of a subordinate clause: *Vim zavam, fai xra vlaidra valru zirna xnaş şirneş xnan brasin dalvait.* | **[Attestation test 146]** |
| time expression as a dative phrase in the prefield: *Vraş zaldreş traivot ro vnan aulen şlim xrañaş larkiñiş.* | **[Attestation §25.2]** — but **U-11**: a bare dative time expression without a preposition is not provided for by §8, §17 and §19 |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Nunda vim melam dun xnaş breuneş vis.* | verb in position 3 — §17.1 [rule-derived] |
| †*Zirna vim ruskaim.* | likewise [rule-derived] |

---

## 5. Adverb and adverbial in the prefield

| Field | Content |
|---|---|
| **(a) German** | In dem Traum sah er die Sonne der Welt. |
| **(b) Orbis** | *Tel xraş navildoş milkot ro xlan luiven xlas eirdes.* — **Attestation §25.2** |
| **(c) English** | In the dream he saw the sun of the world. |
| **(d) Pattern** | P-NP-V-PRON-NP-NP |
| **(h) Rule ID** | ORB-GRAM-SYN-010 (§17.1) |

**(e) Explanation.** A prepositional phrase fills the prefield as **one** position, however many
words it comprises: *Tel xraş navildoş* counts as 1, *milkot* stands on 2, the subject *ro*
follows. *tel* + dative here denotes the location (§19).

**On the adverb in the narrower sense.** §12.4 forms adverbs from adjectives with **-un**
(*vlaidun, zilvun, loşnun*). For such an adverb in the prefield there is **no attestation** —
neither in 0.9.3 nor in test corpus 0.1. Attested is only the position after the verb:
test 059 *Lo melat zilvun.* — She goes quickly. (PRON-V-ADJ)

Attested in the prefield are exclusively the particle adverbs of §24.9 (*nunda*, *zirna*;
see section 4) and prepositional phrases as above.

**(f) Valid permutations.**

| Form | Status |
|---|---|
| prepositional phrase in the middle field: *Vim maldam kru xlaş melvaş.* — I wait on the street. | **[Attestation test 031]** |
| the same in the middle field of a subordinate clause: *…, grali xra morda span xlaş kavlaş vran xarn est.* | **[Attestation test 150]** |
| directional expression in the middle field: *Viñ xa melamen tel xlan kavlan.* | **[Attestation test 089]** |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Tel xraş navildoş ro milkot xlan luiven xlas eirdes.* | verb in position 3 — §17.1 [rule-derived] |
| †*Tel xraş navildon milkot ro …* | case error: *tel* + dative denotes the location, the accusative the direction (§19) [rule-derived] |

---

## 6. Yes/no question

| Field | Content |
|---|---|
| **(a) German** | Gehst du heute? |
| **(b) Orbis** | *Melaş nunda?* — **Attestation §18.1**; with the subject set *Melaş şet nunda?* — **Attestation test 071** |
| **(c) English** | Are you going today? |
| **(d) Pattern** | V-PART (§18.1) · V-PRON-PART (test 071) |
| **(h) Rule ID** | ORB-GRAM-SYN-016 (§18.1) |

**(e) Explanation.** §18.1 requires the finite verb in **position 1**. The prefield stays empty;
everything else follows. The answer particles are **ain** (yes) and **xaus** (no) (§18.1).

Further attestations: test 072 *Vandat xra draun?* — Is the father coming? (V-NP) · test 114
*Valnaten şevar vin zaubex?* — Can you hear me? (V-PRON-PRON-V; polite form §13.2 with 3rd pl,
at the same time verbal bracket §16.1; word for word the same in §25.1).

**(f) Valid permutations.**

| Form | Status |
|---|---|
| without subject pronoun: *Melaş nunda?* | **[Attestation §18.1]** |
| with subject pronoun: *Melaş şet nunda?* | **[Attestation test 071]** |
| with nominal subject: *Vandat xra draun?* | **[Attestation test 072]** |

That both of the first two forms hold is example practice, not a rule — **U-04**: when the
subject pronoun may be dropped, §18 does not say.

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Şet melaş nunda?* as a yes/no question | verb in position 2 — §18.1 requires position 1. §18 says nothing about an intonation question with V2; attested it is not [rule-derived] |
| †*Nunda melaş?* as a yes/no question | likewise: the prefield is filled, the verb stands on 2 [rule-derived] |

---

## 7. Wh-question

| Field | Content |
|---|---|
| **(a) German** | Wer spricht? |
| **(b) Orbis** | *Kem talat?* — **Attestation test 073** |
| **(c) English** | Who speaks? |
| **(d) Pattern** | W-V |
| **(h) Rule ID** | ORB-GRAM-SYN-017 (§18.2) |

**(e) Explanation.** The question word occupies position 1, the finite verb position 2. If the
question word is itself the subject (*Kem talat?*), the pattern coincides with the declarative
sentence; only the question mark distinguishes them.

Attestations from the grammar (§18.2, without translation in the text): *Kan melaş?* ·
*Grais xa vandat?* · *Kellan sarlan milkoş?*

Attestations with translation from the test corpus:

| Test | Orbis | German | Pattern |
|---|---|---|---|
| 077 | *Kur maldaşen şeñ?* | Wo wartet ihr? | W-V-PRON |
| 078 | *Kolm est xla kirva?* | Wie ist die Nacht? | W-V-NP |
| 079 | *Kelnan vreston leşnaş şet?* | Welches Buch liest du? | ADJ-N-V-PRON |
| 080 | *Kelnaş şirneş dalvaş şet xnan brasin?* | Welchem Kind gibst du das Brot? | ADJ-N-V-PRON-NP |

*kelra / kella / kelna* agree adjectivally with their noun and form **one** prefield position
together with it (*Kelnan vreston*, *Kellan sarlan*).

**(f) Valid permutations.**

| Form | Status |
|---|---|
| subject behind the verb: *Kur maldaşen şeñ?* | **[Attestation test 077]** |
| subject omitted: *Kan melaş?*, *Grais xa vandat?* | **[Attestation §18.2]** — **U-04** |
| further complement at the end of the sentence: *Kelnaş şirneş dalvaş şet xnan brasin?* | **[Attestation test 080]** |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Talat kem?* | question word not in position 1 — §18.2 [rule-derived] |
| †*Kem şet milkaş?* | verb in position 3 — §18.2/§17.1 [rule-derived]. **Invalid twice over:** the sentence also presupposes *kem* as an accusative object, and no accusative form of *kem* is defined (L-03). Even with V2 it could not be formed |

> **[REGELLÜCKE L-03]** (rule gap) *kem* and *kelt* are listed only in the base form. "Wen
> siehst du?" (test 074), "Wem gibst du das Buch?" (test 075) and "Wessen Buch liest du?"
> (test 076) are **not formable**: neither case forms nor indeclinability are defined. Test 076
> additionally hangs on L-01. This documentation does not decide.

---

## 8. Negation

| Field | Content |
|---|---|
| **(a) German** | Ich gehe nicht. |
| **(b) Orbis** | *Vim xa melam.* — **Attestation §18.3**, likewise test 081 |
| **(c) English** | I do not go. |
| **(d) Pattern** | PRON-PART-V |
| **(h) Rule ID** | ORB-GRAM-SYN-018 (§18.3) |

**(e) Explanation.** §18.3 knows **a single** negation particle: **xa**, immediately before the
finite verb. The particle travels with the verb, not with the negated notion. Attributively its
place is taken by the declined adjective **xan-** (*xanra valru* — no man, §18.3; test 086
*Xanra valru maldat.*), pronominally by the indefinites **xakaun** / **xakelte** (§13.4;
test 088 *Xakaun vandat.* — Nobody comes).

The adjacency holds in every environment:

| Environment | Attestation |
|---|---|
| subject in the prefield | test 085 *Xna şirn xa soñat.* |
| object behind the verb | test 084 *Lo xa milkat xran narkun.* |
| head + genitive attribute in the prefield | test 045 *Xla taiv xlas eirdes xa vaşnat.* |
| verbal bracket | test 115 *Xna şirn xa vlekat melex.* — *xa* before the **finite** verb |
| subordinate clause | test 090 *Vim zavam, fai ro xa vandat.* |
| wh-question | §18.2 *Grais xa vandat?* |
| directional expression | test 089 *Viñ xa melamen tel xlan kavlan.* |

**(f) Valid permutations.** All lines of the table above are permutations of the same pattern:
the prefield is freely fillable, *xa* stays at the finite verb.

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Vim melam xa.* | *xa* not immediately before the finite verb — §18.3 [rule-derived] |
| †*Xa vim melam.* | likewise: *xa* is separated from the verb [rule-derived] |
| †*Xna şirn vlekat xa melex.* | *xa* before the infinitive instead of before the finite verb — §18.3 [rule-derived] |

> **[REGELUNKLARHEIT U-14]** (rule ambiguity) The second attestation of §18.3, *Vim xa num vna
> breun* ("Ich habe kein Haus"), leaves article and head word in the object unmarked. Conforming
> to §8, §10.3 and §11 would be *vnan breunen* — as test 083 writes it: *Viñ xa numen vnan
> breunen.* The word order is not affected by this.

---

## 9. Modal verb

| Field | Content |
|---|---|
| **(a) German** | Ich kann den Weg sehen. |
| **(b) Orbis** | *Vim valnam xnan melnan milkex.* — **Attestation §16.1** |
| **(c) English** | I can see the way. |
| **(d) Pattern** | PRON-V-NP-V |
| **(h) Rule ID** | ORB-GRAM-SYN-013 (§16.1, §17.3) |

**(e) Explanation.** The **verbal bracket**: the conjugated modal verb stands in position 2, the
main verb in the **infinitive at the end of the sentence** (§16.1). Everything in between is the
middle field. The six modal roots are *valn-* (can), *dolm-* (must), *vlek-* (may), *tirn-*
(shall), *nest-* (want), *suvr-* (like).

Attestations with a growing middle field:

| Middle field | Attestation |
|---|---|
| empty | test 106 *Vim valnam melex.* — I can go. |
| time | §16.1 *Şet dolmaş nunda vandex.* — You must come today. (= test 107) |
| object | test 108 *Ro vlekat xnan vreston leşnex.* — He may read the book. |
| object | test 112 *Şeñ valnaşen xran vrondon milkex.* · test 113 *Oñ dolmaten xlan kavlan traivex.* |
| time + manner + place | §17.3 *Vim valnam nunda zva xraş velkraş dun xlaş kavlaş melex.* |

**(f) Valid permutations.**

| Form | Status |
|---|---|
| middle-field order time – manner – place | **[Attestation §17.3]**, corresponds to the tendency §17.4 — deviations are not violations, because §17.4 calls itself a tendency |
| prefield filled differently | **[rule-derived §17.1]**; an attestation with a topicalized object before a modal verb does not exist |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Vim valnam milkex xnan melnan.* | infinitive not at the end of the sentence — §16.1 [rule-derived] |
| †*Vim xnan melnan valnam milkex.* | finite verb in position 3 — §17.1 [rule-derived] |
| †*Vim milkex xnan melnan valnam.* | finite verb at the end: that is the subordinate-clause order §17.2, not the main clause [rule-derived] |

> **[REGELUNKLARHEIT U-03]** (rule ambiguity) Whether a modal verb may stand without an
> infinitive, that is, as a full verb with a direct object ("Ich mag das Wort"), §16.1 does not
> regulate. Test 111 tests the case and remains open.

---

## 10. Modal verb + negation

| Field | Content |
|---|---|
| **(a) German** | Das Kind darf nicht gehen. |
| **(b) Orbis** | *Xna şirn xa vlekat melex.* — **Attestation test 115** |
| **(c) English** | The child may not go. |
| **(d) Pattern** | NP-PART-V-V |
| **(h) Rule ID** | ORB-GRAM-SYN-013 (§16.1) + ORB-GRAM-SYN-018 (§18.3) |

**(e) Explanation.** Both rules apply independently and without contradiction: *xa* steps before
the **finite** verb (§18.3), the infinitive stays at the end of the sentence (§16.1). The bracket
is thus negated from outside, not from within.

Further attestations: §25.1 *Vim xa valnam soñex, grali xla kirva vran luid est.* — I cannot
sleep, because the night is very bright. · test 150 *Viñ xa valnamen soñex, grali xra morda
span xlaş kavlaş vran xarn est.*

**(f) Valid permutations.**

| Form | Status |
|---|---|
| subject pronoun in the prefield: *Vim xa valnam soñex, …* | **[Attestation §25.1]** |
| subject NP in the prefield: *Xna şirn xa vlekat melex.* | **[Attestation test 115]** |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Xna şirn vlekat xa melex.* | *xa* not at the finite verb — §18.3 [rule-derived] |
| †*Xna şirn xa melex vlekat.* | infinitive not at the end of the sentence — §16.1 [rule-derived] |

> **[REGELKONFLIKT K-05]** (rule conflict) As soon as the same construction enters the
> **subordinate clause**, it is no longer decidable: §16.1 wants the infinitive at the end of
> the sentence, §17.2 the finite verb. Test 105 ("Er weiß, dass sie das Buch nicht lesen kann")
> presents the candidates — *… xa leşnex valnat*? *… leşnex xa valnat*? *… xa valnat leşnex*? —
> and does not decide. No example of the grammar contains a modal verb in a subordinate clause.
> This documentation does not decide.

---

## 11. Subordinate clause

| Field | Content |
|---|---|
| **(a) German** | Ich weiß, dass du kommst. |
| **(b) Orbis** | *Vim zavam, fai şet vandaş.* — **Attestation test 091** |
| **(c) English** | I know that you are coming. |
| **(d) Pattern** | PRON-V-SUBJ-KONJ-PRON-V |
| **(h) Rule ID** | ORB-GRAM-SYN-011 (§17.2) |

**(e) Explanation.** The main clause keeps V2, the subordinate clause puts its finite verb at
the **end** (§17.2). The subordinating conjunction (§20) introduces it and does not count as a
sentence element of the subordinate clause.

Attestations from the grammar: §17.2 *Vim zavam, fai şet nunda dun xnaş breuneş melaş.*
(without translation in the text) · §25.1 *Vim zavam, fai şet zirna vandaiş.* — I know that you
will come tomorrow. · §25.1 *Vim xa valnam soñex, grali xla kirva vran luid est.*

Attestations for all seven conjunctions of §20 are in `SYNTAX.md` §11.2.

If the middle field grows, the final position remains: test 146 *Vim zavam, fai xra vlaidra
valru zirna xnaş şirneş xnan brasin dalvait.* — subject, time, dative object, accusative object,
then the finite verb.

The question word **kur** too introduces, in the attestation, a subordinate clause with verb-final
order: §25.2 *Ro xa zovet, kur xna melna molet* · test 098 *Vim xa zavam, kur xna vresto est.*
§20 does not list *kur* among the subordinating conjunctions; the construction is attested only
by these two sentences.

**(f) Valid permutations.**

| Form | Status |
|---|---|
| subordinate clause preposed | see section 12 — **[Attestation test 093]** |
| negation in the subordinate clause: *Vim zavam, fai ro xa vandat.* | **[Attestation test 090]** |
| middle field of any length | **[Attestation test 146]** |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Vim zavam, fai vandaş şet.* | finite verb not at the end of the subordinate clause — §17.2 [rule-derived] |
| †*Vim zavam, fai şet vandaş nunda.* | likewise: after the finite verb nothing more stands [rule-derived] |
| †*Vim, fai şet vandaş, zavam.* | main-clause verb in position 3 — §17.1. Whether a subordinate clause may be embedded into the main clause at all, §17 does not say; attested it is not [rule-derived] |

---

## 12. Subordinate clause before the main clause

| Field | Content |
|---|---|
| **(a) German** | Wenn du gehst, bleibe ich. |
| **(b) Orbis** | *Tund şet melaş, stanam vim.* — **Attestation test 093** |
| **(c) English** | If you go, I stay. |
| **(d) Pattern** | SUBJ-KONJ-PRON-V-V-PRON |
| **(h) Rule ID** | ORB-GRAM-SYN-012 (§17.1) |

**(e) Explanation.** §17.1 says it literally: "If a subordinate clause stands before the main
clause, it occupies **position 1** — the finite verb follows directly." The whole subordinate
clause is therefore **one** prefield. From this it follows necessarily: the subject of the main
clause stands **after** the verb.

Attestations:

| Test | Orbis | German |
|---|---|---|
| 093 | *Tund şet melaş, stanam vim.* | Wenn du gehst, bleibe ich. |
| 094 | *Şlani xna vresto granz est, leşnam vim non.* | Obwohl das Buch alt ist, lese ich es. |
| 095 | *Dremi viñ maldamen, talat xra valru.* | Während wir warten, spricht der Mann. |
| 096 | *Glemi xla luiv vandat, melamen viñ.* | Bevor die Sonne kommt, gehen wir. |
| 097 | *Trausi ro nastot, soñot ro.* | Nachdem er aß, schlief er. |
| 147 | *Şlani xla kirva girn vot, moleten xrañ melruñ span xran vrondon.* | Obwohl die Nacht kalt war, gingen die Wanderer über den Berg. |
| 148 | *Tund şet xnan vreston xras velkras leşnaş, traivaiş şet xlan klaunuman.* | Wenn du das Buch des Freundes liest, wirst du die Wahrheit finden. |

Grammar attestation with *mai*: §25.1 *Tund vim vra vlaidra valru mai em, mai traivam vim xlan
eirden.* — here *mai traivam* fills position 2 (§16.2).

**(f) Valid permutations.**

| Form | Status |
|---|---|
| subordinate clause postposed, object in the prefield of the main clause: *Xnan melnan traivamen viñ, tund xla luiv luid est.* | **[Attestation §25.1]** |
| subordinate clause postposed, subject in the prefield: *Vim zavam, fai şet zirna vandaiş.* | **[Attestation §25.1]** |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Tund şet melaş, vim stanam.* | main-clause verb in position 3: the subordinate clause already counts as position 1 — §17.1 [rule-derived] |
| †*Tund melaş şet, stanam vim.* | subordinate-clause verb not at the end — §17.2 [rule-derived] |

---

## 13. Relative clause

| Field | Content |
|---|---|
| **(a) German** | Der Mann, der kommt, ist mein Freund. |
| **(b) Orbis** | **no attestation.** Test 100 is rated as **[REGELLÜCKE]** and carries `orbis = null` |
| **(c) English** | The man who is coming is my friend. |
| **(d) Pattern** | not determinable |
| **(h) Rule ID** | ORB-GRAM-SYN-022, status `open`, finding **L-02** |

**(e) Explanation — the situation, not a rule.** §13.4 lists **fai** in the table "remaining
pronouns" under "relative". With that, what 0.9.3 says about the relative clause ends. Missing
are:

| What is missing | Concerns |
|---|---|
| case forms of *fai* | relative pronoun as object (*fain*?), as dative (*faiş*?), as genitive (*fais*?) |
| agreement | gender and number of the antecedent |
| verb position | whether the relative clause takes the final position under §17.2 |
| position | whether the relative clause stands immediately behind the antecedent or is extraposed |
| homonymy | *fai* "that" (§20) against *fai* "who/which" (§13.4) — additionally W-03 |

The affected tests: 100 (relative pronoun as subject), 101 (as accusative object), 102 (as
dative object), 149 (embedded, additionally interlocked with L-01). All four carry
`orbis = null`.

**(f)/(g) Permutations.** Not statable. Without a defined sentence structure there are neither
valid nor invalid permutations; every form would be speculation. Test 100 records this
explicitly: "*Xra valru, fai vandat, xra velkra vis est* wäre reine Spekulation."

> **[REGELLÜCKE L-02]** (rule gap) The structure of the relative clause is entirely missing.
> **This documentation does not decide.** The determination is made by the language designers.

---

## 14. Passive

| Field | Content |
|---|---|
| **(a) German** | Das Haus wird gebaut. |
| **(b) Orbis** | *Xna breun şunargat.* — **Attestation §16.3**, likewise test 136 |
| **(c) English** | The house is being built. |
| **(d) Pattern** | NP-V |
| **(h) Rule ID** | ORB-GRAM-SYN-019, status `provisional`, finding **L-05** |

**(e) Explanation.** The dynamic passive is **morphological**, not syntactic: the prefix **şu-**
attaches to the verb root (§16.3). The word order does not change thereby — the patient stands
as subject in the nominative, the verb stays in position 2.

The **stative passive** forms participle + *esex*: §16.3 *Xna breun şunargut est.* — The house
is built. With that it falls under the predicative construction (section 17) and shares its open
question **U-13**.

| Form | Attestation |
|---|---|
| dynamic passive present | §16.3 / test 136 *Xna breun şunargat.* |
| dynamic passive plural | test 140 *Xnañ vrestoñ şuleşnaten.* — The books are read. |
| stative passive | §16.3 *Xna breun şunargut est.* · test 139 *Xna taisa şutalut est.* — The word is spoken. |

**(f) Valid permutations.** Attested is only the subject-in-prefield order. Topicalization in the
passive sentence is not excluded by §17.1, but it is **not attested**.

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Şunargat xna breun.* (as a statement) | verb in position 1 — §17.1 [rule-derived] |
| ?*Xna breun est şunargut.* | in the stative passive the participle stands before the copula in all attestations; see U-13, section 17 — the reversal is **not decidable**, not attested, and is therefore noted here only as unattested |

> **[REGELLÜCKE L-05] Agent in the passive.** (rule gap) "Das Haus wird **vom Mann** gebaut"
> (test 137) and "Das Buch wurde **von der Frau** gelesen" (test 138) are **not formable**.
> §16.3 regulates only the prefix; no preposition is designated for the agent. *ven* + dative
> would suggest itself — §19 gives *ven* "from" with the dative — but it is nowhere established.
> **This documentation does not decide.**

---

## 15. Dative + accusative

| Field | Content |
|---|---|
| **(a) German** | Die Mutter gibt dem Kind das Brot. |
| **(b) Orbis** | *Xla veiş dalvat xnaş şirneş xnan brasin.* — **Attestation test 023**; in the past tense word for word the same §25.1 *Xla veiş dolvet xnaş şirneş xnan brasin.* — Die Mutter gab dem Kind das Brot. |
| **(c) English** | The mother gives the child the bread. |
| **(d) Pattern** | NP-V-NP-NP |
| **(h) Rule ID** | ORB-GRAM-SYN-023, status `provisional`, finding **U-05** |

**(e) Explanation.** Both objects stand in the middle field, the dative before the accusative.
The roles are marked by case (*xnaş şirneş* dative, *xnan brasin* accusative), not by the order.

Attestations in the same order:

| Test | Orbis | German |
|---|---|---|
| 025 | *Xla sarla dalvat xraş drauneş xnan aulen.* | Die Frau gibt dem Vater das Wasser. |
| 026 | *Vim dalvam xraş velkraş xnan vreston.* | Ich gebe dem Freund das Buch. |
| 034 | *Vim dalvam viş xlan nauşen.* | Ich gebe mir Zeit. (reflexiver Dativ, 1. Person) |
| 064 | *Viñ dalvamen xnañaş şirneiş xnan brasin.* | Wir geben den Kindern das Brot. |
| 120 | *Oñ dolveten xnaş şirneş xnan brasin.* | Sie gaben dem Kind das Brot. |
| 080 | *Kelnaş şirneş dalvaş şet xnan brasin?* | Welchem Kind gibst du das Brot? (Dativ im Vorfeld) |
| 146 | *Vim zavam, fai xra vlaidra valru zirna xnaş şirneş xnan brasin dalvait.* | im Nebensatz, Dativ vor Akkusativ |

**(f) Valid permutations.**

| Form | Status |
|---|---|
| dative object into the prefield: *Kelnaş şirneş dalvaş şet xnan brasin?* | **[Attestation test 080]** — there as a question-word phrase |
| accusative before dative | **not attested.** §17 sets up no rule; U-05 records that dative-before-accusative is **only example practice**. The reversal is thereby not forbidden — but it is not attested either. This documentation does not decide |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Xla veiş xnaş şirneş dalvat xnan brasin.* | finite verb in position 3 — §17.1 [rule-derived] |
| †*Xla veiş dalvat xnaş şirneş xna brasin.* | case error, not an order error: the second object must carry the accusative (§8) [rule-derived] |

> **[REGELUNKLARHEIT U-05]** (rule ambiguity) The object order is the consistent practice of the
> examples, but not a rule.

---

## 16. Genitive attributes

| Field | Content |
|---|---|
| **(a) German** | Die Erinnerung der Zeit vergeht. |
| **(b) Orbis** | *Xla soruma xlas nauşes vaşnat.* — **Attestation test 037**; with degree particle and adverbial §25.1 *Xla soruma xlas nauşes vran tolm vaşnat.* — Die Erinnerung der Zeit vergeht sehr langsam. |
| **(c) English** | The memory of time passes away. |
| **(d) Pattern** | NP-NP-V |
| **(h) Rule ID** | ORB-GRAM-SYN-021, status `open`, finding **L-01** |

**(e) Explanation.** In **all** attestations the genitive attribute stands **behind** its head,
and head + attribute together form **one** sentence position — visible from the fact that the
finite verb follows immediately (*Xla soruma xlas nauşes* = position 1, *vaşnat* = position 2).

Attestations:

| Source | Orbis | German |
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

Related, but not the same: the **possessive** is under §13.3 explicitly **postposed**
(*xna breun vis* — my house · *xla sarla şes* · *xrañ valruñ oñas*). §13.3 regulates only the
possessive pronoun, not the nominal genitive attribute.

**(f) Valid permutations.** The head-attribute group can enter any field as a whole: prefield
(test 037, 045), middle field (test 148), object position (§25.2). That follows from §17.1.

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Xla soruma vaşnat xlas nauşes.* | head and attribute torn apart; no rule allows the extraposition, no attestation shows it [rule-derived] |
| preposing *Xlas nauşes xla soruma vaşnat* | **not decidable** — see L-01 |

> **[REGELLÜCKE L-01] Position of the genitive attribute.** (rule gap) §8 defines the genitive
> only morphologically, §17 is silent on attribute position. Test 036 ("Das Haus des Mannes ist
> alt") presents both candidates — *Xna breun xras valrus granz est* (postposed) and *Xras
> valrus xna breun granz est* (preposed) — and states: **both are morphologically correct**, the
> position is nowhere established. Test 039 ("Das Buch meines Freundes ist neu") additionally
> shows the unregulated **stacking** of genitive attribute and postposed possessive. Test 149
> hangs on L-01 as well as on L-02. **This documentation does not decide**; it only records that
> the uniform practice of the examples postposes.

Affected at the margin: **K-04** — §25.1 uses *tolm* adverbially in this sentence without the
*-un* required by §12.4 (*tolmun*). Test 060 rates this as [REGELKONFLIKT]. The word order is
not affected by it.

---

## 17. Predicative constructions

| Field | Content |
|---|---|
| **(a) German** | Sie ist schön. |
| **(b) Orbis** | *Lo loşn est.* — **Attestation §12.2** |
| **(c) English** | She is beautiful. |
| **(d) Pattern** | PRON-ADJ-V |
| **(h) Rule ID** | ORB-GRAM-SYN-015 (§17.5), finding **U-13** |

**(e) Explanation.** After **esex** (to be), **vurnex** (to become) and **stanex** (to remain)
the adjective stands in the **base form**, without any ending (§12.2). The copula may **not** be
omitted (§17.5) — not even where German or English could delete it.

Attestations §12.2: *Lo loşn est.* (*not:* †*Lo loşna est*) · *Xla kirva girn vot.* · *Xra valru
xarn vurt.* · *Xna breun granz stanat.* · plural *Xrañ larkiñ girn esten.*
Attestation §17.5: *Xla luiv luid vot, xla kirva girn vot.* — The sun was bright, the night was
cold.

**The question of order (U-13).** In **all** attestations of the grammar the predicative stands
**before** the verb; the finite verb thus stands in third **word** position: *Lo*(1) *loşn*(2)
*est*(3). Whether predicative and copula together form one sentence position — as §16.2
explicitly says for *mai* + verb — is nowhere stated. The test corpus attests **both** orders,
both with [OK]:

| Order | Attestation |
|---|---|
| predicative **before** the verb | test 046 *Xra vlaidra vrondo granz est.* · test 053 *Xla girnla kirva trelm est.* · test 057 *Xra valru xarn vurt.* · test 121 *Xla kirva girn vot.* · test 065 *Xrañ larkiñ girn esten.* |
| predicative **after** the verb | test 125 *Viñ voremen xarn.* — We became strong. · test 131 *Xna şirn vurnait xarn.* · test 133 *Şeñ vaişen xarn.* |

A **nominal** predicate is attested too and stands before the copula: test 055 *Lo xla
loşnvaxla sarla est.* — She is the most beautiful woman. Likewise the comparative forms §12.3:
*Ro vlaidvi est kon vim.* — He is bigger than I. · *Lo loşn est zil luiv.* — She is beautiful
like the sun. (test corpus: test 054, test 056 *Lo velm est zil luiv.*)

**(f) Valid permutations.** Both orders attested above. Which conditions govern the choice, the
grammar does not say.

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Lo loşna est.* | predicative declined instead of base form — **§12.2, † of the grammar itself** |
| †*Lo loşn.* | copula omitted — §17.5. The omission as a poetic stylistic device carries in §17.5 the marker **[NOCH ZU ENTSCHEIDEN]** [rule-derived] |

> **[REGELUNKLARHEIT U-13]** (rule ambiguity) Predicative order against V2. The finding was made
> in the corpus run at test 055. **This documentation does not decide** whether *Lo loşn est* is
> an exception to §17.1 or whether predicative + copula count as one position.

---

## 18. Conditional (*mai*)

| Field | Content |
|---|---|
| **(a) German** | Wenn ich ein Haus hätte, würde ich bleiben. |
| **(b) Orbis** | *Tund vim vnan breunen mai num, mai stanam vim.* — **Attestation test 142** |
| **(c) English** | If I had a house, I would stay. |
| **(d) Pattern** | SUBJ-KONJ-PRON-NP-PART-V-PART-V-PRON |
| **(h) Rule ID** | ORB-GRAM-SYN-020 (§16.2), frame ORB-GRAM-SYN-012 (§17.1) |

**(e) Explanation.** §16.2 establishes two things: **mai** stands **immediately before the finite
verb**, and *mai* + finite verb form **one** sentence position. Both together explain the
conditional construction completely:

| Part | Position | Reason |
|---|---|---|
| *Tund vim vnan breunen mai num* | *mai num* at the end of the subordinate clause | §17.2 (verb-final order) + §16.2 (adjacency) |
| *mai stanam vim* | *mai stanam* in position 2 | §17.1 (the subordinate clause is position 1) + §16.2 (*mai* + verb = one position) |

Grammar attestation, §16.2 and §25.1: *Vim mai melam.* — I would go. · *Tund vim vra vlaidra
valru mai em, mai traivam vim xlan eirden.* — If I were a great man, I would find the world.

Further attestations:

| Test | Orbis | German |
|---|---|---|
| 141 | *Vim mai melam.* | Ich würde gehen. |
| 143 | *Tund xla kirva girn mai est, mai maldamen viñ.* | Wenn die Nacht kalt wäre, würden wir warten. |
| 144 | *Ro mai leşnat xnan vreston.* | Er würde das Buch lesen. |
| 145 | *Vim mai valnam melex.* | Ich könnte gehen. (*mai* vor dem **finiten** Modalverb) |

**(f) Valid permutations.**

| Form | Status |
|---|---|
| simple main clause without subordinate clause: *Vim mai melam.* | **[Attestation §16.2]** |
| with object in the middle field: *Ro mai leşnat xnan vreston.* | **[Attestation test 144]** |
| with verbal bracket: *Vim mai valnam melex.* | **[Attestation test 145]** |
| *mai* only in the main clause, not in the subordinate clause | **not attested**: all three conditional attestations (§25.1, test 142, test 143) set *mai* in both parts |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Vim melam mai.* | *mai* not immediately before the finite verb — §16.2 [rule-derived] |
| †*Mai vim melam.* | *mai* separated from the verb — §16.2 [rule-derived] |
| †*Vim valnam mai melex.* | *mai* before the infinitive instead of before the finite verb — §16.2 [rule-derived] |
| †*Tund vim vnan breunen mai num, vim mai stanam.* | main clause: *mai stanam* in position 3, because the subordinate clause already fills position 1 — §17.1 + §16.2 [rule-derived] |

---

## 19. Multiple subordinate clauses

| Field | Content |
|---|---|
| **(a) German** | Er wusste nicht, wohin der Weg führte, aber er ging. |
| **(b) Orbis** | *Ro xa zovet, kur xna melna molet, klas ro molet.* — **Attestation §25.2**. A sentence with **two subordinate clauses** is attested neither in 0.9.3 nor in test corpus 0.1 |
| **(c) English** | He did not know where the way led, but he went. |
| **(d) Pattern** | PRON-PART-V — SUBJ-W-NP-V — KONJ-PRON-V |
| **(h) Rule ID** | ORB-GRAM-SYN-011 (§17.2) + ORB-GRAM-SYN-012 (§17.1) |

**(e) Explanation.** The longest attested sentence chain of the grammar consists of **main clause
+ indirect question + coordinated main clause**. Each part keeps its own verb position:

| Part | Position | Rule |
|---|---|---|
| *Ro xa zovet* | verb on 2, *xa* before it | §17.1, §18.3 |
| *kur xna melna molet* | verb at the end | §17.2 |
| *klas ro molet* | verb on 2 of the conjunct | §17.1, §20 |

**What is not attested.** No sentence of the grammar and no sentence of test corpus 0.1 contains
two subordinate clauses — neither coordinated ("…, dass A, und dass B") nor nested ("…, dass A,
weil B"). Test 149 would have been the maximal test, but it already fails on the relative clause
(L-02). Thus **unregulated and unattested** are:

- the order of two subordinate clauses of equal rank relative to each other,
- the embedding of one subordinate clause in another,
- whether several preposed subordinate clauses may fill position 1 together.

For none of these points is a finding ID assigned in the audit; they are simply not treated.

**(f) Valid permutations.** Attested is only that a single subordinate clause may be preposed or
postposed (sections 11 and 12). Anything further is not derivable.

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Ro xa zovet, kur molet xna melna, klas ro molet.* | subordinate-clause verb not at the end — §17.2 [rule-derived] |
| †*Ro xa zovet, kur xna melna molet, klas molet ro.* | conjunct verb in position 1 — §17.1 [rule-derived] |

As soon as a **modal verb** stands in one of these subordinate clauses, **K-05** applies in
addition.

---

## 20. Coordination

| Field | Content |
|---|---|
| **(a) German** | Er aß, er trank, und er schlief. |
| **(b) Orbis** | *Ro nastot, ro prevot, ze ro soñot.* — **Attestation §25.2** |
| **(c) English** | He ate, he drank, and he slept. |
| **(d) Pattern** | [PRON-V] — [PRON-V] — KONJ-[PRON-V] |
| **(h) Rule ID** | §20 / `ORB-GRAM-SYN-002`; the verb position per conjunct under ORB-GRAM-SYN-010. The block -010…-025 contains **no** rule ID of its own for coordination |

**(e) Explanation.** §20 names four coordinating conjunctions: **ze** (and) · **vu** (or) ·
**klas** (but) · **xer** (for). They join main clauses, and every partial clause keeps its V2
order.

Decisive for the word order: in all attestations the coordinating conjunction does **not** count
as position 1. It is followed by the subject, then the verb:

| Attestation | Count |
|---|---|
| §25.2 *ze ro soñot* | *ze* – *ro*(1) – *soñot*(2) |
| §25.2 *Ze ro dremnot: „Kilna est xna traivute."* | sentence-initial *ze*, after it V2 |
| §25.2 *klas ro molet* | *klas* – *ro*(1) – *molet*(2) |
| §25.1 *klas xla kavla zirv vurt* | *klas* – *xla kavla*(1) – *zirv* – *vurt* → see **U-13** |
| Test 099 *xer xla kirva girn est* | *xer* – *xla kirva*(1) – *girn* – *est* → see **U-13** |

§20 itself says nothing about the counting of positions; the statement rests on these five
attestations.

Likewise attested is the **asyndetic** sequence without a conjunction: §25.2 *Ro nastot, ro
prevot, …* and *Xla luiv luid vot, xla kirva girn vot.* (§17.5). A rule for this is not in §20.

**vu** (or) has **not a single attestation** — neither in 0.9.3 nor in test corpus 0.1.

**(f) Valid permutations.**

| Form | Status |
|---|---|
| *ze* clause-internal: *…, ze ro soñot.* | **[Attestation §25.2]** |
| *ze* sentence-initial: *Ze ro dremnot: …* | **[Attestation §25.2]** |
| asyndetic, without conjunction | **[Attestation §25.2, §17.5]** |
| prefield of the second conjunct filled differently | **[rule-derived §17.1]**, no attestation |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Ro nastot, ze soñot ro.* | conjunct verb in position 1 — §17.1, supported by the consistent counting of the attestations [rule-derived] |
| †*Ro nastot, ro soñot ze.* | postposed conjunction; no attestation, no rule for it [rule-derived] |

---

## 21. Contrast

| Field | Content |
|---|---|
| **(a) German** | Das Haus bleibt alt, aber die Stadt wird neu. |
| **(b) Orbis** | *Xna breun granz stanat, klas xla kavla zirv vurt.* — **Attestation §25.1** |
| **(c) English** | The house stays old, but the city becomes new. |
| **(d) Pattern** | NP-ADJ-V — KONJ-NP-ADJ-V |
| **(h) Rule ID** | §20 / `ORB-GRAM-SYN-002` + ORB-GRAM-SYN-010; concessive ORB-GRAM-SYN-011 / -012 |

**(e) Explanation.** Orbis knows two attested ways of expressing opposition:

| Route | Means | Effect on the word order | Attestation |
|---|---|---|---|
| **coordinating** | *klas* (but) | both partial clauses stay main clauses with V2 | §25.1 *Xna breun granz stanat, klas xla kavla zirv vurt.* · §25.2 *…, klas ro molet.* |
| **subordinating** | *şlani* (although) | the concessive part becomes a subordinate clause with verb-final order and can occupy position 1 | Test 094 *Şlani xna vresto granz est, leşnam vim non.* · Test 147 *Şlani xla kirva girn vot, moleten xrañ melruñ span xran vrondon.* |

The difference is purely syntactic: with *klas* two main clauses of equal rank remain, with
*şlani* the subordinate clause moves into the prefield and forces the main-clause subject behind
the verb (*leşnam vim*, *moleten xrañ melruñ*).

Both *klas* attestations and the *xer* attestation (test 099) contain a **predicative before the
verb** and thereby fall under **U-13**.

**(f) Valid permutations.**

| Form | Status |
|---|---|
| concessive subordinate clause preposed | **[Attestation test 094, test 147]** |
| concessive subordinate clause postposed | **[rule-derived §17.1]** — not attested for *şlani*; attested postposed for *grali* and *tund* (§25.1) |
| causal contrast with *xer*: *Vim maldam, xer xla kirva girn est.* | **[Attestation test 099]** |

**(g) Invalid permutations.**

| Form | Violation |
|---|---|
| †*Xna breun granz stanat, klas vurt xla kavla zirv.* | conjunct verb in position 1 — §17.1 [rule-derived] |
| †*Xna breun granz stanat, xla kavla klas zirv vurt.* | *klas* clause-internal instead of at the head of the conjunct; all attestations put the coordinating conjunction first, §20 does not establish the position explicitly [rule-derived] |
| †*Şlani xna vresto granz est, vim leşnam non.* | main-clause verb in position 3, because the subordinate clause fills position 1 — §17.1 [rule-derived] |

---

## 22. Information structure

| Field | Content |
|---|---|
| **(a) German** | Der Mann sieht den Hund. / Den Hund sieht der Mann. / Heute sieht der Mann den Hund. |
| **(b) Orbis** | *Xra valru milkat xran narkun.* · *Xran narkun milkat xra valru.* · *Nunda milkat xra valru xran narkun.* — **Attestation §17.1** |
| **(c) English** | The man sees the dog. / The dog, the man sees. / Today the man sees the dog. |
| **(d) Pattern** | X-V-… |
| **(h) Rule ID** | ORB-GRAM-SYN-010 (§17.1) for the prefield, ORB-GRAM-SYN-014 (§17.4) for the middle field. A rule ID for information structure does **not** exist in the block -010…-025 |

**(e) Explanation — only as far as attested.** Grammar 0.9.3 makes **no statement about what the
filling of the prefield means**. Attested is exclusively:

1. **The prefield is free.** §17.1 lists three orders of the same statement side by side, without
   marking any of them as the normal case, as emphatic or as marked.
2. **The middle field has a tendency.** §17.4 names time – reason – manner – place and says
   explicitly "tendency, not a hard rule".
3. **Case carries the roles.** Because subject and object are morphologically marked (§8), no
   word order is needed for disambiguation — the freedom of the prefield is structurally
   possible.

What is **not** in 0.9.3: focus particles, cleft sentences, topic markers, a rule for contrastive
emphasis, a statement about given before new. The degree particles *vran* (very) and *skirm*
(little) of §24.9 are means of degree, not of information — attested in §25.1 *vran tolm
vaşnat*, *vran luid est* and test 150 *vran xarn est*.

**(f) Valid permutations.** All three lines under (b), of equal rank.

**(g) Invalid permutations.** Only the general order violations (verb not in position 2, two
elements in the prefield). An information-structural error is not definable in 0.9.3, because no
rule exists against which it could offend.

> **No finding assigned.** The audit lists no ID for information structure. That is not a
> contradiction of the grammar but an undescribed territory. **This documentation does not fill
> it.**

---

## Open points of word order

| ID | Type | Section | Summary |
|---|---|---|---|
| **L-01** | gap | 16 | position of the genitive attribute, incl. stacking with the possessive |
| **L-02** | gap | 13 | structure of the relative clause entirely undefined |
| **L-05** | gap | 14 | agent in the passive |
| **K-05** | conflict | 10, 11, 19 | modal verb in the subordinate clause: infinitive against finite verb at the end of the sentence |
| **U-13** | ambiguity | 17, 20, 21 | predicative before the verb against the V2 rule |
| **U-05** | ambiguity | 15 | object order dative before accusative only practice |
| **U-04** | ambiguity | 6, 7 | subject omission in questions only practice |
| **U-11** | ambiguity | 4 | temporal dative without preposition (*Vraş zaldreş*) |
| **U-03** | ambiguity | 9 | modal verb without infinitive |
| **L-03** | gap | 7 | declension of *kem/kelt* |
| **U-14** | ambiguity | 8 | *Vim xa num vna breun* leaves article and head word unmarked |
| **K-04** | conflict | 16 | *tolm* adverbial without *-un* in §25.1 |

Unattested, but not carried as a finding: adverb in *-un* in the prefield (section 5),
two subordinate clauses in one sentence (section 19), *vu* as a conjunction (section 20),
eight of the sixteen prepositions (`SYNTAX.md` §10).

Full description of all findings: `Orbis-Audit-0_1.md` §A; machine-readable in
`language/findings/findings.json`.

---

*Documentation for Grammar 0.9.3. In case of deviation, `Orbis-Grammatik-0.9.3.md` applies.*
