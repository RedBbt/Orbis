#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""orbis_validator.py — automatische Konsistenzprüfung für Orbis 0.9.3

Prüfbasis: Orbis-Grammatik-0.9.3.md (READ ONLY — dieses Skript ändert nichts
an der Sprache). Alle Regeldaten sind 1:1 aus der Grammatik übernommen;
nichts wurde ergänzt. Wo die Grammatik schweigt, prüft das Skript nicht,
sondern meldet.

Das Skript ist ein HILFSMITTEL. Prüfungen, die semantische oder syntaktische
Interpretation verlangen, werden als MANUELLE_PRÜFUNG gekennzeichnet und
nicht algorithmisch entschieden.

Aufrufe:
  python3 orbis_validator.py --lexicon      Wortschatz prüfen (§24)
  python3 orbis_validator.py --examples     Beispielsätze der Grammatik prüfen
  python3 orbis_validator.py --corpus DATEI "Orbis:"-Zeilen einer Korpusdatei prüfen
  python3 orbis_validator.py --tables       45-Endungen-Tabelle + Verbparadigmen
  python3 orbis_validator.py --manus        Manus-Silbenzerlegung des Wortschatzes
  python3 orbis_validator.py --json DATEI   Testkorpus als JSON exportieren
  python3 orbis_validator.py --all          Gesamtlauf
  python3 orbis_validator.py --strict       Befunde gegen orbis_baseline.json;
                                            Exit 1 bei NEUEN Befunden (CI)
  python3 orbis_validator.py --update-baseline  Baseline neu schreiben
  python3 orbis_validator.py --sim-l09      Silbifizierungs-Simulation
                                            (Entscheidungswerkzeug, KEINE Regel)
