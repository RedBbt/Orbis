# ORBIS — Word Formation

*Derived from the German documentation, which is authoritative (see TRANSLATION_POLICY.md).
Describes Orbis Grammar 0.9.3; the reference grammar itself is Orbis-Grammatik-0.9.3.md.*

---

## 1. Three procedures

§21 knows three ways of forming new words from existing material:

| Procedure | Place | Section |
|---|---|---|
| **Derivation with a suffix** — word family around a root | §21.1 | 2 |
| **Derivation with a prefix** | §21.2 | 3 |
| **Compounding** | §21.3 | 4 |

Above all three stands the **junction rule** (§21.4, section 5), which regulates what
happens at the seam of two morphemes.

**Important restriction.** The vocabulary is frozen as of 0.9.3 (§24). §21 describes how
words **are** built; the fact that a pattern is productive does not make a self-formed
form a word of the lexicon. New lexemes arise only through a decision of the language
designers (ORBIS_CONSTITUTION Art. 5, Art. 16). All forms in this chapter are attested —
from §21, §24 or the test corpus.

---

## 2. Word families and their suffixes (§21.1)

A root plus a suffix yields a word with a fixed function **and** a fixed inflectional
class. The suffix determines both: the semantic role and the class according to §7.

| Function | Suffix | Class |
|---|---|---|
| Verb (infinitive) | **-ex** | infinitive (§14) |
| Person, male | **-ru** | M-A |
| Person, female | **-la** | F-A |
| Place | **-na** | N-A |
| Tool | **-isto** | N-C |
| Property | **-vi** | adjective base form |
| Abstract noun | **-uma** | F-C |

### 2.1 The two attested families

§21.1 demonstrates the procedure in full on exactly two roots. Both are set side by side
here; the rows are the seven suffixes of the table above.

| Suffix | Root *mel-* (to go) | Root *tal-* (to speak) |
|---|---|---|
| **-ex** | **melex** — to go | **talex** — to speak |
| **-ru** | **melru** — wanderer (M-A) | **talru** — speaker (M-A) |
| **-la** | **mela** — wanderer, f. (F-A) | **tala** — speaker, f. (F-A) |
| **-na** | **melna** — way (N-A) | **talna** — meeting place (N-A) |
| **-isto** | **melisto** — vehicle (N-C) | **talisto** — instrument (N-C) |
| **-vi** | **melvi** — eager to travel | **talvi** — talkative |
| **-uma** | **meluma** — journey (F-C) | **taluma** — speech (F-C) |

Both *-la* rows show the junction rule in miniature: *mel + la* → **mela**, *tal + la* →
**tala** (§21.4). The forms are therefore not \**mella*, \**talla*.

§21.1 names two further members of the families which do not follow the regular pattern
but arose through sound history:

| Word | Meaning | Derivation according to §21.1 / §22 |
|---|---|---|
| **taiv** | language (core word, f.) | \*tal-iv, diphthongization through vowel loss (§22, law 2) |
| **melva** | street (F-B) | "old offshoot of *mel-*" (§21.1) — without any statement of a sound law |

These two show that a word family can have more members than the suffix grid yields.
§21.1 gives no formation pattern for such old forms — they are stock, not tool.

### 2.2 The suffix -uma beyond the two model families

**-uma** is the only suffix for which §24.6 shows a larger attested stock. The column
"origin" there shows that -uma does not attach to verb roots only:

| Word | Meaning | Base | Word class of the base |
|---|---|---|---|
| **soruma** | memory | *sor-* to preserve | verb root |
| **nestuma** | will | *nest-* to want | modal root |
| **salvuma** | loss | *salv-* to lose | verb root |
| **vaşnuma** | transience | *vaşn-* to pass away | verb root |
| **mirnuma** | decision | *mirn-* to decide | verb root |
| **tarnuma** | consequence, result | *tarn-* to follow | verb root |
| **saivuma** | love | *saiv-* to love | verb root |
| **meluma** | journey | *mel-* to go | verb root |
| **taluma** | speech | *tal-* to speak | verb root |
| **klaunuma** | truth | *klaun* true | adjective (§24.7) |
| **şauluma** | identity | *şaul* name | noun (core word) |
| **virnuma** | being, existence | *virn* life | noun (core word) |

All these words are F-C (class consonant *m*, theme vowel *a*) and decline regularly
according to §8: *soruma, soruman, sorumaş, sorumas*. Attestation in a sentence: *Xla
soruma xlas nauşes vran tolm vaşnat* (§25.1).

Noteworthy about *şauluma* and *virnuma*: the base is a **core word** with irregular
declension (§10.3), yet the derivation is regular. This is attested stock, not a
formulated rule — §21.1 says nothing about the word class of the base.

