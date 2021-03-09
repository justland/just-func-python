from typing import Union


Literal = Union[int, str, bool, None, dict]
Expr = Union[Literal]


def evaluate(expr: Expr) -> Expr:
    return expr
