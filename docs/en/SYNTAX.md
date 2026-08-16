# ORBIS — Syntax: sentence structure, questions, negation, prepositions, conjunctions

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md). Describes Orbis Grammar 0.9.3.*

---

This chapter gives the overview of **§17 to §20**: the two verb positions, the verbal
bracket, the order of sentence elements, the question types, negation, the prepositional
system and the conjunctions. The detailed treatment of the individual positional patterns
with permutation tests is in `WORD_ORDER.md`.

**Obligation of attestation.** Every rule of this chapter is attested by at least one
sentence that stands literally in `Orbis-Grammatik-0.9.3.md` or in
`Orbis-Testkorpus-0_1.md`. Where no attestation exists, this is stated explicitly.
Ungrammatical forms are marked with **†** — just as the grammar itself does in §12.2
(*†Lo loşna est*).

**This file decides nothing.** Where the grammar is silent or contradicts itself, the
finding ID from `Orbis-Audit-0_1.md` §A is given. The rule IDs `ORB-GRAM-SYN-*` refer to
`language/syntax/rules.json`.

---

## 1. The frame: two verb positions (§17)

Orbis has exactly two positions for the finite verb. Which one applies depends solely on
the sentence type:

| Sentence type | Position of the finite verb | Paragraph | Rule ID |
|---|---|---|---|
| Declarative main clause | position 2 | §17.1 | ORB-GRAM-SYN-010 |
| Yes/no question | position 1 | §18.1 | ORB-GRAM-SYN-016 |
| Wh-question | position 2 (question word in 1) | §18.2 | ORB-GRAM-SYN-017 |
| Subordinate clause | end of clause | §17.2 | ORB-GRAM-SYN-011 |

There is no third pattern. The imperative is described in §14 only morphologically
(*Mel!*, *Meleñ!*, *Melaten!*); a positional rule for the imperative sentence stands
neither in §14 nor in §17.

---

## 2. Main clause — verb in position 2 (§17.1)

> **ORB-GRAM-SYN-010** — The finite verb stands in second position in the declarative main
> clause.

The grammar attests the rule with three arrangements of the same statement. Position 1
changes, the verb stays in 2:

| Position 1 | Verb (2) | Remainder | English |
|---|---|---|---|
| *Xra valru* | *milkat* | *xran narkun.* | The man sees the dog. |
| *Xran narkun* | *milkat* | *xra valru.* | The dog, the man sees. |
| *Nunda* | *milkat* | *xra valru xran narkun.* | Today the man sees the dog. |

All three lines stand literally in §17.1; the first also in §25.1.

Position 1 is **one** sentence position, no matter how many words fill it: *Xra valru* is
one field, *Nunda* likewise. Two special cases are explicitly regulated:

- **The particle *mai* does not count independently.** §16.2: "*mai* and the finite verb
  form **one** sentence position." Attestation §25.1: *Tund vim vra vlaidra valru mai em,
  mai traivam vim xlan eirden.* — the following clause begins with *mai traivam*, and that
  is position 2.
- **A preposed subordinate clause occupies position 1** (see section 4).

For the negation particle *xa*, §18.3 makes **no** corresponding statement about position
counting; §18.3 only fixes the adjacency (*xa* immediately before the finite verb). The
audit records no finding on negation (`Orbis-Audit-0_1.md` §13).

---

## 3. Subordinate clause — verb at the end (§17.2)

> **ORB-GRAM-SYN-011** — In the subordinate clause the finite verb stands at the end.

Attestation §17.2: *Vim zavam, fai şet nunda dun xnaş breuneş melaş.* (The grammar gives no
translation for this sentence.)

Attestation with translation, §25.1: *Vim zavam, fai şet zirna vandaiş.* — I know that you
will come tomorrow. · *Vim xa valnam soñex, grali xla kirva vran luid est.* — I cannot
sleep, because the night is very bright.

Verb-final position applies to all seven subordinating conjunctions of §20 (section 9). In
the attestations it also applies to the **indirect question**: §25.2 *Ro xa zovet, kur xna
melna molet* — He did not know where the way led. §20 does not list *kur* among the
subordinating conjunctions; the construction is attested only by this example and by
test 098 (*Vim xa zavam, kur xna vresto est.*).