### 2.3 Stress of the derivations (§23)

| Case | Rule | Example §23 |
|---|---|---|
| Normal case | penultimate syllable | *VAL-ru, SAR-la* |
| Words in **-uma** and **-isto** | stress stays on the **stem** | **MEL**-uma, **TAL**-isto |
| Words with a prefix | prefix **unstressed** | şu-**NAR**-gat |
| Compounds | first member | **LUIV**-resto |

The two suffixes -uma and -isto therefore behave differently in terms of stress from the
other five. §23 gives the predictability of the stress rule as about 85 %.

### 2.4 A related means of formation: nominalization (§12.5)

§12.5 uses the same person suffixes on a different base — on the **adjective** instead of
on the root — and adds a third one for things:

| Meaning | Suffix | Class | Example §12.5 |
|---|---|---|---|
| male person | **-ru** | M-A | *vlaidru* — the big one (m.) |
| female person | **-la** | F-A | *vlaidla* — the big one (f.) |
| thing or notion | **-te** | N-C | *vlaidte* — the big thing |

With the participle, *-ut* merges with *-te* into **-ute**: *traivut* → **traivute** "that
which has been found" (§12.5), attested in the short text: *Kilna est xna traivute.*
(§25.2).

---

## 3. Prefixes (§21.2)

Five prefixes, each with exactly one attested example:

| Prefix | Meaning | Example §21.2 | Analysis |
|---|---|---|---|
| **şu-** | passive | *şunargat* | şu- + *narg-* (to make) + -a- + -t (3rd sg. pres.) |
| **xa-** | opposite, absence | *xaselvra* | xa- + *selv* (good) + -ra (attributive M, §12.1) |
| **re-** | again | *revandat* | re- + *vand-* (to come) + -a- + -t |
| **dra-** | wholly, through | *dramilkat* | dra- + *milk-* (to see) + -a- + -t |
| **su-** | half | *suluidra* | su- + *luid* (bright) + -ra |

The examples of the grammar stand in **inflected form**, not as dictionary forms. They
thereby also show that the prefix stands **before** the entire inflected word and leaves
both conjugation and declension untouched.

### 3.1 şu- and the passive (§16.3)

*şu-* is the only prefix with a grammatical function of its own outside §21:

| Form | Attestation | Translation |
|---|---|---|
| Dynamic passive | *Xna breun şunargat.* (§16.3; test corpus 136) | The house is being built. |
| Statal passive | *Xna breun şunargut est.* (§16.3) | The house is built. |

> **[REGELLÜCKE L-05] (rule gap) — adjacent.** §16.3 regulates only the prefix. How the
> **agent** is expressed ("built by the man") is not laid down; no preposition from §19 is
> designated for it. Test corpus 137 and 138 fail on this. That is a finding of the
> modality/passive rule, not of word formation — mentioned here only because it hangs on
> *şu-*.

### 3.2 Distinctions

| Pair | Relationship | Source |
|---|---|---|
| **dra-** (prefix) ↔ **dral** (preposition "through") | expressly **separate categories**; *dral* is only a preposition, *dra-* only a prefix | §19 |
| **xa-** (prefix) ↔ **xa** (negation particle "not") | identical in form, but a different category; registered as collision **W-03** | §18.3, §21.2 |

The prefix *xa-* is visible beyond §21.2 in words of the fixed stock: *xakaun* (nobody),
*xakelte* (nothing) in §13.4, *xanur* (never) in §24.9. These words are lexicon entries,
not ad hoc formed forms.

---

## 4. Compounds (§21.3)

> **Modifier in front, head word behind. Gender and class follow the last member.**

The head stands on the right. The left member does not change its form and is not
inflected; only the head is declined.

| Compound | Analysis | Head | Gender/class | Meaning |
|---|---|---|---|---|
| **taivbreun** | *taiv* + *breun* | breun (core word, n.) | n. — class see U-08 | school |
| **aulmelna** | *aul* + *melna* | melna (N-A) | n., N-A | canal |
| **luivresto** | *luiv* + *vresto* | vresto (N-C) | n., N-C | calendar |

*luivresto* additionally shows the junction rule: *luiv + vresto* → **luivresto**, not
\**luivvresto* (§21.4).

The stress lies on the first member: **LUIV**-resto (§23).

### 4.1 [REGELUNKLARHEIT U-08] (rule ambiguity) — compounds with a core word as head

> **[REGELUNKLARHEIT U-08] How does a compound with a core-word head decline?**
> §21.3 says "gender and class" follow the last member. The 15 core words (§10.2–§10.3),
> however, **have** no class in the sense of §7 — they decline with the linking vowel
> *-e-* and form the plural in *-ei*. Whether *taivbreun* (head: *breun*) therefore
> declines like a core word (\**taivbreunen, taivbreunei*) or regularly, §21.3 does not
> say.

