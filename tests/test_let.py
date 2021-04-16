
def test_with_multiple_static_vars(evaluated):
    assert evaluated('''["let", [
        ["name", "'Doe'"],
        ["gender", "'male'"]],
                      ["str", "'Hello '",
         ["if",
          ["==", "gender", "'male'"],
          "'Mr. '",
          "'Mrs. '"],
         "name"
         ]]''') == "Hello Mr. Doe"


def test_with_single_static_variable(evaluated):
    assert evaluated('''["let", [["size", 2]], "size"]''') == 2


def test_with_dynamic_value(evaluated):
    assert evaluated('''["let", [
        ["name", ["str", "'Jo'", "'hn'"]]],
                      "name"]''') == "John"