"""

import sys, re, json, unicodedata

# =========================================================================
# TEIL 1 — REGELDATEN AUS DER GRAMMATIK 0.9.3
# =========================================================================

# --- §2.1: 19 Konsonanten ------------------------------------------------
CONSONANTS = set("ptkbdgçfsşxvzjmnñlr")
assert len(CONSONANTS) == 19

# --- §2.2: 5 Vokale ------------------------------------------------------
VOWELS = set("aeiou")

# --- §2.3: Diphthonge ----------------------------------------------------
DIPHTHONGS_BELEGT = ["ai", "au", "ei", "ui", "eu"]
DIPHTHONG_OI = "oi"          # regulär, aber unbelegt (§2.3)
DIPHTHONGS = DIPHTHONGS_BELEGT + [DIPHTHONG_OI]

# --- §5.1: erlaubte Silbenformen (wörtlich) ------------------------------
# V · KV · KVK · KKV · KKVK · KVKK  — VK und VKK stehen NICHT in der Liste.
# Das Skript prüft strikt nach §5.1 und meldet zusätzlich, welche Wörter nur
# mit den dort fehlenden Formen VK/VKK parsebar wären (Befundklasse §5.1).
SYLLABLE_SHAPES_STRICT = {"V", "KV", "KVK", "KKV", "KKVK", "KVKK"}
SYLLABLE_SHAPES_VK = SYLLABLE_SHAPES_STRICT | {"VK", "VKK"}
SYLLABLE_SHAPES_KKVKK = SYLLABLE_SHAPES_STRICT | {"KKVKK"}
SYLLABLE_SHAPES_EXTENDED = SYLLABLE_SHAPES_STRICT | {"VK", "VKK", "KKVKK"}

# --- §5.2: Anfangsgruppen (genau 25) -------------------------------------
ONSETS2 = {"tr","dr","kr","gr","pr","br","pl","bl","fl","vl","fr","vr","vn",
           "sl","şl","şr","sk","st","sp","xr","xl","xn","zv","gl","kl"}
assert len(ONSETS2) == 25

# --- §5.3: Coda-Bedingungen ----------------------------------------------
CODA_FIRST_OK = set("lrmn")            # (a) erster Laut Fließlaut/Nasal
CODA_SECOND_S = "s"                    # (b) zweiter Laut s
CODA_PAIRS_C = {"şn", "sn", "sk", "st"}  # (c) feste Gruppen

def coda_pair_ok(pair):
    """§5.3: Zweiergruppe am Silbenende erlaubt?"""
    return (pair[0] in CODA_FIRST_OK or pair[1] == CODA_SECOND_S
            or pair in CODA_PAIRS_C)

# --- §7: 45 reguläre Geschlechtsendungen ---------------------------------
CLASS_CONS = {
    "M": {"A": "r", "B": "k", "C": "d"},
    "F": {"A": "l", "B": "v", "C": "m"},
    "N": {"A": "n", "B": "s", "C": "t"},
}
GENDER_OF_CONS = {"r":"M","k":"M","d":"M","l":"F","v":"F","m":"F",
                  "n":"N","s":"N","t":"N"}
SUBCLASS_OF_CONS = {"r":"A","k":"B","d":"C","l":"A","v":"B","m":"C",
                    "n":"A","s":"B","t":"C"}
THEMA_VOWELS = "aeiou"
ALL_45_ENDINGS = [c + v for c in GENDER_OF_CONS for v in THEMA_VOWELS]
assert len(ALL_45_ENDINGS) == 45

# --- §8: Kasusmarker -----------------------------------------------------
CASE_MARKERS = {"nom": "", "akk": "n", "dat": "ş", "gen": "s"}
CASES = ["nom", "akk", "dat", "gen"]

# --- §10.2/§24.1: die 15 Kernwörter --------------------------------------
CORE_NOUNS = {
    "kaun": ("M", "Mensch"),  "veiş": ("F", "Mutter"),  "draun": ("M", "Vater"),
    "şirn": ("N", "Kind"),    "aul":  ("N", "Wasser"),  "xerp":  ("M", "Feuer"),
    "luiv": ("F", "Sonne"),   "grein":("F", "Erde"),    "nauş":  ("F", "Zeit"),
    "virn": ("N", "Leben"),   "moks": ("M", "Tod"),     "eird":  ("F", "Welt"),
    "şaul": ("M", "Name"),    "taiv": ("F", "Sprache"), "breun": ("N", "Haus"),
}
assert len(CORE_NOUNS) == 15

# --- §10.1: 10-Prozent-Gruppe (Bindevokal -e-; Plural in §10.1 NICHT geregelt)
TENPCT_NOUNS = {
    "velkran": ("N", "Freundschaft"),
    "soralm":  ("F", "Denkmal"),
    "prilm":   ("F", "Handwerk"),
}

# --- §24.2–24.4, §24.6, §21.3: reguläre Nomen  (Wort -> (Klasse, Bedeutung))
REGULAR_NOUNS = {
    # §24.2 Maskulin
    "valru":"M-A Mann", "velkra":"M-A Freund", "zaldre":"M-A Tag",
    "melru":"M-A Wanderer", "talru":"M-A Sprecher",
    "narku":"M-B Hund", "larki":"M-B Stein", "vlaiko":"M-B Wind",
    "vlenko":"M-B Vogel",
    "vrondo":"M-C Berg", "luvandi":"M-C Fluss", "navildo":"M-C Traum",
    "morda":"M-C Sturm",
    # §24.3 Feminin
    "sarla":"F-A Frau", "prila":"F-A Hand", "kavla":"F-A Stadt",
    "zenlo":"F-A Blume", "mela":"F-A Wanderin", "tala":"F-A Sprecherin",
    "kirva":"F-B Nacht", "melva":"F-B Straße", "gluvi":"F-B Flamme",
    "drovi":"F-B Wolke",
    "şonma":"F-C Stimme", "soruma":"F-C Erinnerung", "klerma":"F-C Freiheit",
    "taluma":"F-C Rede", "meluma":"F-C Reise",
    # §24.4 Neutrum
    "milne":"N-A Auge", "verno":"N-A Herz", "melna":"N-A Weg",
    "drovna":"N-A Wald", "skelnu":"N-A Himmel", "talna":"N-A Versammlungsort",
    "taisa":"N-B Wort", "pliso":"N-B Feder", "brasi":"N-B Brot",
    "vresto":"N-C Buch", "melisto":"N-C Fahrzeug", "talisto":"N-C Instrument",
    "veltu":"N-C Jahr",
    # §24.6 Abstrakta (alle F-C auf -uma)
    "klaunuma":"F-C Wahrheit", "nestuma":"F-C Wille", "salvuma":"F-C Verlust",
    "vaşnuma":"F-C Vergänglichkeit", "mirnuma":"F-C Entscheidung",
    "şauluma":"F-C Identität", "tarnuma":"F-C Konsequenz",
    "saivuma":"F-C Liebe", "virnuma":"F-C Dasein",
}

# §21.3 Zusammensetzungen. Kopf jeweils letztes Glied.
# taivbreun hat als Kopf das KERNWORT breun -> Deklinationsklasse der
# Zusammensetzung ist in §21.3 nicht geregelt (regulär? Kernwortmuster?).
COMPOUND_NOUNS = {
    "taivbreun": ("N", "Schule",   "Kopf breun = Kernwort -> Deklination ungeregelt"),
    "aulmelna":  ("N", "Kanal",    "Kopf melna = N-A regulär"),
    "luivresto": ("N", "Kalender", "Kopf vresto = N-C regulär"),
}

# --- §11: Artikel ---------------------------------------------------------
def article_forms():
    """Alle Artikelformen erzeugen: x-/v- + r/l/n + a + Marker (§11)."""
    forms = {}
    for det, dname in (("x", "bestimmt"), ("v", "unbestimmt")):
        for g, gc in (("M", "r"), ("F", "l"), ("N", "n")):
            base = det + gc + "a"
            for case in CASES:
                forms[base + CASE_MARKERS[case]] = (dname, g, case, "sg")
            if det == "x":  # §11.2: kein unbestimmter Artikel im Plural
                forms[base + "ñ"] = (dname, g, "nom", "pl")
                for case in ("akk", "dat", "gen"):
                    forms[base + "ñ" + "a" + CASE_MARKERS[case]] = (dname, g, case, "pl")
    return forms

ARTICLES = article_forms()

# --- §13.1: Personalpronomen ---------------------------------------------
PRONOUNS = {}
for nom, akk, dat, gen, label in [
    ("vim","vin","viş","vis","1sg"), ("şet","şen","şeş","şes","2sg"),
    ("şevar","şevan","şevaş","şevas","2höfl"),
    ("ro","ron","roş","ros","3sg-m"), ("lo","lon","loş","los","3sg-f"),
    ("no","non","noş","nos","3sg-n"),
    ("viñ","viñan","viñaş","viñas","1pl"), ("şeñ","şeñan","şeñaş","şeñas","2pl"),
    ("oñ","oñan","oñaş","oñas","3pl"),
]:
    PRONOUNS[nom] = (label, "nom"); PRONOUNS[akk] = (label, "akk")
    PRONOUNS[dat] = (label, "dat"); PRONOUNS[gen] = (label, "gen")

# --- §13.4: übrige Pronomen ----------------------------------------------
# Demonstrativa/Indefinita: NUR Grundformen belegt; Deklination ungeregelt.
DEMONSTRATIVES = {"kilra":"dieser(m)","killa":"diese(f)","kilna":"dieses(n)",
                  "dolra":"jener(m)","dolla":"jene(f)","dolna":"jenes(n)"}
REFLEXIVE = {"se"}                      # keine Kasusformen definiert
RELATIVE = {"fai"}                      # homonym mit fai "dass" (§20)
INDEFINITES = {"kaun":"man (homonym: Mensch)","kelsu":"jemand",
               "xakaun":"niemand","kelte":"etwas","xakelte":"nichts"}

# --- §14/§15: Verben ------------------------------------------------------
PERSON_ENDINGS = {"1sg":"m","2sg":"ş","3sg":"t","1pl":"men","2pl":"şen","3pl":"ten"}
TENSE_VOWELS = {"präs":"a","vgh":"o","fut":"ai"}

# §24.5 reguläre Wurzeln (ohne die 8 unregelmäßigen), inkl. §16.1 Modalwurzeln
REGULAR_VERB_ROOTS = {
    "milk":"sehen","zaub":"hören","tal":"sprechen","nast":"essen",
    "prev":"trinken","soñ":"schlafen","dremn":"denken","prens":"nehmen",
    "saiv":"lieben","vlent":"laufen","rusk":"schreiben","leşn":"lesen",
    "traiv":"finden","mald":"warten","stan":"bleiben","sor":"bewahren",
    "salv":"verlieren (transitiv)","vaşn":"vergehen (intransitiv)",
    "mirn":"entscheiden","tarn":"folgen",
}
MODAL_ROOTS = {"valn":"können","dolm":"müssen","vlek":"dürfen",
               "tirn":"sollen","nest":"wollen","suvr":"mögen"}

# §15.2: die 8 unregelmäßigen Verben.
# Formel laut Grammatik: "Ablautstamm + Bindevokal -e- + Personendung".
# Die Tabellen der Grammatik selbst zeigen: es- ist voll suppletiv (em/est,
# vo+P OHNE -e-, vai+P), nuv- und vurn- haben zusätzlich kontrahierte
# Präsensformen (nu+P, vur+P). Das Skript kodiert die BELEGTEN Tabellen.
def _p(stem):
    return {per: stem + end for per, end in PERSON_ENDINGS.items()}

IRREGULAR_VERBS = {
    "es": {"inf":"esex","bedeutung":"sein",
           "präs":{"1sg":"em","2sg":"eş","3sg":"est","1pl":"emen","2pl":"eşen","3pl":"esten"},
           "vgh":_p("vo"), "fut":_p("vai")},
    "nuv": {"inf":"nuvex","bedeutung":"haben",
            "präs":_p("nu"), "vgh":_p("nove"), "fut":_p("nuvai")},
    "vurn": {"inf":"vurnex","bedeutung":"werden",
             "präs":_p("vur"), "vgh":_p("vore"), "fut":_p("vurnai")},
    "mel": {"inf":"melex","bedeutung":"gehen",
            "präs":_p("mela"), "vgh":_p("mole"), "fut":_p("melai")},
    "vand": {"inf":"vandex","bedeutung":"kommen",
             "präs":_p("vanda"), "vgh":_p("vende"), "fut":_p("vandai")},
    "narg": {"inf":"nargex","bedeutung":"machen",
             "präs":_p("narga"), "vgh":_p("norge"), "fut":_p("nargai")},
    "zav": {"inf":"zavex","bedeutung":"wissen",
            "präs":_p("zava"), "vgh":_p("zove"), "fut":_p("zavai")},
    "dalv": {"inf":"dalvex","bedeutung":"geben",
             "präs":_p("dalva"), "vgh":_p("dolve"), "fut":_p("dalvai")},
}

VERB_PREFIXES = ["şu", "re", "dra", "su"]   # §21.2 (xa- bildet Gegenteile, nicht Verbformen)

# --- §12/§24.7: Adjektive -------------------------------------------------
ADJECTIVES = {
    "vlaid":"groß","nirm":"klein","selv":"gut","morn":"schlecht","loşn":"schön",
    "granz":"alt","zirv":"neu","trelm":"lang","misn":"kurz","velm":"warm",
    "girn":"kalt","luid":"hell","şaln":"dunkel","xarn":"stark","vresn":"schwach",
    "zilv":"schnell","tolm":"langsam","klaun":"wahr","norv":"falsch","xan":"kein",
}
COMPARISON_INFIXES = {"komp":"vi","sup":"vax"}   # §12.3

# --- §18.2: Fragewörter ---------------------------------------------------
# kem/kelt/kur/kan/grais/kolm: nur Grundformen belegt. kelra/kella/kelna
# kongruieren laut Beispiel "Kellan sarlan milkoş?" adjektivisch.
W_WORDS = {"kem":"wer","kelt":"was","kur":"wo/wohin","kan":"wann",
           "grais":"warum","kolm":"wie"}
W_ADJ = {"kelra":"M","kella":"F","kelna":"N"}    # welcher/welche/welches

# --- §19: Präpositionen und Kasus ----------------------------------------
PREPOSITIONS = {
    "zva": {"dat"}, "xun": {"akk"}, "prai": {"akk"}, "dral": {"akk"},
    "dun": {"dat"}, "ven": {"dat"}, "nul": {"dat"},
    "gral": {"gen"}, "şlan": {"gen"},
    "tel": {"dat","akk"}, "kru": {"dat","akk"}, "span": {"dat","akk"},
    "drel": {"dat","akk"}, "glem": {"dat","akk"}, "traus": {"dat","akk"},
    "şlim": {"dat","akk"},
}

# --- §20: Konjunktionen ---------------------------------------------------
CONJ_COORD = {"ze":"und","vu":"oder","klas":"aber","xer":"denn"}
CONJ_SUB = {"fai":"dass","grali":"weil","tund":"wenn","şlani":"obwohl",
            "dremi":"während","glemi":"bevor","trausi":"nachdem"}

# --- §24.8: Zahlen ---------------------------------------------------------
NUMBERS = {"nel":1,"dram":2,"teln":3,"kalm":4,"mern":5,"vesn":6,"zerm":7,
           "glon":8,"pirn":9,"xelm":10,"munar":100,"kraven":1000}
NUMBER_COMPOUNDS = {"xelmnel":11,"dramxelm":20,"telnxelmmern":35}  # wörtlich aus §24.8
ORDINAL_INFIX = "ost"                                              # + Geschlechtsendung

# --- §24.9 / §13.2: Adverbien, Partikeln, Grußformeln ----------------------
PARTICLES = {
    "nunda":"heute","zirna":"morgen","granza":"gestern","nun":"jetzt",
    "dalvur":"immer","xanur":"nie","kilur":"hier","dolur":"dort",
    "vran":"sehr (homonym: vran = unbest. Artikel M Akk)","skirm":"wenig",
    "ain":"ja","xaus":"nein","xa":"nicht","mai":"würde","kon":"als","zil":"wie",
    "selvai":"Hallo","melai":"Auf Wiedersehen","selves":"Danke","praum":"Bitte",
}

# --- Lexemliste für Duplikat-/Kollisionssuche (Phase 7) -------------------
def full_lexeme_inventory():
    """(form, kategorie, bedeutung) für alle Grundformen des Lexikons."""
    inv = []
    for w, (g, b) in CORE_NOUNS.items():   inv.append((w, "Kernwort-"+g, b))
    for w, (g, b) in TENPCT_NOUNS.items(): inv.append((w, "Nomen10%-"+g, b))
    for w, kb in REGULAR_NOUNS.items():
        k, b = kb.split(" ", 1);           inv.append((w, "Nomen-"+k, b))
    for w, (g, b, _) in COMPOUND_NOUNS.items(): inv.append((w, "Nomen-Komp-"+g, b))
    for w, b in REGULAR_VERB_ROOTS.items(): inv.append((w+"-", "Verbwurzel", b))
    for w, b in MODAL_ROOTS.items():        inv.append((w+"-", "Modalwurzel", b))
    for w, d in IRREGULAR_VERBS.items():    inv.append((w+"-", "Verbwurzel-irr", d["bedeutung"]))
    for w, b in ADJECTIVES.items():         inv.append((w, "Adjektiv", b))
    for w, b in W_WORDS.items():            inv.append((w, "Fragewort", b))
    for w, g in W_ADJ.items():              inv.append((w, "Fragewort-adj", "welch- "+g))
    for w, b in DEMONSTRATIVES.items():     inv.append((w, "Demonstrativ", b))
    for w, b in INDEFINITES.items():        inv.append((w, "Indefinit", b))
    for w in REFLEXIVE:                     inv.append((w, "Reflexiv", "sich"))
    for w in RELATIVE:                      inv.append((w, "Relativ", "der/die/das"))
    for w in PREPOSITIONS:                  inv.append((w, "Präposition", ""))
    for w, b in CONJ_COORD.items():         inv.append((w, "Konj-koord", b))
    for w, b in CONJ_SUB.items():           inv.append((w, "Konj-sub", b))
    for w, b in NUMBERS.items():            inv.append((w, "Zahl", str(b)))
    for w, b in NUMBER_COMPOUNDS.items():   inv.append((w, "Zahl-Komp", str(b)))
    for w, b in PARTICLES.items():          inv.append((w, "Partikel/Adverb", b))
    for w in PRONOUNS:                      inv.append((w, "Pronomenform", PRONOUNS[w][0]))
    for w in ARTICLES:                      inv.append((w, "Artikelform", str(ARTICLES[w][:3])))
    return inv

# =========================================================================
# TEIL 2 — PRÜF-ENGINE
# =========================================================================

def strip_punct(text):
    return re.sub(r"[.,;:!?„“\"»«…()\-—]", " ", text)

def tokenize(sentence):
    return [t.lower() for t in strip_punct(sentence).split() if t]

# --- Prüfung 1: Phoneminventar -------------------------------------------
def check_phonemes(word):
    """Nur die 19 Konsonanten und 5 Vokale aus §2? Liefert Liste fremder Zeichen."""
    return [ch for ch in word if ch not in CONSONANTS and ch not in VOWELS]

# --- Geminaten-Check (Folge der Fugenregel §21.4) -------------------------
def check_geminates(word):
    """§21.4: identische Konsonanten verschmelzen an jeder Fuge. Da kein
    Morphem des Lexikons interne Geminaten hat, ist jede Doppelkonsonanz
    verdächtig. Befund, keine automatische Korrektur."""
    hits = []
    for i in range(len(word) - 1):
        if word[i] == word[i+1] and word[i] in CONSONANTS:
            hits.append(word[i] + word[i+1])
    return hits

# --- Silbenzerlegung (§5) -------------------------------------------------
def _nucleus_options(word, i):
    """Mögliche Nuklei ab Position i: Diphthong (2 Zeichen) vor Einzelvokal."""
    opts = []
    if word[i:i+2] in DIPHTHONGS:
        opts.append(word[i:i+2])
    if word[i] in VOWELS:
        opts.append(word[i])
    return opts

def syllabify(word, shapes=SYLLABLE_SHAPES_STRICT):
    """Alle §5-konformen Zerlegungen von word.
    Silbe = (Onset, Nukleus, Coda). shapes steuert, ob nur die wörtliche
    §5.1-Liste gilt (strikt) oder zusätzlich VK/VKK (erweitert)."""
    results = []

    def shape_of(onset, coda):
        return "K" * len(onset) + "V" + "K" * len(coda)

    def onset_ok(onset):
        if len(onset) == 0: return True
        if len(onset) == 1: return onset in CONSONANTS
        if len(onset) == 2: return onset in ONSETS2       # §5.2
        return False                                       # §5.2: nie >2

    def coda_ok(coda):
        if any(ch not in CONSONANTS for ch in coda): return False
        if len(coda) <= 1: return True
        if len(coda) == 2: return coda_pair_ok(coda)       # §5.3
        return False

    def rec(i, acc):
        if i == len(word):
            results.append(list(acc)); return
        for on_len in (0, 1, 2):
            onset = word[i:i+on_len]
            if len(onset) < on_len or not onset_ok(onset): continue
            j = i + on_len
            if j >= len(word): continue
            for nuc in _nucleus_options(word, j):
                k = j + len(nuc)
                for cd_len in (0, 1, 2):
                    coda = word[k:k+cd_len]
                    if len(coda) < cd_len or not coda_ok(coda): continue
                    if shape_of(onset, coda) not in shapes: continue
                    rec(k + cd_len, acc + [(onset, nuc, coda)])

    rec(0, [])
    # Duplikate entfernen, deterministisch sortieren
    uniq = sorted({tuple(r) for r in results})
    return [list(u) for u in uniq]

def phonotactics_verdict(word):
    """Strikte §5.1-Prüfung mit Zusatzbefund:
    'ok'         — nach wörtlicher §5.1-Liste parsebar
    'nur-VK'     — NUR mit den in §5.1 fehlenden Formen VK/VKK parsebar
    'nur-KKVKK'  — NUR mit der in §5.1 fehlenden Form KKVKK parsebar
    'verstoß'    — auch erweitert nicht parsebar"""
    bad = check_phonemes(word)
    if bad:
        return ("fremdzeichen", bad)
    if syllabify(word, SYLLABLE_SHAPES_STRICT):
        return ("ok", None)
    if syllabify(word, SYLLABLE_SHAPES_KKVKK):
        return ("nur-KKVKK", None)
    if syllabify(word, SYLLABLE_SHAPES_VK):
        return ("nur-VK", None)
    if syllabify(word, SYLLABLE_SHAPES_EXTENDED):
        return ("nur-VK+KKVKK", None)
    return ("verstoß", None)

# --- Formengeneratoren ----------------------------------------------------
def decline_regular_noun(noun, case, number):
    """§8/§9: Stamm+Klassenkons.+Themavokal (+ñ+Echovokal) + Kasusmarker."""
    thema = noun[-1]
    if number == "sg":
        return noun + CASE_MARKERS[case]
    if case == "nom":
        return noun + "ñ"
    return noun + "ñ" + thema + CASE_MARKERS[case]

def decline_core_noun(word, case, number):
    """§10.3: Sg Bindevokal -e-, Pl -ei; Nom Sg endungslos."""
    if number == "sg":
        return word if case == "nom" else word + "e" + CASE_MARKERS[case]
    return word + "ei" + CASE_MARKERS[case]

def decline_tenpct_noun(word, case, number):
    """§10.1: Sg mit Bindevokal -e-. Plural ist in §10.1 NICHT geregelt."""
    if number == "sg":
        return word if case == "nom" else word + "e" + CASE_MARKERS[case]
    return None   # [REGELLÜCKE] Plural der 10%-Gruppe

ADJ_GENDER_CONS = {"M": "r", "F": "l", "N": "n"}

def fuse(a, b):
    """§21.4 Fugenregel: identische Konsonanten an der Fuge verschmelzen."""
    if a and b and a[-1] == b[0] and a[-1] in CONSONANTS:
        return a + b[1:]
    return a + b

def adj_attributive(stem, gender, case, number, grade=None):
    """§12.1/§12.3: Stamm (+vi/vax) + r/l/n + a + Marker, mit Fugenregel."""
    if grade:
        stem = fuse(stem, COMPARISON_INFIXES[grade])
    base = fuse(stem, ADJ_GENDER_CONS[gender] + "a")
    if number == "sg":
        return base + CASE_MARKERS[case]
    if case == "nom":
        return base + "ñ"
    return base + "ñ" + "a" + CASE_MARKERS[case]

def adj_predicative(stem, grade=None):
    return fuse(stem, COMPARISON_INFIXES[grade]) if grade else stem

def conj_regular(root, tense, person):
    """§14/§15: Wurzel + Tempusvokal + Personendung."""
    return root + TENSE_VOWELS[tense] + PERSON_ENDINGS[person]

def conj(root, tense, person):
    if root in IRREGULAR_VERBS:
        return IRREGULAR_VERBS[root][tense][person]
    return conj_regular(root, tense, person)

# --- Erkennungs-Lexika (alle wohlgeformten Wortformen) --------------------
def _build_recognizers():
    noun_forms = {}   # form -> (lemma, klasse, kasus, numerus)
    for noun, kb in REGULAR_NOUNS.items():
        klasse = kb.split(" ", 1)[0]
        for case in CASES:
            for num in ("sg", "pl"):
                f = decline_regular_noun(noun, case, num)
                noun_forms.setdefault(f, []).append((noun, klasse, case, num))
    for noun, (g, _) in CORE_NOUNS.items():
        for case in CASES:
            for num in ("sg", "pl"):
                f = decline_core_noun(noun, case, num)
                noun_forms.setdefault(f, []).append((noun, "Kern-" + g, case, num))
    for noun, (g, _) in TENPCT_NOUNS.items():
        for case in CASES:
            f = decline_tenpct_noun(noun, case, "sg")
            noun_forms.setdefault(f, []).append((noun, "10%-" + g, case, "sg"))
    for noun, (g, _, note) in COMPOUND_NOUNS.items():
        # Kopf regulär -> regulär deklinieren; Kernwort-Kopf: beide Muster
        # sind unbelegt, §21.3 schweigt -> nur Nominativ als sicher führen.
        if "Kernwort" in note:
            noun_forms.setdefault(noun, []).append((noun, "Komp-" + g + "(?)", "nom", "sg"))
        else:
            for case in CASES:
                for num in ("sg", "pl"):
                    f = decline_regular_noun(noun, case, num)
                    noun_forms.setdefault(f, []).append((noun, "Komp-" + g, case, num))

    verb_forms = {}   # form -> beschreibung
    all_roots = dict(REGULAR_VERB_ROOTS); all_roots.update(MODAL_ROOTS)
    for root in all_roots:
        for t in TENSE_VOWELS:
            for p in PERSON_ENDINGS:
                verb_forms.setdefault(conj_regular(root, t, p), []).append((root, t, p))
        verb_forms.setdefault(fuse(root, "ex"), []).append((root, "inf", "-"))
        verb_forms.setdefault(fuse(root, "ut"), []).append((root, "part", "-"))
    for root, tbl in IRREGULAR_VERBS.items():
        for t in ("präs", "vgh", "fut"):
            for p, f in tbl[t].items():
                verb_forms.setdefault(f, []).append((root, t, p))
        verb_forms.setdefault(tbl["inf"], []).append((root, "inf", "-"))
        verb_forms.setdefault(fuse(root, "ut"), []).append((root, "part", "-"))

    adj_forms = {}    # form -> beschreibung
    for stem in ADJECTIVES:
        adj_forms.setdefault(stem, []).append((stem, "präd", "-", "-"))
        adj_forms.setdefault(fuse(stem, "un"), []).append((stem, "adverb", "-", "-"))
        for grade in (None, "komp", "sup"):
            if grade:
                adj_forms.setdefault(adj_predicative(stem, grade), []).append(
                    (stem, "präd-" + grade, "-", "-"))
            for g in ("M", "F", "N"):
                for case in CASES:
                    for num in ("sg", "pl"):
                        f = adj_attributive(stem, g, case, num, grade)
                        adj_forms.setdefault(f, []).append(
                            (stem, "attr" + ("-" + grade if grade else ""), g, case + "-" + num))
        # §12.5 Nominalisierung
        adj_forms.setdefault(fuse(stem, "ru"), []).append((stem, "nomin-M", "-", "-"))
        adj_forms.setdefault(fuse(stem, "la"), []).append((stem, "nomin-F", "-", "-"))
        adj_forms.setdefault(fuse(stem, "te"), []).append((stem, "nomin-N", "-", "-"))

    # welch- kongruiert laut §18.2-Beispiel adjektivisch ("Kellan sarlan").
    # Achtung: die belegte Form kella verletzt die Fugenregel §21.4 (kel+la
    # müsste kela ergeben) — der Erkenner folgt den BELEGTEN Formen, der
    # Geminaten-Check meldet den Konflikt separat.
    w_adj_forms = {}
    for stem_full, g in W_ADJ.items():
        for case in CASES:
            w_adj_forms.setdefault(stem_full + CASE_MARKERS[case], []).append(
                ("kel-", g, case, "sg"))
        w_adj_forms.setdefault(stem_full + "ñ", []).append(("kel-", g, "nom", "pl"))
        for case in ("akk", "dat", "gen"):
            w_adj_forms.setdefault(stem_full + "ña" + CASE_MARKERS[case], []).append(
                ("kel-", g, case, "pl"))

    # §12.5: Partizip + -te -> -ute (traivute)
    part_nom = {}
    for root in list(all_roots) + list(IRREGULAR_VERBS):
        part_nom[fuse(fuse(root, "ut"), "te")] = root

    # Ordnungszahlen §24.8: Zahl + -ost- + Geschlechtsendung (adjektivisch)
    ord_forms = {}
    for num_word in NUMBERS:
        for g in ("M", "F", "N"):
            for case in CASES:
                f = adj_attributive(fuse(num_word, ORDINAL_INFIX), g, case, "sg")
                ord_forms.setdefault(f, []).append((num_word, g, case))

    return noun_forms, verb_forms, adj_forms, w_adj_forms, part_nom, ord_forms

(NOUN_FORMS, VERB_FORMS, ADJ_FORMS, W_ADJ_FORMS, PART_NOM, ORD_FORMS) = _build_recognizers()

def classify_token(tok):
    """Alle regelkonformen Lesarten eines Tokens. Leere Liste = unbekannt."""
    readings = []
    if tok in ARTICLES:
        d, g, c, n = ARTICLES[tok]
        readings.append(("ART", f"{d}-{g}-{c}-{n}"))
    if tok in PRONOUNS:
        readings.append(("PRON", "-".join(PRONOUNS[tok])))
    if tok in DEMONSTRATIVES: readings.append(("DEM", DEMONSTRATIVES[tok]))
    if tok in REFLEXIVE:      readings.append(("REFL", "se (indeklinabel? §13.4 offen)"))
    if tok in RELATIVE:       readings.append(("REL/SUB", "fai (Relativ ODER dass)"))
    if tok in INDEFINITES:    readings.append(("INDEF", INDEFINITES[tok]))
    if tok in W_WORDS:        readings.append(("W", W_WORDS[tok]))
    if tok in PREPOSITIONS:   readings.append(("PRÄP", "+".join(sorted(PREPOSITIONS[tok]))))
    if tok in CONJ_COORD:     readings.append(("KONJ", CONJ_COORD[tok]))
    if tok in CONJ_SUB:       readings.append(("SUBKONJ", CONJ_SUB[tok]))
    if tok in NUMBERS:        readings.append(("ZAHL", str(NUMBERS[tok])))
    if tok in NUMBER_COMPOUNDS: readings.append(("ZAHL", str(NUMBER_COMPOUNDS[tok])))
    if tok in PARTICLES:      readings.append(("PART", PARTICLES[tok]))
    if tok in NOUN_FORMS:
        for lemma, klasse, case, num in NOUN_FORMS[tok]:
            readings.append(("NOMEN", f"{lemma} {klasse} {case} {num}"))
    if tok in ADJ_FORMS:
        for stem, art, g, cn in ADJ_FORMS[tok]:
            readings.append(("ADJ", f"{stem} {art} {g} {cn}"))
    if tok in W_ADJ_FORMS:
        for stem, g, case, num in W_ADJ_FORMS[tok]:
            readings.append(("W-ADJ", f"welch- {g} {case} {num}"))
    if tok in PART_NOM: readings.append(("PART-NOM", PART_NOM[tok] + "-ute"))
    if tok in ORD_FORMS:
        for num_word, g, case in ORD_FORMS[tok]:
            readings.append(("ORD", f"{num_word}-ost {g} {case}"))
    # Verbformen, auch mit Vorsilben (şu-, re-, dra-, su-) und Imperative
    def verb_readings(t, prefix=""):
        out = []
        if t in VERB_FORMS:
            for root, tense, per in VERB_FORMS[t]:
                out.append(("VERB", f"{prefix}{root}- {tense} {per}"))
        all_roots = set(REGULAR_VERB_ROOTS) | set(MODAL_ROOTS) | set(IRREGULAR_VERBS)
        if t in all_roots:
            out.append(("VERB", f"{prefix}{t}- Imperativ Sg (§14)"))
        for root in all_roots:
            if t == fuse(root, "eñ"):
                out.append(("VERB", f"{prefix}{root}- Imperativ Pl (§14)"))
            # Imperativ mit Stütz-e bei unzulässiger Endgruppe (§14: Suvre!)
            if t == root + "e" and not syllabify(root, SYLLABLE_SHAPES_EXTENDED):
                out.append(("VERB", f"{prefix}{root}- Imperativ Sg +e (§14)"))
        return out
    readings += verb_readings(tok)
    for pre in VERB_PREFIXES:
        if tok.startswith(pre):
            readings += verb_readings(tok[len(pre):], prefix=pre + "+")
    # xa-/su- als Adjektiv-Vorsilben (§21.2: xaselvra, suluidra)
    for pre in ("xa", "su"):
        if tok.startswith(pre) and tok[len(pre):] in ADJ_FORMS:
            for stem, art, g, cn in ADJ_FORMS[tok[len(pre):]]:
                readings.append(("ADJ", f"{pre}+{stem} {art} {g} {cn}"))
    return readings

# --- Satzprüfung ----------------------------------------------------------
def check_sentence(sentence):
    """Automatisch prüfbar: Lexik/Morphologie je Token, Phonotaktik,
    Geminaten, Präposition->Kasus (Heuristik über Folge-Artikel/-Pronomen).
    NICHT automatisch entscheidbar (MANUELLE_PRÜFUNG): V2-Stellung,
    Verbklammer, Nebensatz-Endstellung, Kongruenz über Distanz, Semantik."""
    report = {"satz": sentence, "unbekannt": [], "phonotaktik": [],
              "geminaten": [], "präp_kasus": [], "kongruenz": [], "lesarten": {}}
    toks = tokenize(sentence)
    for tok in toks:
        r = classify_token(tok)
        report["lesarten"][tok] = r
        if not r:
            report["unbekannt"].append(tok)
        verdict, extra = phonotactics_verdict(tok)
        if verdict.startswith("nur-"):
            report["phonotaktik"].append((tok, f"nur mit {verdict[4:]} parsebar — §5.1 nennt diese Form nicht"))
        elif verdict == "verstoß":
            report["phonotaktik"].append((tok, "keine §5-konforme Zerlegung"))
        elif verdict == "fremdzeichen":
            report["phonotaktik"].append((tok, "fremde Zeichen: " + ",".join(extra)))
        gem = check_geminates(tok)
        if gem:
            report["geminaten"].append((tok, gem))
    # Heuristik: NP-Kongruenz Artikel (+Adjektive) + Nomen in Folge.
    # Konservativ: gemeldet wird nur, wenn KEINE Lesartkombination passt.
    def _g_of_klasse(klasse):
        for ch in klasse:
            if ch in "MFN": return ch
        return None
    def noun_triples(readings):
        out = set()
        for kind, desc in readings:
            if kind == "NOMEN":
                parts = desc.split()
                g = _g_of_klasse(parts[1])
                if g: out.add((g, parts[2], parts[3]))
        return out
    def adj_triples(readings):
        out = set(); is_adj = False
        for kind, desc in readings:
            if kind in ("ADJ", "W-ADJ") and ("attr" in desc or kind == "W-ADJ"):
                parts = desc.split()
                if kind == "ADJ":
                    g, cn = parts[2], parts[3]
                    if "-" in cn:
                        c, n = cn.split("-"); out.add((g, c, n)); is_adj = True
                else:
                    out.add((parts[1], parts[2], parts[3])); is_adj = True
        return out if is_adj else None
    i = 0
    while i < len(toks):
        r = report["lesarten"].get(toks[i], [])
        art_triples = {tuple(d.split("-")[1:4]) for k, d in r if k == "ART"}
        if art_triples:
            j = i + 1; adj_list = []; nset = None; last = None
            while j < len(toks) and j <= i + 3:
                rj = report["lesarten"].get(toks[j], [])
                nt = noun_triples(rj)
                if nt: nset = nt; last = toks[j]; break
                at = adj_triples(rj)
                if at: adj_list.append(at); j += 1; continue
                break
            if nset is not None:
                inter = art_triples & nset
                for at in adj_list: inter &= at
                if not inter:
                    report["kongruenz"].append(
                        (toks[i], last, "keine gemeinsame Genus/Kasus/Numerus-Lesart in der NP"))
        i += 1
    # Heuristik: Präposition + nächster Artikel/Pronomen-Kasus
    for i, tok in enumerate(toks):
        if tok in PREPOSITIONS:
            need = PREPOSITIONS[tok]
            for j in (i + 1, i + 2):
                if j >= len(toks): break
                nxt = toks[j]
                cases = set()
                if nxt in ARTICLES: cases = {ARTICLES[nxt][2]}
                elif nxt in PRONOUNS: cases = {PRONOUNS[nxt][1]}
                elif nxt in NOUN_FORMS:
                    cases = {c for (_, _, c, _) in NOUN_FORMS[nxt]}
                if cases:
                    if not (cases & need):
                        report["präp_kasus"].append(
                            (tok, nxt, f"verlangt {sorted(need)}, gefunden {sorted(cases)}"))
                    break
    return report

# =========================================================================
# TEIL 3 — LÄUFE UND BERICHTE
# =========================================================================

# Alle Beispielsätze der Grammatik 0.9.3 (Fundstelle, Satz).
GRAMMAR_EXAMPLES = [
    ("§12.2", "Lo loşn est."),
    ("§12.2", "Xla kirva girn vot."),
    ("§12.2", "Xra valru xarn vurt."),
    ("§12.2", "Xna breun granz stanat."),
    ("§12.2", "Xrañ larkiñ girn esten."),
    ("§12.3", "Ro vlaidvi est kon vim."),
    ("§12.3", "Lo loşn est zil luiv."),
    ("§12.3", "Xra vlaidvaxra vrondo"),
    ("§12.1", "xra vlaidra valru"),
    ("§12.1", "xlan vlaidlan sarlan"),
    ("§12.1", "xnañaş vlaidnañaş milneñeş"),
    ("§13.2", "Şet melaş."),
    ("§13.2", "Şevar melaten."),
    ("§13.3", "xna breun vis"),
    ("§13.3", "xla sarla şes"),
    ("§13.3", "xrañ valruñ oñas"),
    ("§11.3", "xnaş şirneş"),
    ("§11.3", "xlan eirden"),
    ("§11.3", "xnan aulen"),
    ("§14", "Mel!"),
    ("§14", "Meleñ!"),
    ("§14", "Melaten!"),
    ("§14", "Suvre!"),
    ("§16.1", "Vim valnam xnan melnan milkex."),
    ("§16.1", "Şet dolmaş nunda vandex."),
    ("§16.2", "Vim mai melam."),
    ("§16.2", "Tund vim vra vlaidra valru mai em, mai traivam vim xlan eirden."),
    ("§16.3", "Xna breun şunargat."),
    ("§16.3", "Xna breun şunargut est."),
    ("§17.1", "Xra valru milkat xran narkun."),
    ("§17.1", "Xran narkun milkat xra valru."),
    ("§17.1", "Nunda milkat xra valru xran narkun."),
    ("§17.2", "Vim zavam, fai şet nunda dun xnaş breuneş melaş."),
    ("§17.3", "Vim valnam nunda zva xraş velkraş dun xlaş kavlaş melex."),
    ("§17.4", "Vim melaim zirna gral xlas talumas zva xraş velkraş dun xlaş kavlaş."),
    ("§17.5", "Xla luiv luid vot, xla kirva girn vot."),
    ("§18.1", "Melaş nunda?"),
    ("§18.2", "Kan melaş?"),
    ("§18.2", "Grais xa vandat?"),
    ("§18.2", "Kellan sarlan milkoş?"),
    ("§18.3", "Vim xa melam."),
    ("§18.3", "Vim xa num vna breun."),
    ("§18.3", "xanra valru"),
    ("§19", "Vim melam tel xlan kavlan."),
    ("§19", "Vim em tel xlaş kavlaş."),
    ("§25.1", "Xra valru milkat xran narkun."),
    ("§25.1", "Nunda melam vim dun xnaş breuneş vis."),
    ("§25.1", "Vim zavam, fai şet zirna vandaiş."),
    ("§25.1", "Vim xa valnam soñex, grali xla kirva vran luid est."),
    ("§25.1", "Tund vim vra vlaidra valru mai em, mai traivam vim xlan eirden."),
    ("§25.1", "Valnaten şevar vin zaubex?"),
    ("§25.1", "Xla veiş dolvet xnaş şirneş xnan brasin."),
    ("§25.1", "Xrañ melruñ moleten span xran vrondon."),
    ("§25.1", "Xna breun granz stanat, klas xla kavla zirv vurt."),
    ("§25.1", "Xnan melnan traivamen viñ, tund xla luiv luid est."),
    ("§25.1", "Xla soruma xlas nauşes vran tolm vaşnat."),
    ("§25.2", "Vra melru molet dral xrañan trelmrañan zaldreñen."),
    ("§25.2", "Xla luiv luid vot, xla kirva girn vot."),
    ("§25.2", "Ro xa zovet, kur xna melna molet, klas ro molet."),
    ("§25.2", "Vraş zaldreş traivot ro vnan aulen şlim xrañaş larkiñiş."),
    ("§25.2", "Ze ro dremnot: Kilna est xna traivute."),
    ("§25.2", "Ro nastot, ro prevot, ze ro soñot."),
    ("§25.2", "Tel xraş navildoş milkot ro xlan luiven xlas eirdes."),
    ("§21.1", "melex melru mela melna melisto melvi meluma"),
    ("§21.1", "talex talru tala talna talisto talvi taluma"),
    ("§13.2", "selvai melai selves praum"),
    ("§24.6", "Vim salvam xnan vreston"),
    ("§24.6", "Xla soruma vaşnat"),
    ("§24.8", "nelostra dramostla telnostna"),
    ("§24.8", "xelmnel dramxelm telnxelmmern"),
    ("§21.2", "şunargat xaselvra revandat dramilkat suluidra"),
]

# melvi/talvi (§21.1, Suffix -vi "Eigenschaft") sind produktive Ableitungen,
# keine §24.7-Adjektive; der Erkenner kennt sie nicht als Lexeme.
DERIVED_ADJ_VI = {"melvi": "reiselustig (mel- + -vi)", "talvi": "gesprächig (tal- + -vi)"}

def run_lexicon():
    """Prüfung 1–6 über das gesamte Lexikon."""
    out = []
    inv = full_lexeme_inventory()
    seen = {}
    for form, cat, meaning in inv:
        w = form.rstrip("-")
        verdict, extra = phonotactics_verdict(w)
        if verdict == "fremdzeichen":
            out.append(("FEHLER", w, cat, "fremde Zeichen: " + ",".join(extra)))
        elif verdict == "verstoß":
            out.append(("FEHLER", w, cat, "keine §5-konforme Silbenzerlegung"))
        elif verdict.startswith("nur-"):
            fehlend = verdict[4:].replace("VK", "VK/VKK", 1) if verdict == "nur-VK" else verdict[4:]
            out.append(("§5.1-BEFUND", w, cat,
                        f"nur mit Silbenform {fehlend} parsebar; §5.1 nennt diese Form nicht"))
        gem = check_geminates(w)
        if gem:
            out.append(("GEMINATE", w, cat,
                        "Doppelkonsonanz " + ",".join(gem) + " — kollidiert mit Fugenregel §21.4"))
        seen.setdefault(w, []).append((cat, meaning))
    # Prüfung 4+5: Nomenendung und Geschlecht
    for noun, kb in REGULAR_NOUNS.items():
        klasse = kb.split(" ", 1)[0]
        g, sub = klasse.split("-")
        end = noun[-2:]
        if end[0] not in GENDER_OF_CONS or end[1] not in THEMA_VOWELS:
            out.append(("ENDUNG", noun, "Nomen", f"Endung '{end}' nicht unter den 45 (§7)"))
        else:
            if GENDER_OF_CONS[end[0]] != g:
                out.append(("GENUS", noun, "Nomen",
                            f"Endung '{end}' → {GENDER_OF_CONS[end[0]]}, geführt als {g}"))
            if SUBCLASS_OF_CONS[end[0]] != sub:
                out.append(("UNTERKLASSE", noun, "Nomen",
                            f"Endung '{end}' → {SUBCLASS_OF_CONS[end[0]]}, geführt als {sub}"))
    # Prüfung 6: Kernwörter als Sonderklasse (kein 45er-Ausgang nötig, -e-/-ei)
    for w in CORE_NOUNS:
        if w[-2:] in [c + v for c in GENDER_OF_CONS for v in THEMA_VOWELS]:
            out.append(("HINWEIS", w, "Kernwort",
                        f"Auslaut '{w[-2:]}' sieht aus wie reguläre Endung — Sonderklasse nur im Wörterbuch erkennbar"))
    # Homonyme im Grundformbestand
    for w, cats in seen.items():
        kinds = {c for c, _ in cats}
        if len(cats) > 1 and len(kinds) > 1:
            out.append(("HOMONYM", w, "/".join(sorted(kinds)),
                        " | ".join(f"{c}: {m}" for c, m in cats)))
    return out

def run_examples():
    out = []
    for ref, s in GRAMMAR_EXAMPLES:
        rep = check_sentence(s)
        probs = []
        unk = [u for u in rep["unbekannt"] if u not in DERIVED_ADJ_VI]
        if unk: probs.append("unbekannte Formen: " + ", ".join(unk))
        for tok, msg in rep["phonotaktik"]: probs.append(f"{tok}: {msg}")
        for tok, gem in rep["geminaten"]:   probs.append(f"{tok}: Geminate {','.join(gem)}")
        for p, n, msg in rep["präp_kasus"]: probs.append(f"{p} {n}: {msg}")
        for a, b, msg in rep["kongruenz"]:  probs.append(f"NP {a} … {b}: {msg}")
        out.append((ref, s, probs))
    return out

def extract_corpus_sentences(path):
    """Zieht 'Orbis:'-Zeilen (Zeile nach 'Orbis:') aus einer Korpusdatei."""
    sents = []
    lines = open(path, encoding="utf-8").read().splitlines()
    cur_test = None
    for i, line in enumerate(lines):
        m = re.match(r"##\s*Test\s*(\d+)", line)
        if m: cur_test = int(m.group(1))
        if line.strip() == "Orbis:" and i + 1 < len(lines):
            nxt = lines[i + 1].strip()
            if nxt and not nxt.startswith("["):
                sents.append((cur_test, nxt))
        m2 = re.match(r"Orbis:\s*(.+)", line)
        if m2 and m2.group(1).strip():
            sents.append((cur_test, m2.group(1).strip()))
    return sents

def run_corpus(path):
    out = []
    for test_no, s in extract_corpus_sentences(path):
        s_clean = re.sub(r"\[.*?\]", "", s).strip()   # Marker im Satz ignorieren
        if not s_clean or s_clean.startswith("—"): continue
        rep = check_sentence(s_clean)
        probs = []
        unk = [u for u in rep["unbekannt"]
               if not (u.startswith("teststamm") or u in DERIVED_ADJ_VI)]
        if unk: probs.append("unbekannte Formen: " + ", ".join(unk))
        for tok, msg in rep["phonotaktik"]:
            if "VK" in msg: continue   # §5.1-Befund wird zentral berichtet
            probs.append(f"{tok}: {msg}")
        for tok, gem in rep["geminaten"]: probs.append(f"{tok}: Geminate {','.join(gem)}")
        for p, n, msg in rep["präp_kasus"]: probs.append(f"{p} {n}: {msg}")
        for a, b, msg in rep["kongruenz"]: probs.append(f"NP {a} … {b}: {msg}")
        vk = [tok for tok, msg in rep["phonotaktik"] if "VK" in msg]
        out.append((test_no, s_clean, probs, vk))
    return out

# --- Tabellen (Phase 4 I und J) ------------------------------------------
TESTSTEM = "pren"   # [TESTFORM]-Stamm, rein morphologischer Träger

def table_45():
    """Vollmatrix: 45 Endungen x 8 Formen (4 Kasus Sg + 4 Kasus Pl) = 360."""
    rows = []
    for g in ("M", "F", "N"):
        for sub in ("A", "B", "C"):
            c = CLASS_CONS[g][sub]
            for v in THEMA_VOWELS:
                lemma = TESTSTEM + c + v
                rows.append((g + "-" + sub, c + v, lemma,
                             decline_regular_noun(lemma, "akk", "sg"),
                             decline_regular_noun(lemma, "dat", "sg"),
                             decline_regular_noun(lemma, "gen", "sg"),
                             decline_regular_noun(lemma, "nom", "pl"),
                             decline_regular_noun(lemma, "akk", "pl"),
                             decline_regular_noun(lemma, "dat", "pl"),
                             decline_regular_noun(lemma, "gen", "pl")))
    return rows

def table_verb(root):
    rows = []
    for t in ("präs", "vgh", "fut"):
        for p in ("1sg", "2sg", "3sg", "1pl", "2pl", "3pl"):
            rows.append((t, p, conj(root, t, p)))
    return rows

# --- Phase 8: Manus-Zerlegung --------------------------------------------
def manus_report_data():
    """Silbenzerlegung des Grundwortschatzes nach §26.1.
    Liefert (wort, kategorie, parses, verdikt)."""
    data = []
    for form, cat, _ in full_lexeme_inventory():
        w = form.rstrip("-")
        strict = syllabify(w, SYLLABLE_SHAPES_STRICT)
        ext = syllabify(w, SYLLABLE_SHAPES_EXTENDED)
        parses = strict if strict else ext
        if not parses:
            verdict = "NICHT ZERLEGBAR"
        elif len(parses) == 1:
            verdict = "eindeutig" + ("" if strict else " (nur mit VK/VKK)")
        else:
            verdict = f"[MANUS-AMBIGUITÄT] {len(parses)} Zerlegungen" + \
                      ("" if strict else " (nur mit VK/VKK)")
        data.append((w, cat, parses, verdict))
    return data

def fmt_parse(p):
    return "·".join("".join(s) for s in p) + "  (" + \
           " ".join(f"[{o}|{n}|{c}]" for o, n, c in p) + ")"

# --- CLI -------------------------------------------------------------------
def main(argv):
    args = argv[1:]
    if not args:
        print(__doc__); return 0
    if "--lexicon" in args or "--all" in args:
        print("== LEXIKONPRÜFUNG (Prüfungen 1–6) ==")
        for kind, w, cat, msg in run_lexicon():
            print(f"[{kind}] {w} ({cat}): {msg}")
        print()
    if "--examples" in args or "--all" in args:
        print("== BEISPIELSÄTZE DER GRAMMATIK ==")
        ok = 0
        for ref, s, probs in run_examples():
            if probs:
                print(f"{ref}  {s}")
                for p in probs: print(f"    -> {p}")
            else:
                ok += 1
        print(f"({ok} von {len(GRAMMAR_EXAMPLES)} Beispielen ohne Befund)")
        print()
    if "--corpus" in args:
        path = args[args.index("--corpus") + 1]
        print(f"== KORPUSPRÜFUNG {path} ==")
        ok = 0; n = 0
        for test_no, s, probs, vk in run_corpus(path):
            n += 1
            if probs:
                print(f"Test {test_no}: {s}")
                for p in probs: print(f"    -> {p}")
            else:
                ok += 1
        print(f"({ok} von {n} Orbis-Sätzen ohne automatischen Befund)")
        print("MANUELLE_PRÜFUNG: V2/Verbklammer/Endstellung, Kongruenz über "
              "Distanz, Genitiv-Stellung, Semantik — nicht algorithmisch entschieden.")
        print()
    if "--tables" in args:
        print("== 45 ENDUNGEN — [TESTFORM]-Stamm '" + TESTSTEM + "-' ==")
        print("| Klasse | Endung | Nom Sg | Akk Sg | Dat Sg | Gen Sg | Nom Pl | Akk Pl | Dat Pl | Gen Pl |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for kl, end, nom, akk, dat, gen, npl, apl, dpl, gpl in table_45():
            print(f"| {kl} | -{end} | {nom} | {akk} | {dat} | {gen} | {npl} | {apl} | {dpl} | {gpl} |")
        print()
        print("== REGELMÄSSIGES VERB milk- (6 Personen × 3 Zeiten) ==")
        for t, p, f in table_verb("milk"): print(f"{t:5} {p:4} {f}")
        print()
        for root in IRREGULAR_VERBS:
            print(f"== UNREGELMÄSSIG {IRREGULAR_VERBS[root]['inf']} ({IRREGULAR_VERBS[root]['bedeutung']}) ==")
            for t, p, f in table_verb(root): print(f"{t:5} {p:4} {f}")
            print()
    if "--manus" in args or "--all" in args:
        print("== MANUS-SILBENZERLEGUNG (§26) ==")
        amb = 0; tot = 0
        for w, cat, parses, verdict in manus_report_data():
            tot += 1
            if "AMBIGUITÄT" in verdict or "NICHT" in verdict:
                if "AMBIGUITÄT" in verdict: amb += 1
                print(f"{w} ({cat}): {verdict}")
                for p in parses[:6]: print("    " + fmt_parse(p))
        print(f"({amb} von {tot} Grundformen mehrdeutig zerlegbar)")
        print()
    if "--strict" in args or "--update-baseline" in args:
        return run_strict(update="--update-baseline" in args)
    if "--sim-l09" in args:
        return run_sim_l09()
    if "--json" in args:
        path = args[args.index("--json") + 1]
        data = []
        for test_no, s, probs, vk in run_corpus(path):
            data.append({"test": test_no, "orbis": s,
                         "auto_befunde": probs, "vk_woerter": vk})
        print(json.dumps(data, ensure_ascii=False, indent=1))
    return 0


# =========================================================================
# TEIL 4 — STRICT-MODUS (CI-Baseline) UND L-09-SIMULATION
# =========================================================================
# Nachtrag Runde 2. Der Strict-Modus vergleicht die aktuellen Befunde mit
# einer Baseline bekannter Befunde (orbis_baseline.json): bekannte Befunde
# gelten als akzeptiert (dokumentiert im Audit), NEUE Befunde lassen den
# Lauf mit Exit-Code 1 scheitern. Die L-09-Simulation ist ein reines
# Entscheidungswerkzeug — sie legt KEINE Sprachregel fest.

BASELINE_PATH = "orbis_baseline.json"

def collect_findings(corpus_path=None):
    """Alle automatischen Befunde als stabile Signaturstrings."""
    sigs = set()
    for kind, w, cat, msg in run_lexicon():
        sigs.add(f"LEX|{kind}|{w}")
    for ref, s, probs in run_examples():
        for p in probs:
            sigs.add(f"EX|{ref}|{p.split(':')[0].strip()}|{p.split(':',1)[1].strip()[:40]}")
    if corpus_path:
        for test_no, s, probs, vk in run_corpus(corpus_path):
            for p in probs:
                sigs.add(f"KORPUS|Test{test_no}|{p[:60]}")
    # 360er-Matrix muss immer vollstaendig §5-konform sein
    for row in table_45():
        for f in row[2:]:
            if phonotactics_verdict(f)[0] != "ok":
                sigs.add(f"MATRIX|{f}|nicht §5-konform")
    return sigs

def run_strict(update=False, corpus_path="Orbis-Testkorpus-0_1.md"):
    import os
    current = collect_findings(corpus_path if os.path.exists(corpus_path) else None)
    if update:
        json.dump(sorted(current), open(BASELINE_PATH, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"Baseline geschrieben: {len(current)} bekannte Befunde -> {BASELINE_PATH}")
        return 0
    try:
        baseline = set(json.load(open(BASELINE_PATH, encoding="utf-8")))
    except FileNotFoundError:
        print(f"FEHLER: {BASELINE_PATH} fehlt. Mit --update-baseline erzeugen.")
        return 1
    new = sorted(current - baseline)
    fixed = sorted(baseline - current)
    print(f"Strict-Lauf: {len(current)} Befunde aktuell, {len(baseline)} in der Baseline.")
    if fixed:
        print(f"{len(fixed)} Baseline-Befunde nicht mehr vorhanden (behoben?):")
        for s in fixed: print("  -", s)
    if new:
        print(f"NEUE BEFUNDE ({len(new)}) — nicht in der Baseline:")
        for s in new: print("  -", s)
        return 1
    print("Keine neuen Befunde. OK.")
    return 0

# --- L-09: deterministische Silbifizierung (SIMULATION) -------------------
def pref_syllabify(word, mode="max"):
    """Deterministische Zerlegung nach Kandidatenregel:
    1. Diphthong-Vorrang: an jeder Vokalstelle wird der laengste Nukleus
       (Diphthong vor Einzelvokal) gewaehlt.
    2. Onset-Zuweisung fuer jede Konsonantengruppe zwischen zwei Nuklei:
       mode='max' -> maximal zulaessiger Onset der Folgesilbe (2 wenn in
       §5.2-Liste, sonst 1); mode='min' -> genau 1 Konsonant als Onset,
       Rest als Coda.
    Wortinitiale Gruppe = ganz Onset, wortfinale Gruppe = ganz Coda.
    Liefert (parse, fehler): parse als [(onset,nukleus,coda), ...] oder None."""
    # Kette in Nuklei und Konsonantengruppen zerlegen (Diphthong-Vorrang)
    units = []; i = 0
    while i < len(word):
        if word[i] in VOWELS:
            if word[i:i+2] in DIPHTHONGS:
                units.append(("V", word[i:i+2])); i += 2
            else:
                units.append(("V", word[i])); i += 1
        elif word[i] in CONSONANTS:
            j = i
            while j < len(word) and word[j] in CONSONANTS: j += 1
            units.append(("K", word[i:j])); i = j
        else:
            return None, f"fremdes Zeichen {word[i]!r}"
    sylls = []; onset = ""
    for idx, (kind, seg) in enumerate(units):
        if kind == "K":
            if idx == 0:
                onset = seg
                if len(onset) > 2 or (len(onset) == 2 and onset not in ONSETS2):
                    return None, f"Anlautgruppe {onset!r} unzulaessig"
            elif idx == len(units) - 1:
                if not sylls: return None, "keine Silbe vor Endgruppe"
                if len(seg) > 2: return None, f"Endgruppe {seg!r} zu lang"
                if len(seg) == 2 and not coda_pair_ok(seg):
                    return None, f"Endgruppe {seg!r} unzulaessig (§5.3)"
                o, n, c = sylls[-1]
                if c: return None, "Coda-Kollision"
                sylls[-1] = (o, n, seg)
            else:
                take = 0
                if mode == "max":
                    if len(seg) >= 2 and seg[-2:] in ONSETS2: take = 2
                    elif seg[-1] in CONSONANTS: take = 1
                else:
                    take = 1
                coda = seg[:len(seg) - take]; onset = seg[len(seg) - take:]
                if len(coda) > 2: return None, f"Restcoda {coda!r} zu lang"
                if len(coda) == 2 and not coda_pair_ok(coda):
                    return None, f"Restcoda {coda!r} unzulaessig (§5.3)"
                if coda:
                    o, n, c = sylls[-1]
                    if c: return None, "Coda-Kollision"
                    sylls[-1] = (o, n, coda)
        else:
            sylls.append((onset, seg, "")); onset = ""
    if onset and not sylls:
        return None, "kein Nukleus"
    return sylls, None

def run_sim_l09():
    print("== L-09-SIMULATION (KEINE SPRACHREGEL) ==")
    print("Kandidatenregel: Diphthong-Vorrang + Onset-Zuweisung.")
    print("Variante A = Onset-Maximierung (§5.2-Cluster bevorzugt),")
    print("Variante B = Minimal-Onset (genau 1 Konsonant, Rest Coda).\n")
    stats = {"A": 0, "B": 0, "fail_A": [], "fail_B": [], "diff": []}
    amb_resolved = 0; amb_total = 0
    for w, cat, parses, verd in manus_report_data():
        ambiguous = "AMBIGUITÄT" in verd
        if ambiguous: amb_total += 1
        pa, ea = pref_syllabify(w, "max")
        pb, eb = pref_syllabify(w, "min")
        if pa: stats["A"] += 1
        else: stats["fail_A"].append((w, ea))
        if pb: stats["B"] += 1
        else: stats["fail_B"].append((w, eb))
        if pa and ambiguous: amb_resolved += 1
        if pa and pb and pa != pb:
            stats["diff"].append((w, fmt_parse(pa).split("  ")[0], fmt_parse(pb).split("  ")[0]))
    total = len(manus_report_data())
    print(f"Variante A loest {stats['A']}/{total} Grundformen eindeutig; Fehlschlaege: {len(stats['fail_A'])}")
    for w, e in stats["fail_A"]: print(f"   A-FAIL {w}: {e}")
    print(f"Variante B loest {stats['B']}/{total}; Fehlschlaege: {len(stats['fail_B'])}")
    for w, e in stats["fail_B"]: print(f"   B-FAIL {w}: {e}")
    print(f"\nVon den {amb_total} bisher mehrdeutigen Formen loest Variante A: {amb_resolved}.")
    print(f"\nFormen, bei denen A und B VERSCHIEDEN entscheiden ({len(stats['diff'])}) — hier liegt die eigentliche Designentscheidung:")
    for w, a, b in stats["diff"]:
        print(f"   {w}:  A {a}   |   B {b}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
