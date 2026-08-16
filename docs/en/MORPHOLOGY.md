# ORBIS — Morphology: Overview

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md). Describes Orbis Grammar 0.9.3.*

---

## 1. Subject and structure of this chapter

The morphology of Orbis covers everything that is inflected or derived on a word: gender,
case and number on the noun (§6–§11), agreement and comparison on the adjective (§12),
person, number and tense on the verb (§14–§16), as well as word formation (§21). This
chapter gives the overview; the details are found in the chapters it refers to.

| Chapter | File | Subject |
|---|---|---|
| Noun | `docs/en/NOUNS.md` | §6–§11: 45 endings, four cases, plural, irregular nouns, article |
| Verbs | `docs/en/VERBS.md` | §14–§16: conjugation, tenses, irregular verbs, modality, passive |
| Adjectives | `docs/en/ADJECTIVES.md` | §12: attributive, predicative, comparison, adverb, nominalization |

Not part of morphology are sentence structure (§17–§20), the sound system (§2–§5), stress
(§23) and the script Orbis Manus (§26). Manus and script rules are not mixed with grammar
rules here.

---

## 2. The principle of construction

Orbis builds its word forms agglutinatively from left to right. The basic formula is given
in §8:

> **Stem + class consonant + theme vowel + case marker**

For the noun, §6 adds the purpose of the two middle building blocks: the **class
consonant** carries the gender, the **theme vowel** belongs permanently to the word and
provides variety of sound. According to §9 the plural is inserted between theme vowel and
case marker.

On the fully attested example *valruñuş* (dative plural of *valru* "man", §9):

| Position | Component | Function | Paragraph |
|---|---|---|---|
| 1 | *val-* | lexical stem | §8 |
| 2 | *-r-* | class consonant, masculine (subclass M-A) | §7.1 |
| 3 | *-u-* | theme vowel | §6 |
| 4 | *-ñ-* | plural marker | §9 |
| 5 | *-u-* | echo vowel (only in the oblique cases) | §9, U-09 |
| 6 | *-ş* | case marker, dative | §8 |

The grammar does not give a list of lexical noun stems; it gives the formula (§8) and the
finished forms. Where a stem is explicitly attested, the construction can be shown
directly — §21.1 documents the root **mel-** "to go" together with its word family:

| Form | Construction | Class | Meaning |
|---|---|---|---|
| *melex* | mel- + -ex | infinitive | to go |
| *melru* | mel- + r + u | M-A | wanderer |
| *mela* | mel- + l + a, junction rule §21.4 | F-A | wanderer (f.) |
| *melna* | mel- + n + a | N-A | way |
| *melisto* | mel- + -isto | N-C | vehicle |
| *melvi* | mel- + -vi | adjective base form | eager to travel |
| *meluma* | mel- + -uma | F-C | journey |

The same pattern is carried out a second time in §21.1 on the root *tal-* "to speak"
(*talex, talru, tala, talna, talisto, talvi, taluma*).

---

## 3. The three noun groups

The grammar divides the nouns into one regular main group and two historically explained
residual groups. In detail: `docs/en/NOUNS.md`.

| Group | Extent according to the grammar | Distinguishing feature | Singular | Plural | Paragraph |
|---|---|---|---|---|---|
| **Regular nouns** | "about 90 % of all nouns" | class consonant + theme vowel visible at the end of the word | case marker directly on the theme vowel | **-ñ-** + echo vowel | §6, §7, §8, §9 |
| **Ten-percent group** | 3 words listed by name | final vowel historically lost, gender recognizable from the remaining consonant | linking vowel **-e-** + case marker | **not regulated — L-07** | §10.1 |
| **15 core words** | 15 words, exhaustively enumerated | true exceptions, gender only from the dictionary | linking vowel **-e-** + case marker | **-ei** + case marker | §10.2, §10.3, §24.1 |

Attestations per group:

- regular: *valru · valrun · valruş · valrus* (§8), plural *valruñ · valruñun · valruñuş · valruñus* (§9)
- ten-percent group: *velkran · velkranen · velkraneş · velkranes* (§10.1)
- core words: *kaun · kaunen · kauneş · kaunes*, plural *kaunei · kaunein · kauneiş · kauneis* (§10.3)

