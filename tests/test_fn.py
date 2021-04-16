

def test_with_no_params(evaluated):
    evaluated('["fn", "foo", [], ["not", true]]')
    assert evaluated('["foo"]') is False


def test_with_single_param(evaluated):
    evaluated('''
        ["fn", "hello-world", ["name"], 
        ["str", "'Hello, '", "name"]]''')
    assert evaluated('["hello-world", "\'John\'"]') == "Hello, John"
