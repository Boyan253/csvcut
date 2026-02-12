import pytest

import csvcut


def test_resolve_keeps_requested_order():
    assert csvcut.resolve(["a", "b", "c"], ["c", "a"], []) == ["c", "a"]

def test_resolve_drops_excluded():
    assert csvcut.resolve(["a", "b", "c"], [], ["b"]) == ["a", "c"]
