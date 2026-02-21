"""Font registration and style-sheet application."""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Generator

import matplotlib.pyplot as plt

_FONTS_DIR = Path(__file__).parent / "_fonts"
_STYLE_PATH = str(Path(__file__).parent / "_styles" / "callosum.mplstyle")


def _register_fonts() -> None:
    """Add bundled OTF files to matplotlib's font manager.

    Called once at ``corpus_callosum.plotting`` import time.  Safe to call
    multiple times — duplicates are silently ignored by the font manager.
    """
    import matplotlib.font_manager as fm

    for font_file in sorted(_FONTS_DIR.glob("*.otf")):
        fm.fontManager.addfont(str(font_file))


def use() -> None:
    """Apply the Callosum style sheet globally for the current session.

    All subsequent figures will use the Callosum brand style until another
    style is applied or the session ends.

    Examples
    --------
    >>> import corpus_callosum.plotting as cp
    >>> cp.use()
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()  # styled automatically
    """
    plt.style.use(_STYLE_PATH)


def title(ax: "matplotlib.axes.Axes", text: str, **kwargs) -> None:  # type: ignore[name-defined]
    """Set an all-caps title with standard Callosum styling.

    Use this instead of ``ax.set_title()`` so that capitalisation is enforced
    consistently across all charts.

    Parameters
    ----------
    ax:
        The axes to set the title on.
    text:
        Title text — automatically converted to upper case.
    **kwargs:
        Forwarded to :meth:`matplotlib.axes.Axes.set_title`.

    Examples
    --------
    >>> import corpus_callosum.plotting as cp
    >>> fig, ax = plt.subplots()
    >>> cp.title(ax, "monthly revenue by tier")  # renders as "MONTHLY REVENUE BY TIER"
    """
    ax.set_title(text.upper(), **kwargs)


@contextmanager
def context() -> Generator[None, None, None]:
    """Context manager that applies the Callosum style for a single block.

    Style is restored to whatever it was before on exit, so this is safe to
    use inside libraries or notebooks that have their own global style.

    Examples
    --------
    >>> import corpus_callosum.plotting as cp
    >>> import matplotlib.pyplot as plt
    >>> with cp.context():
    ...     fig, ax = plt.subplots()
    ...     ax.plot([1, 2, 3])
    """
    with plt.style.context(_STYLE_PATH):
        yield
