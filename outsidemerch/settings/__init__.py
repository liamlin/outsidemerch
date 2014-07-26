"""
Settings used by outsidemerch project.

This consists of the general produciton settings, with an optional import of any local
settings.
"""

# Import production settings.
from outsidemerch.settings.production import *

# Import optional local settings.
try:
    from outsidemerch.settings.local import *
except ImportError:
    pass