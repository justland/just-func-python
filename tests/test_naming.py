import pytest

from justfunc.errors import UnknownSymbol
from justfunc.interpreter import evaluate


def test_let():
    assert evaluate(("let", (("size", 5),), ("size",))) == 5
    assert evaluate(("let", (("radius", 10), ("pi", 3.14159)),
                     ("*", ("pi",), ("*", ("radius",), ("radius",))))) == 314.159
    assert evaluate(("let", (("radius", 10), ("pi", 3.14159)),
                     ("let", (("circumference", ("*", 2, ("pi",), ("radius",))),),
                      ("circumference",)))) == 62.8318


def test_let_with_unknown_symbol_raises_an_error():
    with pytest.raises(UnknownSymbol):
        evaluate(("let", (("known", 1),), ("unknown",)))
