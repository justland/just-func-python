import pytest

from justfunc.interpreter import evaluate
from justfunc.errors import TooFewArguments


def test_add():
    assert evaluate(("+",)) == 0
    assert evaluate(("+", 1)) == 1
    assert evaluate(("+", 1, 2)) == 3
    assert evaluate(("+", 21, 35, 12, 7)) == 75
    assert evaluate(("+", 2.7, 10)) == 12.7
    assert evaluate(("+", ("+", 1, 2), ("+", 3, 4))) == 10
    assert evaluate(("+", ("x",), ("y",)), env=(("x", 1), ("y", 2))) == 3
    assert evaluate(("+", 1, ("y",)), env=(("y", ("+", 2, 3)),)) == 6


def test_subtract():
    assert evaluate(("-", 1)) == -1
    assert evaluate(("-", 1000, 334)) == 666
    assert evaluate(("-", 10.6, 2.3)) == 8.3
    assert evaluate(("-", ("-", 3))) == 3
    assert evaluate(("-", ("-", 10, 2), ("-", 3, 1))) == 6
    assert evaluate(("-", ('x',), ("y",)), env=(("x", 10), ("y", 5))) == 5


def test_subtract_with_too_few_arguments_raises_an_error():
    with pytest.raises(TooFewArguments):
        evaluate(("-",))


def test_multiply():
    assert evaluate(("*",)) == 1
    assert evaluate(("*", 5)) == 5
    assert evaluate(("*", 5, 99)) == 495
    assert evaluate(("*", ("*", 5), 10)) == 50
