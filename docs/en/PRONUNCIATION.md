# Orbis — Pronunciation and Stress

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md). Describes Orbis Grammar 0.9.3.*

---

## 1. Subject and caveat

This chapter collects what the grammar says about **sound realization**: the pronunciation
notes in §2.1–2.3, the separation of levels in §4.1–4.2 and the stress rules in §23.

**Important caveat:** Orbis 0.9.3 contains **no binding IPA assignment**. §2.1 describes
the consonants in everyday language and by way of comparisons with German, French and
Spanish; a phonetic transcription of the 19 consonants and 5 vowels does not exist. This
documentation does **not** supply one — an IPA table would be a new rule, and rules are set
by the language designers. See §6 of this chapter.

The historical sound laws (§22) are **not** pronunciation notes; they are in
`PROTO_ORBIS.md`. §4.3 states this expressly.

---

## 2. The three levels (§4)

§4 separates three things "which in earlier versions were mixed and which belong strictly
apart":

| Level | Content | Paragraph | Place in this documentation |
|---|---|---|---|
| **A** | Standard orthography — script to sound | §4.1 | this chapter, §3 |
| **B** | Natural colloquial pronunciation | §4.2 | this chapter, §5 |
| **C** | Historical sound laws | §4.3, §22 | `PROTO_ORBIS.md` |

The separation is itself a rule statement: what stands on level C must not be read as a
pronunciation note, and what stands on level B is not a spelling deviation.

---

## 3. Level A — standard orthography (§4.1)

§4.1 states:

> "**The spelling of Standard Orbis is almost completely predictable.** Every letter has
> exactly one sound value, every sound exactly one sign. There are no silent letters, no
> length signs, no doubling for length."

From this it follows (§4.1): "Whoever knows the 19 consonants, 5 vowels and 6 diphthongs
can pronounce every written Orbis word correctly. The only additional information is the
stress, and that is determined by rules to about 85 % (§23)."

Practical consequences:

- Double consonants do not mark vowel length. Where they would arise at morpheme
  junctures, they merge into a single consonant in any case (juncture rule §21.4:
  *mel + la* → **mela**, *tal + la* → **tala**, *şaln + na* → **şalna**,
  *selv + vi* → **selvi**).
- An *e* at the end of a word is a full *e*, not a schwa (§2.2): *milne* eye, *zaldre*
  day, *kelte* (interrogative word, §18.2).
- Vowel length is not regulated in 0.9.3 and is not supplied here.

---

## 4. What §2 says about sound realization

### 4.1 Consonants (§2.1)

The descriptions are taken over from §2.1 itself (rendered into English here; the German
wording is the authoritative one). The column "Attestations" names words from §24/§25.

| Group | Sounds | Description per §2.1 | Attestations |
|---|---|---|---|
| Voiceless stops | **p t k** | "as in German, **without strong aspiration**" | *xerp, taiv, kaun* (§24.1) |
| Voiced stops | **b d g** | "as in German" | *breun, draun, grein* (§24.1) |
| Affricate | **ç** | "like German *tsch*" | no attestation in the vocabulary (see `PHONOLOGY.md` §6) |
| Voiceless fricatives | **f s ş x** | "*s* **always sharp** (voiceless); *ş* like German *sch*; *x* **far back in the throat**" | *fai* (§20), *sarla* (§24.3), *şirn* (§24.1), *xerp* (§24.1) |
| Voiced fricatives | **v z j** | "*z* as in German *Rose*; *j* as in French *jour*" | *valru* (§24.2), *zaldre* (§24.2); no attestation for *j* |
| Nasals | **m n ñ** | "*ñ* as in Spanish *señor*" | *moks, nauş* (§24.1); plural marker *-ñ-* in *melruñ* (§25.1) |
| Flowing sounds | **l r** | "*r* **distinctly rolled**" | *luiv* (§24.1), *valru* (§24.2) |

The only explicit negative note in §2.1 concerns aspiration: *p t k* are spoken
**without** strong aspiration. That is the only point at which the standard pronunciation
expressly sets itself apart from German.

**Not present** (§2.1): *h, w, th, pf, ts* as well as *ng* as a sound of its own. A
written *ñ* is a nasal as in *señor*, not the German *ng* combination.

