# Orbis — Phonology

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md). Describes Orbis Grammar 0.9.3.*

---

## 1. Subject

This chapter describes the sound inventory of Standard Orbis: the 19 consonants and
5 vowels from §2.1–2.2, the diphthongs from §2.3 and the two sound groups from §3.2.
It further describes which of these statements are **binding** (§3.3) and which are
**descriptive guidelines** without prohibitive force (§3.4, §3.5).

The distribution of sounds over syllables (onset and coda clusters, syllable shapes) is
not found here but in `PHONOTACTICS.md` (§5). Sound values and stress are in
`PRONUNCIATION.md` (§2, §4, §23). The historical origin of the forms is in
`PROTO_ORBIS.md` (§22).

---

## 2. Consonants (§2.1)

Orbis has **19 consonants**. The grouping and the pronunciation notes of the following
table are taken from §2.1 itself (rendered into English here; the German wording is the
authoritative one); the column "Attestations" names words of the frozen vocabulary (§24)
and of the example sentences (§25).

| Group | Sounds | Description per §2.1 | Attestations |
|---|---|---|---|
| Voiceless stops | **p · t · k** | as in German, without strong aspiration | *xerp* fire, *pliso* feather (§24) · *taiv* language, *talru* speaker (§24) · *kaun* human being, *kavla* city (§24) |
| Voiced stops | **b · d · g** | as in German | *breun* house, *brasi* bread (§24) · *draun* father, *zaldre* day (§24) · *grein* earth, *granz* old (§24) |
| Affricate | **ç** | like German *tsch* | **no attestation** — see §6 of this chapter |
| Voiceless fricatives | **f · s · ş · x** | *s* always sharp (voiceless); *ş* like German *sch*; *x* far back in the throat | *fai* that (§20) · *sarla* woman (§24) · *şirn* child (§24) · *xerp* fire (§24) |
| Voiced fricatives | **v · z · j** | *z* as in German *Rose*; *j* as in French *jour* | *valru* man, *virn* life (§24) · *zaldre* day, *zaub-* to hear (§24) · **no attestation for j** — see §6 |
| Nasals | **m · n · ñ** | *ñ* as in Spanish *señor* | *moks* death, *mela* wanderer (f.) (§24) · *nauş* time (§24) · plural marker *-ñ-*: *melruñ* the wanderers (§25.1) |
| Flowing sounds (German *Fließlaute*) | **l · r** | *r* distinctly rolled | *luiv* sun (§24) · *rusk-* to write (§24.5), *valru* man (§24) |

**Not present (§2.1):** *h, w, th, pf, ts* as well as *ng* as a sound of its own.

On the count: the seven groups yield 3 + 3 + 1 + 4 + 3 + 3 + 2 = 19 consonants.
§3.3 declares exactly this inventory binding — a word with any other consonant is not
valid Orbis.

---

## 3. Vowels (§2.2)

Five vowels: **a · e · i · o · u**

§2.2 lays down: "pure and clear, always fully pronounced. No schwa, no reduction.
An *e* at the end of a word is a full *e*."

| Vowel | Attestation |
|---|---|
| a | *sarla* woman (§24.3) |
| e | *milne* eye, *zaldre* day (§24) — final *e* is full |
| i | *brasi* bread, *larki* stone (§24) |
| o | *verno* heart, *vresto* book (§24) |
| u | *skelnu* sky, *veltu* year (§24) |

There is no notation for length, no lengthening sign and no doubling (§4.1). Vowel length
is not regulated phonemically in 0.9.3 and is not supplied here.

On the weakening of unstressed **-a** in colloquial pronunciation (*sarla* → [sarlə])
see §4.2 and `PRONUNCIATION.md` — that is level B, not level A.

---

## 4. Diphthongs (§2.3)

§2.3 heads the section "Diphthongs (6)" and thereby expressly distinguishes between
**attested**, **regular but unattested** and **open**.

