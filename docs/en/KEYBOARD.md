# Orbis — Keyboard: state of planning

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md).
Describes Orbis Grammar 0.9.3; the reference grammar itself is Orbis-Grammatik-0.9.3.md.*

---

## 1. Subject and status

This chapter describes what the grammar prescribes in §26.8 for the input of Orbis Manus,
what the planned processing chain looks like and why it currently cannot be
built. It describes a **state of planning**, not a specification.

| Subject | State |
|---|---|
| Orbis Keyboard | **no released version** (0.x); not listed as compatible |
| Rule basis | exclusively §26.8; the keyboard has **no rule basis of its own** |
| Precondition | a numbered Manus version (`ROADMAP.md`, phase F blocks phase G) |
| Blockage | **[REGELLÜCKE L-09]** (syllable division), additionally **[REGELLÜCKE L-10]** and **[REGELUNKLARHEIT U-10]** |

The direction of derivation is fixed: a layout is derived **from** the Manus specification,
not the other way round. A layout wish changes no script rule. As long as L-09,
L-10 and U-10 are open, all layouts are drafts (`experimental`).

---

## 2. What §26.8 prescribes

### 2.1 The input principle

> Input as with Korean Hangul: type sounds **in the order spoken**, the system
> assembles the syllable block.

What is typed is therefore the sound chain, what is displayed is the finished syllable block according to §26.1. The
keyboard is thus not a sign mapping, but an **input method with a
composing step**.

### 2.2 The input order

> **Core consonant → second initial consonant → vowel → coda 1 → coda 2**

The order corresponds position for position to the syllable formula §26.1. Two further
stipulations of §26.8:

| Stipulation | Wording §26.8 |
|---|---|
| Block closure | "A new core consonant closes the previous block." |
| Punctuation | "The closing mark lies on a key of its own." |

The block closure is implicit: there is no confirmation key for a finished syllable.
The closing mark, by contrast, is expressly typed and is thus the only
language level above the syllable that §26.8 assigns to the keyboard.

### 2.3 The key-count calculation and [REGELUNKLARHEIT U-10] (rule ambiguity)

§26.8 calculates:

> **20 consonant keys + 4 vowel keys + 1 diphthong key + 6 closure keys = 31 key assignments.**

**Finding ID: U-10** (`Orbis-Audit-0_1.md` §21 and §A). Orbis has **19** consonants (§2.1);
the 20th core form is, according to §26.2, the **vowel carrier** and therefore not a consonant. Correct would be
"19 consonant keys + 1 vowel-carrier key"; the **total 31 remains correct**. The audit
classifies the point as a documentation error, not as a system error.

For layout planning the difference is nevertheless practical: the vowel-carrier key is
the key for vowel-initial syllables (*aul*, *eird*, *ain*, *oñ*) and behaves differently in
input logic from a consonant key — it opens a block without an
initial consonant. The correction of the wording will appear in a future
grammar version, not through a change to 0.9.3; this documentation only marks it.

**Not spelled out in §26.8:** how a single diphthong key produces the six diphthongs from
§26.4 (there every diphthong is a first-vowel mark plus a small second dot).
Likewise not spelled out: numerals, capital/emphasis forms and behaviour on
phonotactically inadmissible input. The audit assigns no finding IDs for this; nothing is
added here.

---

## 3. Architectural sketch of the processing chain

The planned chain has three stages (`ROADMAP.md`, phase G). Every stage reads exclusively
from `language/` or `script/`; there is no second rule version in the code.

```
Input (sound chain + grammatical features)
        │
        ▼
  MorphologyEngine      stem + case/number/tense/person  →  word form
        │                (language/morphology/, §8–§16)
        ▼
  Syllabifier           word form  →  syllable sequence
        │                (language/phonology/, §5 — BLOCKED by L-09)
        ▼
  ManusComposer         syllable sequence  →  Manus syllable blocks
        │                (script/manus/, §26.1–26.7)
        ▼
Output (Manus text, optionally with closing mark §26.7)
```

### 3.1 Example: *valru* + DATIVE → *valruş* → Manus

| Stage | Input | Output | Basis |
|---|---|---|---|
| **MorphologyEngine** | *valru* (man, class M-A, §24.2) + dative singular | **valruş** | §8: dative marker **-ş**; attested series *valru · valrun · valruş · valrus* (§8) |
| **Syllabifier** | *valruş* | syllable sequence — **not unambiguously determinable** | §5.1 lists admissible syllable shapes, but no division rule → **L-09** |
| **ManusComposer** | syllable sequence | syllable blocks according to §26.1 | §26.2–26.6 |

With the division *val·ruş* the composer would yield two blocks:

| Block | Core form | Subsidiary mark | Vowel | Coda |
|---|---|---|---|---|
| 1 | *v* (family ISH) | — | *a*, inherent (not written, §26.4) | *l*, lower right (§26.5) |
| 2 | *r* (family TAL) | — | *u*, dot below (§26.4) | *ş*, lower right (§26.5) |