---

## 4. The preposed subordinate clause (§17.1)

> **ORB-GRAM-SYN-012** — If a subordinate clause stands in position 1, the finite verb of
> the main clause follows immediately.

§17.1 says it literally: "If a subordinate clause stands before the main clause, it
occupies position 1 — the finite verb follows directly."

Attestation §25.1: *Xnan melnan traivamen viñ, tund xla luiv luid est.* (subordinate clause
postposed) · *Tund vim vra vlaidra valru mai em, mai traivam vim xlan eirden.* (subordinate
clause preposed, then *mai traivam*).

Attestations from the test corpus: test 093 *Tund şet melaş, stanam vim.* · test 095 *Dremi
viñ maldamen, talat xra valru.* · test 097 *Trausi ro nastot, soñot ro.*

The effect is regular: because the subordinate clause fills position 1, the subject of the
main clause stands **after** the verb.

---

## 5. Verbal bracket (§17.3, §16.1)

> **ORB-GRAM-SYN-013** — Modal verb in position 2, infinitive at the end of the sentence.

§16.1: "Conjugated modal verb in position 2, main verb in the **infinitive at the end of
the sentence**."

Attestation §17.3: *Vim valnam nunda zva xraş velkraş dun xlaş kavlaş melex.* (without
translation in the grammar) · Attestation §16.1: *Vim valnam xnan melnan milkex.* — I can
see the way. · *Şet dolmaş nunda vandex.* — You must come today.

Everything between modal verb and infinitive is the middle field. The six modal roots are
*valn-* (can), *dolm-* (must), *vlek-* (may), *tirn-* (shall), *nest-* (want), *suvr-*
(like) (§16.1).

> **[REGELKONFLIKT K-05]** (rule conflict) **Verbal bracket in the subordinate clause.**
> §16.1 requires the infinitive "at the end of the sentence", §17.2 the finite verb at the
> end of the subordinate clause. In the subordinate clause both claim the same position. No
> example in 0.9.3 contains a modal verb in a subordinate clause; test 103 and test 105 test
> the case deliberately and remain undecidable. This documentation does not decide.

> **[REGELUNKLARHEIT U-03]** (rule ambiguity) **Modal verb without infinitive.**
> Whether a modal verb may stand as a main verb with a direct object is not regulated by
> §16.1 (test 111).

---

## 6. Order of elements in the middle field (§17.4)

> **ORB-GRAM-SYN-014** — Time – reason – manner – place. Status: `provisional`.

§17.4 names the order **time – reason – manner – place** and says explicitly about it:
"tendency, not a hard rule."

Attestation §17.4: *Vim melaim zirna gral xlas talumas zva xraş velkraş dun xlaş kavlaş.*
(without translation in the grammar)

| Field | Expression | Type |
|---|---|---|
| Prefield | *Vim* | subject |
| Verb (2) | *melaim* | 1 sg future |
| Time | *zirna* | adverb |
| Reason | *gral xlas talumas* | *gral* + genitive |
| Manner | *zva xraş velkraş* | *zva* + dative |
| Place | *dun xlaş kavlaş* | *dun* + dative |

Because §17.4 marks the order itself as a tendency, a deviation is **not a violation**. An
attestation of a deviating order stands in §17.3: there *nunda* (time) precedes the manner
and place expressions, a reason is absent — the order remains intact.

> **[REGELUNKLARHEIT U-05] Object order.** Dative before accusative is the consistent
> practice of the examples (*dolvet xnaş şirneş xnan brasin*, §25.1), but not a rule
> (ORB-GRAM-SYN-023).

> **[REGELUNKLARHEIT U-11] Temporal dative.** §25.2 uses *Vraş zaldreş* ("on a day") as a
> bare dative time expression without a preposition. §8, §17 and §19 do not provide for this
> construction (ORB-GRAM-SYN-025).

---

## 7. No omission of the copula (§17.5)

> **ORB-GRAM-SYN-015** — The copula is not omitted.

Attestation §17.5: *Xla luiv luid vot, xla kirva girn vot.* — The sun was bright, the night
was cold. Both partial clauses set *vot*; neither omits it.

