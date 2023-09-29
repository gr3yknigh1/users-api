from __future__ import annotations


def add(x: int, y: int) -> int:
    return x + y


def test_add_0():
    assert add(1, 2) == 3


def test_add_1():
    assert add(2, 4) == 6
