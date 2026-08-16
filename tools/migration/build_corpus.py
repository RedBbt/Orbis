#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_corpus.py — Migration Phase 7: Testkorpus in die Datenbasis ueberfuehren.

Liest Orbis-Testkorpus-0_1.md (kanonisch) und Orbis-Testdaten.json und erzeugt
language/corpus/tests/testkorpus-0_1.json nach sentence.schema.json.

GRENZEN:
- Die Orbis-Formen werden UNVERAENDERT uebernommen.
- Deutsch bleibt die semantische Quelle.
- Englisch wird aus dem Deutschen abgeleitet (TRANSLATION_POLICY).
- Saetze, die nach 0.9.3 nicht eindeutig bildbar sind, erhalten orbis=null,
  Status open/conflict/unclear/testproblem und KEINE kanonische Uebersetzung
  ihres nicht existierenden Orbis-Satzes (die englische Zeile uebersetzt dann
  nur die deutsche Vorgabe des Tests).
"""

import json, os, re, sys, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "language", "corpus", "tests", "testkorpus-0_1.json")

# Englische Entsprechungen der 150 deutschen Testsaetze.
# Abgeleitet aus der deutschen Quelle; Bedeutungsumfang unveraendert.
EN = {
1:"The man goes.",2:"The woman speaks.",3:"The child sleeps.",4:"The dog runs.",
5:"I come.",6:"You wait.",7:"We stay.",8:"You (pl.) read.",9:"They write.",
10:"The wind comes.",11:"The speaker speaks.",12:"The water remains.",13:"The bird sees.",
14:"The night comes.",15:"The human being thinks.",16:"The mother waits.",17:"The book remains.",
18:"The friend eats.",19:"The wanderer (f.) goes.",20:"The father hears.",
21:"I see the dog.",22:"You see yourself.",23:"The mother gives the child the bread.",
24:"We write a word.",25:"The woman gives the father the water.",
26:"I give the friend the book.",27:"I drink the water.",28:"I know the name.",
29:"She loves the language.",30:"We see the sun.",31:"I wait on the street.",
32:"I see myself.",33:"He sees himself.",34:"I give myself time.",35:"She speaks about herself.",
36:"The house of the man is old.",37:"The memory of time passes away.",
38:"The name of the woman is beautiful.",39:"The book of my friend is new.",
40:"The flame of the fire is warm.",41:"The way of life is long.",
42:"The day of death comes.",43:"The water of the earth is cold.",
44:"The voice of the human being is strong.",45:"The language of the world does not pass away.",
46:"The big mountain is old.",47:"I see the small bird.",48:"The beautiful woman speaks.",
49:"We walk on the long street.",50:"The dark water is cold.",51:"The found book is old.",
52:"I read a new book.",53:"The cold night is long.",54:"He is bigger than I am.",
55:"She is the most beautiful woman.",56:"She is as warm as the sun.",
57:"The man becomes strong.",58:"We wait in the dark city.",59:"She goes quickly.",
60:"The memory passes away slowly.",
61:"The men go.",62:"I see the dogs.",63:"The women speak.",
64:"We give the children the bread.",65:"The stones are cold.",66:"The mothers wait.",
67:"I read the books.",68:"The human beings remain.",69:"We hear the languages.",
70:"Two men come.",
71:"Are you going today?",72:"Is the father coming?",73:"Who speaks?",74:"Whom do you see?",
75:"To whom do you give the book?",76:"Whose book are you reading?",77:"Where are you (pl.) waiting?",
78:"How is the night?",79:"Which book are you reading?",80:"To which child do you give the bread?",
81:"I do not go.",82:"He does not come.",83:"We have no house.",84:"She does not see the dog.",
85:"The child does not sleep.",86:"No man waits.",87:"I do not know it.",88:"Nobody comes.",
89:"We do not go into the city.",90:"I know that he does not come.",
91:"I know that you are coming.",92:"He waits because the night is cold.",
93:"If you go, I stay.",94:"Although the book is old, I read it.",
95:"While we wait, the man speaks.",96:"Before the sun comes, we go.",
97:"After he ate, he slept.",98:"I do not know where the book is.",
99:"I wait, for the night is cold.",100:"The man who is coming is my friend.",
101:"The woman whom I see speaks.",102:"The man to whom I give the book waits.",
103:"I know that the man must go into the city tomorrow.",104:"She says that she is coming.",
105:"He knows that she cannot read the book.",
106:"I can go.",107:"You must come today.",108:"He may read the book.",109:"We shall wait.",
110:"She wants to sleep.",111:"I like the word.",112:"You (pl.) can see the mountain.",
113:"They must find the city.",114:"Can you hear me?",115:"The child may not go.",
116:"I went.",117:"You came.",118:"He saw the dog.",119:"We knew it.",
120:"They gave the child the bread.",121:"The night was cold.",122:"I had a house.",
123:"The man made the vehicle.",124:"You (pl.) waited.",125:"We became strong.",
126:"I will go.",127:"You will come.",128:"He will read the book.",129:"We will wait.",
130:"They will make the vehicle.",131:"The child will become strong.",
132:"Tomorrow I will write.",133:"You (pl.) will be strong.",134:"I will have a house.",
135:"She will know the truth.",
136:"The house is being built.",137:"The house is being built by the man.",
138:"The book was read by the woman.",139:"The word is spoken.",140:"The books are being read.",
141:"I would go.",142:"If I had a house, I would stay.",
143:"If the night were cold, we would wait.",144:"He would read the book.",145:"I could go.",
146:"I know that the man will give the child the bread tomorrow.",
147:"Although the night was cold, the wanderers went over the mountain.",
148:"If you read the book of the friend, you will find the truth.",
149:"The man who came yesterday gave the child the bread of the house.",
150:"We cannot sleep because the storm over the city is very strong.",
}

KATEGORIE = [
 (1,20,"einfache_hauptsaetze"),(21,35,"akkusativ_dativ"),(36,45,"genitiv"),
 (46,60,"adjektive"),(61,70,"plural"),(71,80,"fragen"),(81,90,"negation"),
 (91,105,"nebensaetze"),(106,115,"modalverben"),(116,125,"vergangenheit"),
 (126,135,"zukunft"),(136,140,"passiv"),(141,145,"mai_konditional"),(146,150,"komplex"),
]
STATUS = {"[OK]":"canonical","[REGELLÜCKE]":"open","[REGELKONFLIKT]":"conflict",
          "[REGELUNKLARHEIT]":"unclear","[TESTPROBLEM]":"testproblem"}

def kategorie(n):
    for lo, hi, k in KATEGORIE:
        if lo <= n <= hi: return k
    return None

def satzmuster(satz, v):
    """Abstraktes Satzmuster aus den erkannten Wortformen (nur beschreibend)."""
    teile = []
    for tok in v.tokenize(satz):
        arten = {k for k, _ in v.classify_token(tok)}
        if "ART" in arten: teile.append("DET")
        elif "VERB" in arten: teile.append("V")
        elif "NOMEN" in arten: teile.append("N")
        elif "PRON" in arten: teile.append("PRON")
        elif "ADJ" in arten or "W-ADJ" in arten: teile.append("ADJ")
        elif "PRÄP" in arten: teile.append("P")
        elif "SUBKONJ" in arten or "REL/SUB" in arten: teile.append("SUBJ-KONJ")
        elif "KONJ" in arten: teile.append("KONJ")
        elif "W" in arten: teile.append("W")
        elif "PART" in arten: teile.append("PART")
        elif "ZAHL" in arten: teile.append("NUM")
        else: teile.append("?")
    # DET (ADJ) N zu NP zusammenfassen
    out, i = [], 0
    while i < len(teile):
        if teile[i] == "DET":
            j = i + 1
            while j < len(teile) and teile[j] == "ADJ": j += 1
            if j < len(teile) and teile[j] == "N":
                out.append("NP"); i = j + 1; continue
        out.append(teile[i]); i += 1
    return "-".join(out)

def load_validator():
    spec = importlib.util.spec_from_file_location(
        "orbis_validator", os.path.join(ROOT, "orbis_validator.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def main():
    v = load_validator()
    md = open(os.path.join(ROOT, "Orbis-Testkorpus-0_1.md"), encoding="utf-8").read()
    daten = {t["test"]: t for t in json.load(
        open(os.path.join(ROOT, "Orbis-Testdaten.json"), encoding="utf-8"))["tests"]}
    lex_idx = json.load(open(os.path.join(ROOT, "language/lexicon/index.json"),
                             encoding="utf-8"))["eintraege"]

    # Lemma -> lexeme_id (erste Lesart; Homonyme werden nicht aufgeloest)
    lem2id = {}
    for e in lex_idx:
        lem2id.setdefault(e["lemma"], e["lexeme_id"])
    # Vollformen -> Lemma ueber die Erkenner des Validators
    def lexeme_ids(satz):
        ids, unresolved = [], []
        for tok in v.tokenize(satz):
            lemma = None
            if tok in v.NOUN_FORMS: lemma = v.NOUN_FORMS[tok][0][0]
            elif tok in v.VERB_FORMS: lemma = v.VERB_FORMS[tok][0][0]
            elif tok in lem2id: lemma = tok
            elif tok in v.ADJ_FORMS: lemma = v.ADJ_FORMS[tok][0][0]
            elif tok in v.ARTICLES or tok in v.PRONOUNS: lemma = tok
            if lemma and lemma in lem2id:
                lid = lem2id[lemma]
                if lid not in ids: ids.append(lid)
            else:
                unresolved.append(tok)
        return ids, unresolved

    bloecke = re.split(r"^## Test ", md, flags=re.M)[1:]
    saetze = []
    for b in bloecke:
        n = int(b.split("\n", 1)[0].strip())
        d = daten[n]
        feld = lambda name: (re.search(rf"^- {name}: (.+)$", b, re.M).group(1).strip()
                             if re.search(rf"^- {name}: (.+)$", b, re.M) else None)
        ergebnis = d["ergebnis"]
        status = STATUS[ergebnis]
        orbis = d["orbis"]
        analyse_satztyp = feld("Satztyp") or ""
        ids, unresolved = lexeme_ids(orbis) if orbis else ([], [])
        regeln = feld("verwendete Regeln") or ""
        regel_liste = [r.strip() for r in re.split(r"[,;]", regeln) if r.strip().startswith("§")]
        wortstellung = feld("Wortstellung") or ""
        v2 = None
        if orbis:
            v2 = True if "V2 ✓" in wortstellung else (
                 False if "V1" in wortstellung else None)
        s = {
            "id": f"ORB-SENT-{n:06d}",
            "legacy_nummer": n,
            "status": status,
            "orbis": orbis,
            "de": d["deutsch"],
            "en": EN[n],
            "en_status": "derived",
            "rollen": ["test"] + (["example"] if status == "canonical" else []),
            "kategorie": kategorie(n),
            "schwierigkeit": "unbestimmt",
            "themenbereich": None,
            "syntax": {
                "typ": analyse_satztyp.split(",")[0].strip() or "unbestimmt",
                "muster": satzmuster(orbis, v) if orbis else None,
                "v2": v2,
                "nebensatz": "Nebensatz" in analyse_satztyp or "nebensatz" in (kategorie(n) or ""),
                "verbklammer": "Klammer" in wortstellung or "Verbklammer" in analyse_satztyp,
                "wortstellung_regel": None,
                "satzglieder": None,
                "subjekt": feld("Subjekt"),
                "finites_verb": feld("Verb"),
                "objekte": [],
                "kasus": sorted(set(re.findall(r"\b(Nom|Akk|Dat|Gen)\b", feld("Kasus") or "")),
                                key=["Nom","Akk","Dat","Gen"].index),
                "tempus": feld("Tempus"),
                "person": feld("Person/Numerus"),
                "numerus": None,
            },
            "lexeme": ids,
            "regeln": regel_liste,
            "qualitaet": {
                "validatorstatus": "ok" if orbis else "nicht_pruefbar",
                "befunde": [d["befund_id"]] if d["befund_id"] else [],
                "ergebnis_testkorpus": ergebnis,
                "anmerkung": d.get("anmerkung"),
                "letzte_pruefung": "2026-08-16",
            },
        }
        if unresolved:
            s["qualitaet"]["anmerkung"] = ((s["qualitaet"]["anmerkung"] or "") +
                f" [Migration: nicht auf Lexeme aufgeloeste Formen: {', '.join(unresolved)}]").strip()
        saetze.append(s)

    assert len(saetze) == 150, len(saetze)
    stat = {}
    for s in saetze: stat[s["status"]] = stat.get(s["status"], 0) + 1
    payload = {
        "korpus_id": "testkorpus-0_1",
        "corpus_version": "0.1",
        "grammar_version": "0.9.3",
        "quelle": "Orbis-Testkorpus-0_1.md",
        "erzeugt_von": "tools/migration/build_corpus.py",
        "hinweis": "Orbis-Formen unveraendert uebernommen. Deutsch ist semantische Quelle, "
                   "Englisch daraus abgeleitet. Saetze ohne eindeutige Orbis-Form tragen "
                   "orbis=null und einen Befund.",
        "anzahl": len(saetze),
        "nach_status": stat,
        "stabilitaetsquote_prozent": round(stat.get("canonical", 0) / len(saetze) * 100, 1),
        "saetze": saetze,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2); f.write("\n")
    print(f"{len(saetze)} Saetze -> language/corpus/tests/testkorpus-0_1.json")
    print("  nach Status:", stat)
    print("  Quote:", payload["stabilitaetsquote_prozent"], "%")
    print("  mit englischer Uebersetzung:", sum(1 for s in saetze if s["en"]))
    return 0

if __name__ == "__main__":
    sys.exit(main())
