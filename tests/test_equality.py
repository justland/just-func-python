import pytest


@pytest.mark.parametrize("expr", [
    ["==", 1, 1],
    ["==", "a", "a"],
    ["==", True, True],
    ["==", 0, False],
    ["==", 1, True],
    ["==", None, None]
])
def test_equal(expr, evaluate):
    assert evaluate(expr)
