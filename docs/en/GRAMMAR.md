# ORBIS — Grammar: Overview and Entry Point

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md).
Describes Orbis Grammar 0.9.3; the reference grammar itself is Orbis-Grammatik-0.9.3.md.*

---

## 1. The binding reference

The **binding reference of the Orbis language is `Orbis-Grammatik-0.9.3.md`**. This
documentation under `docs/en/` describes it; it does not replace it, does not extend it and
does not narrow it.

| | |
|---|---|
| **Reference** | `Orbis-Grammatik-0.9.3.md` — canonical, frozen, READ ONLY |
| **German documentation** | `docs/de/*.md` — derived description, German is the canonical documentation language |
| **This English version** | `docs/en/*.md` — derived from the German (`TRANSLATION_POLICY.md`) |
| **Machine-readable data** | `language/*.json` — a mapping of the same rules, not yet the source of truth |

Three principles follow from this and apply to every file in this directory:

- **Where this documentation diverges from the grammar, the grammar prevails.** The
  divergence is a finding and is reported, not silently aligned away.
- **Nothing is decided here.** Where the grammar is silent or contradicts itself, the
  finding ID from `Orbis-Audit-0_1.md` is given, together with the marker `[REGELLÜCKE]`,
  `[REGELKONFLIKT]` or `[REGELUNKLARHEIT]`. Gaps are named, not closed.
- **Obligation of attestation.** Every Orbis form in this documentation comes from the
  grammar (§24, §25), from the test corpus (`Orbis-Testkorpus-0_1.md`), or is explicitly
  marked as rule-derived. Ungrammatical forms carry **†**.

Script and spoken language are separate levels: Manus rules (§26) and grammar rules are not
mixed, and a script finding is not a grammar finding.

---

## 2. The 18 chapters of this documentation

### 2.1 Sound level

| Chapter | File | Content |
|---|---|---|
| Phonology | `PHONOLOGY.md` | The sound inventory: 19 consonants and 5 vowels (§2.1–2.2), the diphthongs (§2.3), the two sound groups (§3.2), and the question of which of these statements are binding (§3.3) and which are merely descriptive (§3.4, §3.5). |
| Pronunciation | `PRONUNCIATION.md` | What the grammar says about sound realization (§2.1–2.3), the separation of the three levels A/B/C (§4) and the stress rules (§23) — with the explicit caveat that 0.9.3 contains no binding IPA assignment. |
| Phonotactics | `PHONOTACTICS.md` | §5: the permitted syllable shapes (§5.1), the consonant clusters at the beginning (§5.2) and at the end of a syllable (§5.3), as well as word length and word ending (§5.4), together with the caveats K-01 and L-09. |

### 2.2 Morphology

| Chapter | File | Content |
|---|---|---|
| Morphology | `MORPHOLOGY.md` | The overview of everything that is inflected or derived: the agglutinative building principle (§8), the three noun groups, verb and adjective in outline, the sound rules (§3.5) and the junction rule (§21.4). |
| Noun | `NOUNS.md` | §6–§11: class consonant and theme vowel (§6), the 45 regular gender endings (§7), the four cases (§8), the plural (§9), the 15 core words and the ten-percent group (§10) as well as the article (§11). |
| Adjective | `ADJECTIVES.md` | §12: the two states attributive (§12.1) and predicative (§12.2), comparison (§12.3), adverb formation (§12.4), nominalization (§12.5) and the 20 base adjectives (§24.7). |
| Pronouns | `PRONOUNS.md` | §13, separated by degree of maturity: the fully declined personal pronouns with polite form and possessive (§13.1–§13.3) and the open stock of the remaining pronouns (§13.4) with L-02, L-04, L-06 and K-02. |
| Verb | `VERBS.md` | §14–§16: root + tense vowel + person ending (§14), the regular conjugation and the eight irregular verbs (§15), modal verbs (§16.1), the potential form *mai* (§16.2) and the passive (§16.3). |
| Word formation | `WORD_FORMATION.md` | §21: the three procedures suffix derivation (§21.1), prefix derivation (§21.2) and compounding (§21.3), above them the junction rule (§21.4) — and the statement that productivity creates no new lexeme. |

### 2.3 Sentence level

| Chapter | File | Content |
|---|---|---|
| Syntax | `SYNTAX.md` | The overview of §17–§20: the two verb positions, the verbal bracket, the order of sentence elements, the question types (§18.1, §18.2), negation (§18.3), the prepositional system (§19) and the conjunctions (§20). |
| Word order | `WORD_ORDER.md` | Every attestable sentence construction one by one — 22 sections from the basic order to information structure, each with attestation, pattern, valid and invalid permutations and rule ID. |

### 2.4 Vocabulary and meaning