The percentages are statements of the grammar about the vocabulary as a whole (§6: "In
about 90 % of all nouns the gender is immediately recognizable from the ending"), not a
count of the words listed by name in 0.9.3.

---

## 4. The verb

> **Root + tense vowel + person ending** (§14)

The tense vowel is **-a-** (present), **-o-** (past) or **-ai-** (future, §15); the person
endings are **-m · -ş · -t** in the singular and **-men · -şen · -ten** in the plural
(§14). Attestation: *milkam · milkoş · milkait · milkaten* from the complete paradigm of
*milkex* "to see" (§15.1).

The verb has neither a class consonant nor a theme vowel — the nominal formula from §8
does not apply to the verb. Eight frequent verbs deviate in the stem (§15.2); details in
`docs/en/VERBS.md`.

---

## 5. The adjective

The adjective has two states (§12):

| State | Form | Attestation |
|---|---|---|
| attributive | stem + **r / l / n** + **a** + marker, agreeing with the noun | *xra vlaidra valru* (§12.1) |
| predicative | unchanged base form after *esex*, *vurnex*, *stanex* | *Lo loşn est.* (§12.2) |

The attributive building block **r / l / n + a** is the same as in the article (§11) — the
A series of the class consonants. Adjective and article therefore always show only the
gender, never the subclass of the noun: *xnañaş vlaidnañaş milneñeş* (§12.1). Details in
`docs/en/ADJECTIVES.md`.

---

## 6. What the sound rules do not count (§3.5)

The sound guidelines (§3.4) apply **exclusively to the lexical stem**. Grammatical
morphology may never make a word phonaesthetically "invalid" after the fact. Explicitly
not counted are (§3.5):

- case markers *-n, -ş, -s*
- plural marker *-ñ-* together with echo vowel, and *-ei*
- the 45 gender endings
- person endings *-m, -ş, -t, -men, -şen, -ten*
- tense markers *-a-, -o-, -ai-*
- regular adjective endings *-ra, -la, -na* …
- infinitive *-ex* and participle *-ut*
- productive derivational morphemes *-ru, -la, -na, -isto, -uma, -vi, şu-, xa-, re-, dra-, su-*

Attested example from the grammar: *milkaiten* is faultless; only the stem *milk-* is
examined.

---

## 7. The junction rule (§21.4)

One rule applies throughout the whole of morphology:

> **Where two identical consonants meet at a morpheme junction, they merge into one.**
> This applies equally to compounds, derivations and endings.

| Field of application | Attestation | Paragraph |
|---|---|---|
| compound | *luiv + vresto* → *luivresto* | §21.3, §21.4 |
| derivation | *mel + la* → *mela*, *tal + la* → *tala* | §21.1, §21.4 |
| adjective ending | *şaln + na* → *şalna*, *girn + na* → *girna*, *xarn + na* → *xarna* | §12.1 |
| comparison infix | *selv + vi* → *selvi*, *zilv + vira* → *zilvira* | §12.3 |

It does not apply to different consonants; these are retained, provided §5.2 and §5.3
permit them (attested: *şaln + la* → *şalnla*, test corpus 0.1, test 058 *şalnlaş*).

Two attested forms contradict this rule: the pronouns *killa, dolla, kella* (§13.4,
§18.2) with an unmerged *l+l* junction — **[REGELKONFLIKT]** (rule conflict) **K-02** —
and the numeral *telnxelmmern* "35" (§24.8) with an *m+m* junction —
**[REGELKONFLIKT] K-03**. Neither can be resolved here.

---

## 8. Open points of morphology

This documentation decides nothing. Where Grammar 0.9.3 is silent or contradicts itself,
the finding ID from `Orbis-Audit-0_1.md` §A is given.

| ID | Type | Concerns | Short |
|---|---|---|---|
| K-02 | conflict | §13.4, §18.2 ↔ §21.4 | *killa/dolla/kella* against the junction rule |
| K-03 | conflict | §24.8 ↔ §21.4 | *telnxelmmern* against the junction rule |
| K-04 | conflict | §25.1 ↔ §12.4 | example sentence uses *tolm* adverbially instead of *tolmun* |
| L-03 | gap | §18.2 | declension of *kem/kelt* |
| L-04 | gap | §13.4 | case forms of the reflexive *se* |
| L-06 | gap | §13.4 | declension of the demonstratives and indefinites |
| L-07 | gap | §10.1 | plural of the ten-percent group |
| L-08 | gap | §24.8 | syntax of the cardinal numbers |
| U-01 | ambiguity | §15.2 | the formula does not cover *es-/nuv-/vurn-* |
| U-02 | ambiguity | §12, §14 | can the participle be used attributively? |
| U-08 | ambiguity | §21.3 | declension of compounds with a core-word head (*taivbreun*) |
| U-09 | ambiguity | §9 | "echo vowel" is defined only by the tables |
| U-12 | ambiguity | §14 | imperative supporting -e checks §5.3, not §5.1 |

One further finding touches morphology only indirectly: **K-01** (§5.1 does not list the
syllable shapes VK/VKK/KKVKK, although *aul, eird, em, eş, est* and inflected forms such
as *trelmrañan* require them).

---

*Documentation of Grammar 0.9.3. In case of divergence, `Orbis-Grammatik-0.9.3.md` prevails.*
