# ORBIS — The sentence corpus: structure, IDs, roles, key figures

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md).
Describes Orbis Grammar 0.9.3; the reference grammar itself is Orbis-Grammatik-0.9.3.md.*

---

This chapter describes how Orbis sentences are maintained in the repository: which holdings
exist, how the IDs are assigned, which roles a sentence can carry, which fields are
mandatory, and what happens to sentences that **cannot be formed** under 0.9.3.

The corpus is **test material, not a source of rules.** The sole truth is
`Orbis-Grammatik-0.9.3.md`. If a corpus sentence diverges from the grammar, the grammar
prevails, and the divergence is a finding.

---

## 1. The holdings

| Holding | File | Sentences | Content |
|---|---|---|---|
| **Test corpus 0.1** | `Orbis-Testkorpus-0_1.md` (prose version) · `language/corpus/tests/testkorpus-0_1.json` (machine-readable) | 150 | test sentences against the frozen grammar, with a full analysis per sentence |
| **Grammar examples** | `language/corpus/examples/grammatik-beispiele.json` | 71 | all Orbis examples attested in the grammar text, taken over unchanged |
| **Test data** | `Orbis-Testdaten.json` | — | raw data of the validator run |

Both JSON holdings can be validated against `language/corpus/sentence.schema.json`.

**Not to be used as a source:** `archive/corpus/Orbis-Testkorpus-0.1.md` (the version with a
dot) is the archived chat draft. It is retained as a reference, is not edited, and contains
errors that the test version corrects (among others sentence 048: \*loşna → loşnla).

### 1.1 The grammar examples

The 71 sentences from `grammatik-beispiele.json` are the **regression basis**: they come
verbatim from the grammar and must remain compatible with the rule data in `language/`. All
71 carry `status = canonical` and the role `example`. Their German and English lines are
**null**, because the translations are not part of the grammar text everywhere.

Distribution of attestations (excerpt): §25.1 eleven sentences · §25.2 seven · §12.2 five ·
§14 four · §12.1, §12.3, §13.2, §13.3, §11.3, §17.1, §18.2, §18.3 three each.

### 1.2 The appendix of the test corpus

`Orbis-Testkorpus-0_1.md` additionally contains two appendices which are **not sentences**
and therefore carry no `ORB-SENT-` ID:

- the **45-ending test table** on the expressly marked `[TESTFORM]` stem **pren-**. These 45
  forms are **not words of the vocabulary**; they exist exclusively for the morphological
  test of §7–§9.
- the **verb paradigms** of the irregular verbs.

---

## 2. Stable IDs: `ORB-SENT-*`

Every corpus sentence carries a stable ID following the pattern `^ORB-SENT-[0-9]{6}$`
(`sentence.schema.json`).

| Block | Assigned to | Holding |
|---|---|---|
| `ORB-SENT-000001` – `ORB-SENT-000150` | Test corpus 0.1, in the order of the test numbers | 150 |
| `ORB-SENT-900001` – `ORB-SENT-900071` | Grammar examples from 0.9.3 | 71 |

Rules for ID assignment (`VERSIONING.md`):

- **IDs are never reused.** A withdrawn sentence does not release its number.
- The ID is independent of the test number. The field `legacy_nummer` records the old number
  from `Orbis-Testkorpus-0_1.md` (1–150; it is omitted for the grammar examples).
- The ID stays constant even when the sentence changes its status — for instance when a rule
  gap is closed and an `open` becomes a `canonical`.

---

## 3. Roles

A sentence can carry **several** roles at the same time (`rollen` is an array). The schema
enumerates six values; a spelled-out definition per role is **not** given there. The
following table therefore names the attested usage in the holding and marks what is still
unused.

| Role | Attested usage | Count |
|---|---|---|
| **test** | test sentence: serves to show whether a rule holds | 150 (all sentences of the test corpus) |
| **example** | teaching example: the sentence is unambiguously formable under 0.9.3 and may be quoted | 130 in the test corpus + 71 grammar examples |
| **learning** | **not yet assigned** — intended for the learning corpus, `ROADMAP.md` phase H | 0 |
| **dialogue** | **not yet assigned** | 0 |
| **literary** | **not yet assigned**; the short text §25.2 is maintained as `example` | 0 |
| **spoken** | **not yet assigned** | 0 |

**The coupling of role and status is without exception in holding 0.1:** exactly the 130
sentences with `status = canonical` carry `["test", "example"]`; the 20 sentences with a
finding carry only `["test"]`. A sentence that is not unambiguously formable under 0.9.3 is
therefore **never** a teaching example. This is the central protective rule of the corpus: a
case that cannot be decided may nowhere be quoted as exemplary.

---

## 4. Mandatory fields

### 4.1 By schema (`sentence.schema.json`)

