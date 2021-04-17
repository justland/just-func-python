import pytest

from justfunc import read
from justfunc.reader import Symbol


@pytest.mark.parametrize("src,expected", [
    ("1", 1),
    ("1.5", 1.5),
    ('"\'hello\'"', "hello"),
    ('"a"', Symbol("a")),
    ('["+", 1, 2]', [Symbol("+"), 1, 2]),
    ('{"name": "John"}', {"name": "John"})
])
def test_reads(src, expected):
    assert read(src) == expected
