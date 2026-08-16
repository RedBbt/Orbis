# -*- coding: utf-8 -*-
"""tools.validator.schema — Struktur- und Integritaetspruefung der Sprachdaten.

Prueft ohne externe Abhaengigkeiten (kein pip install noetig):
  * JSON-Wohlgeformtheit aller Dateien unter language/
  * Pflichtfelder gegen die Schemata (lexicon, concept, sentence, findings)
  * ID-Format und ID-Eindeutigkeit
  * Referenzintegritaet: Relationen, Konzepte, Saetze, Befunde
  * Uebersetzungsfelder nach TRANSLATION_POLICY

Es ist KEIN Sprachpruefer — es prueft die Datenbasis, nicht Orbis.
"""

import json, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LANG = os.path.join(ROOT, "language")

ID_PATTERNS = {
    "lexeme_id": re.compile(r"^ORB-LEX-\d{6}$"),
    "concept_id": re.compile(r"^ORB-CON-\d{6}$"),
    "sentence_id": re.compile(r"^ORB-SENT-\d{6}$"),
    "finding_id": re.compile(r"^[KLUW]-\d{2}$"),
}


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def check_json_wellformed():
    fehler = []
    for p in sorted(glob.glob(os.path.join(LANG, "**", "*.json"), recursive=True)):
        try:
            _load(p)
        except Exception as e:
            fehler.append(f"{os.path.relpath(p, ROOT)}: ungueltiges JSON ({e})")
    return fehler


def check_lexicon(findings=None):
    fehler = []
    findings = findings or set()
    idx_p = os.path.join(LANG, "lexicon", "index.json")
    idx = _load(idx_p)
    gesehen_id, gesehen_datei = {}, set()
    concepts = {c["concept_id"] for c in
                _load(os.path.join(LANG, "lexicon", "concepts", "concepts.json"))["concepts"]}
    alle_lex = set()
    eintraege = []
    for e in idx["eintraege"]:
        p = os.path.join(LANG, "lexicon", e["datei"])
        if not os.path.exists(p):
            fehler.append(f"index.json verweist auf fehlende Datei {e['datei']}")
            continue
        if e["datei"] in gesehen_datei:
            fehler.append(f"index.json: Datei doppelt referenziert: {e['datei']}")
        gesehen_datei.add(e["datei"])
        d = _load(p)
        eintraege.append(d)
        alle_lex.add(d["lexeme_id"])

    for d in eintraege:
        lid = d["lexeme_id"]
        wo = f"{d['lemma']} ({lid})"
        if not ID_PATTERNS["lexeme_id"].match(lid):
            fehler.append(f"{wo}: ID-Format ungueltig")
        if lid in gesehen_id:
            fehler.append(f"{wo}: doppelte lexeme_id (auch {gesehen_id[lid]})")
        gesehen_id[lid] = d["lemma"]
        for pflicht in ("lemma", "status", "wortart", "de", "phonologie", "qualitaet"):
            if pflicht not in d:
                fehler.append(f"{wo}: Pflichtfeld '{pflicht}' fehlt")
        if not d.get("de", {}).get("short") or not d.get("de", {}).get("definition"):
            fehler.append(f"{wo}: deutsche Kurzglosse oder Definition fehlt "
                          f"(ORBIS_CONSTITUTION Art. 1/5)")
        for cid in d.get("semantik", {}).get("concept_ids", []):
            if cid not in concepts:
                fehler.append(f"{wo}: verweist auf unbekanntes Konzept {cid}")
        for rel in d.get("semantik", {}).get("relationen", []):
            ziel = rel["ziel"]
            if ziel.startswith("ORB-LEX-") and ziel not in alle_lex:
                fehler.append(f"{wo}: Relation {rel['typ']} zeigt auf unbekanntes Lexem {ziel}")
            if ziel.startswith("ORB-CON-") and ziel not in concepts:
                fehler.append(f"{wo}: Relation {rel['typ']} zeigt auf unbekanntes Konzept {ziel}")
        for b in d.get("qualitaet", {}).get("offene_befunde", []):
            if findings and b not in findings:
                fehler.append(f"{wo}: unbekannte Befund-ID {b}")
        for syn in d.get("semantik", {}).get("synonyme", []):
            if not syn.get("bedeutungsunterschied_de"):
                fehler.append(f"{wo}: Synonymrelation ohne Bedeutungsunterschied "
                              f"(ORBIS_CONSTITUTION Art. 12)")
    return fehler, eintraege, concepts


