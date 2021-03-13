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
    assert evaluate(("+", ("x",), ("y",)), dict(x=1, y=2)) == 3
    assert evaluate(("+", 1, ("y",)), dict(y=("+", 2, 3))) == 6


def test_subtract():
    assert evaluate(("-", 1)) == -1
    assert evaluate(("-", 1000, 334)) == 666
    assert evaluate(("-", 10.6, 2.3)) == 8.3
    assert evaluate(("-", ("-", 3))) == 3
    assert evaluate(("-", ("-", 10, 2), ("-", 3, 1))) == 6
    assert evaluate(("-", ('x',), ("y",)), dict(x=10, y=5)) == 5


def test_subtract_with_too_few_arguments_raises_an_error():
    with pytest.raises(TooFewArguments):
        evaluate(("-",))


def test_multiply():
    assert evaluate(("*",)) == 1
    assert evaluate(("*", 5)) == 5
    assert evaluate(("*", 5, 99)) == 495
    assert evaluate(("*", ("*", 5), 10)) == 50


def test_divide():
    assert evaluate(("/", 3)) == ("ratio", 1, 3)
    assert evaluate(("/", 1, 2)) == ("ratio", 1, 2)
    assert evaluate(("/", 12.5)) == 0.08
    assert evaluate(("/", 4.5, 1.2)) == 3.75
    assert evaluate(("/", ("ratio", 1, 2), ("ratio", 3, 4))) == ("ratio", 2, 3)
    assert evaluate(("/", ("ratio", 1, 3), 10.0)) == 0.03333333333333333
    assert evaluate(("/", ("ratio", 2, 3), 4)) == ("ratio", 1, 6)
