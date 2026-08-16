# ORBIS — Semantics: how meaning is modelled

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md).
Describes Orbis Grammar 0.9.3; the reference grammar itself is Orbis-Grammatik-0.9.3.md.*

---

## 1. What this chapter is for

Grammar 0.9.3 has **no semantics chapter**. It supplies meaning in the form of dictionary
glosses (§24), antonym pairs in the adjective stock (§24.7) and distinctions of meaning at
individual points (§24.6 on *salv-* and *vaşn-*). A model that orders these statements
belongs to the **data level** of the project, not to the language itself.

What is described here is therefore the structure of the language data under
`language/lexicon/`, as laid down in `lexicon.schema.json` and `concept.schema.json`. For
the **content** of every individual meaning, Grammar 0.9.3 alone remains authoritative; the
data model maps it and does not supplement it.

Two principles frame everything that follows:

- **German is the semantic authority** (TRANSLATION_POLICY §1, ORBIS_CONSTITUTION Art. 1).
  English fields are derived and may neither widen nor narrow nor sharpen the scope of
  meaning.
- **No silent changes of meaning** (Art. 6). A sharpening too is a change and requires a
  documented decision.

---

## 2. Two levels: concept and lexeme

The model separates **what** is meant from the **word** that expresses it.

| Level | ID pattern | File | Stock |
|---|---|---|---|
| **Concept** — language-independent unit of meaning | `ORB-CON-000000` | `language/lexicon/concepts/concepts.json` | 131 |
| **Lexeme** — word of the Orbis language | `ORB-LEX-000000` | `language/lexicon/entries/<lemma>.json` | 281 |

The link runs in both directions: the lexeme names under `semantik.concept_ids` the
concepts it realizes; the concept carries the back-references under `lexeme` (redundant
according to `concept.schema.json`, derivable from the entries).

The point of the separation: several lexemes can carry the same or an overlapping concept —
this is exactly where synonym differentiation starts (section 4). Conversely a lexeme can
carry several concepts if it is ambiguous. IDs never change, not even when the lemma is
renamed (`lexicon.schema.json`, field `lexeme_id`; ORBIS_CONSTITUTION Art. 7).

### 2.1 Fields of a concept

| Field | Content |
|---|---|
| `concept_id` | stable ID `ORB-CON-*` |
| `de.label` | short designation, e.g. "Erinnerung" |
| `de.hauptdefinition` | canonical definition (mandatory field) |
| `de.abgrenzung` | what the concept is delimited against |
| `en.label`, `en.definition`, `en.status` | derived English version |
| `domaene` | semantic domain, e.g. `natur`, `zeit`, `familie` (mandatory field) |
| `oberbegriffe`, `unterbegriffe`, `verwandte`, `gegensaetze` | references to other `ORB-CON-*` |
| `lexeme` | realizing `ORB-LEX-*` |
| `status` | `draft` / `canonical` / `experimental` / `deprecated` |
| `quelle` | source reference, here throughout "Orbis-Grammatik-0.9.3.md §24" |

### 2.2 Which lexemes carry a concept

Not every lexeme is a bearer of meaning in the sense of the concept model. Of the 281
entries, 131 refer to a concept:

| Word class | with concept | without concept |
|---|---|---|
| nomen | 71 | — |
| verb | 34 | — |
| adjektiv | 20 | — |
| pronomen | 6 (*kem, kelt, kur, kan, grais, kolm*) | 52 |
| artikel | — | 36 |
| partikel | — | 20 |
| präposition | — | 16 |
| zahl | — | 15 |
| konjunktion | — | 11 |
| **Total** | **131** | **150** |

The 150 concept-less entries are function words and inflectional forms of closed classes
(for instance the 36 article forms *xra … vnaş* from §11 or the 36 personal pronoun forms
from §13.1). Their meaning is grammatical, not lexical. The six interrogative pronouns
carry a concept because they have a content of meaning that can be asked for ("who",
"what", "where/whither", "when", "why", "how", §18.2).

### 2.3 Domains

Every concept lies in exactly one domain. The stock is distributed across 26 domains:

| Domain | Concepts | Domain | Concepts |
|---|---|---|---|
| grammatik | 13 | mensch | 5 |
| natur | 11 | wetter | 5 |
| kommunikation | 10 | familie | 3 |
| abstrakta | 10 | beziehungen | 3 |
| zeit | 9 | tiere | 3 |
| raum | 8 | gesellschaft | 3 |
| bewegung | 8 | essen | 3 |
| existenz | 6 | bewertung | 3 |
| wahrnehmung | 6 | kultur | 2 |
| koerper | 6 | arbeit | 2 |
| denken | 6 | gefuehle | 2 |
| | | wohnen · pflanzen · transport · werkzeug | 1 each |

The domains are an ordering aid of the data level, not a category of Grammar 0.9.3.

### 2.4 State of the stock

All 131 concepts carry `status: draft`. Their `hauptdefinition` is the migrated dictionary
gloss of the grammar in sentence form; `abgrenzung`, `oberbegriffe`, `unterbegriffe`,
`verwandte` and `gegensaetze` are empty throughout, as is every English `definition`. The
concept register expressly records: "One concept per documented gloss. Finer semantic
differentiation is designer work."