§17.5 additionally carries the marker **[NOCH ZU ENTSCHEIDEN]** (still to be decided) for
omission as a poetic stylistic device. Until then the rule holds without exception.

The predicative adjective stands in this case in the **basic form** (§12.2): *Lo loşn est.*,
*Xra valru xarn vurt.*, *Xna breun granz stanat.*, *Xrañ larkiñ girn esten.*

> **[REGELUNKLARHEIT U-13] Predicative and V2.**
> In all examples of the grammar the predicative stands **before** the verb, so the verb
> stands in third word position (*Lo loşn est* = 1 *Lo*, 2 *loşn*, 3 *est*). Whether
> predicative and copula together form one sentence position is not stated by the grammar.
> The test corpus attests both orders: test 057 *Xra valru xarn vurt* (predicative before the
> verb) and test 125 *Viñ voremen xarn* (predicative after the verb) are both rated [OK].

---

## 8. Questions (§18.1, §18.2)

### 8.1 Yes/no question — verb in position 1

> **ORB-GRAM-SYN-016** — The finite verb stands in position 1.

Attestation §18.1: *Melaş nunda?* — Are you going today? Answer particles: **ain** (yes) ·
**xaus** (no).

Attestations from the test corpus: test 071 *Melaş şet nunda?* · test 072 *Vandat xra
draun?* · test 114 *Valnaten şevar vin zaubex?* (polite form §13.2 + verbal bracket).

The grammar attestation *Melaş nunda?* omits the subject pronoun, test 071 sets it. Both
count as correct — see U-04 below.

### 8.2 Wh-question — question word in 1, verb in 2

> **ORB-GRAM-SYN-017** — Question word position 1, finite verb position 2.

| Orbis | English |
|---|---|
| **kem** | who |
| **kelt** | what |
| **kur** | where, whither |
| **kan** | when |
| **grais** | why |
| **kolm** | how |
| **kelra / kella / kelna** | which (m / f / n) |

Attestations §18.2: *Kan melaş?* · *Grais xa vandat?* · *Kellan sarlan milkoş?*
Attestations from the test corpus: test 073 *Kem talat?* · test 077 *Kur maldaşen şeñ?* ·
test 078 *Kolm est xla kirva?* · test 079 *Kelnan vreston leşnaş şet?* · test 080 *Kelnaş
şirneş dalvaş şet xnan brasin?*

*kelra / kella / kelna* agree adjectivally with their noun — attested by *Kellan sarlan*
(accusative, §18.2) and tests 079/080.

> **[REGELLÜCKE L-03]** (rule gap) **Declension of *kem/kelt*.**
> §18.2 lists only the basic forms. "Whom?", "To whom?", "Whose?" cannot be formed; neither
> case forms nor indeclinability are established (tests 074, 075, 076).

> **[REGELUNKLARHEIT U-04] Subject omission (pro-drop).**
> The §18 examples omit the subject pronoun (*Melaş nunda?*, *Kan melaş?*, *Grais xa
> vandat?*), all declarative examples retain it. When omission is admissible is stated by no
> rule (ORB-GRAM-SYN-024).

---

## 9. Negation (§18.3)

> **ORB-GRAM-SYN-018** — Particle *xa* immediately before the finite verb; attributively
> *xan-*.

§18.3 knows **one single** negation particle: **xa**, immediately before the finite verb.

| Function | Means | Attestation |
|---|---|---|
| Clause/verb negation | particle **xa** before the finite verb | *Vim xa melam.* (§18.3) — I do not go. |
| Attributive negation | adjective **xan-**, declined as in §12.1 | *xanra valru* (§18.3) — no man; test 086 *Xanra valru maldat.* |
| Negative indefinite pronoun | **xakaun** (nobody), **xakelte** (nothing), §13.4 | test 088 *Xakaun vandat.* — Nobody comes. |

The particle stays directly before the finite verb even when the prefield is filled or a
verbal bracket is present:

- Test 045 *Xla taiv xlas eirdes xa vaşnat.* — prefield with genitive attribute, *xa* stays
  at the verb.
- Test 115 *Xna şirn xa vlekat melex.* — with the verbal bracket *xa* stands before the
  **finite** verb, not before the infinitive.
