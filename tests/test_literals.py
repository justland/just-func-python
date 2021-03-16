from justfunc.interpreter import evaluate


def test_evaluates_literals():
    assert evaluate(0) == 0
    assert evaluate(1) == 1
    assert evaluate(1.5) == 1.5
    assert evaluate("") == ""
    assert evaluate("a string") == "a string"
    assert evaluate(True) is True
    assert evaluate(False) is False
    assert evaluate({}) == {}
    assert evaluate(None) is None
