

def test_add(evaluated):
    assert evaluated('["+"]') == 0
    assert evaluated('["+", 1]') == 1
    assert evaluated('["+", 137, 349]') == 486
    assert evaluated('["+", 2.7, 10]') == 12.7
    assert evaluated('["+", 21, 35, 12, 7]') == 75
    assert evaluated('["+", ["+", 1, 2], ["+", 3, 4]]') == 10
    assert evaluated('["let", [["x", 1], ["y", 2]], ["+", "x", "y"]]') == 3


def test_subtract(evaluated):
    assert evaluated('["-", 1]') == -1
    assert evaluated('["-", 1000, 334]') == 666
    assert evaluated('["-", ["-", 1000, 334], ["-", 70, 4]]') == 600
    assert evaluated('["let", [["x", 100], ["y", 50]], ["-", "x", "y"]]') == 50


def test_multiply(evaluated):
    assert evaluated('["*"]') == 1
    assert evaluated('["*", 20]') == 20
    assert evaluated('["*", 5, 99]') == 495
    assert evaluated('["*", ["*", 10, 5], ["*", 2, 3]]') == 300
    assert evaluated('["let", [["x", 5], ["y", 5]], ["*", "x", "y"]]') == 25


def test_divide(evaluated):
    assert evaluated('["/", 10]') == 0.1
    assert evaluated('["/", 10, 5]') == 2
    assert evaluated('["/", ["/", 1, 2], ["/", 1, 2]]') == 1
    assert evaluated('["let", [["x", 9], ["y", 3]], ["/", "x", "y"]]') == 3


def test_operator_combinations(evaluated):
    return evaluated('["+", ["*", 3, 5], ["-", 10, 6]]') == 19
