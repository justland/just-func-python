from functools import reduce

from justfunc.errors import UnknownSymbol, TooFewArguments
from justfunc.number import Float, Int, Ratio


def evaluate(source, env=None):
    return expression(source, env if env is not None else dict())


def merge_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def lookup(key, ctx):
    return ctx.get(key)


def assign(name, value, ctx):
    return merge_dicts(ctx, {name: value})


def expression(expr, ctx):
    if type(expr) == tuple:
        symbol, *args = expr
        if symbol == "*":
            return multiply(args, ctx)
        if symbol == "+":
            return add(args, ctx)
        if symbol == "-":
            return subtract(args, ctx)
        if symbol == "/":
            return divide(args, ctx)
        if symbol == "let":
            return let(args, ctx)
        value = lookup(symbol, ctx)
        if value is None:
            raise UnknownSymbol(symbol)
        return expression(value, ctx)
    return expr


def add(args, ctx):
    if not args:
        return Int(0)
    return reduce(lambda x, y: x + y, (expression(arg, ctx) for arg in args))


def subtract(args, ctx):
    if not args:
        raise TooFewArguments(1, 0)
    if len(args) == 1:
        return Int(-expression(args[0], ctx).value)
    return reduce(
        lambda x, y: x - y,
        (expression(arg, ctx) for arg in args))


def multiply(args, ctx):
    if not args:
        return Int(1)
    return reduce(
        lambda x, y: x * y,
        (expression(arg, ctx) for arg in args))


def divide(args, ctx):
    if len(args) == 1:
        d = expression(args[0], ctx)
        if type(d) == Float:
            return Int(1) / d
        if type(d) == Ratio:
            return Ratio.make(1, 1) / d
        return Ratio.make(1, d.value)
    return reduce(lambda x, y: x / y, (expression(arg, ctx) for arg in args))


def let(args, ctx):
    param_assignments, expr = args
    new_ctx = ctx
    for assignment in param_assignments:
        if type(assignment) == tuple:
            name, value = assignment
            new_ctx = assign(name, value, new_ctx)
    return expression(expr, new_ctx)
