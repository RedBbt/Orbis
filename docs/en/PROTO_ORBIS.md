# Orbis — Proto-Orbis and Sound History

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md). Describes Orbis Grammar 0.9.3.*

---

## 1. Subject

This chapter describes §22 of the grammar: the seven historical sound laws, their
attestations and the working instruction for new words derived from them. Added to this
are the status classification of etymologies in the data model of this repository and a
sober statement of how many lexemes have a derivation documented at all.

**Proto-Orbis is not a text corpus and not a speakable language.** In 0.9.3 it exists
exclusively as a set of reconstructed precursor forms of individual words, notated
throughout in the grammar with an asterisk (\*kau-nu, \*tal-iv, \*vir-na). A proto-grammar,
a proto-lexicon or a proto-phonology does not exist and is not supplied here.

---

## 2. Level C — purely diachronic (§4.3)

§4.3 classifies the sound laws unambiguously:

> "The seven sound laws in §22 explain **how the present-day word forms arose out of
> Proto-Orbis**. They are language history, **not pronunciation notes and not spelling
> deviations**. A speaker of present-day Orbis does not apply them — he speaks *taiv*,
> not \*tal-iv."

§22 repeats this in its first sentence: "These laws are **language history** (§4.3), not
modern pronunciation notes."

From this three delimitations follow:

| Not to be confused with | Location | Difference |
|---|---|---|
| Level A, standard orthography | §4.1 | Level A is the spelling in force; the sound laws do not generate it anew |
| Level B, colloquial pronunciation | §4.2 | Level B describes present-day reductions (*sarla* → [sarlə]); with language history it has "nothing to do" (§4.2) |
| Synchronic rules | §3.3, §5 | For checking the validity of a word the sound laws are **without effect**; what is checked is the modern form against §3.3 |

