#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""orbis_validator.py — Einstiegspunkt des Orbis-Validators.

Seit der Infrastruktur-Migration 0.1 ist die eigentliche Logik in das Paket
`tools/validator/` ausgelagert; die Sprachdaten liegen maschinenlesbar unter
`language/` (Single Source of Truth). Diese Datei bleibt als stabiler Aufruf
erhalten, damit vorhandene Befehle, CI-Schritte und Dokumentation weiter gelten.

Gleichwertig:
    python3 orbis_validator.py --strict
    python3 -m tools.validator --strict

Die monolithische Vorfassung ist unter
`archive/orbis_validator-0_1-monolith.py` archiviert.

Aufrufe: siehe `python3 orbis_validator.py` ohne Argumente.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tools.validator.cli import main   # noqa: E402

if __name__ == "__main__":
    sys.exit(main(sys.argv))
