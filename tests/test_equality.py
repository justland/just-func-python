import pytest


@pytest.mark.parametrize("expr", [
    '["==", 1, 1]',
    '["==", "\'a\'", "\'a\'"]',
    '["==", true, true]',
    '["==", 0, false]',
    '["==", 1, true]',
    '["==", null, null]'
])
def test_equal(expr, evaluated):
    assert evaluated(expr)