| Diphthong | Status per §2.3 | Attestations from §2.3 / §24 |
|---|---|---|
| **ai** | attested, necessary in the vocabulary | *taiv, saiv-, traiv-, vlaid, taisa, mai*; future vowel *-ai-* (§15) |
| **au** | attested, necessary in the vocabulary | *kaun, nauş, şaul, draun, zaub-, klaun, traus* |
| **ei** | attested, necessary in the vocabulary | *veiş, grein, eird*; core-word plural *-ei* (§10.3) |
| **ui** | attested, necessary in the vocabulary | *luiv, luid* |
| **eu** | attested, necessary in the vocabulary | *breun* — the only attestation |
| **oi** | **regular, but currently unattested** | no word of the lexicon; writable in Orbis Manus (§26.4) |
| **ou** | **[NOCH ZU ENTSCHEIDEN]** (to be decided) (§2.3, §30) | none — **do not use** as long as it is undecided |

**On *oi*:** §2.3 states the status expressly: *oi* "is a permitted productive diphthong
and writable in Orbis Manus. It is so far used by no word of the lexicon and is therefore
not an attestation of the necessity of the system, but an open gap which new words may
fill." *oi* is thus permitted, but unattested.

**On *ou*:** §2.3 and §30 carry *ou* as an open point. Whether it is admitted is a
decision of the language designers. Until then *ou* is **not** a part of the inventory and
must not be used in words, test sentences or tools. This documentation does not decide the
question.

**No further diphthongs are added** (§2.3).

All diphthongs are spoken in **one** syllable, "with a clear transition and without
slurring" (§2.3).

For their position in the word, guideline 4 (§3.4) applies: at most one diphthong per
word, preferably in the stressed syllable. That is a guideline, not a prohibition
(see §5).

---

## 5. Sound groups and rule status

### 5.1 The two sound groups (§3.2)

§3.2 divides the 19 consonants into two sound groups:

| Group | Sounds |
|---|---|
| **Flowing sounds** (German *Fließlaute*) | l · r · n · m · ñ · v · z · s · j |
| **Hard sounds** (German *Härtelaute*) | p · t · k · b · d · g · f · x · ş · ç |

§3.1 justifies the division: "The flow comes from **l, r, n, m, v, z, s**; the hardness
from **p, t, k, b, d, g, f, x, ş, ç**. What is decisive is the ratio in the
**vocabulary as a whole**, not the arithmetic in the individual word."

To be noted: the sound groups of §3.2 are **not** identical with the articulatory groups
of §2.1. *s* and *z* stand articulatorily with the fricatives, but by sound with the
flowing sounds; *ş* and *x* stand with the hard sounds. The division of §3.2 is a sound
category, not a phonetic one.

The coda rule §5.3(a), by contrast, uses the expression "flowing sound or nasal
(l, r, m, n)" in a narrower sense — there only these four sounds are meant, not the nine
of §3.2. See `PHONOTACTICS.md` §4.

### 5.2 Binding: §3.3

§3.3 names the conditions under which a word is **not valid Orbis**. Phonologically
relevant are the first three lines:

| Area | Rule (§3.3) |
|---|---|
| Phoneme inventory | only the 19 consonants, 5 vowels and 6 diphthongs from §2 |
| Syllable structure | only V, KV, KVK, KKV, KKVK, KVKK (§5.1) |
| Onset clusters | only the list from §5.2 |
| Coda clusters | only under the conditions in §5.3 |

§3.3 closes with the sentence: "Everything else is sound, not law."

For the syllable-structure line, the rule conflict **K-01** is to be noted: §5.1 does not
carry all the syllable shapes that the frozen vocabulary actually needs. See
`PHONOTACTICS.md` §3.

### 5.3 Descriptive: §3.4 and §3.5

§3.4 sets up five **sound guidelines** and says of them expressly: "A word does **not
become invalid** because it deviates from them. They are a tool when coining, not a stamp
of approval when admitting."

| No. | Guideline (§3.4) | Short form |
|---|---|---|
| 1 | Flow tendency | In the vocabulary as a whole the flowing sounds clearly predominate; not recomputed for the individual word |
| 2 | Hard sounds | Typically 0–2 hard sounds in the lexical stem; more is rare, but not forbidden |
| 3 | Word ending | Soft endings in a vowel or *n, r, l, m, s* form the majority |
| 4 | Diphthong placement | At most one diphthong per word, preferably in the stressed syllable |
| 5 | Syllable weight | Everyday words 2 syllables, weighty/abstract concepts 3–4; monosyllables mostly function words or core words |

