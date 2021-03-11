from functools import reduce

from justfunc.errors import TooFewArgumentsError


def evaluate(source, env=()):
    def _add(args, ctx):
        if not args:
            return 0
        return sum(_evaluate(arg, ctx) for arg in args)

    def _subtract(args, ctx):
        if not args:
            raise TooFewArgumentsError(1, 0)
        if len(args) == 1:
            return -_evaluate(args[0], ctx)
        return reduce(
            lambda x, y: x - y,
            (_evaluate(arg, ctx) for arg in args))

    def _multiply(args, ctx):
        if not args:
            return 1
        return reduce(
            lambda x, y: x * y,
            (_evaluate(arg, ctx) for arg in args))

    def _lookup(key, ctx):
        value = next((v for (k, v) in ctx if k == key), None)
        return value

    def _evaluate(expr, ctx):
        if type(expr) == tuple:
            symbol, *args = expr
            if symbol == "*":
                return _multiply(args, ctx)
            if symbol == "+":
                return _add(args, ctx)
            if symbol == "-":
                return _subtract(args, ctx)
            value = _lookup(symbol, ctx)
            return _evaluate(value, ctx)
        return expr

    return _evaluate(source, env)