def check_translations(eintraege):
    """TRANSLATION_POLICY: canonical braucht en.short; Fehlende werden gezaehlt,
    nicht als Fehler gewertet, solange die Migration laeuft."""
    fehlen = [d["lemma"] for d in eintraege
              if d["status"] == "canonical" and not d.get("en", {}).get("short")]
    return fehlen


def check_corpus(alle_lex):
    fehler = []
    p = os.path.join(LANG, "corpus", "tests", "testkorpus-0_1.json")
    d = _load(p)
    gesehen = set()
    findings = {f["id"] for f in
                _load(os.path.join(LANG, "findings", "findings.json"))["findings"]}
    for s in d["saetze"]:
        sid = s["id"]
        if not ID_PATTERNS["sentence_id"].match(sid):
            fehler.append(f"{sid}: ID-Format ungueltig")
        if sid in gesehen:
            fehler.append(f"{sid}: doppelte Satz-ID")
        gesehen.add(sid)
        if not s.get("de"):
            fehler.append(f"{sid}: deutsche Quelle fehlt")
        if s["status"] == "canonical" and not s.get("orbis"):
            fehler.append(f"{sid}: status canonical, aber keine Orbis-Form")
        if s["status"] != "canonical" and s.get("orbis"):
            fehler.append(f"{sid}: status {s['status']}, traegt aber eine Orbis-Form")
        for lid in s.get("lexeme", []):
            if lid not in alle_lex:
                fehler.append(f"{sid}: verweist auf unbekanntes Lexem {lid}")
        for b in s.get("qualitaet", {}).get("befunde", []):
            if b not in findings:
                fehler.append(f"{sid}: unbekannte Befund-ID {b}")
    return fehler, d


def check_findings():
    fehler = []
    d = _load(os.path.join(LANG, "findings", "findings.json"))
    gesehen = set()
    for f in d["findings"]:
        if not ID_PATTERNS["finding_id"].match(f["id"]):
            fehler.append(f"Befund {f['id']}: ID-Format ungueltig")
        if f["id"] in gesehen:
            fehler.append(f"Befund {f['id']}: doppelt")
        gesehen.add(f["id"])
        if not f.get("description_de"):
            fehler.append(f"Befund {f['id']}: deutsche Beschreibung fehlt")
    return fehler, d


def run_schema(args):
    nur_ids = "--ids" in args and "--schema" not in args
    nur_trans = "--translations" in args and "--schema" not in args
    nur_rel = "--relations" in args and "--schema" not in args
    alles = "--schema" in args

    print("== SCHEMA- UND INTEGRITÄTSPRÜFUNG DER SPRACHDATEN ==")
    fehler = []
    if alles:
        fehler += check_json_wellformed()

    fin_ids = {f["id"] for f in
               _load(os.path.join(LANG, "findings", "findings.json"))["findings"]}
    lex_fehler, eintraege, concepts = check_lexicon(fin_ids)
    alle_lex = {d["lexeme_id"] for d in eintraege}
    cor_fehler, korpus = check_corpus(alle_lex)
    fin_fehler, findings = check_findings()

    if alles or nur_ids or nur_rel:
        fehler += lex_fehler + cor_fehler + fin_fehler

    fehlende_en = check_translations(eintraege)
    if alles or nur_trans:
        print(f"Übersetzungen: {len(eintraege) - len(fehlende_en)} von {len(eintraege)} "
              f"kanonischen Lexemen haben eine englische Kurzglosse.")
        if fehlende_en:
            print(f"  ohne en.short ({len(fehlende_en)}): "
                  f"{', '.join(sorted(fehlende_en)[:20])}"
                  f"{' …' if len(fehlende_en) > 20 else ''}")
            print("  Hinweis: Pflicht erst nach Abschluss der Migration "
                  "(TRANSLATION_POLICY.md); derzeit kein Fehler.")

    print(f"Lexeme: {len(eintraege)} | Konzepte: {len(concepts)} | "
          f"Sätze: {korpus['anzahl']} | Befunde: {findings['anzahl']}")

    if fehler:
        print(f"\n{len(fehler)} FEHLER:")
        for f in fehler:
            print("  -", f)
        return 1
    print("\nKeine Strukturfehler. OK.")
    return 0
