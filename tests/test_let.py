from justfunc.interpreter import evaluate


def test_with_multiple_static_vars():
    assert evaluate(["let", [
        ["name", "Doe"],
        ["gender", "male"]],
        ["str", "Hello ",
         ["if",
          ["==", ["ret", "gender"], "male"],
          "Mr. ",
          "Mrs. "],
         ["ret", "name"]
         ]]) == "Hello Mr. Doe"


def test_with_single_static_variable():
    assert evaluate(["let", [
        ["size", 2]], ["ret", "size"]]) == 2


def test_with_dynamic_variable_name():
    assert evaluate(["let", [
        [["str", "na", "me"], "John"]],
        ["ret", "name"]]) == "John"


def test_with_dynamic_value():
    assert evaluate(["let", [
        ["name", ["str", "Jo", "hn"]]],
        ["ret", "name"]]) == "John"
