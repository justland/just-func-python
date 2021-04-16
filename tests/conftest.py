import pytest

from justfunc.interpreter import Interpreter


@pytest.fixture
def evaluated():
    return Interpreter().run
