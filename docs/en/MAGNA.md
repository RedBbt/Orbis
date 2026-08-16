# Orbis — Orbis Magna, the solemn script

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md).
Describes Orbis Grammar 0.9.3; the reference grammar itself is Orbis-Grammatik-0.9.3.md.*

---

## 1. Subject

This chapter describes §27 of the grammar. §27 is short; this chapter remains so
as well. Nothing is added, spelled out or elaborated.

Orbis possesses its script "in two stages" (§1): **Orbis Manus** as the everyday script
(§26, see `MANUS.md`) and **Orbis Magna** as the solemn execution.

---

## 2. What §27 lays down

§27 determines Magna not as a second script, but as a **stylistic layer over
the same core forms**:

> "The same 20 core forms, the same syllable formula, the same language — solemnly
> executed."

From this it follows: whoever can read Manus also reads Magna. There is no additional sign,
no second syllable formula and no divergent grammar. All statements from §26.1–26.7
continue to apply unchanged.

**Purpose of use (§27):** quotations, inscriptions, symbols, art, titles.

**The five stipulations (§27):**

| No. | Stipulation | Kind |
|---|---|---|
| 1 | Circular arrangement, text from the inside outward in a spiral | Arrangement |
| 2 | Core forms may be embellished as long as the two distinguishing features remain | Permission with limit |
| 3 | Vowel dots may become circles or lozenges | Permission |
| 4 | **Coda signs may not be embellished** | Prohibition |
| 5 | The closure of a text forms the outer ring | Arrangement |

Stipulation 2 refers back to §26.2 ("Every core form must differ from every other in
at least two features"): the embellishment may not use up the feature distance.
Stipulation 4 protects the coda; it is the only class of signs whose legibility depends solely on size and place [derived from §26.5–26.7; §27 states only the prohibition]
(§26.5–26.7) and which through ornament would become confusable with a subsidiary mark or a closing
mark.

**Attestations.** The grammar shows no text and no sign in Orbis Magna; §27 consists
entirely of the quoted stipulations. An example can therefore not be adduced
here. The attested Manus decompositions (*mel*, *kaun*, *breun*, *tel*, *moks*, *virn*,
*xerp*, *teln*; §26.5–26.6) apply according to the wording of §27 to Magna as well, because
the same syllable formula holds there.

---

## 3. What is expressly open

§27 closes with an open marking of its own, which §30 repeats among the open points of the
overall document ("Spiral rules of Orbis Magna"):

> **[NOCH ZU ENTSCHEIDEN]** (to be decided) Spiral direction, line break, very long texts.

| Open point | What is unresolved |
|---|---|
| **Spiral direction** | §27 lays down "from the inside outward", but not the sense of rotation (clockwise or counter-clockwise) |
| **Line break** | How a line in the spiral ends and the next begins |
| **Very long texts** | What happens when a text bursts the ring (several spirals, continuation mark, different format) |

The audit lists Magna expressly as **open, but without a test finding**
(`Orbis-Audit-0_1.md` §21): the spiral rules are not a rule conflict and not a
rule gap in the sense of the finding IDs, but an area marked as undecided by the grammar
itself. There is therefore no finding ID K-xx / L-xx / U-xx for Magna.

**This documentation decides none of these points** and also derives no rule from
§26. As long as the spiral rules are open, there is no testable Magna layout; a
Magna sentence cannot be checked for correctness.

---

## 4. Delimitation and status

| Point | Determination |
|---|---|
| Sign inventory | identical with Manus: 20 core forms, 8 families (§26.2) |
| Syllable formula | identical with Manus (§26.1) |
| Language | identical — Magna is execution, not variety |
| Rules of its own | only the five stipulations from §27 |
| Versioning | Orbis Manus stands at 0.x without a released version; Magna has no version of its own (`STATUS.md`) |
| Storage in the repo | `script/magna/` — separate from `script/manus/` and from `language/` |

Magna depends technically on Manus: as long as **[REGELLÜCKE L-09]** (rule gap, no syllable-division rule)
and **[REGELLÜCKE L-10]** (rule gap, stroke weight) are open, the Magna syllable blocks too are not
unambiguously determined, because they use the same blocks (see `MANUS.md` §10 and §11).
A release of Magna before Manus is thus not possible.

---

## 5. Cross-references

| Topic | Place |
|---|---|
| Core forms, syllable formula, coda, closing marks | `MANUS.md` (§26) |
| State of keyboard planning | `KEYBOARD.md` (§26.8) |
| Open points of the overall document | Grammar §30 |
| Finding situation on §26/§27 | `Orbis-Audit-0_1.md` (§21) |

---

*Source of all rule statements: `Orbis-Grammatik-0.9.3.md` (READ ONLY). In case of divergence
between this documentation and the grammar, the grammar applies.*