| Chapter | File | Content |
|---|---|---|
| Lexicon | `LEXICON.md` | The structure of the machine-readable lexicon under `language/lexicon/` for the frozen vocabulary of §24: mandatory fields of an entry, status model, frequency levels and the vocabulary gap W-01. |
| Semantics | `SEMANTICS.md` | How meaning is modelled in the data model — concept (`ORB-CON-*`) and lexeme (`ORB-LEX-*`), relation types, the obligation to differentiate synonyms, the nine attested antonym pairs (§24.7) and homonymy. |
| Corpus | `CORPUS.md` | How Orbis sentences are maintained: the holdings, the stable IDs `ORB-SENT-*`, roles and mandatory fields of a sentence, the key figures of test corpus 0.1 and the handling of sentences that cannot be formed. |
| Proto-Orbis | `PROTO_ORBIS.md` | §22: the seven historical sound laws with their attestations, their classification as level C (§4.3) — language history, not pronunciation notes — and the status values for etymologies. |

### 2.5 Script and input

| Chapter | File | Content |
|---|---|---|
| Manus | `MANUS.md` | §26 in full: syllable formula (§26.1), the 20 core forms in 8 families (§26.2), second initial consonant (§26.3), vowel dots and diphthongs (§26.4), one and two final consonants (§26.5–26.6), coda and sentence closure (§26.7), keyboard input (§26.8), writing rules (§26.9) — with L-09, L-10, U-10. |
| Magna | `MAGNA.md` | §27: Orbis Magna as the solemn execution of the same core forms, not as a second script — kept as short as §27 itself, including what is expressly left open there. |
| Keyboard | `KEYBOARD.md` | The state of planning for input: what §26.8 prescribes, the architectural sketch of the processing chain and why L-09, L-10 and U-10 block its construction — a plan, not a specification. |

---

## 3. Brief overview of the language system

This overview is a signpost into the chapters, not a source of rules. Authoritative are the
paragraphs of the grammar named here.

### 3.1 Sound system

- **19 consonants and 5 vowels** (§2.1–2.2); in addition diphthongs (§2.3). The special
  characters *ş*, *ñ* and *ç* are consonants in their own right, not spelling variants.
- **Two sound groups** (§3.2); §3.3 distinguishes binding rules from the merely descriptive
  guidelines in §3.4 and §3.5.
- **Syllable shapes** V · KV · KVK · KKV · KKVK · KVKK (§5.1), onset clusters (§5.2), coda
  conditions (§5.3), word length and word ending (§5.4). A word that violates them is not
  valid Orbis (§3.3).
- **Stress** according to §23. A binding IPA assignment does not exist in 0.9.3.
- **Historical sound laws** (§22) belong to level C and are expressly not pronunciation
  notes (§4.3).

### 3.2 Noun

- Formula **class consonant + theme vowel** (§6); in about 90 % of nouns the gender is
  recognizable from the ending.
- Mnemonic of the grammar (§7.3): **r-k-d masculine · l-v-m feminine · n-s-t neuter.**
- Nine class consonants × five theme vowels = **45 regular gender endings** (§7).
- **Four cases** — nominative, accusative, dative, genitive (§8) — and a regular
  **plural** (§9).
- Irregular stock: the 15 core words and the ten-percent group (§10); **article**
  according to §11.
- The **adjective** agrees when attributive (stem + *r / l / n* + *a* + marker, §12.1) and
  is endingless when predicative (§12.2); the dictionary form is the base form (§24.7).
- **Personal pronouns** are declined through all four cases (§13.1), with a polite form
  (§13.2) and a possessive (§13.3).

### 3.3 Verbs

- Formula **root + tense vowel + person ending** (§14); no class consonant, no theme vowel.
- **Person endings** -m / -ş / -t in the singular, plural throughout + **-en** (§14, §28).
- **Tense vowels**: present **-a-**, past **-o-**, future **-ai-** (§15).
- **Eight irregular verbs** (§15.2).
- **Modality**: the conjugated modal verb in position 2, the full verb as an infinitive at
  the end of the sentence (§16.1); potential form with the particle *mai* immediately
  before the finite verb (§16.2); **passive** with the prefix *şu-*, stative passive with
  participle + *esex* (§16.3).

### 3.4 Sentence structure

- **Two verb positions**: the finite verb in position 2 in a declarative main clause
  (§17.1), at the end in a subordinate clause (§17.2).
- **Verbal bracket** (§17.3, §16.1); the order of elements in the middle field as an
  explicit tendency time – reason – manner – place (§17.4); **no omission of the copula**
  (§17.5).
- **Questions**: yes/no question with the verb in position 1 (§18.1), wh-questions with
  *kem*, *kelt*, *kur*, *kan*, *grais*, *kolm*, *kelra/kella/kelna* (§18.2).
- **Negation**: particle *xa* before the finite verb, attributive declined *xan-* (§18.3).
- **Prepositions** govern fixed cases, in part dative = location against accusative =
  direction (§19); **conjunctions** divide into coordinating ones with main-clause order
  and subordinating ones with verb-final order (§20).