In the written image the dative is therefore **not a sign of its own**, but the coda of the last
block. That is exactly the point at which the experimental morpheme level would come in
(§5) — grammar 0.9.3 does not know it.

The alternative division *valr·uş*, by contrast, would yield a first block with **two** codas
(*l* and *r*, staggered according to §26.6) and a second block with a **vowel carrier** instead of a
core consonant — a visibly different written image for the same word form.

> Recalculated with the repo's decomposition tool (analysis tool, **not a
> language rule**): *valruş* has one division against the literal §5.1 list (*val·ruş*),
> two against the list extended by VK/VKK/KKVKK (*val·ruş*, *valr·uş*). The
> base form *valru* is already listed as ambiguous in the writing test (*val·ru* /
> *valr·u*, `Orbis-Manus-Schreibtest-0_1.md`). Which division applies is open: it depends
> on **L-09** and additionally on **[REGELKONFLIKT K-01]**, because this decides the extended
> list of forms.

### 3.2 Further requirements on the chain

- **Round-trip test** as acceptance criterion: input → Manus → back-decomposition → original form,
  across the entire lexicon stock (`ROADMAP.md`, phase G).
- **Error behaviour** on phonotactically inadmissible inputs is to be laid down; §26.8 says
  nothing about it.
- **Platform question** is open; for an MVP first a desktop layout, mobile
  input method later.
- **No rule copy in the code**: every sign assignment and every language rule has exactly one
  machine-readable source.

---

## 4. The blockage through [REGELLÜCKE L-09] (rule gap)

**Finding ID: L-09** (`Orbis-Audit-0_1.md` §2.4 and §A, priority P2). Concerns §5 and §26.

### 4.1 Why the chain comes to a halt at the middle stage

§5 lays down which syllables are permitted — not how a sound chain is divided. For
pronunciation this is without consequence (§23 counts syllables from the end and yields the same result);
for the script it is not, because §26.1 writes syllable by syllable. **77 of 281 base forms
(27 %) have more than one rule-conforming Manus spelling**
(`Orbis-Manus-Schreibtest-0_1.md`; 203 unambiguous, 1 not divisible). With inflected
forms the proportion rises, because every V-K-V sequence is ambiguous.

The syllabifier thus has no rule from which it could choose. A program that
chooses anyway would make a language decision — which is expressly forbidden to tools.

### 4.2 Input order solved, back-transfer not

The decisive point for the keyboard (`Orbis-Manus-Schreibtest-0_1.md`, section 3):

- **Solved by §26.8:** the **input order**. Whoever types in the order spoken
  determines the block boundaries themselves; "a new core consonant closes the previous block".
- **Not solved:** the **back-transfer** from the Latin spelling. The same
  letter chain remains ambiguous — *mela* is `[m;e;l] + [carrier;a]` **or**
  `[m;e] + [l;a]`.

This affects exactly the functions a usable input method needs: conversion
of existing texts, autocompletion from the lexicon, round-trip test and every output
that was not typed sign by sign by hand. The core problem remains: after a vowel
the next consonant can be coda of the current syllable, core consonant of the next syllable or
second initial consonant.

### 4.3 What is additionally open

| Point | Effect on the keyboard |
|---|---|
| **L-09** syllable division | syllabifier without a rule; no unambiguous output, no round-trip test |
| **L-10** stroke weight *f s ş x v z j ç* | 8 of 19 consonants without sign parameters — concerns the display, not the key assignment |
| **U-10** "20 consonant keys" | terminology of the key assignment; total 31 untouched |
| **K-01** VK/VKK/KKVKK missing in §5.1 | co-decides which divisions are admissible at all |
| **Glyph set** | sign IDs, form variants and reference forms are not yet available (`ROADMAP.md`, phase F) |

**No preference rule is laid down here and none of the open questions is decided.**
The repo contains a simulation (`python3 orbis_validator.py --sim-l09`) that
calculates candidate strategies; the test report additionally names the possibility of declaring
free variation and leaving the script ambiguous. **Syllable-division simulations
are analysis tools, not language rules, and are never cited as a rule.** The selection
is made exclusively by the language designers.

---

## 5. EXPERIMENTAL — NOT CANONICAL

> **This section describes ideas that are not part of grammar 0.9.3.**
> They are **EXPERIMENTAL and NOT CANONICAL**, may nowhere be presented as existing
> Orbis grammar, existing lexicon or existing script, and
> are not taken over into language data, corpus sentences or test runs. They become canonical
> solely through a decision of the language designers.

### 5.1 EXPERIMENTAL — visible morpheme signs

**Idea:** a keyboard could set grammatical features not only as sounds, but
make them **visible** in the written image — for instance case, number and tense marks as separate
marks on the syllable block.

**State in grammar 0.9.3:** in §26 there is **no sign and no position** for this.
The dative of *valru* is in Manus the coda *ş* of the last block (§3.1) and is not distinguished from any
other *ş* coda. The syllable formula §26.1 knows exactly five positions;
a morpheme position is not one of them.

**Conditions, should this level ever become visible** (`ROADMAP.md`, phases F and G):

