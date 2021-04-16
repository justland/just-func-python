

def test_evaluates_literals(evaluated):
    assert evaluated('0') == 0
    assert evaluated('1') == 1
    assert evaluated('1.5') == 1.5
    assert evaluated('"\'\'"') == ""
    assert evaluated('"\'a string\'"') == "a string"
    assert evaluated('true') is True
    assert evaluated('false') is False
    assert evaluated('{}') == {}
    assert evaluated('null') is None