- **Word formation**: suffix, prefix, compounding, above them the junction rule (§21). The
  vocabulary is frozen as of 0.9.3 (§24) — a productive pattern does not create a new
  lexeme.

### 3.5 Script

- **Orbis Manus** is the everyday script and a **syllabic script**: one writes syllable
  block by syllable block, not letter by letter (§26.1).
- **20 core forms in 8 families** (§26.2), second initial consonant (§26.3), vowel dots and
  composed diphthongs (§26.4).
- One and two final consonants have fixed places (§26.5–26.6); coda and sentence closure
  are two levels, with six closing marks (§26.7).
- **Input** follows the Hangul principle, in the order of speech (§26.8); writing rules and
  stroke weight in §26.9.
- **Orbis Magna** is not a second script but a stylistic layer over the same core forms,
  for quotations, inscriptions, symbols, art and titles (§27).
- The **morpheme level** for Manus and keyboard (visible case and tense marks) as well as
  the **word traces** (possibility, memory, heard/reported, personally experienced) are
  **EXPERIMENTAL and NOT CANONICAL**; they are not part of Orbis 0.9.3.

---

## 4. What is open

Audit 0.1 (`Orbis-Audit-0_1.md`) records **no P0** for 0.9.3. Six findings are classified as
**P1**; all of them are solvable additively, that is, without changing existing rules. Two
further findings block script and keyboard.

### 4.1 The six P1 findings

| ID | Type | Concerns | What is open |
|---|---|---|---|
| **L-01** | [REGELLÜCKE] | §8, §17 | The position of the genitive attribute is not laid down; all examples postpose it, but that is no rule for noun genitives — including the order when stacked with the possessive. |
| **L-02** | [REGELLÜCKE] | §13.4, §17 | The construction of relative clauses is missing entirely: case, agreement and verb position of *fai* are unregulated, and there is in addition the homonymy with *fai* "that" (§20). |
| **L-03** | [REGELLÜCKE] | §18.2 | The declension of *kem* and *kelt* is undefined; "whom?", "to whom?", "whose?" cannot be formed, and neither case forms nor indeclinability are laid down. |
| **L-04** | [REGELLÜCKE] | §13.4 | For the reflexive pronoun *se* the case forms are missing; it also remains unresolved whether it is indeclinable and for which persons it applies. |
| **L-05** | [REGELLÜCKE] | §16.3 | The agent in the passive is undefined: "the house is built by the man" cannot be formed, since §16.3 regulates only the prefix *şu-*. |
| **K-05** | [REGELKONFLIKT] | §16.1 ↔ §17.2 | Modal verb in a subordinate clause: infinitive (§16.1) and finite verb (§17.2) both claim the end of the sentence; no example in 0.9.3 contains this case. |

### 4.2 The two blocking findings

| ID | Type | Concerns | What is open |
|---|---|---|---|
| **L-09** | [REGELLÜCKE] | §5, §26 | There is no syllabification preference rule; 77 of 281 base forms have more than one rule-conforming Manus spelling. Blocks Manus and thereby the keyboard. |
| **L-10** | [REGELLÜCKE] | §26.9 | For *f s ş x v z j ç* no stroke weight is defined; the stroke-weight rule does not cover all 19 consonants. Blocks completion of the script specification. |

### 4.3 How these points are to be handled

**These points are decided by the language designers.** Neither this documentation nor the
tool chain closes them: no formation by analogy, no interpretation, no interim solution that
later reads like a rule. Until a documented decision with a decision ID (`ORB-ADR-*`)
exists, the cases remain visibly marked with their marker and their finding ID.

The syllabification simulation `--sim-l09` of the validator is an analysis tool for
quantifying L-09 and is **not a language rule**; it must never be cited as a rule.

The rule findings K-01 to K-05, L-01 to L-10 and U-01 to U-14 are listed in
`Orbis-Audit-0_1.md` (§A). The vocabulary and documentation findings W-01 to W-04 come from
phase 7 of the test report or were added during the migration; the complete register of all
33 findings is `language/findings/findings.json`. The overall verdict for a direct jump to
1.0 is **NOT READY**.

---

## 5. Cross-references

| File | Content |
|---|---|
| `Orbis-Grammatik-0.9.3.md` | the binding reference (READ ONLY) |
| `Orbis-Audit-0_1.md` | all findings K-xx, L-xx, U-xx, W-xx |
| `Orbis-Testkorpus-0_1.md` | test corpus 0.1, 150 test sentences |
| `ORBIS_CONSTITUTION.md` | the highest norm of the project, articles 1–20 |
| `TRANSLATION_POLICY.md` | language and translation policy, German as the semantic authority |
| `VERSIONING.md` | separate versioning of Grammar, Lexicon, Manus, Keyboard, Corpus, Tools |
| `docs/de/GRAMMATIK.md` | the authoritative German version of this chapter |
