import pytest

from justfunc import JustFunc


@pytest.fixture
def evaluated():
    return JustFunc().run
