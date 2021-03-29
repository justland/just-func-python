from justfunc.interpreter import evaluate


def test_with_no_params():
    assert evaluate(
        ["mod",
         ["fn", "foo", [], ["not", True]],
         ["foo"]]) is False


def test_with_single_param():
    assert evaluate(
        ["mod",
         ["fn", "hello-world", ["name"], ["str", "Hello, ", ["name"]]],
         ["hello-world", "John"],
         ]) == "Hello, John"