- exclusively as a **switchable, clearly marked EXPERIMENTAL mode**,
- never as a default setting and never in canonical outputs,
- no presentation as existing Orbis grammar — at every occurrence with a status statement,
- whether it becomes visible at all is decided by the language designers.

### 5.2 EXPERIMENTAL — word traces

**Idea:** an evidential level indicating where a statement comes from, with four values:

| Word trace | Intended meaning |
|---|---|
| **possibility** | the statement is possible, not secured |
| **memory** | the statement comes from memory |
| **heard / reported** | the statement comes from third parties |
| **experienced oneself** | the statement rests on one's own experience |

**State in grammar 0.9.3:** word traces do not occur — neither as morpheme, nor as
particle, nor as written sign. There is no Orbis example for them, neither in the
grammar nor in the test corpus.

**Not to be confused with the canonical stock.** For "possibility" Orbis already has
two attested means, and both are grammar, not word trace:

| Canonical means | Level | Attestation |
|---|---|---|
| Particle **mai** before the finite verb (§16.2) | morphology/syntax | *Vim mai melam.* — I would go (§16.2) |
| Closing mark **fading** (§26.7) | script/pragmatics | "possibility, uncertainty (corresponds to *mai*)" (§26.7) |

For "memory", "heard/reported" and "experienced oneself" the grammar knows **no**
grammatical category. The noun *soruma* (memory, §24.6, attested in §25.1: *Xla
soruma xlas nauşes vran tolm vaşnat.*) is a lexeme, not an evidential marking. Introducing an
evidential category would be a language decision and is not made here.

Storage in the repo: `script/traces/` — expressly listed as **EXPERIMENTAL, NOT CANONICAL**
and separate from `language/`.

### 5.3 Why the levels are modelled separately in technical terms

The four levels are modelled separately so that an experiment does not migrate by quotation into the
canonical stock and so that a finding on one level does not trigger a step on
another:

| Level | Responsible for | Place in the repo | Status |
|---|---|---|---|
| **Phonology** | sounds → Manus syllables (syllable construction, division) | `language/phonology/` → `script/manus/` | canonical (§5, §26); division open: L-09 |
| **Morphology** | case, number, tense (word-form building) | `language/morphology/` | canonical (§8–§16) |
| **Evidentiality** | word traces (possibility, memory, heard/reported, experienced oneself) | `script/traces/` | **EXPERIMENTAL, NOT CANONICAL** |
| **Pragmatics** | sentence closures (statement, continuation, contrast, question, possibility, end) | `script/manus/` | canonical (§26.7) |

Practical consequence for the processing chain: the MorphologyEngine produces *valruş* from
*valru* + dative without knowing anything about written signs; the ManusComposer sets
syllable blocks without knowing anything about case; the closing mark is set as a level of its own
and never treated as a third coda (§26.7); an evidential level exists in no
canonical stage. Script rules (§26, `script/`) and grammar rules (`language/`)
remain separately versioned.

---

## 6. Summary of rule status

| Point | Paragraph | Status |
|---|---|---|
| Input in the order spoken, block closure by a new core consonant | §26.8 | prescribed, unambiguous |
| Closing mark on a key of its own | §26.8 / §26.7 | prescribed, unambiguous |
| Key-count calculation, total 31 | §26.8 | total correct; **[REGELUNKLARHEIT U-10]** in the naming |
| Production of the 6 diphthongs via 1 key | §26.8 / §26.4 | not spelled out; no finding ID |
| Error behaviour, numerals, platform | — | not regulated in §26; work packages phase G |
| Syllable division for the syllabifier | — | **[REGELLÜCKE L-09]** — blocking |
| Stroke weight *f s ş x v z j ç* | §26.9 | **[REGELLÜCKE L-10]** |
| Syllable shapes VK/VKK/KKVKK | §5.1 | **[REGELKONFLIKT K-01]** |
| Morpheme signs, word traces | — | **EXPERIMENTAL, NOT CANONICAL** |

---

## 7. Cross-references

| Topic | Place |
|---|---|
| §26 in full: core forms, vowel dots, coda, closing marks | `MANUS.md` |
| Solemn script form and its open spiral rules | `MAGNA.md` (§27) |
| Syllable shapes, initial clusters, coda conditions, K-01 and L-09 | `PHONOTACTICS.md` (section 5 of that file) |
| Case markers and paradigms (*valru · valrun · valruş · valrus*) | `NOUNS.md` (§8–§10) |
| Decomposition table of all 281 base forms | `Orbis-Manus-Schreibtest-0_1.md` |
| Finding IDs L-09, L-10, U-10, K-01 | `Orbis-Audit-0_1.md`, `language/findings/findings.json` |
| Work packages and acceptance criteria | `ROADMAP.md` (phases F and G) |
| Marking obligation for experimental material | `ORBIS_CONSTITUTION.md` (Art. 20) |

---

*Source of all rule statements: `Orbis-Grammatik-0.9.3.md` (READ ONLY). In case of divergence
between this documentation and the grammar, the grammar applies.*
