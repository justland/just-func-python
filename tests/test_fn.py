

def test_with_no_params(evaluate):
    assert evaluate(
        ["mod",
         ["fn", "foo", [], ["not", True]],
         ["foo"]]) is False


def test_with_single_param(evaluate):
    assert evaluate(
        ["mod",
         ["fn", "hello-world", ["name"], ["str", "Hello, ", ["name"]]],
         ["hello-world", "John"],
         ]) == "Hello, John"
