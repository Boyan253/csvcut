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


def test_resolve_ignore_missing():
    assert csvcut.resolve(["a"], ["a", "zzz"], [], ignore_missing=True) == ["a"]

def test_split_list_trims():
    assert csvcut.split_list(" a , b ,, c ") == ["a", "b", "c"]
