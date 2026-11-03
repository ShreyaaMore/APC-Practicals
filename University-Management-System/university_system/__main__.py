"""
Executable package entry point:
    python -m university_system
"""
import sys
import os

pkg_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(pkg_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