### 4.2 Vowels (§2.2)

> "**a e i o u** — pure and clear, **always fully pronounced**. No schwa, no reduction.
> An *e* at the end of a word is a full *e*."

That holds for level A. On level B (§4.2) unstressed *-a* at the end of a word is the
express exception, see §5.

### 4.3 Diphthongs (§2.3)

> "All diphthongs are spoken **in one syllable**, **with a clear transition and without
> slurring**."

Attested: *ai* (*taiv*), *au* (*kaun*), *ei* (*grein*), *ui* (*luiv*), *eu* (*breun*).
*oi* is regular, but unattested; *ou* is **[NOCH ZU ENTSCHEIDEN]** (to be decided) and not
to be used. Overview of status: `PHONOLOGY.md` §4.

---

## 5. Level B — natural colloquial pronunciation (§4.2)

§4.2 records: "In everyday use one does not speak as one writes. **About 65 % of the
everyday forms correspond directly to the spelling; in around 35 % reductions take
effect.**" The figure describes "exclusively the relation of standard form to everyday
form — it has nothing to do with the history of the language."

The five phenomena named in §4.2:

| Phenomenon | Example (§4.2) |
|---|---|
| Unstressed **-a** at the end of a word becomes weak | *sarla* → [sarlə] |
| The plural marker **-ñ-** nasalizes the vowel before it | *sarlañan* → [sarlãan] |
| **xr-, xl-, xn-** at the beginning of a word: *x* becomes a breath | *xra* → [ʰra] |
| Frequent monosyllables lose their final consonant before a consonant | *xa melam* → [xamelam] |
| Identical vowels merge at the word boundary | *vanda aul* → [vandaul] |

**The standard pronunciation remains binding** — §4.2 closes: "The standard pronunciation
— slow, distinct, every syllable full — remains binding for teaching, dictionary and
ceremonial speech."

Two notes on the status of this table:

- It describes tendencies of spoken everyday language, not the spelling. A text is not
  written in everyday form.
- The five lines are **not an exhaustive list**. The grammar names no conditions, no
  frequencies per phenomenon and no interaction of the rules with one another. Where it is
  silent, nothing is supplied here.

---

## 6. No IPA assignment

Grammar 0.9.3 **fixes no IPA values**. What it actually contains:

- **§2.1:** descriptions in everyday language with comparisons — "as in German", "like
  *tsch*", "as in *Rose*", "as in French *jour*", "as in *señor*", "far back in the
  throat", "distinctly rolled".
- **§4.2:** five transcriptions in square brackets which show exclusively the
  **reduction phenomena** — [sarlə], [sarlãan], [ʰra], [xamelam], [vandaul]. They use
  IPA-like signs (ə, nasalization, superscript h), but are not a systematic transcription
  and cover only these five cases.
- **§26.2:** a division of the signs into script families (NER, TAL, SOR, VEL, MOR, ISH,
  KAI, RUUN). That is script systematics, not phonetics — Manus and grammar are to be kept
  apart.

**Not documented and not supplied here:**

| Open question | What the grammar says about it |
|---|---|
| IPA value of **x** | only "far back in the throat" (§2.1) — whether velar or uvular, voiceless or otherwise, is not fixed |
| IPA value of **r** | only "distinctly rolled" (§2.1) — whether tip of the tongue or uvula is not fixed |
| IPA value of **ç** | only "like *tsch*" (§2.1); carried in the inventory as an **affricate** |
| IPA value of **ñ** | only "as in *señor*" (§2.1) |
| Exact vowel qualities of **a e i o u** | only "pure and clear" (§2.2) |
| Vowel length | not regulated; §4.1 only excludes length signs and doubling |
| Syllable weight / quantity | not regulated |

The audit assigns **no finding ID of its own** for this gap; it is recorded here as an
observation. To supply an IPA table would be a language decision and is reserved to the
language designers.

---

## 7. Stress (§23)

### 7.1 Basic rule

> Normally on the **penultimate syllable**.

Examples from §23: **VAL**-ru · **SAR**-la · mil-**NE**-ñeş · me-**LA**-men.