*aulmelna* and *luivresto* are not affected by this: their heads *melna* and *vresto* are
regular nouns with a class and a theme vowel.

---

## 5. The junction rule (§21.4)

> **Where two identical consonants meet at a morpheme junction, they merge into one.**
> This applies to **compounds, derivations and endings equally.**

| Junction | Result | Field |
|---|---|---|
| *luiv + vresto* | **luivresto** | compounding |
| *mel + la* | **mela** | derivation (suffix -la) |
| *tal + la* | **tala** | derivation (suffix -la) |
| *şaln + na* | **şalna** | ending (adjective attributive, §12.1) |
| *selv + vi* | **selvi** | comparison/property (§12.3, §21.1) |

The rule is narrowly framed: it applies **only to identical consonants**. Different
consonants at the junction are retained, provided §5.2 and §5.3 permit them (§21.4). The
rule does not mention vowels.

### 5.1 [REGELKONFLIKT K-02] (rule conflict) — killa, dolla, kella

> **[REGELKONFLIKT K-02] Attested pronoun forms contradict the junction rule.**
> §13.4 gives **killa** (this one, f.) and **dolla** (that one, f.), §18.2 gives **kella /
> kellan** (which) — each with an unmerged *l+l* junction. According to §21.4, which
> expressly applies to endings as well, the forms would have to be *kila*, *dola*, *kela*.
> Either the pronouns are exceptions — which is stated nowhere — or the forms are wrong.

The conflict is also attested in a sentence: *Kellan sarlan milkoş?* ("Which woman did you
see?", §18.2). The masculine and neuter forms (*kilra, kilna, dolra, dolna, kelra, kelna*)
are not affected. Treated in detail in `PRONOUNS.md` §5.6.

### 5.2 [REGELKONFLIKT K-03] (rule conflict) — telnxelmmern

> **[REGELKONFLIKT K-03] The number 35 contradicts the junction rule.**
> §24.8 notes 35 as **telnxelmmern** — compounded from *teln* (3), *xelm* (10) and *mern*
> (5), with a double *m* at the junction *xelm + mern*. According to §21.4 the form would
> have to be *telnxelmern*.

The remaining attested numeral compounds are unremarkable, because no identical consonants
meet at their junctions: *xelmnel* (11, *xelm + nel*), *dramxelm* (20, *dram + xelm*).

K-02 and K-03 are the same type of conflict: **an attested word against a generally
formulated rule.** Since the vocabulary is frozen (§24) and the grammar is READ ONLY, both
remain open; the decision is made by the language designers, not by interpretation
(ORBIS_CONSTITUTION Art. 16, Art. 17).

In the machine-readable lexicon the affected entries are marked: *killa*, *dolla* and
*kella* carry `K-02`, *telnxelmmern* carries `K-03` in the field
`qualitaet.offene_befunde`.

---

## 6. New words do not arise here (§22)

For the case that the language designers decide on a new word, §22 describes the path via
Proto-Orbis: posit a proto-form → apply the sound laws → check against §3.3 (binding sound
rules) → compare with §3.4 (sound guidelines). The seven sound laws (§22) are expressly
**language history** (§4.3), not pronunciation notes and not a word-formation procedure of
the present-day language.

For tools and documentation the following holds: word-formation patterns are described,
not applied. The only vocabulary gap registered in the stock — **W-01** ("to say", "to
show", "to search", the existential construction "there is") — remains open and is not
closed by self-formed derivations.

---

## 7. Overview of findings for this chapter

| ID | Type | Concerns | Short |
|---|---|---|---|
| **K-02** | REGELKONFLIKT | §13.4, §18.2 ↔ §21.4 | *killa/dolla/kella* with an unmerged l+l junction |
| **K-03** | REGELKONFLIKT | §24.8 ↔ §21.4 | *telnxelmmern* with an m+m junction |
| **U-08** | REGELUNKLARHEIT | §21.3 | declension of compounds with a core-word head (*taivbreun*) |
| **L-05** | REGELLÜCKE | §16.3 | agent in the passive (adjacent to the prefix *şu-*) |
| **W-01** | WORTSCHATZLÜCKE | §24 | "to say", "to show", "to search", "there is" are missing |
| **W-03** | WORTSCHATZKOLLISION | §18.3, §21.2 | *xa* (particle) ↔ *xa-* (prefix) |

The suffix and prefix lists themselves (§21.1, §21.2) are carried in the audit **without a
finding**; the conflicts lie at the junctions and with individual attested words.
