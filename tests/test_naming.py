import pytest

from justfunc.errors import UnknownSymbol
from justfunc.interpreter import evaluate
from justfunc.number import Int, Float


def test_let():
    assert evaluate(("let", (("size", Int(5)),), ("size",))) == Int(5)
    assert evaluate(("let", (("radius", Int(10)), ("pi", Float(3.14159))),
                     ("*", ("pi",), ("*", ("radius",), ("radius",))))) == Float(314.159)
    assert evaluate(("let", (("radius", Int(10)), ("pi", Float(3.14159))),
                     ("let", (("circumference", ("*", Int(2), ("pi",), ("radius",))),),
                      ("circumference",)))) == Float(62.8318)


def test_let_with_unknown_symbol_raises_an_error():
    with pytest.raises(UnknownSymbol):
        evaluate(("let", (("known", Int(1)),), ("unknown",)))
