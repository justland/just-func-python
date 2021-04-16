import pytest

from justfunc.env import Env, UnboundVariableError


@pytest.fixture
def an_env():
    return Env.new({"a": 1, "b": 2})


def test_look_ups_variable_value(an_env):
    assert an_env.lookup_variable_value("a") == 1
    assert an_env.lookup_variable_value("b") == 2


def test_signals_error_if_variable_unbound(an_env):
    with pytest.raises(UnboundVariableError):
        an_env.lookup_variable_value("c")


def test_returns_a_new_environment(an_env):
    extended_env = an_env.extend({"c": 3})
    assert extended_env.lookup_variable_value("c") == 3
    assert extended_env.lookup_variable_value("a") == 1
    assert extended_env.lookup_variable_value("b") == 2


def test_defines_a_variable(an_env):
    an_env.define_variable("c", 3)
    assert an_env.lookup_variable_value("c") == 3


def test_definitions_in_initial_environment_reflect_in_extended(an_env):
    extended_env = an_env.extend({})
    an_env.define_variable("d", 4)
    assert extended_env.lookup_variable_value("d") == 4

