"""Callosum colormaps, built from brand colours and registered with matplotlib."""

from __future__ import annotations

import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

from .palette import palette

# ── Colormap definitions ──────────────────────────────────────────────────────
# Each entry is a list of hex stops that matplotlib interpolates into a smooth
# LinearSegmentedColormap.  Add new colormaps here; they are registered
# automatically when this module is imported via plotting/__init__.py.

_DEFINITIONS: dict[str, list[str]] = {
    "callosum_blues": [
        palette.deep_blue,
        palette.royal_blue,
        palette.pale_blue,
    ],
    "callosum_greens": [
        palette.deep_green,
        palette.royal_green,
        palette.pale_green,
    ],
    "callosum_purples": [
        palette.purple_brown,
        palette.royal_purple,
        palette.pale_purple,
    ],
}

# ── Registration ──────────────────────────────────────────────────────────────

def _register_all() -> None:
    """Register all Callosum colormaps (and their ``_r`` reverses) with matplotlib."""
    for name, stops in _DEFINITIONS.items():
        cmap = LinearSegmentedColormap.from_list(name, stops)
        cmap_r = cmap.reversed(f"{name}_r")
        for cm in (cmap, cmap_r):
            try:
                mpl.colormaps.register(cm)
            except ValueError:
                pass  # already registered on re-import


# ── Public helpers ────────────────────────────────────────────────────────────

def get_cmap(name: str = "default", reverse: bool = False) -> LinearSegmentedColormap:
    """Return a Callosum colormap by short name.

    Parameters
    ----------
    name:
        Short name without the ``callosum_`` prefix, e.g. ``"default"``.
    reverse:
        If ``True``, return the reversed variant.

    Examples
    --------
    >>> from corpus_callosum.plotting import get_cmap
    >>> cmap = get_cmap("default")
    >>> cmap_r = get_cmap("default", reverse=True)
    """
    full_name = f"callosum_{name}" + ("_r" if reverse else "")
    try:
        return mpl.colormaps[full_name]
    except KeyError:
        available = list_colormaps()
        raise KeyError(
            f"Colormap {full_name!r} not found. "
            f"Available Callosum colormaps: {available}"
        ) from None


def list_colormaps() -> list[str]:
    """Return the short names of all registered Callosum colormaps."""
    return [
        k.removeprefix("callosum_")
        for k in mpl.colormaps
        if k.startswith("callosum_") and not k.endswith("_r")
    ]
