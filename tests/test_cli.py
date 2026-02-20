"""Basic smoke tests for the callosum CLI."""

import pytest

from corpus_callosum.cli import main
from corpus_callosum import __version__


def test_main_no_args_returns_zero():
    assert main([]) == 0


def test_version(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert __version__ in captured.out
