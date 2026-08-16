# -*- coding: utf-8 -*-
"""Gemeinsame Testvorbereitung: Repo-Wurzel in den Suchpfad."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
