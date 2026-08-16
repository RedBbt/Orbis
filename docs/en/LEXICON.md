# ORBIS — Structure of the Lexicon

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md).
Describes Orbis Grammar 0.9.3; the reference grammar itself is Orbis-Grammatik-0.9.3.md.*

---

## 1. What the lexicon is

The vocabulary of Orbis stands in §24 of the grammar — as lists, thematically ordered, with
a short German gloss. As of version 0.9.3 it is **frozen** (§24): a word is changed only if
it violates the phonotactics, is grammatically inconsistent, collides problematically with
another word or carries a contradictory meaning. Matters of taste are no longer sufficient.

The lexicon under `language/lexicon/` is the **machine-readable version of exactly this
stock**. It adds no words and changes no meaning; it makes the statements of the grammar
checkable, referenceable and generatable. Where it diverges from the grammar, the grammar
prevails — the divergence is a finding.

| File | Content |
|---|---|
| `language/lexicon/index.json` | overall register, 281 entries with a file pointer |
| `language/lexicon/entries/<lemma>.json` | one entry per base form |
| `language/lexicon/lexicon.schema.json` | schema of an entry |
| `language/lexicon/concepts/concepts.json` | 131 concepts of meaning (`ORB-CON-*`) |
| `language/lexicon/concept.schema.json` | schema of a concept |
| `language/lexicon/word_families.json` | the two word families attested in §21.1 |

On the modelling of meaning (concept ↔ lexeme, relations, synonym differentiation) see
`SEMANTICS.md`.

---

## 2. Overview of the stock

**281 base forms · 131 concepts · Lexicon 0.1 against Grammar 0.9.3.**

The 281 are base forms in the sense of the lexicon: dictionary forms of the open classes
and in addition the completely enumerated forms of the closed classes (articles, personal
pronouns). Inflected forms of open words — *valrun, milkaten, vlaidnañaş* — are not
entries; they are generated from the paradigms (`docs/generated/de/PARADIGMEN.md`).

### 2.1 By word class

| Word class | Entries | Origin in the grammar |
|---|---|---|
| **nomen** | 71 | 15 core words (§24.1) + 3 of the ten-percent group (§10.1) + 13 M (§24.2) + 15 F (§24.3) + 13 N (§24.4) + 9 abstract nouns in -uma (§24.6) + 3 compounds (§21.3) |
| **pronomen** | 58 | 36 personal pronoun forms (§13.1) + 6 demonstratives + *se* + *fai* + 5 indefinites (§13.4) + 6 interrogatives + *kelra/kella/kelna* (§18.2) |
| **artikel** | 36 | definite 3 genders × 4 cases × 2 numbers + indefinite 3 × 4 (no plural, §11.2) |
| **verb** | 34 | 28 verb roots (§24.5, 8 of them irregular) + 6 modal roots (§16.1) |
| **adjektiv** | 20 | §24.7 |
| **partikel** | 20 | 16 adverbs/particles (§24.9) + 4 greeting formulas (§13.2) |
| **präposition** | 16 | §19 |
| **zahl** | 15 | 10 cardinal numbers + *munar*, *kraven* + 3 compounds (§24.8) |
| **konjunktion** | 11 | 4 coordinating + 7 subordinating (§20) |
| **Total** | **281** | |

The conjunctions *ze, vu, klas, xer* stand in §24.9 together with the particles, but in the
lexicon they are carried according to their function in §20 as conjunctions. That is a
classification of the data level, not a change of meaning.

### 2.2 By concept binding

131 of the 281 entries refer to a concept `ORB-CON-*`: all nouns, verbs and adjectives as
well as the six interrogative pronouns. The remaining 150 are function words and
inflectional forms of closed classes with purely grammatical meaning. Details in
`SEMANTICS.md` §2.2.

### 2.3 File names

The file name is an ASCII transcription of the lemma: *ş* → `sh`, *ñ* → `nn`, *ç* → `ch` (*veiş* → `veish.json`,
*şirn* → `shirn.json`, *nauş* → `naush.json`, *şaul* → `shaul.json`). Homonyms receive an
appended digit: `fai.json` (conjunction "that") and `fai__2.json` (relative pronoun),
likewise `kaun`/`kaun__2` and `vran`/`vran__2` — see finding **W-03**. The lemma itself
stands unchanged in Orbis standard spelling in the field `lemma`.

---

## 3. Mandatory fields of an entry

The schema knows two stages: fields without which an entry is not valid, and fields that an
entry additionally needs in order to be **canonical**.

### 3.1 Mandatory for every entry (`required`)