At the lexeme level this corresponds to finding **W-04** (documentation gap), which is
noted on all 281 entries: they carry a gloss and structural data, but no formulated
definition, no nuances of meaning, no collocations. This is open editorial work for the
language designers — tools may not invent definitions themselves (ORBIS_CONSTITUTION
Art. 6, Art. 16).

---

## 3. Relation types

Relations of meaning stand at two places in the lexeme schema. This is no accident but a
consequence of Article 12 of the constitution: synonymy demands more fields than any other
relation and therefore gets a block of its own.

### 3.1 semantik.synonyme — synonymy with a mandatory statement

| Field | Values / content |
|---|---|
| `lexeme_id` | target word `ORB-LEX-*` (mandatory) |
| `staerke` | **`synonym`** · **`near_synonym`** · `lose_verwandt` (mandatory) |
| `austauschbar` | `ja` · `nein` · `teilweise` |
| `bedeutungsunterschied_de` | in what the two words differ |
| `registerunterschied` | difference of style/register |
| `konnotationsunterschied` | difference of evaluation |
| `typische_kontexte` | contexts in which the one word stands and the other does not |

On this the schema says expressly: "Synonym relation WITH a difference of meaning. A mere
list is not enough."

### 3.2 semantik.relationen — all remaining relations

An entry consists of `typ` (mandatory), `ziel` (`ORB-LEX-*` or `ORB-CON-*`, mandatory) and
`anmerkung_de`.

| Type | Meaning | Example direction |
|---|---|---|
| **antonym** | opposite | *vlaid* (big) ↔ *nirm* (small) |
| **hypernym** | superordinate term of the entry word | a word → its superordinate category |
| **hyponym** | subordinate term | a word → a more specific word |
| **part_of** | part-whole relation | part → whole |
| **related** | thematically related, without closer specification | — |
| **derived_from** | morphologically derived from | *meluma* → *mel-* (§21.1) |
| **historical_relation** | related through sound history | *taiv* → \*tal-iv (§22) |
| **metaphorical_extension** | transferred meaning | — |

The last two types map what the grammar itself documents in the way of development of
meaning: §21.1 names *taiv* and *melva* as members of the families *tal-* and *mel-*, §22
supplies the sound laws for this.

**On the state:** in stock 0.1 only `antonym` relations are attested — 18 of them, that is
the nine pairs from §24.7 in both directions. `synonyme` is empty in all 281 entries, as
are `konnotation` and `bedeutungsnuancen`. There is no documented synonym pair in 0.9.3
that would have to be distinguished; the fields are prepared, not left unused.

---

## 4. The duty of synonym differentiation

> **ORBIS_CONSTITUTION Art. 12 — Synonyms must be semantically distinguished.**
> "Two canonical lexemes may not carry the same meaning. Every synonym pair receives an
> express distinction in the lexicon (nuance of meaning, register, collocation or field of
> use). […] If no difference can be stated, one of the forms is not a lexeme of its own."

The reason is one of testability: undistinguished synonyms make translations undecidable.
Neither human nor tool can give grounds for which form is correct, and a test corpus
becomes ambiguously assessable. The distinction may be narrow, but it must be named and
checkable.

**The model stands in the grammar itself.** §24.6 distinguishes two roots that easily
coincide in German:

| Root | Meaning | Valency | Attestation §24.6 |
|---|---|---|---|
| **salv-** | to lose | **transitive** — somebody loses something | *Vim salvam xnan vreston.* — I lose the book. |
| **vaşn-** | to pass away, to fade | **intransitive** — something passes of itself | *Xla soruma vaşnat.* — The memory fades. |

§24.6 concludes expressly: "They are not interchangeable." Exactly this kind of statement
is what Art. 12 demands for every future synonym pair — stored in the data model as
`austauschbar: nein` plus `bedeutungsunterschied_de`.

---

## 5. Antonymy: the nine attested pairs (§24.7)

§24.7 lists 20 adjectives as base forms. Eighteen of them stand in pairs; the pairing
follows from the order and the glosses of the list:

| No. | Word | Meaning | Counterpart | Meaning |
|---|---|---|---|---|
| 1 | **vlaid** | big | **nirm** | small |
| 2 | **selv** | good | **morn** | bad |
| 3 | **granz** | old | **zirv** | new |
| 4 | **trelm** | long | **misn** | short |
| 5 | **velm** | warm | **girn** | cold |
| 6 | **luid** | bright | **şaln** | dark |
| 7 | **xarn** | strong | **vresn** | weak |
| 8 | **zilv** | fast | **tolm** | slow |
| 9 | **klaun** | true | **norv** | false |

The two remaining adjectives of the list are left without a partner: **loşn** (beautiful)
and **xan** (no). *xan* is a special case in any event — according to §18.3 it serves as
attributive negation (*xanra valru*, "no man") and not as a descriptive adjective.

