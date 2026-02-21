"""Callosum brand colour palette."""

from __future__ import annotations

from typing import ClassVar, Iterator


class Palette:
    """Named access to Callosum brand colours.

    Colours are available as attributes, by dict-style key access, and as an
    iterable of hex strings.

    Examples
    --------
    >>> from corpus_callosum.plotting import palette
    >>> palette.deep_blue
    '#053362'
    >>> palette["pale_blue"]
    '#9AE1D4'
    >>> list(palette)
    ['#F4EEE8', '#9AE1D4', ...]
    """

    off_white: ClassVar[str] = "#F4EEE8"
    dark_off_white: ClassVar[str] = "#EADFCF"
    pale_blue: ClassVar[str] = "#9AE1D4"
    royal_blue: ClassVar[str] = "#0062E5"
    deep_blue: ClassVar[str] = "#053362"
    royal_green: ClassVar[str] = "#1EAD52"
    pale_green: ClassVar[str] = "#9CEDAE"
    pale_mint: ClassVar[str] = "#97E2A4"
    deep_green: ClassVar[str] = "#3D4733"
    cold_grey: ClassVar[str] = "#9E9E9E"
    pale_purple: ClassVar[str] = "#D69ECF"
    royal_purple: ClassVar[str] = "#8B35AD"
    pale_khaki_green: ClassVar[str] = "#C8CDAC"
    deep_khaki_green: ClassVar[str] = "#392F25"
    purple_brown: ClassVar[str] = "#4B261E"

    _registry: ClassVar[dict[str, str]] = {
        "off_white": "#F4EEE8",
        "dark_off_white": "#EADFCF",
        "pale_blue": "#9AE1D4",
        "royal_blue": "#0062E5",
        "deep_blue": "#053362",
        "royal_green": "#1EAD52",
        "pale_green": "#9CEDAE",
        "pale_mint": "#97E2A4",
        "deep_green": "#3D4733",
        "cold_grey": "#9E9E9E",
        "pale_purple": "#D69ECF",
        "royal_purple": "#8B35AD",
        "pale_khaki_green": "#C8CDAC",
        "deep_khaki_green": "#392F25",
        "purple_brown": "#4B261E",
    }

    def __getitem__(self, key: str) -> str:
        try:
            return self._registry[key]
        except KeyError:
            raise KeyError(f"{key!r} is not a Callosum brand colour. "
                           f"Available: {list(self._registry)}") from None

    def __iter__(self) -> Iterator[str]:
        return iter(self._registry.values())

    def __repr__(self) -> str:  # pragma: no cover
        lines = "\n".join(f"  {k}: {v}" for k, v in self._registry.items())
        return f"Palette(\n{lines}\n)"

    def keys(self):
        """Return colour names."""
        return self._registry.keys()

    def values(self):
        """Return hex strings."""
        return self._registry.values()

    def items(self):
        """Return (name, hex) pairs."""
        return self._registry.items()

    def as_dict(self) -> dict[str, str]:
        """Return a plain ``{name: hex}`` dictionary."""
        return dict(self._registry)

    def cycle(self, *names: str):
        """Return a :class:`cycler.Cycler` over the given colour names.

        If no names are given, cycles through all palette colours in order.

        Parameters
        ----------
        *names:
            Palette colour names, e.g. ``"deep_blue"``, ``"royal_blue"``.

        Examples
        --------
        >>> import matplotlib.pyplot as plt
        >>> from corpus_callosum.plotting import palette
        >>> plt.rcParams["axes.prop_cycle"] = palette.cycle("deep_blue", "royal_blue", "pale_green")
        """
        from cycler import cycler  # matplotlib ships cycler as a dependency

        colours = [self[n] for n in names] if names else list(self._registry.values())
        return cycler(color=colours)


#: Singleton instance — import and use directly.
palette = Palette()