| Field | Content |
|---|---|
| `lexeme_id` | stable ID `ORB-LEX-000000`. "Never changes, not even when the lemma is renamed." |
| `lemma` | base form in Orbis standard spelling |
| `status` | one of the eight status values (section 4) |
| `wortart` | one of 13 word classes (nomen … wurzel) |
| `de` | `short` (short gloss) and `definition` — **canonical and authoritative** |
| `phonologie` | at least `phonemfolge` |
| `qualitaet` | `geprueft` and `validatorstatus` |

### 3.2 Additionally for `status: canonical` (`required_for_canonical`)

`de.short` · `de.definition` · **`en.short`** · **`en.definition`** · `wortart` ·
`phonologie.phonemfolge` · `qualitaet.validatorstatus`

Only a canonical entry may be used without a warning in official examples (schema, field
`status`).

**State 0.1:** all 281 entries carry `status: canonical`, `de.short`, `de.definition` and
`en.short`. **`en.definition` is filled in no entry** — the German definition is so far the
migrated dictionary gloss in sentence form, the English version is limited to the short
gloss. This gap is registered as **W-04** (documentation gap, P2, open) and is expressly
editorial work for the language designers: tools may not formulate definitions themselves
(ORBIS_CONSTITUTION Art. 6 and Art. 16).

### 3.3 The further field groups

| Group | Purpose | State 0.1 |
|---|---|---|
| `grammatik` | gender, class, theme vowel, generated `kasusformen`, conjugation class, government, transitivity | generated from the rule data |
| `phonologie` | `phonemfolge`, `silbifizierung` or `silbifizierung_kandidaten`, `phonotaktik_status` | in 77 entries the syllabification is ambiguous → `null` plus a list of candidates (**L-09**) |
| `manus` | script analysis, `ambiguitaet`, `befund` | `blocked` where L-09 takes hold; otherwise `provisional` |
| `semantik` | `concept_ids`, `synonyme`, `relationen`, `konnotation`, `bedeutungsnuancen` | only 18 `antonym` relations attested (§24.7) |
| `wortfamilie` | root, `family_id`, derivations, compounds | filled for the two families from §21.1 |
| `etymologie` | `status`, `proto_form`, `lautgesetze` | `unknown` where §22 yields nothing — nothing is reconstructed |
| `gebrauch` | collocations, typical constructions | empty (W-04) |
| `beispiele` | references to `ORB-SENT-*` | the generated pages resolve them from the test corpus |
| `qualitaet` | `validatorstatus`, `offene_befunde`, `quelle` | completely filled; `quelle` names the paragraph |

The field `qualitaet.offene_befunde` is the anchor between lexicon and findings register.
Distribution in the stock: **W-04** on all 281 entries, **L-09** on 77, **L-08** on 15,
**K-01** on 14, **L-06** on 11, **U-01** on 8, **K-05** and **U-03** on 6 each, **W-03** on
4, **L-07**, **U-07** and **K-02** on 3 each, **L-03** on 2, and **K-03**, **L-02**,
**L-04** and **U-08** on one each.

---

## 4. Status model

Eight values, graded from draft to rejection:

| Status | Meaning |
|---|---|
| **draft** | draft, not yet submitted |
| **proposed** | submitted to the language designers for decision |
| **review** | under examination |
| **canonical** | decided stock — **only this status may be used without a warning in official examples** |
| **deprecated** | superseded, but still documented |
| **historical** | historical form (Proto-Orbis, older layer), not present-day language |
| **experimental** | expressly marked as an experiment (ORBIS_CONSTITUTION Art. 20) |
| **rejected** | examined and discarded; the entry is retained as a memory of the decision |

**State 0.1:** all 281 entries `canonical`. That is consistent — they all come from the
frozen vocabulary of Grammar 0.9.3. New words would begin at `draft` and take the path via
`proposed` and a documented decision (Art. 4, Art. 5).

The 131 concepts, by contrast, carry `status: draft` throughout — the words are decided,
their formulated definitions of meaning are not yet (W-04).

---

## 5. Frequency levels

The field `haeufigkeit` carries nine values:

| Level | Reading |
|---|---|
| **CORE** | core stock, to be expected in every text |
| **VERY_COMMON** | very frequent |
| **COMMON** | frequent |
| **STANDARD** | normal everyday vocabulary |
| **SPECIALIZED** | technical, tied to a field |
| **RARE** | rare |
| **ARCHAIC** | archaic |
| **POETIC** | poetic |
| **UNRATED** | not yet classified |

> **These levels are expressly target values of the language designers, not corpus
> statistics.** The schema puts it unmistakably: "Orbis-interne Zielhäufigkeit
> (designer_frequency), KEINE gemessene Korpusstatistik." Orbis has no usage corpus from
> which frequencies could be measured; test corpus 0.1 is a **testing** collection of 150
> sentences and measures rule coverage, not word usage.

**State 0.1** — the classification so far follows the word class, not an individual
assessment:

