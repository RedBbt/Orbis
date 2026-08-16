# Orbis Keyboard — geplant

Noch keine Implementierung. Dieses Verzeichnis hält den Planungsstand.

## Blockade

Ein deterministischer Manus-Composer ist **nicht möglich**, solange **L-09** offen ist:
§5 legt erlaubte Silbenformen fest, aber keine Präferenz, wie eine Lautkette zerlegt wird.
77 von 281 Grundformen haben deshalb mehrere zulässige Manus-Schreibungen — *mela* etwa
als `me·la` oder `mel·a`.

`python3 orbis_validator.py --sim-l09` vergleicht vier Kandidatenstrategien und beziffert
ihre Wirkung. **Das Werkzeug entscheidet nichts**; die Wahl treffen die Sprachdesigner
(Vorlage: `decisions/Entscheidungsvorlage-0_9_4.md`, Abschnitt E7).

## Vorgesehene Architektur

```
Eingabe → OrbisMorphologyEngine → vollständige Lautform
        → OrbisSyllabifier (braucht L-09) → ManusComposer → Glyphen
        → optionale Wortspuren (EXPERIMENTELL)
```

Jede Stufe liest ihre Regeln aus `language/` bzw. `script/manus/spec/`; keine Stufe
hält eigene Sprachregeln.

## Was §26.8 bereits vorgibt

Die Eingabereihenfolge ist beschrieben: ein neuer Kernkonsonant schließt den
vorherigen Block ab. Das löst die **Eingabe**, nicht die **Rückübertragung** aus der
Lateinschreibung — dieselbe Buchstabenkette bleibt ohne L-09 mehrdeutig.

Terminologiebefund **U-10**: §26.8 nennt „20 Konsonantentasten"; korrekt sind
19 Konsonantentasten + 1 Vokalträgertaste (die Gesamtzahl von 31 Belegungen bleibt).

## Voraussetzungen vor dem MVP

1. L-09 entschieden (Silbifizierung)
2. L-10 entschieden (Strichstärke für die sieben Reibelaute und die Affrikate)
3. U-10 in der Grammatik nachgezogen
4. Glyphenformen als SVG spezifiziert (`script/manus/glyphs/`)
