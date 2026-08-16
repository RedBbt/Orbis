# Wortspuren — EXPERIMENTELL, NICHT KANONISCH

> **Warnung:** Alles in diesem Verzeichnis ist eine **Designidee**, keine bestehende
> Orbis-Regel. Nichts davon steht in `Orbis-Grammatik-0.9.3.md`. Kein Werkzeug, kein
> Bericht und keine Dokumentation darf Wortspuren als geltendes System darstellen
> (`ORBIS_CONSTITUTION.md` Art. 20).

## Was Wortspuren sein sollen

Eine Ebene, die festhält, **wie der Sprecher zu einer Aussage steht** — Möglichkeit,
Erinnerung, Hörensagen, eigenes Erleben. Das ist etwas anderes als Kasus, Numerus oder
Tempus: Diese sagen, *was* im Satz geschieht, Wortspuren sagen, *woher der Sprecher es weiß*.

## Warum sie strikt getrennt bleiben

Vier Ebenen, die nicht vermischt werden dürfen:

| Ebene | Inhalt | Status |
|---|---|---|
| Phonologie | Manus-Silben (§26) | kanonisch |
| Morphologie | Kasus, Numerus, Tempus, Person (§7–§16) | kanonisch |
| Evidenz / Perspektive | **Wortspuren** | **experimentell** |
| Pragmatik | Satzabschlüsse (§26.7) | kanonisch |

Würden Wortspuren wie Flexionsendungen behandelt, wäre Orbis nicht mehr das System, das
0.9.3 beschreibt — die Entscheidung darüber gehört den Sprachdesignern, nicht dem Prüfstand.

## Stand

Vier Arbeitskonzepte sind in `spec.experimental.json` notiert (Möglichkeit, Erinnerung,
Hörensagen, Selbsterlebtes), dazu die offenen Fragen. **Kein Zeichen ist festgelegt**,
kein ADR existiert.

## Verhältnis zur Morphem-Ebene

Die getrennt diskutierte Idee, grammatische Morpheme in Manus **sichtbar** zu machen
(eigene Zeichen für Akkusativ, Plural, Vergangenheit …), ist ebenfalls experimentell und
liegt auf einer anderen Ebene als die Wortspuren. Die vorbereitete Architektur umgeht
beides bewusst:

```
Eingabe (Lemma + grammatische Geste)
        ↓
OrbisMorphologyEngine      valru + DATIV  →  valruş
        ↓
OrbisSyllabifier           blockiert durch L-09
        ↓
ManusComposer              schreibt valruş nach §26
        ↓
(optional) Wortspuren      EXPERIMENTELL
```

Die Dativ-Geste erzeugt damit **kein neues Manus-Zeichen** — sie ist eine
Tastaturfunktion, die eine reguläre Wortform bildet, die dann normal geschrieben wird.
Ob Manus später eine sichtbare Morphemebene bekommt, bleibt eine offene
Designentscheidung.