- Test 090 *Vim zavam, fai ro xa vandat.* — in the subordinate clause before the
  clause-final finite verb.
- §18.2 *Grais xa vandat?* — also in the wh-question.

> **[REGELUNKLARHEIT U-14] Unmarked object in §18.3.**
> The attestation *Vim xa num vna breun* ("I have no house") leaves article and core word
> unmarked; in accordance with §8/§10.3/§11 it would be *vnan breunen* — which is how
> test 083 writes it (*Viñ xa numen vnan breunen.*).

---

## 10. Prepositions (§19)

> **ORB-GRAM-SYN-001** (data set `language/syntax/prepositions.json`)

Sixteen prepositions, divided into three fixed case groups and one alternating group. The
column "Attestation" names an attested source or states that none exists.

### 10.1 Fixed case

| Orbis | English | Case | Attestation |
|---|---|---|---|
| **zva** | with | dative | *zva xraş velkraş* (§17.3, §17.4) |
| **dun** | to, towards | dative | *dun xnaş breuneş vis* (§25.1); *dun xlaş kavlaş* (§17.3) |
| **ven** | from | dative | **no attestation** in grammar or test corpus |
| **nul** | at, by | dative | **no attestation** |
| **xun** | without | accusative | **no attestation** |
| **prai** | for | accusative | **no attestation** |
| **dral** | through | accusative | *dral xrañan trelmrañan zaldreñen* (§25.2) |
| **gral** | because of | genitive | *gral xlas talumas* (§17.4) |
| **şlan** | despite | genitive | **no attestation** |

### 10.2 Alternating prepositions — dative = place, accusative = direction

| Orbis | English | Attestation |
|---|---|---|
| **tel** | in | *Vim melam tel xlan kavlan.* (acc = direction, §19) · *Vim em tel xlaş kavlaş.* (dat = place, §19) · *Tel xraş navildoş milkot ro …* (§25.2) |
| **kru** | on | test 031 *Vim maldam kru xlaş melvaş.* (dat = place) |
| **span** | over | *span xran vrondon* (§25.1, direction) · test 150 *span xlaş kavlaş* (place) |
| **drel** | under | **no attestation** |
| **glem** | before, in front of | **no attestation** |
| **traus** | behind | **no attestation** |
| **şlim** | between | *şlim xrañaş larkiñiş* (§25.2, dative) |

Eight of the sixteen prepositions have **not a single example sentence** in 0.9.3 and in
test corpus 0.1: *ven, nul, xun, prai, şlan, drel, glem, traus*. Their case assignment
stands in the table of §19 and is thereby regulated; attested it is not. (Test 137 considers
*ven xraş valruş* for the passive agent, but explicitly rejects the form as unregulated —
see L-05.)

### 10.3 Preposition and prefix

§19 states explicitly: **preposition and prefix are separate categories.** *dral* is only a
preposition, *dra-* only a prefix (§21.2, *dramilkat*).

---

## 11. Conjunctions (§20)

> **ORB-GRAM-SYN-002** (data set `language/syntax/conjunctions.json`)

### 11.1 Coordinating — main-clause position

| Orbis | English | Attestation |
|---|---|---|
| **ze** | and | §25.2 *Ro nastot, ro prevot, ze ro soñot.* · *Ze ro dremnot: „Kilna est xna traivute."* |
| **vu** | or | **no attestation** in grammar or test corpus |
| **klas** | but | §25.1 *Xna breun granz stanat, klas xla kavla zirv vurt.* · §25.2 *…, klas ro molet.* |
| **xer** | for, because | test 099 *Vim maldam, xer xla kirva girn est.* |

The coordinating conjunction does **not** count as position 1: in *ze ro soñot* and *klas ro
molet* the conjunction is followed by the subject, then the verb — so the verb still stands
in position 2 of the partial clause. This also holds clause-initially: *Ze ro dremnot …*
(§25.2).

### 11.2 Subordinating — verb-final position

