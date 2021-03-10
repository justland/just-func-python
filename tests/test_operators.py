from justfunc.interpreter import evaluate


def test_add():
    assert evaluate(("+",)) == 0
    assert evaluate(("+", 1)) == 1
    assert evaluate(("+", 1, 2)) == 3
    assert evaluate(("+", 21, 35, 12, 7)) == 75
    assert evaluate(("+", 2.7, 10)) == 12.7
    assert evaluate(("+", ("+", 1, 2), ("+", 3, 4))) == 10
    assert evaluate(("+", ("x",), ("y",)), dict(x=1, y=2)) == 3
    assert evaluate(("+", 1, ("y",)), dict(y=("+", 2, 3))) == 6

