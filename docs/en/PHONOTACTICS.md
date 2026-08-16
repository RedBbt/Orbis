# Orbis — Phonotactics

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md). Describes Orbis Grammar 0.9.3.*

---

## 1. Subject

This chapter describes §5 of the grammar: which syllable shapes are permitted (§5.1),
which consonant clusters may stand at the beginning of a syllable (§5.2), under which
conditions two consonants may stand at the end of a syllable (§5.3) and what §5.4 says
about word length and word ending.

All three rules are **binding** through §3.3: a word that violates them is not valid
Orbis. The sound inventory itself is in `PHONOLOGY.md` (§2).

One central caveat applies to the whole chapter: **the list of syllable shapes in §5.1 is
incomplete** (rule conflict K-01, §3), and **a rule for syllable division does not exist**
(rule gap L-09, §5). Both are named here, not remedied.

---

## 2. Permitted syllable shapes (§5.1)

§5.1 names six shapes. K = consonant (the grammar's notation, from German *Konsonant*),
V = vowel or diphthong.

> **V · KV · KVK · KKV · KKVK · KVKK** (the last one rare)

§5.1 itself lists **no example words**. The following table therefore attests every shape
with **monosyllabic** words of the grammar, for which the assignment is unambiguous —
with polysyllabic words it would depend on the missing syllable-division rule (L-09, §7).

| Shape | Structure | Monosyllabic attestations |
|---|---|---|
| **V** | vowel only | **no monosyllabic attestation** — the vocabulary contains no word consisting of a bare vowel. Open V syllables arise only when polysyllabic words are divided (e.g. *oñas* as *o·ñas*, §13.1) and thus depend on L-09 |
| **KV** | consonant + vowel | *ro* he, *lo* she, *no* it (§13.1) · *xa* not, *ze* and, *vu* or (§24.9) · *se* oneself (§13.4) |
| **KVK** | consonant + vowel + consonant | *kaun* human being, *nauş* time, *şaul* name (§24.1) · *vim* I (§13.1) |
| **KKV** | two-consonant cluster + vowel | *xra · xla · xna* definite article, *vra · vla · vna* indefinite article (§11) · *zva* with, *kru* on (§19) |
| **KKVK** | two-consonant cluster + vowel + consonant | *breun* house, *grein* earth, *draun* father (§24.1) · *span* over, *şlim* between (§19) |
| **KVKK** | consonant + vowel + two-consonant coda (**rare**) | *virn* life, *moks* death, *xerp* fire (§24.1) · *tolm* slow (§24.7) · *kalm* 4, *mern* 5, *xelm* 10 (§24.8) |

§3.3 refers to exactly this list and makes it binding. Three or more consonants at the
beginning of a syllable are "forbidden without exception" (§5.2); more than two consonants
in the coda are not admitted by §5.3.

---

## 3. [REGELKONFLIKT K-01] (rule conflict) — the list in §5.1 is incomplete

**Finding ID: K-01** (`Orbis-Audit-0_1.md` §2.1 and §A). Priority P1.

§5.1 carries neither **VK/VKK** (closed syllables with a vocalic onset) nor **KKVKK**
(two-consonant onset + two-consonant coda). Both shapes are used by the frozen vocabulary
and by the examples of the grammar itself. By the wording of §3.3 the words concerned
would be "not valid Orbis" — although the grammar carries them.

### 3.1 Missing shape VK / VKK

| Word | Syllable shape | Place of occurrence |
|---|---|---|
| **aul** water | VK | core word §24.1; all forms *aulen, auleş, aules* §10.3 |
| **eird** world | VKK | core word §24.1; all forms *eirden, eirdeş, eirdes* §10.3 |
| **ain** yes | VK | §24.9 |
| **oñ** they | VK | personal pronoun §13.1 |
| **est** he/she/it is | VKK | *esex*, §15.2 |
| **em**, **eş** I am / you are | VK | *esex*, §15.2 |
| **aulmelna** canal | VK (first member) | compound §21.3 |

Attestation in the running text of the grammar: *"Lo loşn est."* — She is beautiful
(§12.2); *"Vim xa valnam soñex, grali xla kirva vran luid est."* (§25.1).

### 3.2 Missing shape KKVKK

| Word | Syllable shape | Place of occurrence |
|---|---|---|
| **granz** old | KKVKK | adjective §24.7 — and at the same time a coda example in §5.3(a) |
| **trelm** long | KKVKK | adjective §24.7; inflected *trelmrañan* §25.2 |
| **vresn** weak | KKVKK | adjective §24.7 |
| **skirm** little, few | KKVKK | adverb §24.9 |
| **prilm** craft | KKVKK | 10-percent group §10.1 |
| **prens-** to take | KKVKK (imperative *Prens!*) | verb root §24.5 — and a coda example in §5.3(b) |
| **dremn-** to think | KKVKK (imperative *Dremn!*) | verb root §24.5 |
| **vlent-** to run | KKVKK (imperative *Vlent!*) | verb root §24.5 |

Attestation in the running text: *"Xna breun granz stanat, klas xla kavla zirv vurt."*
(§25.1); *"Vra melru molet dral xrañan trelmrañan zaldreñen."* (§25.2).

### 3.3 The severity of the conflict

§5.3 itself names **granz** and **prens** as examples of permitted codas. The coda rule
thereby presupposes syllable shapes which §5.1 does not carry. The conflict lies within
§5, not between §5 and the lexicon alone.

**Not decidable at this place:** whether §5.1 is extended by VK, VKK and KKVKK, whether
the words concerned are to be divided differently, or whether some other resolution
applies. That is a designer decision (editorial candidate for 0.9.4). The tools of the
repository check strictly against the **listed** set and report deviations as K-01 instead
of silently extending the list (`language/phonology/syllable_shapes.json`,
`orbis_validator.py --lexicon | --examples`, finding class "§5.1-BEFUND").

§30 carries "Final consonant-cluster list" as **[NOCH ZU ENTSCHEIDEN]** (to be decided)
in any case.

---

## 4. Consonant clusters at the beginning of a syllable (§5.2)

**At most two consonants. Three or more are forbidden without exception.**

Permitted is only this closed list of **25** clusters (§5.2, in the order of the grammar):

> **tr · dr · kr · gr · pr · br · pl · bl · fl · vl · fr · vr · vn · sl · şl · şr · sk · st · sp · xr · xl · xn · zv · gl · kl**

Ordered by structure type, with attestations from §24/§25:

| Type | Clusters | Attestations |
|---|---|---|
| stop + *r* | **tr · dr · kr · gr · pr · br** | *trelm* long · *draun* father · *kraven* 1000 · *grein* earth · *prila* hand · *breun* house |
| stop + *l* | **pl · bl · gl · kl** | *pliso* feather · **bl unattested** · *gluvi* flame · *klaun* true |
| *f/v* + liquid/nasal | **fl · vl · fr · vr · vn** | **fl unattested** · *vlaiko* wind · **fr unattested** · *vresto* book · *vnan* (article, §11.2) |
| *s/ş* + consonant | **sl · şl · şr · sk · st · sp** | **sl unattested** · *şlim* between · **şr unattested** · *skelnu* sky · *stan-* to stay · *span* over |
| *x* + consonant | **xr · xl · xn** | *xra / xla / xna* (definite article, §11.1) |
| *z* + *v* | **zv** | *zva* with (§19) |

**Observation on attestation** (`Orbis-Audit-0_1.md` §2.2, recomputed against
`language/lexicon/entries/`): **bl, fl, fr, sl, şr** are permitted, but are attested by
**no** word in the frozen vocabulary. *fr* appears exclusively in the §5.3 example word
*frisk*, which does not stand in the vocabulary §24. The audit notes on this expressly:
**no finding against the list itself** — unattested means permitted, not invalid. New
words may fill these gaps (analogously to the diphthong *oi*, §2.3).

---

## 5. Consonant clusters at the end of a syllable — coda (§5.3)

**At most two consonants.** A two-consonant cluster is permitted if **one** of the three
conditions applies (the conditions are alternative, not cumulative):

| Condition | Wording of §5.3 | Examples of the grammar |
|---|---|---|
| **(a)** | The first sound is a flowing sound or nasal (**l, r, m, n**) | *virn, xerp, tolm, teln, xarn, granz* |
| **(b)** | The second sound is **s** | *moks, prens* |
| **(c)** | The cluster is **şn, sn, sk** or **st** | *loşn, leşn, vesn, frisk, nast* |

Notes:

- Condition (a) uses "flowing sound" (German *Fließlaut*) **more narrowly** than §3.2.
  What is expressly meant here are only *l, r, m, n* — not the nine flowing sounds of the
  sound group (§3.2: l r n m ñ v z s j). See `PHONOLOGY.md` §5.1.
- Condition (c) is a closed list of four clusters. *sn* was added only in 0.9.3; §29
  records that *vesn* (6), *vresn* (weak) and *misn* (short) were formally impermissible
  under the coda rule of 0.9.2 — "an error from 0.9.2 which does not concern the words
  themselves".
- The example word *frisk* from (c) does **not** stand in the vocabulary §24 (see
  `Orbis-Testbericht-0_1.md`, phase 7). It attests the rule, not the lexicon.
- The rule itself is unambiguous and machine-checkable; the audit notes **no finding
  against the rule**. The conflict concerns only the list of syllable shapes (K-01, §3).

Single consonants in the coda are covered by KVK/KKVK in any case: *kaun, nauş, şaul,
şirn, mel-* (§24).

---

## 6. Word length and word ending (§5.4)

§5.4 is short and expressly subordinate:

> "Word length and word ending follow the guidelines in §3.4 — they are a tendency, not
> law. **Binding is §5.3 alone.**"

Thus: a word with a hard final consonant or an unusual number of syllables is
phonotactically correct as long as §5.1–5.3 are observed. Guidelines 3 and 5 (§3.4) only
describe the frequency distribution — see `PHONOLOGY.md` §5.3.

Attested hard endings are named by §3.4 itself: the verb stems *milk-, nast-, rusk-* and
the core words *xerp, moks, eird*.

---

## 7. [REGELLÜCKE L-09] (rule gap) — there is no syllable-division rule

**Finding ID: L-09** (`Orbis-Audit-0_1.md` §2.4 and §A). Priority P2. Concerns §5 and §26.

§5 lays down which syllables are **permitted**. Nowhere does the grammar lay down how a
sound chain is **divided** into syllables — there is no onset maximization, no sonority
rule, no preference. As a result many words can be divided in more than one rule-conforming
way:

| Word | Possible divisions (all conforming to §5) |
|---|---|
| **mela** wanderer (f.) (§24.3) | **me·la** (KV + KV) or **mel·a** (KVK + V) |
| **kavla** city (§24.3) | **kav·la** (KVK + KV) or **ka·vla** (KV + KKV) |
| **drovna** forest (§24.4) | **drov·na** (KKVK + KV) or **dro·vna** (KKV + KKV) |
| **vresto** book (§24.4) | **vres·to** or **vre·sto** — the conceivable third reading *vrest·o* requires the syllable shape KKVKK, which §5.1 does **not** list (K-01), and is therefore not counted here |

**Where the gap has no consequences:** for pronunciation and stress. The stress rule §23
counts syllables from the end and yields for *mela* the same result under both divisions.

**Where the gap takes effect:** in **Orbis Manus** (§26) and in keyboard input (§26.8).
The Manus syllable formula (§26.1: core consonant + optional second onset consonant +
vowel sign + 0–2 final consonants) writes syllable by syllable. The same standard spelling
therefore has several permitted Manus spellings: *mela* is either m core form + e + l coda
followed by an a vowel carrier, **or** m core form + e followed by l core form + a. Both
are correct under §5 and §26.

**Quantification: 77 of 281 base forms** of the lexicon can be divided ambiguously
(`Orbis-Manus-Schreibtest-0_1.md`; verifiable with `orbis_validator.py --manus`). A
deterministic Manus composer is thereby blocked.

**Important:** the syllabification simulations of the repository
(`orbis_validator.py --sim-l09`, `tests/manus`) are **analysis tools, not language rules**.
They must never be cited as a rule. Which division applies is decided by the language
designers; this documentation does not decide it.

---

## 8. Summary of rule status

| Rule | Paragraph | Status |
|---|---|---|
| Syllable shapes V/KV/KVK/KKV/KKVK/KVKK | §5.1 | binding through §3.3 — but **[REGELKONFLIKT K-01]**: VK/VKK/KKVKK are missing |
| Onset clusters, list of 25, max. 2 | §5.2 | binding, unambiguous, no finding |
| Coda, max. 2, conditions (a)/(b)/(c) | §5.3 | binding, unambiguous, no finding |
| Word length and word ending | §5.4 | expressly a tendency, not law |
| Syllable division | — | **[REGELLÜCKE L-09]** — not regulated |
| Final consonant-cluster list | §30 | **[NOCH ZU ENTSCHEIDEN]** |

---

## 9. Cross-references

| Topic | Location |
|---|---|
| Sound inventory, sound groups, rule status §3.3/§3.4 | `PHONOLOGY.md` (§2, §3) |
| Stress and sound realization | `PRONUNCIATION.md` (§23, §2, §4) |
| Derivation of new word forms | `PROTO_ORBIS.md` (§22) |
| Syllabic script, Manus formula | Grammar §26 |
| Finding IDs K-01, L-09 and rule basis | `Orbis-Audit-0_1.md`, `language/findings/findings.json` |
| Machine-readable version | `language/phonology/syllable_shapes.json`, `onsets.json`, `codas.json`, `syllabification.json` |

---

*Source of all rule statements: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Where this
documentation and the grammar diverge, the grammar prevails. Where this English version
and the German version diverge, the German version prevails (TRANSLATION_POLICY.md, section 1).*
