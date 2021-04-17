import json
import sys
from dataclasses import dataclass
from json import JSONDecodeError


@dataclass(frozen=True)
class Symbol:
    value: str


def tokenize(src):
    return json.loads(src)


def parse(expr):
    if type(expr) == list:
        return [parse(e) for e in expr]
    return atom(expr)


def atom(token):
    if token is None or type(token) in [float, int, bool, dict]:
        return token
    if type(token) == str and (token.startswith("'") and token.endswith("'")):
        return token[1:-1]
    return Symbol(sys.intern(token))


def read(src):
    try:
        tokens = tokenize(src)
    except JSONDecodeError as e:
        raise RuntimeError(e)
    return parse(tokens)