| Level | Entries | Composition |
|---|---|---|
| **CORE** | 95 | 36 article forms · 36 personal pronoun forms · 15 core words (§24.1) · 8 irregular verbs (§15.2) |
| **VERY_COMMON** | 39 | 16 prepositions · 11 conjunctions · 6 modal verbs · 6 interrogatives |
| **COMMON** | 32 | 20 particles and greeting formulas · 12 cardinal numbers |
| **STANDARD** | 3 | the ten-percent group *velkran, soralm, prilm* |
| **UNRATED** | 112 | 53 regular nouns · 20 regular verbs · 20 adjectives · 16 pronouns from §13.4/§18.2 · 3 numeral compounds |

The levels **SPECIALIZED**, **RARE**, **ARCHAIC** and **POETIC** are attested by no entry
in stock 0.1. The fields `register` (all `neutral`) and `lernstufe` (all `unbestimmt`) are
likewise waiting for a designer decision.

---

## 6. Vocabulary gaps — [W-01]

> **W-01 (P2, open): vocabulary gaps for basic communication.**
> Common basic verbs and one construction are missing:

| Missing | Situation |
|---|---|
| **to say** | §24.5 defines *tal-* as "to speak". Test corpus 104 ("She says that she is coming") is therefore rated as [TESTPROBLEM]: *Lo talat, fai lo vandat* would shift the meaning without a dictionary basis. |
| **to show** | no root in the stock |
| **to search** | no root in the stock; *traiv-* is "to find", not "to search" |
| **there is** | no existential construction; *es-* is the copula (§15.2, §17.5) |

W-01 is **not a rule violation** but a gap in the stock: the grammar works, the vocabulary
is not sufficient for certain everyday sentences. Test report 0.1 names two directions of
solution — targeted new words via the §22 workshop, or a documented extension of meaning of
existing roots — and decides neither of them. Until a decision by the language designers the
gap is **named, not filled** (CLAUDE.md §2, ORBIS_CONSTITUTION Art. 16).

Alongside stand the two collision findings of the vocabulary: **W-02** (*velkran* =
nominative "friendship" and accusative of *velkra*) and **W-03** (homonyms *fai*, *kaun*,
*vran*, *xa*). Both are set out in `SEMANTICS.md` §6.

---

## 7. Generated detail pages

From the data, `tools/documentation/build.py` generates one detail page per entry:

**`docs/generated/de/lexicon/`** — 281 lemma pages plus `INDEX.md` as an overall register.
The English counterpart lies under `docs/generated/en/lexicon/`.

Every page shows, in a fixed arrangement:

| Section | Content |
|---|---|
| Head | lemma, short gloss, German definition |
| Master data | ID, word class, gender, class, status, frequency, domain, source (§ reference) |
| English | derived version with translation status |
| Declension / conjugation | the generated full forms |
| Sound and script | phoneme sequence, syllabification (or candidates in the case of L-09), phonotactics status, Manus status |
| Meaning | linked concepts, relations |
| Word family, etymology | root; where attestation is lacking, expressly "keine Herleitung dokumentiert" |
| Example sentences | from the test corpus, resolved via the lexeme link |
| Test bench | validator status, open findings in plain text, date of the last check |

These pages carry the head `AUTO-GENERATED — DO NOT EDIT DIRECTLY`. Corrections belong in
the data under `language/`, not in the generated file. Likewise generated:
`docs/generated/de/PARADIGMEN.md` (full-form tables) and `docs/generated/de/BEFUNDE.md`
(findings register with all 33 IDs).

---

## 8. Checking

Before every change to language data or the validator:

```
python3 orbis_validator.py --strict
python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md
```

`--strict` compares against `orbis_baseline.json`; exit code 1 means **new** findings.
Further runs: `--lexicon` (vocabulary against phonotactics and the ending system),
`--tables` (generated paradigms), `--manus` (syllabification ambiguity, L-09),
`--examples` (grammar examples). `--update-baseline` only on express instruction.

---

## 9. Overview of findings for this chapter

| ID | Type | Concerns | Short |
|---|---|---|---|
| **W-01** | WORTSCHATZLÜCKE | §24 | "to say", "to show", "to search", "there is" are missing |
| **W-02** | WORTSCHATZKOLLISION | §10.1, §24.2 | form collision *velkran* |
| **W-03** | WORTSCHATZKOLLISION | §11, §13.4, §18.3, §20, §21.2, §24 | further homonyms |
| **W-04** | DOKUMENTATIONSLÜCKE | §24 | 281 entries without a formulated definition |
| **L-09** | REGELLÜCKE | §5, §26 | 77 entries with ambiguous syllabification |

Complete register: `language/findings/findings.json` and `docs/generated/de/BEFUNDE.md`
(33 findings: 29 from the audit, plus W-01 to W-04).
