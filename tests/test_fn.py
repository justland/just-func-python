from justfunc.interpreter import evaluate


def test_with_no_params():
    env = dict()
    evaluate(["fn", "foo", [], ["not", True]], env)
    assert evaluate(["foo"], env) is False


def test_with_single_param():
    env = dict()
    evaluate(["fn", "hello-world", ["name"], ["str", "Hello, ", ["name"]]], env)
    assert evaluate(["hello-world", "John"], env) == "Hello, John"
