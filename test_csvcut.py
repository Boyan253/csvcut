import pytest

import csvcut


def test_resolve_keeps_requested_order():
    assert csvcut.resolve(["a", "b", "c"], ["c", "a"], []) == ["c", "a"]

def test_resolve_drops_excluded():
    assert csvcut.resolve(["a", "b", "c"], [], ["b"]) == ["a", "c"]


def test_resolve_passthrough():
    assert csvcut.resolve(["a", "b"], [], []) == ["a", "b"]

def test_resolve_missing_column_raises():
    with pytest.raises(KeyError):
        csvcut.resolve(["a"], ["zzz"], [])