For guideline 2, §3.4 names as examples of phonologically flawless forms: *kadru*,
*grondo*, root *kred-*. For guideline 3, §3.4 names as attested hard endings the verb
stems *milk-, nast-, rusk-* and the core words *xerp, moks, eird*.

**§3.5 limits the scope:** the guidelines apply "**exclusively to the lexical stem**.
Grammatical morphology must never make a word phonologically 'invalid' after the fact."

Not counted in, according to §3.5:

- case markers (*-n, -ş, -s*)
- plural markers (*-ñ-* together with the echo vowel, *-ei*)
- gender endings (the 45 endings, §7)
- person endings (*-m, -ş, -t, -men, -şen, -ten*)
- tense markers (*-a-, -o-, -ai-*)
- regular adjective endings (*-ra, -la, -na* …)
- infinitive *-ex* and participle *-ut*
- productive derivational morphemes (*-ru, -la, -na, -isto, -uma, -vi, şu-, xa-, re-, dra-, su-*)

Attestation from §3.5: *milkaiten* is a flawless word — only the stem *milk-* is checked.

The term **Echovokal** ("echo vowel") in the plural-marker line is defined nowhere in the
grammar, but only attested through tables in §9 — finding **U-09** (rule unclarity).

### 5.4 Side effect on the subclasses (§3.6)

The class consonants **k, d, t** are themselves hard sounds. Nouns of the subclasses M-B,
M-C and N-C therefore tend to carry one hard sound more than the A series (§3.6):
*narku* (M-B), *vrondo* (M-C), *vresto* (N-C) as against *valru* (M-A), *sarla* (F-A).

§3.6 expressly calls this "an observation, not a prescription". Whether a grammatical
function additionally arises from it is **[NOCH ZU ENTSCHEIDEN]** (§3.6, §30).

---

## 6. Open points and observations

| Point | Status |
|---|---|
| Diphthong *ou* | **[NOCH ZU ENTSCHEIDEN]** (§2.3, §30) — do not use |
| Vowel harmony throughout | **[NOCH ZU ENTSCHEIDEN]** (§30) |
| Final consonant-cluster list | **[NOCH ZU ENTSCHEIDEN]** (§30) |
| Syllable-shape list §5.1 incomplete | **[REGELKONFLIKT K-01]** (rule conflict) — see `PHONOTACTICS.md` |
| "Echovokal" defined nowhere | **[REGELUNKLARHEIT U-09]** (rule unclarity) (§9) |
| Stroke weight for *f s ş x v z j ç* undefined | **[REGELLÜCKE L-10]** (rule gap) (§26.9) — concerns Manus, not phonology |
| Final function of the subclasses | **[NOCH ZU ENTSCHEIDEN]** (§3.6, §30) |

**Observation without a finding ID:** for the affricate **ç** and the voiced fricative
**j** the frozen vocabulary of 0.9.3 (§24, 281 recorded base forms in
`language/lexicon/entries/`) contains **not a single word**. Both sounds are, through §2.1
and §3.3, a regular part of the inventory and are represented in Orbis Manus with core
forms of their own (§26.2: family KAI for *ç*, family ISH for *v z j*) — they are merely
unattested, like *oi*. The grammar does not explain this gap and the audit assigns no
finding ID for it; here it is only recorded, neither assessed nor closed.

---

## 7. Cross-references

| Topic | Location |
|---|---|
| Syllable shapes, onset and coda clusters, syllable boundaries | `PHONOTACTICS.md` (Abschnitt 5 dieser Datei) |
| Sound values, colloquial pronunciation, stress | `PRONUNCIATION.md` (§2, §4, §23) |
| Sound laws and word derivation | `PROTO_ORBIS.md` (§22) |
| Script signs for sounds and diphthongs | Grammar §26 (Orbis Manus) |
| Finding IDs and rule basis | `Orbis-Audit-0_1.md` |

---

*Source of all rule statements: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Where this
documentation and the grammar diverge, the grammar prevails. Where this English version
and the German version diverge, the German version prevails (TRANSLATION_POLICY.md, section 1).*
