#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extract_language_data.py — Migration Phase 5

Extrahiert die in `orbis_validator.py` (TEIL 1) hartkodierten Regeldaten
1:1 in maschinenlesbare JSON-Dateien unter `language/`.

WICHTIG: Dieses Werkzeug erfindet KEINE Regeln. Es liest ausschliesslich die
bereits vorhandenen Datenstrukturen des Validators aus, die ihrerseits 1:1 aus
Orbis-Grammatik-0.9.3.md uebernommen wurden. Wo die Grammatik schweigt, traegt
der Datensatz einen Status ("open", "conflict", "unclear") mit Befund-ID statt
einer erfundenen Regel.

Aufruf:  python3 tools/migration/extract_language_data.py
"""

import json, os, sys, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LANG = os.path.join(ROOT, "language")

def load_validator():
    spec = importlib.util.spec_from_file_location(
        "orbis_validator", os.path.join(ROOT, "orbis_validator.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def write(relpath, payload):
    path = os.path.join(LANG, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return relpath

HEAD = {
    "quelle": "Orbis-Grammatik-0.9.3.md",
    "erzeugt_von": "tools/migration/extract_language_data.py",
    "hinweis": "Maschinenlesbare Fassung bestehender Regeln. Keine neuen Regeln. "
               "Bei Abweichung zur Grammatik gilt die Grammatik (Befund melden).",
}

def meta(paragraph, rule_id, status="canonical", findings=None):
    d = dict(HEAD)
    d.update({"paragraph": paragraph, "regel_id": rule_id, "status": status})
    if findings:
        d["befunde"] = findings
    return d


def main():
    v = load_validator()
    written = []

    # ---------------- METADATA ----------------
    written.append(write("metadata/language.json", {
        **HEAD,
        "name": "Orbis",
        "primary_language": "de",
        "secondary_documentation_language": "en",
        "sprachpolitik": "Deutsch ist semantische Autoritaet. Englisch wird aus der "
                         "deutschen kanonischen Bedeutung abgeleitet und darf sie nicht veraendern.",
        "versionen": {
            "grammar": "0.9.3", "lexicon": "0.1", "manus": "0.x",
            "keyboard": "0.x", "corpus": "0.1", "tools": "0.2",
        },
        "id_praefixe": {
            "lexem": "ORB-LEX-", "konzept": "ORB-CON-", "satz": "ORB-SENT-",
            "regel_phonologie": "ORB-GRAM-PHON-", "regel_morphologie": "ORB-GRAM-MOR-",
            "regel_syntax": "ORB-GRAM-SYN-", "manus": "ORB-MANUS-",
            "entscheidung": "ORB-ADR-", "befund": "ORB-FIND-",
        },
        "status_werte": {
            "lexem": ["draft", "proposed", "review", "canonical", "deprecated",
                      "historical", "experimental", "rejected"],
            "regel": ["canonical", "provisional", "open", "conflict",
                      "deprecated", "experimental"],
            "uebersetzung": ["missing", "draft", "derived", "reviewed"],
        },
    }))

    # ---------------- PHONOLOGIE ----------------
    KONS_GRUPPEN = [
        ("stimmlose_verschlusslaute", ["p", "t", "k"]),
        ("stimmhafte_verschlusslaute", ["b", "d", "g"]),
        ("affrikate", ["ç"]),
        ("stimmlose_reibelaute", ["f", "s", "ş", "x"]),
        ("stimmhafte_reibelaute", ["v", "z", "j"]),
        ("nasale", ["m", "n", "ñ"]),
        ("fliesslaute", ["l", "r"]),
    ]
    written.append(write("phonology/phonemes.json", {
        **meta("§2.1–2.2", "ORB-GRAM-PHON-001"),
        "konsonanten": {"anzahl": len(v.CONSONANTS),
                        "gruppen": {k: val for k, val in KONS_GRUPPEN},
                        "alle": sorted(v.CONSONANTS)},
        "vokale": {"anzahl": len(v.VOWELS), "alle": sorted(v.VOWELS),
                   "hinweis": "voll, kein Schwa (§2.2)"},
        "nicht_vorhanden": ["h", "w", "th", "pf", "ts", "ng (als eigener Laut)"],
        "klanggruppen": {
            "paragraph": "§3.2",
            "fliesslaute": ["l", "r", "n", "m", "ñ", "v", "z", "s", "j"],
            "haertelaute": ["p", "t", "k", "b", "d", "g", "f", "x", "ş", "ç"],
        },
    }))
    written.append(write("phonology/diphthongs.json", {
        **meta("§2.3", "ORB-GRAM-PHON-002"),
        "diphthonge": [
            {"form": "ai", "status": "attested"}, {"form": "au", "status": "attested"},
            {"form": "ei", "status": "attested"}, {"form": "ui", "status": "attested"},
            {"form": "eu", "status": "attested",
             "hinweis": "nur durch ein Wort belegt (breun)"},
            {"form": "oi", "status": "allowed",
             "hinweis": "regulaer und schreibbar, derzeit unbelegt"},
            {"form": "ou", "status": "open",
             "hinweis": "[NOCH ZU ENTSCHEIDEN] in 0.9.3 ausdruecklich offen — "
                        "nicht verwenden, bis entschieden"},
        ],
        "im_validator_aktiv": v.DIPHTHONGS,
    }))
    written.append(write("phonology/onsets.json", {
        **meta("§5.2", "ORB-GRAM-PHON-003"),
        "max_konsonanten": 2,
        "erlaubte_zweiergruppen": sorted(v.ONSETS2),
        "anzahl": len(v.ONSETS2),
        "regel": "Drei und mehr Konsonanten im Anlaut sind ausnahmslos verboten.",
    }))
    written.append(write("phonology/codas.json", {
        **meta("§5.3", "ORB-GRAM-PHON-004"),
        "max_konsonanten": 2,
        "bedingungen": {
            "a_erster_laut": sorted(v.CODA_FIRST_OK),
            "b_zweiter_laut": v.CODA_SECOND_S,
            "c_feste_gruppen": sorted(v.CODA_PAIRS_C),
        },
        "regel": "Eine Zweiergruppe ist erlaubt, wenn (a) der erste Laut ein "
                 "Fliesslaut oder Nasal ist, ODER (b) der zweite Laut s ist, "
                 "ODER (c) die Gruppe in der festen Liste steht.",
    }))
    written.append(write("phonology/syllable_shapes.json", {
        **meta("§5.1", "ORB-GRAM-PHON-005", status="conflict", findings=["K-01"]),
        "in_grammatik_gelistet": sorted(v.SYLLABLE_SHAPES_STRICT),
        "faktisch_benoetigt_aber_nicht_gelistet": ["VK", "VKK", "KKVKK"],
        "konflikt": {
            "befund": "K-01",
            "beschreibung": "Der eingefrorene Wortschatz und die Beispielsaetze der "
                            "Grammatik verwenden VK/VKK (aul, eird, est, ain, oñ) und "
                            "KKVKK (granz, trelm, vresn, skirm, prilm, prens-, dremn-, "
                            "vlent-). §5.1 fuehrt diese Formen nicht.",
            "aufloesung": "offen — Designerentscheidung (Redaktionskandidat fuer 0.9.4)",
        },
        "hinweis": "Werkzeuge pruefen strikt gegen die gelistete Menge und melden "
                   "Abweichungen als K-01, statt die Liste stillschweigend zu erweitern.",
    }))
    written.append(write("phonology/syllabification.json", {
        **meta("§5, §26", "ORB-GRAM-PHON-006", status="open", findings=["L-09"]),
        "regel": None,
        "beschreibung": "Es existiert KEINE Silbifizierungs-Praeferenzregel. §5 legt "
                        "erlaubte Silbenformen fest, aber nicht, wie eine Lautkette "
                        "zerlegt wird.",
        "auswirkung": "77 von 281 Grundformen sind mehrdeutig zerlegbar; blockiert einen "
                      "deterministischen Manus-Composer.",
        "simulationen": "tools/validator (--sim-l09) und tests/manus — Analysewerkzeuge, "
                        "KEINE Sprachregeln.",
    }))
    written.append(write("phonology/stress.json", {
        **meta("§23", "ORB-GRAM-PHON-007"),
        "grundregel": "vorletzte Silbe",
        "ausnahmen": [
            {"muster": "-uma", "regel": "Stammbetonung"},
            {"muster": "-isto", "regel": "Stammbetonung"},
            {"muster": "15 Kernwoerter", "regel": "letzte Silbe"},
            {"muster": "Zusammensetzungen", "regel": "erstes Glied"},
            {"muster": "Vorsilben", "regel": "unbetont"},
        ],
        "vorhersagbarkeit_laut_grammatik": "ca. 85 %",
    }))

    # ---------------- MORPHOLOGIE ----------------
    written.append(write("morphology/cases.json", {
        **meta("§8", "ORB-GRAM-MOR-001"),
        "kasus": [
            {"name": "nom", "marker": v.CASE_MARKERS["nom"], "bezeichnung": "Nominativ"},
            {"name": "akk", "marker": v.CASE_MARKERS["akk"], "bezeichnung": "Akkusativ"},
            {"name": "dat", "marker": v.CASE_MARKERS["dat"], "bezeichnung": "Dativ"},
            {"name": "gen", "marker": v.CASE_MARKERS["gen"], "bezeichnung": "Genitiv"},
        ],
        "aufbau": "Stamm + Klassenkonsonant + Themavokal + Kasusmarker",
    }))
    written.append(write("morphology/noun_classes.json", {
        **meta("§6–§7", "ORB-GRAM-MOR-002"),
        "klassenkonsonanten": v.CLASS_CONS,
        "themavokale": list(v.THEMA_VOWELS),
        "endungen": [{"endung": e,
                      "genus": v.GENDER_OF_CONS[e[0]],
                      "unterklasse": v.SUBCLASS_OF_CONS[e[0]]}
                     for e in sorted(v.ALL_45_ENDINGS)],
        "anzahl_endungen": len(v.ALL_45_ENDINGS),
        "merksatz": "r-k-d maennlich, l-v-m weiblich, n-s-t saechlich",
        "unterklassen_bedeutung": {"status": "open",
                                   "hinweis": "§7.4: Tendenz; endgueltige Funktion "
                                              "[NOCH ZU ENTSCHEIDEN]"},
    }))
    written.append(write("morphology/plural.json", {
        **meta("§9, §10.3", "ORB-GRAM-MOR-003", findings=["U-09"]),
        "regulaer": {"marker": "ñ",
                     "position": "zwischen Themavokal und Kasusmarker",
                     "obliquer_echovokal": "Themavokal des Nomens; bei Artikel und "
                                           "Adjektiv immer a",
                     "unklarheit": {"befund": "U-09",
                                    "beschreibung": "Der Begriff Echovokal ist nirgends "
                                                    "definiert; er ergibt sich nur aus "
                                                    "den Tabellen."}},
        "kernwoerter": {"marker": "ei", "hinweis": "§9/§10.3, den 15 Kernwoertern vorbehalten"},
        "zehn_prozent_gruppe": {"status": "open", "befund": "L-07",
                                "beschreibung": "Plural der Gruppe velkran/soralm/prilm "
                                                "ist nicht geregelt."},
    }))
    written.append(write("morphology/core_nouns.json", {
        **meta("§10.2–§10.3, §24.1", "ORB-GRAM-MOR-004"),
        "anzahl": len(v.CORE_NOUNS),
        "deklination": {"singular": "Stamm + Bindevokal -e- + Kasusmarker "
                                    "(Nominativ endungslos)",
                        "plural": "Stamm + -ei- + Kasusmarker",
                        "hinweis": "Bindevokal immer -e- (aulan, eirdas sind ausdruecklich falsch)"},
        "woerter": [{"lemma": w, "genus": g, "bedeutung_de": b}
                    for w, (g, b) in v.CORE_NOUNS.items()],
    }))
    written.append(write("morphology/tenpct_nouns.json", {
        **meta("§10.1", "ORB-GRAM-MOR-005", status="provisional", findings=["L-07"]),
        "beschreibung": "Endvokal geschwunden; Geschlecht am Restkonsonanten erkennbar.",
        "deklination_singular": "Stamm + Bindevokal -e- + Kasusmarker",
        "deklination_plural": {"status": "open", "befund": "L-07"},
        "woerter": [{"lemma": w, "genus": g, "bedeutung_de": b}
                    for w, (g, b) in v.TENPCT_NOUNS.items()],
    }))
    written.append(write("morphology/articles.json", {
        **meta("§11", "ORB-GRAM-MOR-006"),
        "aufbau": "Bestimmtheitszeichen (x- bestimmt / v- unbestimmt) + "
                  "Geschlechtskonsonant der A-Reihe (r/l/n) + -a + Kasusmarker",
        "geschlechtskonsonanten": {"M": "r", "F": "l", "N": "n"},
        "kein_unbestimmter_plural": True,
        "zeigt_nur_genus": "Der Artikel zeigt nie die Unterklasse (§11.3, immer A-Reihe).",
        "formen": [{"form": f, "bestimmtheit": d, "genus": g, "kasus": c, "numerus": n}
                   for f, (d, g, c, n) in sorted(v.ARTICLES.items())],
    }))
    written.append(write("morphology/adjectives.json", {
        **meta("§12", "ORB-GRAM-MOR-007", findings=["U-02", "U-13", "K-04"]),
        "attributiv": {"aufbau": "Stamm + r/l/n + a + Kasus-/Pluralmarker",
                       "fugenregel": "identische Konsonanten an der Fuge verschmelzen "
                                     "(§21.4): şaln+na → şalna"},
        "praedikativ": {"regel": "Grundform, unveraendert, auch im Plural",
                        "nach": ["esex", "vurnex", "stanex"],
                        "unklarheit": {"befund": "U-13",
                                       "beschreibung": "Alle Beispiele stellen das "
                                                       "Praedikativ VOR das Verb; das "
                                                       "Verhaeltnis zur V2-Regel ist ungesagt."}},
        "steigerung": {"komparativ_infix": v.COMPARISON_INFIXES["komp"],
                       "superlativ_infix": v.COMPARISON_INFIXES["sup"],
                       "vergleichswoerter": {"kon": "als", "zil": "wie"},
                       "kasus_nach_vergleich": {"status": "unclear", "befund": "U-06"}},
        "adverb": {"suffix": "un", "paragraph": "§12.4",
                   "konflikt": {"befund": "K-04",
                                "beschreibung": "§25.1 verwendet tolm adverbial ohne -un."}},
        "nominalisierung": {"-ru": "M-A Person m", "-la": "F-A Person f",
                            "-te": "N-C Sache", "partizip": "-ut + -te → -ute"},
        "partizip_attributiv": {"status": "unclear", "befund": "U-02"},
        "grundadjektive": [{"lemma": w, "bedeutung_de": b} for w, b in v.ADJECTIVES.items()],
    }))
    written.append(write("morphology/pronouns.json", {
        **meta("§13", "ORB-GRAM-MOR-008", findings=["L-02", "L-04", "L-06"]),
        "personalpronomen": sorted(
            [{"form": f, "person": p, "kasus": c} for f, (p, c) in v.PRONOUNS.items()],
            key=lambda d: (d["person"], d["kasus"])),
        "possessiv": {"regel": "Genitiv des Personalpronomens, nachgestellt (§13.3)"},
        "hoeflichkeitsform": {"pronomen": "şevar", "kongruenz": "3. Person Plural (§13.2)"},
        "demonstrativa": {"formen": v.DEMONSTRATIVES,
                          "deklination": {"status": "open", "befund": "L-06"}},
        "reflexiv": {"formen": sorted(v.REFLEXIVE),
                     "kasusformen": {"status": "open", "befund": "L-04"},
                     "personenbereich": {"status": "open", "befund": "L-04"}},
        "relativ": {"formen": sorted(v.RELATIVE),
                    "satzbau": {"status": "open", "befund": "L-02"},
                    "homonymie": "fai ist zugleich Konjunktion 'dass' (§20)"},
        "indefinita": {"formen": v.INDEFINITES,
                       "deklination": {"status": "open", "befund": "L-06"}},
        "fugenkonflikt": {"befund": "K-02",
                          "betroffen": ["killa", "dolla", "kella"],
                          "beschreibung": "unverschmolzene l+l-Fuge gegen §21.4"},
    }))
    written.append(write("morphology/verbs.json", {
        **meta("§14–§15", "ORB-GRAM-MOR-009"),
        "aufbau": "Wurzel + Tempusvokal + Personendung",
        "tempusvokale": v.TENSE_VOWELS,
        "personendungen": v.PERSON_ENDINGS,
        "infinitiv_suffix": "ex",
        "partizip_suffix": "ut",
        "imperativ": {"du": "bloße Wurzel", "ihr": "-eñ",
                      "hoeflich": "3. Pl. Praesens",
                      "stuetz_e": "bei nach §5.3 unzulaessiger Endgruppe (Suvre!)",
                      "unklarheit": {"befund": "U-12",
                                     "beschreibung": "Stuetz-e prueft §5.3, nicht §5.1; "
                                                     "Dremn!/Prens!/Vlent! haetten KKVKK-Form."}},
        "vorsilben": v.VERB_PREFIXES,
        "regulaere_wurzeln": [{"wurzel": w, "bedeutung_de": b}
                              for w, b in v.REGULAR_VERB_ROOTS.items()],
    }))
    written.append(write("morphology/irregular_verbs.json", {
        **meta("§15.2", "ORB-GRAM-MOR-010", status="canonical", findings=["U-01"]),
        "anzahl": len(v.IRREGULAR_VERBS),
        "beschreibung_laut_grammatik": "Ablautstamm + Bindevokal -e- + Personendung",
        "unklarheit": {"befund": "U-01",
                       "beschreibung": "Die Formel deckt es- (suppletiv: em/eş/est, "
                                       "vo+Endung ohne -e-, Futurstamm vai-) sowie die "
                                       "kontrahierten Praesensstaemme nu-/vur- nicht. "
                                       "Massgeblich sind die belegten Tabellen."},
        "verben": {root: {"infinitiv": d["inf"], "bedeutung_de": d["bedeutung"],
                          "praesens": d["präs"], "vergangenheit": d["vgh"],
                          "zukunft": d["fut"]}
                   for root, d in v.IRREGULAR_VERBS.items()},
    }))
    written.append(write("morphology/modals.json", {
        **meta("§16.1", "ORB-GRAM-MOR-011", findings=["U-03", "K-05"]),
        "wurzeln": [{"wurzel": w, "bedeutung_de": b} for w, b in v.MODAL_ROOTS.items()],
        "konstruktion": "konjugiertes Modalverb auf Position 2, Vollverb im Infinitiv "
                        "am Satzende (Verbklammer)",
        "vollverbgebrauch": {"status": "unclear", "befund": "U-03"},
        "im_nebensatz": {"status": "conflict", "befund": "K-05",
                         "beschreibung": "§16.1 (Infinitiv am Satzende) und §17.2 "
                                         "(finites Verb am Ende) beanspruchen dieselbe Position."},
        "imperativ": "Modalverben bilden im Normalfall keinen Imperativ (§14).",
    }))
    written.append(write("morphology/word_formation.json", {
        **meta("§21", "ORB-GRAM-MOR-012", findings=["K-02", "K-03", "U-08"]),
        "suffixe": {"-ex": "Verb", "-ru": "Person m", "-la": "Person f", "-na": "Ort",
                    "-isto": "Werkzeug", "-vi": "Eigenschaft", "-uma": "Abstraktum"},
        "vorsilben": {"şu-": "Passiv", "xa-": "Gegenteil", "re-": "wieder",
                      "dra-": "ganz/hindurch", "su-": "halb"},
        "zusammensetzung": {"regel": "Bestimmungswort + Grundwort; Geschlecht und Klasse "
                                     "nach dem letzten Glied",
                            "unklarheit": {"befund": "U-08",
                                           "beschreibung": "Deklination bei Kernwort-Kopf "
                                                           "(taivbreun) ungeregelt"}},
        "fugenregel": {"paragraph": "§21.4",
                       "regel": "Identische Konsonanten an der Morphemfuge verschmelzen; "
                                "gilt fuer Zusammensetzungen, Ableitungen und Endungen.",
                       "konflikte": [{"befund": "K-02", "formen": ["killa", "dolla", "kella"]},
                                     {"befund": "K-03", "formen": ["telnxelmmern"]}]},
    }))
    written.append(write("morphology/numbers.json", {
        **meta("§24.8", "ORB-GRAM-MOR-013", findings=["L-08", "K-03"]),
        "kardinalzahlen": [{"lemma": w, "wert": n} for w, n in v.NUMBERS.items()],
        "komposita_belegt": [{"lemma": w, "wert": n} for w, n in v.NUMBER_COMPOUNDS.items()],
        "ordinalzahl_infix": v.ORDINAL_INFIX,
        "syntax": {"status": "open", "befund": "L-08",
                   "beschreibung": "Kongruenz und Numerus des gezaehlten Nomens ungeregelt."},
    }))

    # ---------------- SYNTAX ----------------
    written.append(write("syntax/prepositions.json", {
        **meta("§19", "ORB-GRAM-SYN-001"),
        "praepositionen": [{"lemma": p, "kasus": sorted(c),
                            "typ": "wechsel" if len(c) > 1 else "fest"}
                           for p, c in sorted(v.PREPOSITIONS.items())],
        "wechselregel": "Dativ bei Ort, Akkusativ bei Richtung",
    }))
    written.append(write("syntax/conjunctions.json", {
        **meta("§20", "ORB-GRAM-SYN-002", findings=["U-07"]),
        "nebenordnend": [{"lemma": k, "bedeutung_de": b, "stellung": "Hauptsatzstellung"}
                         for k, b in v.CONJ_COORD.items()],
        "unterordnend": [{"lemma": k, "bedeutung_de": b, "stellung": "Verbendstellung"}
                         for k, b in v.CONJ_SUB.items()],
        "unklarheit": {"befund": "U-07",
                       "beschreibung": "Die Behauptung 'systematisch aus Praepositionen "
                                       "+ -i abgeleitet' trifft auf dremi, tund und fai nicht zu."},
    }))
    written.append(write("syntax/rules.json", {
        **meta("§17–§18", "ORB-GRAM-SYN-003",
               findings=["L-01", "L-02", "K-05", "U-04", "U-05", "U-11", "U-13"]),
        "regeln": [
            {"id": "ORB-GRAM-SYN-010", "name": "Hauptsatz V2", "paragraph": "§17.1",
             "status": "canonical",
             "beschreibung": "Das finite Verb steht im Aussagehauptsatz an zweiter Position."},
            {"id": "ORB-GRAM-SYN-011", "name": "Nebensatz Verbendstellung",
             "paragraph": "§17.2", "status": "canonical",
             "beschreibung": "Im Nebensatz steht das finite Verb am Ende."},
            {"id": "ORB-GRAM-SYN-012", "name": "Nebensatz im Vorfeld", "paragraph": "§17.1",
             "status": "canonical",
             "beschreibung": "Steht ein Nebensatz auf Position 1, folgt das finite Verb "
                             "des Hauptsatzes unmittelbar."},
            {"id": "ORB-GRAM-SYN-013", "name": "Verbklammer", "paragraph": "§17.3",
             "status": "canonical", "einschraenkung": "im Nebensatz ungeklaert (K-05)",
             "beschreibung": "Modalverb Position 2, Infinitiv am Satzende."},
            {"id": "ORB-GRAM-SYN-014", "name": "Satzgliedfolge", "paragraph": "§17.4",
             "status": "provisional",
             "beschreibung": "Zeit – Grund – Art – Ort; ausdrueckliche Tendenz, keine harte Regel."},
            {"id": "ORB-GRAM-SYN-015", "name": "Keine Kopula-Auslassung", "paragraph": "§17.5",
             "status": "canonical", "beschreibung": "Die Kopula wird nicht ausgelassen."},
            {"id": "ORB-GRAM-SYN-016", "name": "Ja/Nein-Frage V1", "paragraph": "§18.1",
             "status": "canonical", "beschreibung": "Das finite Verb steht an Position 1."},
            {"id": "ORB-GRAM-SYN-017", "name": "W-Frage", "paragraph": "§18.2",
             "status": "canonical", "einschraenkung": "Kasusformen von kem/kelt fehlen (L-03)",
             "beschreibung": "Fragewort Position 1, finites Verb Position 2."},
            {"id": "ORB-GRAM-SYN-018", "name": "Negation", "paragraph": "§18.3",
             "status": "canonical",
             "beschreibung": "Partikel xa unmittelbar vor dem finiten Verb; attributiv xan-."},
            {"id": "ORB-GRAM-SYN-019", "name": "Passiv", "paragraph": "§16.3",
             "status": "provisional", "einschraenkung": "Agens undefiniert (L-05)",
             "beschreibung": "Vorsilbe şu-; Zustandspassiv Partizip + esex."},
            {"id": "ORB-GRAM-SYN-020", "name": "Moeglichkeitsform mai", "paragraph": "§16.2",
             "status": "canonical",
             "beschreibung": "Partikel mai unmittelbar vor dem finiten Verb; "
                             "mai + Verb bilden eine Satzposition."},
            {"id": "ORB-GRAM-SYN-021", "name": "Genitivattribut-Stellung", "paragraph": "§8, §17",
             "status": "open", "befund": "L-01",
             "beschreibung": "Nicht festgelegt. Alle Beispiele stellen nach; §13.3 regelt "
                             "nur das Possessiv."},
            {"id": "ORB-GRAM-SYN-022", "name": "Relativsatz", "paragraph": "§13.4",
             "status": "open", "befund": "L-02",
             "beschreibung": "Kein Satzbau definiert (Kasus, Kongruenz, Verbstellung)."},
            {"id": "ORB-GRAM-SYN-023", "name": "Objektreihenfolge", "paragraph": "§17",
             "status": "provisional", "befund": "U-05",
             "beschreibung": "Dativ vor Akkusativ ist Beispielpraxis, keine Regel."},
            {"id": "ORB-GRAM-SYN-024", "name": "Subjektauslassung", "paragraph": "§18",
             "status": "open", "befund": "U-04",
             "beschreibung": "Pro-Drop erscheint in Fragebeispielen, ist aber nicht geregelt."},
            {"id": "ORB-GRAM-SYN-025", "name": "Temporaler Dativ", "paragraph": "§25.2",
             "status": "unclear", "befund": "U-11",
             "beschreibung": "Vraş zaldreş als blosse Dativ-Zeitangabe ist nicht vorgesehen."},
        ],
    }))

    # ---------------- PROTO-ORBIS ----------------
    written.append(write("proto/sound_laws.json", {
        **meta("§22", "ORB-GRAM-PHON-020"),
        "hinweis": "Rein diachron (§4.3). Fuer synchrone Pruefungen ohne Wirkung.",
        "gesetze": [
            {"nr": 1, "name": "Endvokalschwund"}, {"nr": 2, "name": "Diphthongierung"},
            {"nr": 3, "name": "Erweichung"}, {"nr": 4, "name": "Assimilation"},
            {"nr": 5, "name": "Verlust vor Nasal"}, {"nr": 6, "name": "Ablaut"},
            {"nr": 7, "name": "Reduktion"},
        ],
        "arbeitsanweisung_neue_woerter": "Proto-Form → Lautgesetze → §3.3 (verbindlich) "
                                         "→ §3.4 (Klangrichtlinien)",
        "status_werte_etymologie": ["documented", "reconstructed", "provisional", "unknown"],
    }))

    print(f"{len(written)} Datendateien geschrieben:")
    for w in written:
        print("  language/" + w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
