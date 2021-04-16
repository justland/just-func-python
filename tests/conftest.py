import pytest

from justfunc.interpreter import Interpreter


@pytest.fixture
def evaluate():
    return Interpreter().run
