# -*- coding: utf-8 -*-
"""Einstiegspunkt: python3 -m tools.documentation build [--check]"""
import sys
from .build import build

args = sys.argv[1:]
if not args or args[0] != "build":
    print(__doc__)
    sys.exit(0)
sys.exit(build(check="--check" in args))