| Orbis | English | Attestation |
|---|---|---|
| **fai** | that | §25.1 *Vim zavam, fai şet zirna vandaiş.* |
| **grali** | because | §25.1 *…, grali xla kirva vran luid est.* |
| **tund** | if, when | §25.1 *Xnan melnan traivamen viñ, tund xla luiv luid est.* |
| **şlani** | although | test 094 *Şlani xna vresto granz est, leşnam vim non.* |
| **dremi** | while | test 095 *Dremi viñ maldamen, talat xra valru.* |
| **glemi** | before | test 096 *Glemi xla luiv vandat, melamen viñ.* |
| **trausi** | after | test 097 *Trausi ro nastot, soñot ro.* |

### 11.3 The derivation claim (U-07)

§20 writes: "systematically derived from the prepositions, suffix **-i**."

| Conjunction | Preposition | Derivation |
|---|---|---|
| grali | gral (because of) | holds |
| şlani | şlan (despite) | holds |
| glemi | glem (before) | holds |
| trausi | traus (behind) | holds |
| **dremi** | — | no preposition \*drem; *drel* "under" would give *dreli* |
| **tund** | — | no *-i*, no base |
| **fai** | — | no base |

> **[REGELUNKLARHEIT U-07]** The claim holds for four of seven forms. For *dremi*, *tund*
> and *fai* it is false or empty. This documentation does not correct the claim; it reports
> the finding.

In addition **fai** is homonymous: §13.4 lists it as a relative pronoun, §20 as the
conjunction "that" (see L-02 and W-03).

---

## 12. Comparison particles (§12.3)

Not counted among the conjunctions of §20, but clause-linking: **kon** (than) and **zil**
(like, as).

Attestations §12.3: *Ro vlaidvi est kon vim.* — He is bigger than I. · *Lo loşn est zil
luiv.* — She is beautiful like the sun. Test corpus: test 054 (*kon vim*), test 056 (*Lo
velm est zil luiv.*).

> **[REGELUNKLARHEIT U-06]** Which case follows *kon* and *zil* is not established; the
> attestations show the nominative (*kon vim*, *zil luiv*), a rule on this is missing.

---

## 13. Open points of the syntax

This documentation decides nothing. Complete description of all findings:
`Orbis-Audit-0_1.md` §A; machine-readable in `language/findings/findings.json`.

| ID | Type | Concerns | Short | Rule ID |
|---|---|---|---|---|
| L-01 | gap | §8, §17 | position of the genitive attribute, incl. stacking with the possessive | ORB-GRAM-SYN-021 |
| L-02 | gap | §13.4, §17 | relative-clause construction: case, agreement, verb position of *fai*; homonymy with *fai* "that" | ORB-GRAM-SYN-022 |
| K-05 | conflict | §16.1 ↔ §17.2 | modal verb in the subordinate clause: infinitive and finite verb claim the same final position | ORB-GRAM-SYN-013 |
| U-04 | ambiguity | §18 | pro-drop only the practice of the examples | ORB-GRAM-SYN-024 |
| U-05 | ambiguity | §17 | object order dative before accusative only practice | ORB-GRAM-SYN-023 |
| U-11 | ambiguity | §25.2 | temporal dative without preposition (*Vraş zaldreş*) | ORB-GRAM-SYN-025 |
| U-13 | ambiguity | §12.2 ↔ §17.1 | predicative stands before the verb in all grammar examples; rubs against V2 | ORB-GRAM-SYN-015 |

Further findings concern the syntax indirectly:

| ID | Type | Concerns | Short |
|---|---|---|---|
| L-03 | gap | §18.2 | declension of *kem/kelt* (whom/to whom/whose) |
| L-04 | gap | §13.4 | case forms of the reflexive *se* — affects every reflexive sentence pattern |
| L-05 | gap | §16.3 | agent in the passive |
| L-08 | gap | §24.8 | syntax of the cardinal numbers |
| U-02 | ambiguity | §12, §14 | can the participle be used attributively? |
| U-03 | ambiguity | §16.1 | modal verb without infinitive |
| U-06 | ambiguity | §12.3 | case after *kon/zil* |
| U-07 | ambiguity | §20 | derivation claim does not fit *dremi/tund/fai* |
| U-14 | ambiguity | §18.3 | *Vim xa num vna breun* leaves article and core word unmarked |

---

*Documentation of Grammar 0.9.3. In case of divergence, `Orbis-Grammatik-0.9.3.md` prevails.*