In the lexicon these nine pairs are stored as two `antonym` relations each, with the note
"Gegensatzpaar aus dem Adjektivbestand §24.7". They are the only part of the relation
network that could be derived from the grammar at all — from the order and glosses of the
list in §24.7. The grammar nowhere states anything about antonymy; the pairing is a
**derivation**, not an attestation.

**Attestations in sentences** (test corpus / §25):

| Pair | Attestation | Translation |
|---|---|---|
| granz ↔ zirv | *Xna breun granz stanat, klas xla kavla zirv vurt.* (§25.1) | The house stays old, but the city becomes new. |
| *luid* and *girn* — **not a pair** | *Xla luiv luid vot, xla kirva girn vot.* (§25.2) | The sun was bright, the night was cold. The sentence attests both adjectives in use, not their oppositeness: the pairs are luid ↔ şaln and velm ↔ girn. |
| *tolm* (one side only) | *Xla soruma xlas nauşes vran tolm vaşnat.* (§25.1) | The memory of time fades very slowly. Only *tolm* is attested; its partner *zilv* does not occur in any attestation. |

The last sentence is at the same time the subject of **K-04**: it uses *tolm* adverbially
without the *-un* required by §12.4. That concerns adjective morphology, not antonymy (see
`ADJECTIVES.md`).

---

## 6. Homonymy: when one form carries two meanings

In the model homonymy is not a relation type but a **finding**: two lexemes with separate
IDs but the same phonetic form. The data model keeps them cleanly apart (two entries, two
`lexeme_id`); the question whether the collision is acceptable is decided by the language
designers.

### 6.1 [WORTSCHATZKOLLISION W-02] (vocabulary collision) — velkran

> **W-02 (P2, open): form collision *velkran*.**
> *velkran* "friendship" (nominative, ten-percent group §10.1) is identical in form with
> the **accusative** of *velkra* "friend" (M-A, §24.2). Both belong to the same semantic
> field; article-less contexts are ambiguous.

This is the only **hard inflectional collision** in the whole stock: it is not two
dictionary forms that coincide, but a dictionary form and an inflectional form. The
vocabulary freeze (§24) expressly permits changes in the case of a "problematic collision
with another word" — a renaming was however not carried out; the decision is prepared as
an ADR and is outstanding.

### 6.2 [WORTSCHATZKOLLISION W-03] (vocabulary collision) — further homonyms

> **W-03 (P3, open): further homonyms and confusable forms.**

| Form | Meaning 1 | Meaning 2 | Sources |
|---|---|---|---|
| **fai** | conjunction "that" | relative pronoun | §20 / §13.4 (on this L-02) |
| **kaun** | core word "human being" | indefinite pronoun "one" | §24.1 / §13.4 |
| **vran** | indefinite article M acc. | particle "very" | §11 / §24.9 |
| **xa** | negation particle "not" | prefix "opposite, absence" | §18.3 / §21.2 |

In addition W-03 registers similar but not identical pairs where confusion threatens:
*nest-* (to want) / *nast-* (to eat), *tolm* (slow) / *dolm-* (must), *şaln* (dark) /
*şlan* (despite), *kalm* (four) / *kolm* (how), *xer* (for) / *xerp* (fire).

In the lexicon the genuine homonyms appear as separate files with an appended digit
(*fai.json* and *fai__2.json*, *kaun.json* and *kaun__2.json*, *vran.json* and
*vran__2.json*); four entries carry `W-03` in `qualitaet.offene_befunde`.

ORBIS_CONSTITUTION Art. 6 names precisely the case *fai* as an example of what may **not**
happen: the homonymy "may not be resolved by an incidental reformulation; it is the subject
of the open decision on finding L-02."

---

## 7. What the model does not do

| Not permitted | Reason |
|---|---|
| Supplementing, sharpening or shifting meanings | Art. 6 — no silent changes of meaning |
| Inventing relations for which no attestation exists | Art. 16 — no independent language decisions |
| Filling English fields divergently from the German version | TRANSLATION_POLICY §1 — German is the authority |
| Resolving homonyms by renaming | Art. 7 — no silent renamings; vocabulary frozen (§24) |
| Forming missing words oneself | W-01 remains open until it is decided |

---

## 8. Overview of findings for this chapter

| ID | Type | Concerns | Short |
|---|---|---|---|
| **W-02** | WORTSCHATZKOLLISION | §10.1, §24.2 | *velkran* = nominative "friendship" and accusative of *velkra* |
| **W-03** | WORTSCHATZKOLLISION | §11, §13.4, §18.3, §20, §21.2, §24 | *fai*, *kaun*, *vran*, *xa* and similar pairs |
| **W-04** | DOKUMENTATIONSLÜCKE | §24 | 281 entries without a formulated definition |
| **W-01** | WORTSCHATZLÜCKE | §24 | "to say", "to show", "to search", "there is" are missing |

Sources of this chapter: `language/lexicon/lexicon.schema.json`,
`language/lexicon/concept.schema.json`, `language/lexicon/concepts/concepts.json`,
`language/findings/findings.json`, `ORBIS_CONSTITUTION.md`, `TRANSLATION_POLICY.md` and,
for all language content, `Orbis-Grammatik-0.9.3.md`.