| Field | Mandatory per schema | Content |
|---|---|---|
| `id` | yes | `ORB-SENT-######` |
| `status` | yes | `canonical` · `open` · `conflict` · `unclear` · `testproblem` · `draft` |
| `de` | yes | German source, **semantic authority** |
| `syntax` | yes | analysis object, at least `syntax.typ` |
| `qualitaet` | yes | at least `qualitaet.validatorstatus` |
| `orbis` | typed `string \| null` | `null` if not unambiguously formable under 0.9.3 |
| `en` | typed `string \| null` | derived from the German, never guessed from the Orbis word |

`additionalProperties` is set to **false**: unknown fields make a sentence invalid.

### 4.2 By language policy (`TRANSLATION_POLICY.md` §3.2)

For a corpus sentence, **`orbis`, `de`, `en`** and the translation status are **mandatory**;
excepted are open sentences without a canonical Orbis form (section 7).

> **Divergence at the documentation level, reported here, not fixed:**
> `TRANSLATION_POLICY.md` §3.2 names the field `translation_status`, the schema maintains it
> as `en_status` (`missing` · `draft` · `derived` · `reviewed`). Not a language finding — an
> inconsistency between two governance files.

In holding 0.1 **all 150** sentences carry `en_status = derived`.

### 4.3 The analysis object `syntax`

| Field | Content | Holding 0.1 |
|---|---|---|
| `typ` | e.g. "main clause", "main clause + subordinate clause" | 150 filled |
| `muster` | abstract sentence pattern, e.g. `NP-V-NP` | 130 filled, 20 `null` |
| `v2`, `nebensatz`, `verbklammer` | positional features | filled where decidable |
| `wortstellung_regel` | rule ID, e.g. `ORB-GRAM-SYN-010` | throughout `null` in holding 0.1 |
| `subjekt`, `finites_verb`, `objekte`, `kasus`, `tempus`, `person`, `numerus` | analysis | filled |

Further fields per sentence: `lexeme` (the lexemes used, as `ORB-LEX-` IDs; in holding 0.1
filled for the 130 canonical sentences, empty for the 20 open ones), `regeln` (paragraphs
and/or rule IDs), `kategorie`, `schwierigkeit`, `themenbereich`.

**Not yet filled:** `schwierigkeit` is set to `unbestimmt` for all 150 sentences,
`themenbereich` to `null` for all 150, `wortstellung_regel` to `null` for all 150. This is
open editorial work, not a language finding.

### 4.4 The quality object `qualitaet`

| Field | Values | Holding 0.1 |
|---|---|---|
| `validatorstatus` | `ok` · `befund` · `nicht_pruefbar` · `ungeprueft` | 130 × `ok`, 20 × `nicht_pruefbar` |
| `befunde` | list of finding IDs | 20 sentences carry exactly one ID |
| `ergebnis_testkorpus` | original marker, e.g. `[OK]` | 150 filled |
| `anmerkung`, `letzte_pruefung` | free text / date | — / 2026-08-16 |

---

## 5. Key figures of test corpus 0.1

| Result | Status in the JSON | Count | Share |
|---|---|---|---|
| **[OK]** | `canonical` | **130** | 86.7 % |
| **[REGELLÜCKE]** | `open` | **14** | 9.3 % |
| **[REGELKONFLIKT]** | `conflict` | **3** | 2.0 % |
| **[REGELUNKLARHEIT]** | `unclear` | **2** | 1.3 % |
| **[TESTPROBLEM]** | `testproblem` | **1** | 0.7 % |
| **Total** | | **150** | 100 % |

**Stability rate: 86.7 %** (130 of 150). It measures which share of the test sentences is
**unambiguously formable** under 0.9.3 — not which share is "correct".

Overall verdict of the test report: **NOT READY** for a direct jump to 1.0; six P1 problems,
solvable additively (`Orbis-Testbericht-0_1.md`).

### 5.1 Counting convention

The test corpus counts an open point of the grammar **only at those tests** that examine it
specifically — there the sentence is expressly recorded as "not unambiguously formable" or
"not unambiguously decidable". Tests that merely **touch** the same open point but follow
the uniform example practice of the grammar (such as the postposed genitive attribute)
receive **[OK]** with a reference to the finding ID.

The statistics thus measure **the number of open points, not the frequency with which they
are touched.** Without this convention the rate would not be comparable: L-01, for instance,
touches ten sentences but is a single open point.

A second note of the same kind concerns **K-01**: forms such as *est, em, granz, trelm, aul,
eird* are affected by the syllable-shape conflict K-01 (§5.1). This is a central finding of
the grammar, not an error of individual sentences; the phonotactics line records it, the
result remains unaffected by it.

---

## 6. Distribution by categories

