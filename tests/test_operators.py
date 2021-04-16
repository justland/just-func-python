

def test_add(evaluate):
    assert evaluate(["+"]) == 0
    assert evaluate(["+", 1]) == 1
    assert evaluate(["+", 137, 349]) == 486
    assert evaluate(["+", 2.7, 10]) == 12.7
    assert evaluate(["+", 21, 35, 12, 7]) == 75
    assert evaluate(["+", ["+", 1, 2], ["+", 3, 4]]) == 10
    assert evaluate(["let", [["x", 1], ["y", 2]], ["+", ["x"], ["y"]]]) == 3


def test_subtract(evaluate):
    assert evaluate(["-", 1]) == -1
    assert evaluate(["-", 1000, 334]) == 666
    assert evaluate(["-", ["-", 1000, 334], ["-", 70, 4]]) == 600
    assert evaluate(["let", [["x", 100], ["y", 50]], ["-", ["x"], ["y"]]]) == 50


def test_multiply(evaluate):
    assert evaluate(["*"]) == 1
    assert evaluate(["*", 20]) == 20
    assert evaluate(["*", 5, 99]) == 495
    assert evaluate(["*", ["*", 10, 5], ["*", 2, 3]]) == 300
    assert evaluate(["let", [["x", 5], ["y", 5]], ["*", ["x"], ["y"]]]) == 25


def test_divide(evaluate):
    assert evaluate(["/", 10]) == 0.1
    assert evaluate(["/", 10, 5]) == 2
    assert evaluate(["/", ["/", 1, 2], ["/", 1, 2]]) == 1
    assert evaluate(["let", [["x", 9], ["y", 3]], ["/", ["x"], ["y"]]]) == 3


def test_operator_combinations(evaluate):
    return evaluate(["+", ["*", 3, 5], ["-", 10, 6]]) == 19
