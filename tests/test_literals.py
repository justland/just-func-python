from justfunc.interpreter import evaluate


def test_evaluates_literals():
    assert evaluate(0) == 0
    assert evaluate("") == ""
    assert evaluate(True) is True
    assert evaluate(False) is False
    assert evaluate(dict()) == dict()
    assert evaluate(None) is None