| Block | Category (`kategorie`) | Tests | Sentences | canonical | open | conflict | unclear | testproblem |
|---|---|---|---|---|---|---|---|---|
| A | `einfache_hauptsaetze` | 001–020 | 20 | 20 | — | — | — | — |
| B | `akkusativ_dativ` | 021–035 | 15 | 13 | 2 | — | — | — |
| C | `genitiv` | 036–045 | 10 | 8 | 2 | — | — | — |
| D | `adjektive` | 046–060 | 15 | 13 | — | 1 | 1 | — |
| E | `plural` | 061–070 | 10 | 9 | 1 | — | — | — |
| F | `fragen` | 071–080 | 10 | 7 | 3 | — | — | — |
| G | `negation` | 081–090 | 10 | 10 | — | — | — | — |
| H | `nebensaetze` | 091–105 | 15 | 9 | 3 | 2 | — | 1 |
| I | `modalverben` | 106–115 | 10 | 9 | — | — | 1 | — |
| J | `vergangenheit` | 116–125 | 10 | 10 | — | — | — | — |
| K | `zukunft` | 126–135 | 10 | 10 | — | — | — | — |
| L | `passiv` | 136–140 | 5 | 3 | 2 | — | — | — |
| M | `mai_konditional` | 141–145 | 5 | 5 | — | — | — | — |
| N | `komplex` | 146–150 | 5 | 4 | 1 | — | — | — |
| | **Total** | | **150** | **130** | **14** | **3** | **2** | **1** |

Blocks B, C, D, F and H expressly carry **stress tests**: B contains the reflexive stress
tests, C the genitive stress test A, F the question stress test C, H the relative and modal
stress tests. That the findings cluster there is intentional — the test corpus seeks out the
open points deliberately.

**Five categories are completely clean:** simple main clauses, negation, past tense, future
tense and `mai`/conditional pass at 100 %.

---

## 7. Handling of sentences that cannot be formed

The rule is simple and without exception:

> **A sentence that is not unambiguously formable under 0.9.3 carries `orbis = null` and a
> finding ID.** No form is guessed, no gap is closed, no choice is made.

Concretely this means:

| Field | Value for a sentence that cannot be formed |
|---|---|
| `orbis` | `null` |
| `de` | filled — the German sentence exists independently of it |
| `en` | filled — derived from the German |
| `status` | `open` · `conflict` · `unclear` · `testproblem` |
| `rollen` | only `["test"]`, **never** `example` |
| `qualitaet.validatorstatus` | `nicht_pruefbar` |
| `qualitaet.befunde` | at least one ID |
| `syntax.muster` | `null` |
| `lexeme` | empty |

At the same place the prose version `Orbis-Testkorpus-0_1.md` writes, instead of an Orbis
line, the text "— nicht bildbar: …" or "— nicht eindeutig bildbar: …" and presents the
competing candidates with question marks. These candidates are **not Orbis sentences**; they
document what the decision hinges on.

### 7.1 The 20 sentences in detail

| ID | Test | German | Status | Finding |
|---|---|---|---|---|
| ORB-SENT-000033 | 033 | Er sieht sich. | open | L-04 |
| ORB-SENT-000035 | 035 | Sie spricht über sich. | open | L-04 |
| ORB-SENT-000036 | 036 | Das Haus des Mannes ist alt. | open | L-01 |
| ORB-SENT-000039 | 039 | Das Buch meines Freundes ist neu. | open | L-01 |
| ORB-SENT-000051 | 051 | Das gefundene Buch ist alt. | unclear | U-02 |
| ORB-SENT-000060 | 060 | Die Erinnerung vergeht langsam. | conflict | K-04 |
| ORB-SENT-000070 | 070 | Zwei Männer kommen. | open | L-08 |
| ORB-SENT-000074 | 074 | Wen siehst du? | open | L-03 |
| ORB-SENT-000075 | 075 | Wem gibst du das Buch? | open | L-03 |
| ORB-SENT-000076 | 076 | Wessen Buch liest du? | open | L-03 |
| ORB-SENT-000100 | 100 | Der Mann, der kommt, ist mein Freund. | open | L-02 |
| ORB-SENT-000101 | 101 | Die Frau, die ich sehe, spricht. | open | L-02 |
| ORB-SENT-000102 | 102 | Der Mann, dem ich das Buch gebe, wartet. | open | L-02 |
| ORB-SENT-000103 | 103 | Ich weiß, dass der Mann morgen in die Stadt gehen muss. | conflict | K-05 |
| ORB-SENT-000104 | 104 | Sie sagt, dass sie kommt. | testproblem | W-01 |
| ORB-SENT-000105 | 105 | Er weiß, dass sie das Buch nicht lesen kann. | conflict | K-05 |
| ORB-SENT-000111 | 111 | Ich mag das Wort. | unclear | U-03 |
| ORB-SENT-000137 | 137 | Das Haus wird vom Mann gebaut. | open | L-05 |
| ORB-SENT-000138 | 138 | Das Buch wurde von der Frau gelesen. | open | L-05 |
| ORB-SENT-000149 | 149 | Der Mann, der gestern kam, gab dem Kind das Brot des Hauses. | open | L-02 |

