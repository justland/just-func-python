import pytest

from justfunc.interpreter import evaluate
from justfunc.errors import TooFewArguments
from justfunc.number import Ratio, Int, Float


def test_add():
    assert evaluate(("+",)) == Int(0)
    assert evaluate(("+", Int(1))) == Int(1)
    assert evaluate(("+", Int(1), Int(2))) == Int(3)
    assert evaluate(("+", Int(21), Int(35), Int(12), Int(7))) == Int(75)
    assert evaluate(("+", Float(2.7), Int(10))) == Float(12.7)
    assert evaluate(("+", ("+", Int(1), Int(2)), ("+", Int(3), Int(4)))) == Int(10)
    assert evaluate(("+", ("x",), ("y",)), dict(x=Int(1), y=Int(2))) == Int(3)
    assert evaluate(("+", Int(1), ("y",)), dict(y=("+", Int(2), Int(3)))) == Int(6)


def test_subtract():
    assert evaluate(("-", Int(1))) == Int(-1)
    assert evaluate(("-", Int(1000), Int(334))) == Int(666)
    assert evaluate(("-", Float(10.6), Float(2.3))) == Float(8.3)
    assert evaluate(("-", ("-", Int(3)))) == Int(3)
    assert evaluate(("-", ("-", Int(10), Int(2)), ("-", Int(3), Int(1)))) == Int(6)
    assert evaluate(("-", ('x',), ("y",)), dict(x=Int(10), y=Int(5))) == Int(5)


def test_subtract_with_too_few_arguments_raises_an_error():
    with pytest.raises(TooFewArguments):
        evaluate(("-",))


def test_multiply():
    assert evaluate(("*",)) == Int(1)
    assert evaluate(("*", Int(5))) == Int(5)
    assert evaluate(("*", Int(5), Int(99))) == Int(495)
    assert evaluate(("*", ("*", Int(5)), Int(10))) == Int(50)


def test_divide():
    assert evaluate(("/", Int(3))) == Ratio(1, 3)
    assert evaluate(("/", Int(1), Int(2))) == Ratio(1, 2)
    assert evaluate(("/", Float(12.5))) == Float(0.08)
    assert evaluate(("/", Float(4.5), Float(1.2))) == Float(3.75)
    assert evaluate(("/", Ratio(1, 2), Ratio(3, 4))) == Ratio(2, 3)
    assert evaluate(("/", Ratio(1, 3), Float(10.0))) == Float(0.03333333333333333)
    assert evaluate(("/", Ratio(2, 3), Int(4))) == Ratio(1, 6)