For tools this means: the sound laws must not be applied in any synchronic check
(`language/proto/sound_laws.json`: "Purely diachronic (§4.3). Without effect for
synchronic checks.").

Level C has practical use, according to §4.3, at one point only: "Its practical use is
word formation: whoever coins a new word can derive it via Proto-Orbis and thereby obtains
a credible form." See §4 of this chapter.

---

## 3. The seven sound laws (§22)

All examples are taken verbatim from §22 or §10; \* marks the reconstructed precursor
form.

### Law 1 — Loss of the final vowel

The final vowel of the proto-form drops.

| Proto-form | Modern | Meaning | Place of occurrence |
|---|---|---|---|
| \*kau-nu | **kaun** | human being | §22, §10.2 |
| \*vir-na | **virn** | life | §22, §10.2 |
| \*mok-sa | **moks** | death | §22, §10.2 |
| \*velkra-na | **velkran** | friendship | §10.1 |
| \*soral-mu | **soralm** | monument | §10.1 |

This law explains at the same time why the words concerned carry their gender on the
**penultimate** consonant: in *velkran* the *-n-* is the class consonant (neuter), in
*soralm* the *-m-* (feminine), §10.1.

### Law 2 — Diphthongization through vowel loss

When an internal vowel drops out, the remaining vowels merge into a diphthong.

| Proto-form | Modern | Meaning | Place of occurrence |
|---|---|---|---|
| \*tal-iv | **taiv** | language | §22, §10.2, §21.1 |
| \*luv-iv | **luiv** | sun | §22, §10.2 |
| \*veş-iv | **veiş** | mother | §22, §10.2 |

§21.1 records expressly that *taiv* belongs to the word family of *tal-* (to speak) —
the etymology here establishes a connection of meaning which can no longer be seen in the
modern form.

### Law 3 — Softening

> "Voiceless stops between vowels become voiced: **k → g, t → d, p → b**."

§22 names **no example word** for this law. An attestation is thus missing in the grammar;
this documentation supplies none.

### Law 4 — Assimilation

> "*n* assimilates to the following consonant: **n+p → mp, n+k → ñk**."

Here too §22 names **no example word**. To be noted: the rule describes a historical
process, not the synchronic juncture rule §21.4 (there two **identical** consonants merge
at the morpheme juncture, e.g. *mel + la* → *mela*). The two must not be conflated.

### Law 5 — Loss before a nasal

> "*k* drops out before *n*."

| Proto-form | Modern | Meaning | Place of occurrence |
|---|---|---|---|
| \*milk-ne | **milne** | eye, to the root \*milk- | §22 |

The attestation connects the noun *milne* (eye, N-A, §24.4) with the verb stem *milk-*
(to see, §24.5) — the same root, surface forms separated by the law.

### Law 6 — Ablaut in frequent verbs

> "\*mel- → **molet** instead of \*melot."

This law explains the eight irregular verbs from §15.2 which "preserve an older vowel
grade in the past": *est/vot*, *nut/novet*, *vurt/voret*, *melat/molet*,
*vandat/vendet*, *nargat/norget*, *zavat/zovet*, *dalvat/dolvet*. Attestation in the
running text: *"Vra melru molet dral xrañan trelmrañan zaldreñen."* (§25.2).

### Law 7 — Reduction of frequent words

High-frequency function words are shortened.

| Proto-form | Modern | Meaning | Place of occurrence |
|---|---|---|---|
| \*xa-ra | **xra** | definite article M nom sg (§11.1) | §22 |
| \*vima | **vim** | I (§13.1) | §22 |
| \*şeta | **şet** | you (§13.1) | §22 |

The selection is telling: all three attestations are function words, not content words.
This agrees with guideline 5 (§3.4), according to which monosyllables are "mostly function
words or core words".

### Overview

| No. | Name | Attestations in §22 |
|---|---|---|
| 1 | Loss of the final vowel | 3 (+2 in §10.1) |
| 2 | Diphthongization through vowel loss | 3 |
| 3 | Softening | **none** |
| 4 | Assimilation | **none** |
| 5 | Loss before a nasal | 1 |
| 6 | Ablaut in frequent verbs | 1 (effective for the 8 verbs from §15.2) |
| 7 | Reduction of frequent words | 3 |

That laws 3 and 4 are unattested is an observation about the grammar; the audit assigns
**no finding ID** for it, and this documentation invents no attestations.

---

## 4. Working instruction for new words (§22)

§22 closes with a rule for word formation:

> "**Rule for new words:** first form it regularly in Proto-Orbis, then apply laws 1–7,
> then check against §3.3 and align with §3.4."

As a sequence:

| Step | Action | Standard | Status |
|---|---|---|---|
| **1** | Form the proto-form regularly | §22 | tool — produces a credible form (§4.3) |
| **2** | Apply sound laws 1–7 | §22 | tool |
| **3** | Check the result against the hard language rules | **§3.3** — phoneme inventory (§2), syllable shapes (§5.1), onset clusters (§5.2), coda clusters (§5.3) | **binding** — here the decision about validity falls |
| **4** | Align the result with the sound guidelines | **§3.4**, lexical stem only (§3.5) | descriptive — no word becomes invalid through deviation |

Important for the order: step 3 is the **sieve**, step 4 the **file**. §3.3 says:
"Everything else is sound, not law." §3.4 says: "A word does **not become invalid**
because it deviates from them." A proto-derivation therefore justifies no form that
violates §3.3 — the derivation is a justification, not a licence.

Two caveats for step 3:

- The list of syllable shapes §5.1 is incomplete (**[REGELKONFLIKT K-01]**, rule conflict).
  Whoever produces a word of the shape VK, VKK or KKVKK by following this instruction meets
  the conflict and must report it as K-01, not resolve it himself. See `PHONOTACTICS.md` §3.
- The diphthong *ou* is **[NOCH ZU ENTSCHEIDEN]** (to be decided) (§2.3, §30) and must not
  appear in a new form; *oi*, by contrast, is regular and expressly open for new words
  (§2.3). See `PHONOLOGY.md` §4.

**This documentation forms no new words.** The vocabulary is frozen as of 0.9.3 (§24):
"A word is changed only if it violates the phonotactics, is grammatically inconsistent,
collides problematically with another word or carries a contradictory meaning. Matters of
taste are no longer sufficient." New words arise only on commission by the language
designers.

---

## 5. Status values for etymologies

The data model of the repository (`language/lexicon/lexicon.schema.json`, field
`etymologie`) knows four status values. **They do not stand in the grammar** — they are a
bookkeeping convention of this repository which implements §4.3 and discloses how well a
derivation is attested. They change no language rule.

| Status | Meaning | Example |
|---|---|---|
| **documented** | The grammar names the proto-form expressly | *kaun* < \*kau-nu (§10.2, §22) |
| **reconstructed** | Proto-form derived from the laws of §22, but not recorded in the grammar | — |
| **provisional** | Provisional derivation, not yet confirmed | — |
| **unknown** | No derivation known; the default when there is no attestation | all entries currently recorded, see §6 |

The schema records the basic rule itself: **"Do not invent an etymology. Without
attestation status=unknown."** A plausible derivation is not yet an attestation. Whoever
upgrades an etymology from `unknown` needs either a place of occurrence in the grammar
(→ `documented`) or a traceable derivation via laws 1–7 (→ `reconstructed`), which remains
marked as such.

---

## 6. For most lexemes no derivation is documented

The grammar names proto-forms at three places only:

| Place | Extent | Words |
|---|---|---|
| §10.1 (10-percent group) | 3 | *velkran* < \*velkra-na · *soralm* < \*soral-mu · *prilm* < \*prila-mu |
| §10.2 (15 core words) | 15 | *kaun* < \*kau-nu · *veiş* < \*veş-iv · *draun* < \*drau-nu · *şirn* < \*şir-ni · *aul* < \*au-lu · *xerp* < \*xer-pa · *luiv* < \*luv-iv · *grein* < \*gre-ina · *nauş* < \*nau-şa · *virn* < \*vir-na · *moks* < \*mok-sa · *eird* < \*e-irda · *şaul* < \*şa-ulo · *taiv* < \*tal-iv · *breun* < \*breu-na |
| §22 (attestations for the laws) | 5 additional | *milne* < \*milk-ne · *xra* < \*xa-ra · *vim* < \*vima · *şet* < \*şeta · *molet* < ablaut to \*mel- |

That amounts to **23 lexemes** with an expressly recorded precursor form. Against this
stand **281 recorded base forms** in `language/lexicon/entries/`; in the machine-readable
lexicon **every** one of these 281 entries currently carries
`etymologie.status = "unknown"` (state of this version, verifiable in the entries
themselves).

For the great majority of the vocabulary the following therefore holds: **no derivation is
documented.** That is not an error and not a finding of the audit, but simply the state of
0.9.3. Two consequences:

1. **Do not compute backwards.** To derive a proto-form from a modern form and enter it as
   an etymology would be an invention. Without attestation the status remains `unknown`.
2. **Word families are not the same as etymology.** §21.1 documents productive word
   families (*mel-* → *melex, melru, mela, melna, melisto, melvi, meluma*; *tal-* →
   *talex, talru, tala, talna, talisto, talvi, taluma*). These are **synchronic**
   derivations according to §21, not sound history. Only where §21.1 speaks expressly
   historically — *taiv* as \*tal-iv, *melva* (street) as an "old offshoot of *mel-*" —
   does it touch level C; for *melva*, however, the grammar names **no** proto-form.

---

## 7. Outlook: dialects (§31)

§31 records that future dialects will "later be derived exclusively from Standard Orbis",
"through further sound laws on the pattern of §22: a harder, a softer-melodic and a
conservative dialect". These sound laws do **not yet exist**; §31 says expressly "Not yet
developed". This documentation too describes exclusively Standard Orbis (§1).

---

## 8. Cross-references

| Topic | Location |
|---|---|
| Sound inventory, §3.3 as against §3.4/§3.5 | `PHONOLOGY.md` (§2, §3) |
| Syllable shapes, onset/coda clusters, K-01 | `PHONOTACTICS.md`, Abschnitt 5 |
| Levels A and B, stress, missing IPA assignment | `PRONUNCIATION.md` (§4, §23) |
| Word formation, prefixes, juncture rule (synchronic) | Grammar §21 |
| Irregular verbs (law 6) | Grammar §15.2 |
| Data model and status values | `language/lexicon/lexicon.schema.json`, `language/proto/sound_laws.json` |
| Finding IDs and rule basis | `Orbis-Audit-0_1.md` |

---

*Source of all rule statements: `Orbis-Grammatik-0.9.3.md` (READ ONLY). Where this
documentation and the grammar diverge, the grammar prevails. Where this English version
and the German version diverge, the German version prevails (TRANSLATION_POLICY.md, section 1).*
