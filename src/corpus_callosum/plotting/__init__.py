"""corpus_callosum.plotting — Callosum brand styling for matplotlib.

Quickstart
----------
>>> import corpus_callosum.plotting as cp
>>> import matplotlib.pyplot as plt

>>> # Apply the Callosum style globally
>>> cp.use()

>>> # Or scope it to a single block
>>> with cp.context():
...     fig, ax = plt.subplots()
...     ax.plot([1, 2, 3], color=cp.palette.royal_blue)

>>> # Access brand colours
>>> cp.palette.deep_blue
'#053362'

>>> # Use a Callosum colormap
>>> cmap = cp.get_cmap("default")
"""

from __future__ import annotations

from .colormaps import get_cmap, list_colormaps
from .palette import Palette, palette
from .style import context, title, use

# ── Auto-registration ─────────────────────────────────────────────────────────
# Fonts and colormaps are registered once when this module is first imported.
# The try/except guards against environments where matplotlib is unavailable
# (e.g. CI jobs that only test non-plotting code paths).

try:
    from . import style as _style_mod
    from . import colormaps as _cm_mod

    _style_mod._register_fonts()
    _cm_mod._register_all()
except Exception:  # pragma: no cover
    pass

__all__ = [
    "palette",
    "Palette",
    "get_cmap",
    "list_colormaps",
    "use",
    "context",
    "title",
]
