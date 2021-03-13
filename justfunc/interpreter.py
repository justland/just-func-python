from functools import reduce
from math import gcd

from justfunc.errors import TooFewArguments, UnknownSymbol


def evaluate(source, env=None):
    def _add(args, ctx):
        if not args:
            return 0
        return sum(_expression(arg, ctx) for arg in args)

    def _subtract(args, ctx):
        if not args:
            raise TooFewArguments(1, 0)
        if len(args) == 1:
            return -_expression(args[0], ctx)
        return reduce(
            lambda x, y: x - y,
            (_expression(arg, ctx) for arg in args))

    def _multiply(args, ctx):
        if not args:
            return 1
        return reduce(
            lambda x, y: x * y,
            (_expression(arg, ctx) for arg in args))

    def _denom(r):
        return r[2]

    def _numer(r):
        return r[1]

    def _is_ratio(x):
        return type(x) == tuple and len(x) == 3 and x[0] == "ratio"

    def _make_ratio(x, y):
        g = gcd(x, y)
        return "ratio", (x // g), (y // g)

    def _divide(args, ctx):
        def _div_ratios(x, y):
            return _make_ratio(_numer(x) * _denom(y), _denom(x) * _numer(y))

        def _div(x, y):
            x = _expression(x, ctx)
            y = _expression(y, ctx)
            if type(x) == int and type(y) == int:
                return _make_ratio(x, y)
            if type(x) == float and type(y) == float:
                return x / y
            if _is_ratio(x) and _is_ratio(y):
                return _div_ratios(x, y)
            if _is_ratio(x) and type(y) == float:
                return (_numer(x) / _denom(x)) / y
            if _is_ratio(x) and type(y) == int:
                return _div_ratios(x, _make_ratio(y, 1))
            if type(x) == int and _is_ratio(y):
                return _div_ratios(_make_ratio(1, 1), y)
            return _make_ratio(x, y)

        if len(args) == 1:
            d = _expression(args[0], ctx)
            if type(args[0]) == float:
                return 1 / d
            if _is_ratio(args[0]):
                return _div_ratios(_make_ratio(1, 1), d)
            return _make_ratio(1, d)
        return reduce(_div, args)

    def _let(args, ctx):
        param_assignments, expr = args
        new_ctx = ctx
        for assignment in param_assignments:
            if type(assignment) == tuple:
                name, value = assignment
                new_ctx = _assign(name, value, new_ctx)
        return _expression(expr, new_ctx)

    def _merge_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z

    def _lookup(key, ctx):
        return ctx.get(key)

    def _assign(name, value, ctx):
        return _merge_dicts(ctx, {name: value})

    def _expression(expr, ctx):
        if _is_ratio(expr):
            return expr
        if type(expr) == tuple:
            symbol, *args = expr
            if symbol == "*":
                return _multiply(args, ctx)
            if symbol == "+":
                return _add(args, ctx)
            if symbol == "-":
                return _subtract(args, ctx)
            if symbol == "/":
                return _divide(args, ctx)
            if symbol == "let":
                return _let(args, ctx)
            value = _lookup(symbol, ctx)
            if value is None:
                raise UnknownSymbol(symbol)
            return _expression(value, ctx)
        return expr

    return _expression(source, env if env is not None else dict())
