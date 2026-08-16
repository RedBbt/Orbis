#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_lexicon.py — Migration Phase 6: Lexikon aufbauen.

Erzeugt aus dem bestehenden Wortschatz (Grammatik 0.9.3, gespiegelt in
orbis_validator.py) die Lexem- und Konzepteintraege nach
language/lexicon/lexicon.schema.json bzw. concept.schema.json.

GRENZEN (ORBIS_CONSTITUTION Art. 6, 8, 16):
- Keine neuen Woerter, keine neuen Bedeutungen.
- de.short ist die im Woerterbuch dokumentierte Glosse, unveraendert.
- de.definition ergaenzt ausschliesslich STRUKTURELLE Angaben aus der Grammatik
  (Wortart, Klasse, Ableitung, Fundstelle) — keine semantische Anreicherung.
  Ausformulierte Definitionen sind Designerarbeit; die Eintraege tragen dafuer
  qualitaet.offene_befunde = ["W-04"] (Definitionstiefe ausstehend).
- en wird aus de.short abgeleitet (TRANSLATION_POLICY), Status "derived".
- Etymologie bleibt "unknown", solange die Grammatik keine Herleitung nennt.
"""

import json, os, re, sys, importlib.util, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEXDIR = os.path.join(ROOT, "language", "lexicon")

def load_validator():
    spec = importlib.util.spec_from_file_location(
        "orbis_validator", os.path.join(ROOT, "orbis_validator.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

# ---------------------------------------------------------------------------
# Englische Entsprechungen der dokumentierten deutschen Glossen.
# Abgeleitet aus der deutschen kanonischen Bedeutung (TRANSLATION_POLICY §4).
# ---------------------------------------------------------------------------
EN = {
 "Mensch":"human being","Mutter":"mother","Vater":"father","Kind":"child","Wasser":"water",
 "Feuer":"fire","Sonne":"sun","Erde":"earth","Zeit":"time","Leben":"life","Tod":"death",
 "Welt":"world","Name":"name","Sprache":"language","Haus":"house","Freundschaft":"friendship",
 "Denkmal":"monument","Handwerk":"craft","Mann":"man","Freund":"friend","Tag":"day",
 "Wanderer":"wanderer","Sprecher":"speaker","Hund":"dog","Stein":"stone","Wind":"wind",
 "Vogel":"bird","Berg":"mountain","Fluss":"river","Traum":"dream","Sturm":"storm",
 "Frau":"woman","Hand":"hand","Stadt":"city","Blume":"flower","Wanderin":"wanderer (f.)",
 "Sprecherin":"speaker (f.)","Nacht":"night","Straße":"street","Flamme":"flame","Wolke":"cloud",
 "Stimme":"voice","Erinnerung":"memory","Freiheit":"freedom","Rede":"speech","Reise":"journey",
 "Auge":"eye","Herz":"heart","Weg":"way","Wald":"forest","Himmel":"sky",
 "Versammlungsort":"meeting place","Wort":"word","Feder":"feather","Brot":"bread","Buch":"book",
 "Fahrzeug":"vehicle","Instrument":"instrument","Jahr":"year","Wahrheit":"truth","Wille":"will",
 "Verlust":"loss","Vergänglichkeit":"transience","Entscheidung":"decision","Identität":"identity",
 "Konsequenz":"consequence","Liebe":"love","Dasein":"existence","Schule":"school","Kanal":"canal",
 "Kalender":"calendar",
 "sehen":"to see","hören":"to hear","sprechen":"to speak","essen":"to eat","trinken":"to drink",
 "schlafen":"to sleep","denken":"to think","nehmen":"to take","lieben":"to love","laufen":"to run",
 "schreiben":"to write","lesen":"to read","finden":"to find","warten":"to wait","bleiben":"to stay",
 "bewahren":"to preserve","verlieren (transitiv)":"to lose (transitive)",
 "vergehen (intransitiv)":"to pass away (intransitive)","entscheiden":"to decide","folgen":"to follow",
 "können":"can, to be able to","müssen":"must, to have to","dürfen":"may, to be allowed to",
 "sollen":"shall, ought to","wollen":"to want","mögen":"to like",
 "sein":"to be","haben":"to have","werden":"to become","gehen":"to go","kommen":"to come",
 "machen":"to make","wissen":"to know","geben":"to give",
 "groß":"big","klein":"small","gut":"good","schlecht":"bad","schön":"beautiful","alt":"old",
 "neu":"new","lang":"long","kurz":"short","warm":"warm","kalt":"cold","hell":"bright",
 "dunkel":"dark","stark":"strong","schwach":"weak","schnell":"fast","langsam":"slow",
 "wahr":"true","falsch":"false","kein":"no, none",
 "wer":"who","was":"what","wo/wohin":"where / where to","wann":"when","warum":"why","wie":"how",
 "heute":"today","morgen":"tomorrow","gestern":"yesterday","jetzt":"now","immer":"always",
 "nie":"never","hier":"here","dort":"there","wenig":"little, few","ja":"yes","nein":"no",
 "nicht":"not","würde":"would","als":"than","Hallo":"hello","Auf Wiedersehen":"goodbye",
 "Danke":"thank you","Bitte":"please",
 "und":"and","oder":"or","aber":"but","denn":"for, because","dass":"that","weil":"because",
 "wenn":"if, when","obwohl":"although","während":"while","bevor":"before","nachdem":"after",
 "jemand":"someone","niemand":"nobody","etwas":"something","nichts":"nothing",
 "dieser(m)":"this (m.)","diese(f)":"this (f.)","dieses(n)":"this (n.)",
 "jener(m)":"that (m.)","jene(f)":"that (f.)","jenes(n)":"that (n.)",
 "sich":"oneself","der/die/das":"who, which, that",
 "man (homonym: Mensch)":"one, people (homonym with kaun 'human being')",
 "sehr":"very",
}

DOMAENE = {
 "Mensch":"mensch","Mutter":"familie","Vater":"familie","Kind":"familie","Wasser":"natur",
 "Feuer":"natur","Sonne":"natur","Erde":"natur","Zeit":"zeit","Leben":"existenz","Tod":"existenz",
 "Welt":"natur","Name":"kommunikation","Sprache":"kommunikation","Haus":"wohnen",
 "Freundschaft":"beziehungen","Denkmal":"kultur","Handwerk":"arbeit","Mann":"mensch",
 "Freund":"beziehungen","Tag":"zeit","Wanderer":"mensch","Sprecher":"kommunikation",
 "Hund":"tiere","Stein":"natur","Wind":"wetter","Vogel":"tiere","Berg":"natur","Fluss":"natur",
 "Traum":"wahrnehmung","Sturm":"wetter","Frau":"mensch","Hand":"koerper","Stadt":"gesellschaft",
 "Blume":"pflanzen","Wanderin":"mensch","Sprecherin":"kommunikation","Nacht":"zeit",
 "Straße":"raum","Flamme":"natur","Wolke":"wetter","Stimme":"kommunikation",
 "Erinnerung":"denken","Freiheit":"abstrakta","Rede":"kommunikation","Reise":"bewegung",
 "Auge":"koerper","Herz":"koerper","Weg":"raum","Wald":"natur","Himmel":"natur",
 "Versammlungsort":"gesellschaft","Wort":"kommunikation","Feder":"tiere","Brot":"essen",
 "Buch":"kultur","Fahrzeug":"transport","Instrument":"werkzeug","Jahr":"zeit",
 "Wahrheit":"abstrakta","Wille":"denken","Verlust":"abstrakta","Vergänglichkeit":"abstrakta",
 "Entscheidung":"denken","Identität":"abstrakta","Konsequenz":"abstrakta","Liebe":"gefuehle",
 "Dasein":"existenz","Schule":"gesellschaft","Kanal":"raum","Kalender":"zeit",
}
DOM_VERB = {
 "sehen":"wahrnehmung","hören":"wahrnehmung","sprechen":"kommunikation","essen":"essen",
 "trinken":"essen","schlafen":"koerper","denken":"denken","nehmen":"bewegung","lieben":"gefuehle",
 "laufen":"bewegung","schreiben":"kommunikation","lesen":"kommunikation","finden":"wahrnehmung",
 "warten":"zeit","bleiben":"raum","bewahren":"abstrakta","verlieren (transitiv)":"abstrakta",
 "vergehen (intransitiv)":"zeit","entscheiden":"denken","folgen":"bewegung",
 "sein":"existenz","haben":"existenz","werden":"existenz","gehen":"bewegung","kommen":"bewegung",
 "machen":"arbeit","wissen":"denken","geben":"beziehungen",
}
DOM_ADJ = {
 "groß":"raum","klein":"raum","gut":"bewertung","schlecht":"bewertung","schön":"bewertung",
 "alt":"zeit","neu":"zeit","lang":"raum","kurz":"raum","warm":"wetter","kalt":"wetter",
 "hell":"wahrnehmung","dunkel":"wahrnehmung","stark":"koerper","schwach":"koerper",
 "schnell":"bewegung","langsam":"bewegung","wahr":"abstrakta","falsch":"abstrakta",
 "kein":"grammatik",
}

# §24.7 dokumentierte Gegensatzpaare (aus den deutschen Glossen ablesbar)
ANTONYME = [("vlaid","nirm"),("selv","morn"),("granz","zirv"),("trelm","misn"),
            ("velm","girn"),("luid","şaln"),("xarn","vresn"),("zilv","tolm"),
            ("klaun","norv")]

# §21.1 dokumentierte Wortfamilien
FAMILIEN = {
 "mel-": {"bedeutung": "gehen / sich fortbewegen",
          "mitglieder": ["melex","melru","mela","melna","melisto","melvi","meluma"],
          "quelle": "§21.1"},
 "tal-": {"bedeutung": "sprechen",
          "mitglieder": ["talex","talru","tala","talna","talisto","talvi","taluma"],
          "quelle": "§21.1"},
}

def slug(lemma):
    """Dateiname ohne Sonderzeichen, aber verlustfrei rueckfuehrbar ueber lemma-Feld."""
    repl = {"ş":"sh","ñ":"nn","ç":"ch"}
    return "".join(repl.get(c, c) for c in lemma)

KAS_EN = {"nom":"nominative","akk":"accusative","dat":"dative","gen":"genitive"}
NUM_EN = {"sg":"singular","pl":"plural"}
GEN_EN = {"M":"masculine","F":"feminine","N":"neuter"}

def en_of(de_gloss):
    """Englische Entsprechung. Fuer strukturelle Glossen (Artikel, Pronomen,
    Praepositionen, Zahlen) wird die Beschreibung uebersetzt, nicht geraten."""
    if de_gloss in EN: return EN[de_gloss]
    base = de_gloss.split(" (")[0].split(" —")[0].strip()
    if base in EN: return EN[base]
    m = re.match(r"^Artikel (bestimmt|unbestimmt) ([MFN]) (nom|akk|dat|gen) (sg|pl)$", de_gloss)
    if m:
        return (f"{'definite' if m.group(1)=='bestimmt' else 'indefinite'} article, "
                f"{GEN_EN[m.group(2)]} {KAS_EN[m.group(3)]} {NUM_EN[m.group(4)]}")
    m = re.match(r"^Personalpronomen (\S+) (nom|akk|dat|gen)$", de_gloss)
    if m:
        lbl = m.group(1).replace("sg", " sg.").replace("pl", " pl.").replace("-", " ")
        return f"personal pronoun, {lbl}, {KAS_EN[m.group(2)]}"
    m = re.match(r"^Praeposition mit (.+)$", de_gloss)
    if m:
        kas = " / ".join(KAS_EN.get(k, k) for k in m.group(1).split("/"))
        return f"preposition governing the {kas}"
    m = re.match(r"^Zahl (\d+)$", de_gloss)
    if m: return f"number {m.group(1)}"
    m = re.match(r"^welch- \(([MFN])\)$", de_gloss)
    if m: return f"which ({GEN_EN[m.group(1)]})"
    return None


def main():
    v = load_validator()
    entries, concepts = [], {}
    next_lex, next_con = 1, 1

    def concept_for(gloss, domaene, wortart):
        nonlocal next_con
        key = (gloss, wortart)
        if key in concepts:
            return concepts[key]["concept_id"]
        cid = f"ORB-CON-{next_con:06d}"; next_con += 1
        concepts[key] = {
            "concept_id": cid,
            "de": {"label": gloss,
                   "hauptdefinition": f"Bedeutungskonzept „{gloss}“ ({wortart}), "
                                      f"migriert aus dem Woerterbuch der Grammatik 0.9.3.",
                   "abgrenzung": None},
            "en": {"label": en_of(gloss), "definition": None,
                   "status": "derived" if en_of(gloss) else "missing"},
            "domaene": domaene,
            "oberbegriffe": [], "unterbegriffe": [], "verwandte": [], "gegensaetze": [],
            "lexeme": [], "status": "draft",
            "quelle": "Orbis-Grammatik-0.9.3.md §24",
        }
        return cid

    def add(lemma, wortart, gloss, *, kategorie=None, grammatik=None, domaene="unbestimmt",
            quelle=None, haeufigkeit="UNRATED", produktivitaet="unbekannt",
            definition_zusatz=None, konzept=True, befunde=None, register="neutral"):
        nonlocal next_lex
        lid = f"ORB-LEX-{next_lex:06d}"; next_lex += 1
        verdict, _ = v.phonotactics_verdict(lemma)
        strict = v.syllabify(lemma, v.SYLLABLE_SHAPES_STRICT)
        ext = v.syllabify(lemma, v.SYLLABLE_SHAPES_EXTENDED)
        parses = strict if strict else ext
        ambig = len(parses) > 1
        cids = []
        if konzept:
            cid = concept_for(gloss, domaene, wortart)
            concepts[(gloss, wortart)]["lexeme"].append(lid)
            cids = [cid]
        definition = f"{gloss}."
        if definition_zusatz:
            definition += " " + definition_zusatz
        definition += f" (Migrierte Woerterbuchglosse aus {quelle or '§24'}; " \
                      f"ausformulierte Definition steht aus.)"
        bef = list(befunde or [])
        if verdict != "ok" and verdict.startswith("nur-"):
            bef.append("K-01")
        if ambig:
            bef.append("L-09")
        e = {
            "lexeme_id": lid, "lemma": lemma, "status": "canonical",
            "eingefuehrt_in": "grammar-0.9.3", "letzte_aenderung": "2026-08-16",
            "wortart": wortart, "grammatische_kategorie": kategorie,
            "register": register,
            "haeufigkeit": haeufigkeit, "produktivitaet": produktivitaet,
            "domaenen": [domaene] if domaene != "unbestimmt" else [],
            "lernstufe": "unbestimmt",
            "de": {"short": gloss, "definition": definition,
                   "alternativen": [], "gebrauchshinweis": None},
            "en": {"short": en_of(gloss), "definition": None, "alternativen": [],
                   "usage_note": None,
                   "status": "derived" if en_of(gloss) else "missing"},
            "grammatik": grammatik or {},
            "phonologie": {
                "phonemfolge": list(lemma),
                "ipa": None,
                "silbifizierung": ["".join(s) for s in parses[0]] if len(parses) == 1 else None,
                "silbifizierung_kandidaten": ["·".join("".join(s) for s in p)
                                              for p in parses[:8]] if ambig else None,
                "betonung": None,
                "phonotaktik_status": "ok" if verdict == "ok"
                                      else ("K-01" if verdict.startswith("nur-") else "verstoss"),
            },
            "manus": {
                "silben": ["".join(s) for s in parses[0]] if len(parses) == 1 else None,
                "kompositionsdaten": None,
                "status": "provisional" if len(parses) == 1 else "blocked",
                "ambiguitaet": ambig,
                "ambiguitaet_anzahl": len(parses) if ambig else None,
                "befund": "L-09" if ambig else None,
            },
            "semantik": {"concept_ids": cids, "synonyme": [], "relationen": [],
                         "konnotation": None, "bedeutungsnuancen": []},
            "wortfamilie": {"wurzel": None, "family_id": None, "abgeleitete": [],
                            "komposita": [], "verwandte_wurzeln": []},
            "etymologie": {"status": "unknown", "proto_form": None, "zwischenformen": [],
                           "lautgesetze": [], "bedeutungsentwicklung": None,
                           "besonderheiten": None},
            "gebrauch": {"kollokationen": [], "typische_konstruktionen": [],
                         "typische_praepositionen": [], "typische_objekte": [],
                         "typische_subjekte": [], "stil": None, "bereich": None},
            "beispiele": [],
            "qualitaet": {"geprueft": True, "validatorstatus": "befund" if bef else "ok",
                          "offene_befunde": sorted(set(bef + ["W-04"])),
                          "letzte_pruefung": "2026-08-16",
                          "quelle": quelle or "§24"},
        }
        entries.append(e)
        return e

    # ---------------- Nomen: Kernwoerter ----------------
    for lemma, (genus, gloss) in v.CORE_NOUNS.items():
        formen = {f"{c}_{n}": v.decline_core_noun(lemma, c, n)
                  for n in ("sg", "pl") for c in v.CASES}
        add(lemma, "nomen", gloss, kategorie="kernwort", domaene=DOMAENE.get(gloss, "unbestimmt"),
            quelle="§24.1", haeufigkeit="CORE", produktivitaet="produktiv",
            definition_zusatz=f"Historisches Kernwort ({genus}); dekliniert mit Bindevokal -e- "
                              f"im Singular und -ei im Plural (§10.3).",
            grammatik={"genus": genus, "klasse": "kernwort", "unterklasse": None,
                       "themavokal": None, "deklination": "kernwort",
                       "kasusformen": formen, "plural": formen["nom_pl"],
                       "zaehlbarkeit": "unbestimmt"})

    # ---------------- Nomen: 10-Prozent-Gruppe ----------------
    for lemma, (genus, gloss) in v.TENPCT_NOUNS.items():
        formen = {f"{c}_sg": v.decline_tenpct_noun(lemma, c, "sg") for c in v.CASES}
        add(lemma, "nomen", gloss, kategorie="10prozent",
            domaene=DOMAENE.get(gloss, "unbestimmt"), quelle="§10.1",
            haeufigkeit="STANDARD",
            definition_zusatz=f"Gehoert zur 10-Prozent-Gruppe ({genus}): Endvokal geschwunden, "
                              f"Singular mit Bindevokal -e-; der Plural ist nicht geregelt (L-07).",
            befunde=["L-07"] ,
            grammatik={"genus": genus, "klasse": "10prozent", "unterklasse": None,
                       "themavokal": None, "deklination": "10prozent",
                       "kasusformen": formen, "plural": None})

    # ---------------- Nomen: regulaer ----------------
    for lemma, kb in v.REGULAR_NOUNS.items():
        klasse, gloss = kb.split(" ", 1)
        genus, sub = klasse.split("-")
        formen = {f"{c}_{n}": v.decline_regular_noun(lemma, c, n)
                  for n in ("sg", "pl") for c in v.CASES}
        quelle = "§24.6" if lemma.endswith("uma") and lemma != "şauluma" or lemma in (
            "klaunuma","nestuma","salvuma","vaşnuma","mirnuma","şauluma","tarnuma","saivuma",
            "virnuma") else ("§24.2" if genus == "M" else "§24.3" if genus == "F" else "§24.4")
        zusatz = f"Regulaeres Nomen der Klasse {klasse} (Themavokal -{lemma[-1]})."
        if lemma.endswith("uma"):
            zusatz += " Abstraktum auf -uma (§21.1/§24.6)."
        add(lemma, "nomen", gloss, kategorie="regulaer",
            domaene=DOMAENE.get(gloss, "unbestimmt"), quelle=quelle,
            definition_zusatz=zusatz,
            grammatik={"genus": genus, "klasse": klasse, "unterklasse": sub,
                       "themavokal": lemma[-1], "deklination": "regulaer",
                       "kasusformen": formen, "plural": formen["nom_pl"],
                       "zaehlbarkeit": "unzaehlbar" if lemma.endswith("uma") else "zaehlbar"})

    # ---------------- Nomen: Zusammensetzungen ----------------
    for lemma, (genus, gloss, note) in v.COMPOUND_NOUNS.items():
        kern = "Kernwort" in note
        formen = None if kern else {f"{c}_{n}": v.decline_regular_noun(lemma, c, n)
                                    for n in ("sg", "pl") for c in v.CASES}
        add(lemma, "nomen", gloss, kategorie="kompositum",
            domaene=DOMAENE.get(gloss, "unbestimmt"), quelle="§21.3",
            definition_zusatz=f"Zusammensetzung; {note}.",
            befunde=["U-08"] if kern else None,
            grammatik={"genus": genus, "klasse": "kompositum",
                       "deklination": "undefiniert" if kern else "regulaer",
                       "kompositionshinweis": note,
                       "kasusformen": formen, "plural": None if kern else formen["nom_pl"]})

    # ---------------- Verben ----------------
    for root, gloss in v.REGULAR_VERB_ROOTS.items():
        para = {t: {p: v.conj_regular(root, t, p) for p in v.PERSON_ENDINGS}
                for t in v.TENSE_VOWELS}
        trans = "transitiv" if "transitiv" in gloss and "intransitiv" not in gloss else (
                "intransitiv" if "intransitiv" in gloss else None)
        add(root, "verb", gloss, kategorie="vollverb", domaene=DOM_VERB.get(gloss, "unbestimmt"),
            quelle="§24.5", produktivitaet="produktiv",
            definition_zusatz="Regelmaessige Verbwurzel; konjugiert mit Tempusvokal "
                              "(-a- / -o- / -ai-) und Personendung (§14–§15).",
            grammatik={"verbwurzel": root, "konjugationsklasse": "regelmaessig",
                       "infinitiv": v.fuse(root, "ex"), "partizip": v.fuse(root, "ut"),
                       "kasusformen": None, "unregelmaessige_formen": para,
                       "transitivitaet": trans})
    for root, gloss in v.MODAL_ROOTS.items():
        para = {t: {p: v.conj_regular(root, t, p) for p in v.PERSON_ENDINGS}
                for t in v.TENSE_VOWELS}
        add(root, "verb", gloss, kategorie="modalverb", domaene="grammatik",
            quelle="§16.1", haeufigkeit="VERY_COMMON",
            definition_zusatz="Modalverb; steht auf Position 2, das Vollverb im Infinitiv am "
                              "Satzende (Verbklammer §16.1). Der Vollverbgebrauch ohne Infinitiv "
                              "ist ungeregelt (U-03); die Stellung im Nebensatz ist offen (K-05).",
            befunde=["U-03", "K-05"],
            grammatik={"verbwurzel": root, "konjugationsklasse": "modal",
                       "infinitiv": v.fuse(root, "ex"), "partizip": v.fuse(root, "ut"),
                       "unregelmaessige_formen": para})
    for root, d in v.IRREGULAR_VERBS.items():
        add(root, "verb", d["bedeutung"], kategorie="unregelmaessig",
            domaene=DOM_VERB.get(d["bedeutung"], "unbestimmt"), quelle="§15.2",
            haeufigkeit="CORE", produktivitaet="produktiv",
            definition_zusatz="Unregelmaessiges Verb; die belegten Tabellen sind massgeblich, "
                              "die Formelbeschreibung in §15.2 deckt sie nicht vollstaendig (U-01).",
            befunde=["U-01"],
            grammatik={"verbwurzel": root, "konjugationsklasse": "unregelmaessig",
                       "infinitiv": d["inf"], "partizip": v.fuse(root, "ut"),
                       "unregelmaessige_formen": {"praesens": d["präs"],
                                                  "vergangenheit": d["vgh"],
                                                  "zukunft": d["fut"]}})

    # ---------------- Adjektive ----------------
    for lemma, gloss in v.ADJECTIVES.items():
        add(lemma, "adjektiv", gloss, domaene=DOM_ADJ.get(gloss, "unbestimmt"),
            quelle="§24.7", produktivitaet="produktiv",
            definition_zusatz="Attributiv dekliniert (Stamm + r/l/n + a + Marker), praedikativ "
                              "in der Grundform (§12.1–§12.2); Adverb auf -un (§12.4).",
            grammatik={"steigerung": {"komparativ": v.adj_predicative(lemma, "komp"),
                                      "superlativ": v.adj_predicative(lemma, "sup")},
                       "kasusformen": {f"{g}_{c}_{n}": v.adj_attributive(lemma, g, c, n)
                                       for g in ("M", "F", "N")
                                       for c in v.CASES for n in ("sg", "pl")}})

    # ---------------- Funktionswoerter ----------------
    for lemma, cases in v.PREPOSITIONS.items():
        typ = "Wechselpraeposition" if len(cases) > 1 else "feste Praeposition"
        add(lemma, "praeposition", f"Praeposition mit {'/'.join(sorted(cases))}",
            domaene="grammatik", quelle="§19", konzept=False, haeufigkeit="VERY_COMMON",
            definition_zusatz=f"{typ}; verlangt {', '.join(sorted(cases))}"
                              + (" (Dativ bei Ort, Akkusativ bei Richtung)." if len(cases) > 1 else "."),
            grammatik={"rektion": sorted(cases)})
    for lemma, gloss in v.CONJ_COORD.items():
        add(lemma, "konjunktion", gloss, kategorie="nebenordnend", domaene="grammatik",
            quelle="§20", konzept=False, haeufigkeit="VERY_COMMON",
            definition_zusatz="Nebenordnend; der folgende Satz behaelt Hauptsatzstellung.")
    for lemma, gloss in v.CONJ_SUB.items():
        bef = ["U-07"] if lemma in ("dremi", "tund", "fai") else None
        zus = "Unterordnend; loest Verbendstellung aus (§17.2)."
        if lemma == "fai":
            zus += " Homonym mit dem Relativpronomen fai (L-02)."
        if bef:
            zus += " Die Ableitungsbehauptung in §20 trifft auf diese Form nicht zu (U-07)."
        add(lemma, "konjunktion", gloss, kategorie="unterordnend", domaene="grammatik",
            quelle="§20", konzept=False, haeufigkeit="VERY_COMMON",
            definition_zusatz=zus, befunde=bef)
    for lemma, gloss in v.W_WORDS.items():
        bef = ["L-03"] if lemma in ("kem", "kelt") else None
        add(lemma, "pronomen", gloss, kategorie="fragewort", domaene="grammatik",
            quelle="§18.2", haeufigkeit="VERY_COMMON", befunde=bef,
            definition_zusatz="Fragewort; steht auf Position 1, das finite Verb folgt (§18.2)."
                              + (" Kasusformen sind nicht definiert (L-03)." if bef else ""))
    for lemma, genus in v.W_ADJ.items():
        add(lemma, "pronomen", f"welch- ({genus})", kategorie="fragewort-adjektivisch",
            domaene="grammatik", quelle="§18.2", konzept=False,
            befunde=["K-02"] if lemma == "kella" else None,
            definition_zusatz="Kongruiert adjektivisch (Beispiel §18.2: Kellan sarlan milkoş?)."
                              + (" Die Form verletzt die Fugenregel (K-02)."
                                 if lemma == "kella" else ""))
    for lemma, gloss in v.DEMONSTRATIVES.items():
        add(lemma, "pronomen", gloss, kategorie="demonstrativ", domaene="grammatik",
            quelle="§13.4", konzept=False, befunde=["L-06"] + (["K-02"] if lemma in ("killa","dolla") else []),
            definition_zusatz="Nur die Grundform ist belegt; die Deklination ist nicht "
                              "definiert (L-06).")
    for lemma, gloss in v.INDEFINITES.items():
        add(lemma, "pronomen", gloss, kategorie="indefinit", domaene="grammatik",
            quelle="§13.4", konzept=False, befunde=["L-06"] + (["W-03"] if lemma == "kaun" else []),
            definition_zusatz="Nur die Grundform ist belegt; die Deklination ist nicht "
                              "definiert (L-06).")
    add("se", "pronomen", "sich", kategorie="reflexiv", domaene="grammatik", quelle="§13.4",
        konzept=False, befunde=["L-04"],
        definition_zusatz="Reflexivpronomen ohne definierte Kasusformen; auch der "
                          "Personenbereich ist offen (L-04).")
    add("fai", "pronomen", "der/die/das", kategorie="relativ", domaene="grammatik",
        quelle="§13.4", konzept=False, befunde=["L-02", "W-03"],
        definition_zusatz="Relativpronomen; der Relativsatzbau ist nicht definiert (L-02). "
                          "Formgleich mit der Konjunktion fai „dass“ (§20).")
    for lemma, wert in v.NUMBERS.items():
        add(lemma, "zahl", f"Zahl {wert}", domaene="zahlen", quelle="§24.8", konzept=False,
            befunde=["L-08"], haeufigkeit="COMMON",
            definition_zusatz=f"Kardinalzahl {wert}; Ordnungszahl mit Infix -ost- + "
                              f"Geschlechtsendung. Die Syntax der Kardinalzahlen ist "
                              f"ungeregelt (L-08).")
    for lemma, wert in v.NUMBER_COMPOUNDS.items():
        add(lemma, "zahl", f"Zahl {wert}", domaene="zahlen", quelle="§24.8", konzept=False,
            befunde=["L-08"] + (["K-03"] if lemma == "telnxelmmern" else []),
            definition_zusatz=f"Belegtes Zahlkompositum fuer {wert}."
                              + (" Die Form verletzt die Fugenregel (K-03)."
                                 if lemma == "telnxelmmern" else ""))
    for lemma, gloss in v.PARTICLES.items():
        clean = gloss.split(" (homonym")[0]
        bef = ["W-03"] if "homonym" in gloss else None
        kat = "grussformel" if lemma in ("selvai", "melai", "selves", "praum") else "partikel"
        add(lemma, "partikel", clean, kategorie=kat, domaene="grammatik", quelle="§24.9",
            konzept=False, befunde=bef, haeufigkeit="COMMON",
            definition_zusatz=("Formgleich mit einer anderen Wortform (W-03)." if bef else None))
    for form, (person, kasus) in sorted(v.PRONOUNS.items()):
        add(form, "pronomen", f"Personalpronomen {person} {kasus}", kategorie="personal",
            domaene="grammatik", quelle="§13.1", konzept=False, haeufigkeit="CORE",
            definition_zusatz="Vollstaendig dekliniert (§13.1); der Genitiv dient zugleich "
                              "als nachgestelltes Possessiv (§13.3).",
            grammatik={"kasusformen": {kasus: form}})
    for form, (best, genus, kasus, num) in sorted(v.ARTICLES.items()):
        add(form, "artikel", f"Artikel {best} {genus} {kasus} {num}", kategorie=best,
            domaene="grammatik", quelle="§11", konzept=False, haeufigkeit="CORE",
            befunde=["W-03"] if form == "vran" else None,
            definition_zusatz="Zeigt nur Geschlecht, nie die Unterklasse (§11.3)."
                              + (" Formgleich mit der Partikel vran „sehr“ (W-03)."
                                 if form == "vran" else ""),
            grammatik={"genus": genus, "kasusformen": {f"{kasus}_{num}": form}})

    # ---------------- Relationen nachtragen ----------------
    by_lemma = {e["lemma"]: e for e in entries}
    for a, b in ANTONYME:
        if a in by_lemma and b in by_lemma:
            by_lemma[a]["semantik"]["relationen"].append(
                {"typ": "antonym", "ziel": by_lemma[b]["lexeme_id"],
                 "anmerkung_de": "Gegensatzpaar aus dem Adjektivbestand §24.7."})
            by_lemma[b]["semantik"]["relationen"].append(
                {"typ": "antonym", "ziel": by_lemma[a]["lexeme_id"],
                 "anmerkung_de": "Gegensatzpaar aus dem Adjektivbestand §24.7."})
    familien = []
    for wurzel, d in FAMILIEN.items():
        stem = wurzel.rstrip("-")
        mitglieder = []
        for m in d["mitglieder"]:
            lex = by_lemma.get(m)
            if lex:
                mitglieder.append(lex["lexeme_id"])
                lex["wortfamilie"]["wurzel"] = wurzel
                lex["wortfamilie"]["family_id"] = "ORB-FAM-" + stem
            else:
                mitglieder.append({"form": m, "status": "abgeleitete Form, kein eigener Eintrag"})
        familien.append({"family_id": "ORB-FAM-" + stem, "wurzel": wurzel,
                         "grundbedeutung_de": d["bedeutung"], "quelle": d["quelle"],
                         "mitglieder": mitglieder,
                         "produktive_ableitungen": d["mitglieder"],
                         "blockierte_formen": [],
                         "semantische_veraenderungen": None})
    # Ableitungen im Kopf-Lexem eintragen
    for wurzel, d in FAMILIEN.items():
        stem = wurzel.rstrip("-")
        head = by_lemma.get(stem)
        if head:
            head["wortfamilie"]["abgeleitete"] = [m for m in d["mitglieder"]]
    for komp, (g, gloss, note) in v.COMPOUND_NOUNS.items():
        if komp in by_lemma:
            by_lemma[komp]["wortfamilie"]["komposita"] = [komp]

    # ---------------- Schreiben ----------------
    os.makedirs(os.path.join(LEXDIR, "entries"), exist_ok=True)
    os.makedirs(os.path.join(LEXDIR, "concepts"), exist_ok=True)
    belegt = {}
    for e in entries:
        base = slug(e["lemma"]); name = base
        i = 2
        while name in belegt:
            name = f"{base}__{i}"; i += 1
        belegt[name] = e["lexeme_id"]
        e["_datei"] = "entries/" + name + ".json"
        p = os.path.join(LEXDIR, "entries", name + ".json")
        payload = {k: val for k, val in e.items() if k != "_datei"}
        with open(p, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2); f.write("\n")
    con_list = sorted(concepts.values(), key=lambda c: c["concept_id"])
    with open(os.path.join(LEXDIR, "concepts", "concepts.json"), "w", encoding="utf-8") as f:
        json.dump({"anzahl": len(con_list), "quelle": "Orbis-Grammatik-0.9.3.md §24",
                   "hinweis": "Ein Konzept je dokumentierter Glosse. Feinere semantische "
                              "Differenzierung ist Designerarbeit.",
                   "concepts": con_list}, f, ensure_ascii=False, indent=2); f.write("\n")
    with open(os.path.join(LEXDIR, "word_families.json"), "w", encoding="utf-8") as f:
        json.dump({"anzahl": len(familien), "quelle": "§21.1",
                   "hinweis": "Nur die in der Grammatik ausdruecklich belegten Familien.",
                   "familien": familien}, f, ensure_ascii=False, indent=2); f.write("\n")
    idx = [{"lexeme_id": e["lexeme_id"], "lemma": e["lemma"], "wortart": e["wortart"],
            "de": e["de"]["short"], "en": e["en"]["short"], "status": e["status"],
            "datei": e["_datei"]} for e in entries]
    with open(os.path.join(LEXDIR, "index.json"), "w", encoding="utf-8") as f:
        json.dump({"anzahl": len(idx), "lexicon_version": "0.1",
                   "grammar_version": "0.9.3", "eintraege": idx},
                  f, ensure_ascii=False, indent=2); f.write("\n")

    print(f"{len(entries)} Lexeme, {len(con_list)} Konzepte, {len(familien)} Wortfamilien")
    wa = {}
    for e in entries: wa[e["wortart"]] = wa.get(e["wortart"], 0) + 1
    print("  nach Wortart:", dict(sorted(wa.items(), key=lambda x: -x[1])))
    print("  mit Befunden:", sum(1 for e in entries if e["qualitaet"]["validatorstatus"] == "befund"))
    print("  Manus blockiert (L-09):", sum(1 for e in entries if e["manus"]["ambiguitaet"]))
    return 0

if __name__ == "__main__":
    sys.exit(main())