The examples show that the rule operates on the **fully inflected** form and that the
stress moves with the endings: *milne* (eye, §24.4) → *milneñeş* (dat. pl., §9) carries
the accent on *-NE-*; *melamen* (we go, root *mel-* with tense vowel *-a-* and person
ending *-men*, §15.1) carries it on *-LA-*. The stress rule thus takes effect after the
morphology, not on the bare stem.

### 7.2 The four exception groups

| Exception group | Rule (§23) | Example (§23) |
|---|---|---|
| Abstract nouns in **-uma**, tool nouns in **-isto** | stress remains on the **stem** | **MEL**-uma, **TAL**-isto |
| The **15 old core words** (§24.1) | stress on the **last** syllable | *kaUN, breUN, taIV* |
| **Compounds** (§21.3) | stress on the **first member** | **LUIV**-resto |
| Words with a **prefix** (§21.2) | prefix **unstressed** | şu-**NAR**-gat |

Further affected words which follow from the vocabulary:

- **-uma** (§24.6, §21.1): *soruma, klaunuma, nestuma, salvuma, vaşnuma, mirnuma,
  şauluma, tarnuma, saivuma, virnuma* as well as *taluma* (speech) and *meluma* (journey)
  — stem stress. Not affected are words which happen to end in *-ma* without carrying the
  suffix (*şonma* voice, *klerma* freedom, §24.3); for them the basic rule applies.
- **-isto** (§21.1, §24.4): *melisto* (vehicle), *talisto* (instrument) — stem stress.
  *vresto* (book) does end in *-sto*, but does not carry the suffix *-isto* and therefore
  falls under the basic rule.
- **Compounds** (§21.3): *taivbreun* school, *aulmelna* canal, *luivresto* calendar —
  stress on the first member.
- **Prefixes** (§21.2): *şu-* (passive), *xa-* (opposite), *re-* (again), *dra-* (whole),
  *su-* (half) — unstressed; attestations *şunargat, xaselvra, revandat, dramilkat,
  suluidra*.

### 7.3 Predictability

§23 closes with: "**Approx. 85 % predictable.**" §4.1 names the same figure. The grammar
does not say which 15 % are not predictable, and names no procedure for determining the
stress of such words. This gap is not closed here.

### 7.4 Stress and syllable division (L-09)

The stress rule counts syllables, and a **syllable-division rule does not exist** (rule
gap **L-09**, see `PHONOTACTICS.md` §7). For the stress this is, according to
`Orbis-Audit-0_1.md` §2.4, **without consequences**: whether *mela* is divided as *me·la*
or *mel·a* changes nothing about the number of syllables and hence nothing about the
penultimate syllable. L-09 becomes effective only in Orbis Manus (§26) and in keyboard
input (§26.8).

### 7.5 Observations without a finding ID

Two points this documentation records without deciding them:

1. **Core words in inflected forms.** The three attestations in §23 (*kaUN, breUN, taIV*)
   are monosyllabic nominative forms; there "last syllable" and every other rule coincide.
   Only in inflected forms (*kaunei, kauneiş, eirdes*, §10.3) does the exception differ
   from the basic rule. For such forms §23 gives no example. What applies is not decided.
2. **Co-occurrence of several exceptions.** §23 regulates each group for itself, but not
   which rule wins when two apply — for instance with a prefix before an *-uma* abstract
   noun, or with a compound having a core word as its first member (*taivbreun*: the
   compound rule and the core-word rule both apply). The grammar names no attestations for
   such cases.

Both points are observations on the wording of the rule, not findings of the audit, and
are here neither filled in nor interpreted.

---

## 8. Cross-references

| Topic | Location |
|---|---|
| Sound inventory and sound groups | `PHONOLOGY.md` (§2, §3) |
| Syllable shapes, onset and coda clusters, L-09 | `PHONOTACTICS.md` (Abschnitt 5 dieser Datei) |
| Sound laws (level C) and word derivation | `PROTO_ORBIS.md` (§22, §4.3) |
| Script signs, Manus syllable formula | Grammar §26 |
| Finding IDs and rule basis | `Orbis-Audit-0_1.md` |
| Machine-readable version of the stress rule | `language/phonology/stress.json` |

---

*Source of all rule statements: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Where this
documentation and the grammar diverge, the grammar prevails. Where this English version
and the German version diverge, the German version prevails (TRANSLATION_POLICY.md, section 1).*