### 7.2 Frequency of the findings in the corpus

| Finding | Sentences | Short |
|---|---|---|
| L-02 | 4 | relative clause construction |
| L-03 | 3 | declension of *kem/kelt* |
| K-05 | 2 | modal verb in the subordinate clause |
| L-01 | 2 | position of the genitive attribute |
| L-04 | 2 | case forms of *se* |
| L-05 | 2 | agent in the passive |
| K-04 | 1 | *tolm* adverbial without *-un* |
| L-08 | 1 | syntax of the cardinal numbers |
| U-02 | 1 | participle used attributively |
| U-03 | 1 | modal verb without infinitive |
| W-01 | 1 | vocabulary gap ("to say") |

### 7.3 The special case `testproblem`

**[TESTPROBLEM]** separates a deficiency of the **test** from a deficiency of the
**grammar**. Test 104 ("Sie sagt, dass sie kommt") does not fail on the syntax — the *fai*
construction is attested and regulated — but on the fact that there is **no verb "to say"**.
*tal-* is defined as "to speak" (§24.5); *Lo talat, fai lo vandat* would shift the meaning
without a dictionary basis.

The case is therefore maintained as **W-01** (vocabulary gap), not as a rule gap, and does
not count against the grammar. This separation is the precondition for the stability rate to
say anything about the grammar at all.

---

## 8. Checking

| Call | Purpose |
|---|---|
| `python3 orbis_validator.py --strict` | comparison against `orbis_baseline.json`; exit code 1 = **new** findings |
| `python3 orbis_validator.py --corpus Orbis-Testkorpus-0_1.md` | corpus run; reproduces 130 [OK] and 86.7 % |
| `--all \| --lexicon \| --examples \| --tables \| --manus` | partial checks |
| `--json DATEI \| --update-baseline \| --sim-l09` | output, baseline, syllabification simulation |

Run `--update-baseline` only on explicit instruction.

**What the validator checks:** lexis, morphology, phonotactics, NP agreement and the
assignment preposition → case. **What it cannot check** and what is therefore checked
manually (`MANUELLE_PRÜFUNG`): V2 position, verbal bracket, subordinate-clause final
position, agreement across distance, semantics.

Precisely for this reason the 20 sentences that cannot be formed carry
`validatorstatus = nicht_pruefbar` and not, say, `befund`: the validator cannot assess them
because there is no Orbis line.

---

## 9. Growth of the corpus

The same rules apply to new sentences:

1. **German first.** The German sentence is the semantic authority; Orbis and English follow
   (`TRANSLATION_POLICY.md` §1, §4).
2. **No new words.** If a lexeme is missing, the sentence is a `testproblem` with a
   vocabulary finding — not an occasion to invent a word (`CLAUDE.md` §2).
3. **No decision through the back door.** A sentence that would require an open point
   carries `orbis = null` and the finding ID — not one of the variants (`CLAUDE.md` §3).
4. **A new ID, never a reused one.**
5. **Regression run before the commit** (section 8).

Planned but not yet started: the **learning corpus** with the roles `learning`, `dialogue`,
`literary` and `spoken`, graded by learning levels (`ROADMAP.md` phase H). Until then these
four role values remain defined in the schema and unused in the holding.

---

## 10. Open points of the corpus

| Point | Kind | Short |
|---|---|---|
| `schwierigkeit` | editorial | all 150 sentences at `unbestimmt` |
| `themenbereich` | editorial | all 150 sentences at `null` |
| `syntax.wortstellung_regel` | editorial | throughout `null`, although the rule IDs `ORB-GRAM-SYN-010`…`-025` are available |
| `translation_status` / `en_status` | inconsistency | two names for the same field (section 4.2) |
| Roles `learning`/`dialogue`/`literary`/`spoken` | holding | defined, unused |
| German/English of the grammar examples | holding | 71 sentences with `de = null`, `en = null` |

None of these points is a language finding. The language findings are recorded in
`Orbis-Audit-0_1.md` §A and machine-readably in `language/findings/findings.json`
(33 entries: 5 conflicts, 10 gaps, 14 unclarities, 1 vocabulary gap,
2 vocabulary collisions, 1 documentation gap; by priority 6 × P1, 11 × P2, 16 × P3).

---

*Documentation of Grammar 0.9.3. In case of divergence, `Orbis-Grammatik-0.9.3.md` prevails.*
