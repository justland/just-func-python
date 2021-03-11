from functools import reduce

from justfunc.errors import TooFewArguments, UnknownSymbol


def evaluate(source, env=()):
    def _add(args, ctx):
        if not args:
            return 0
        return sum(_evaluate(arg, ctx) for arg in args)

    def _subtract(args, ctx):
        if not args:
            raise TooFewArguments(1, 0)
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

    def _let(args, ctx):
        param_assignments, expr = args
        new_ctx = ctx
        for assignment in param_assignments:
            if type(assignment) == tuple:
                name, value = assignment
                new_ctx = _assign(name, value, new_ctx)
        return _evaluate(expr, new_ctx)

    def _assign(name, value, ctx):
        return ctx + ((name, value),)

    def _evaluate(expr, ctx):
        if type(expr) == tuple:
            symbol, *args = expr
            if symbol == "*":
                return _multiply(args, ctx)
            if symbol == "+":
                return _add(args, ctx)
            if symbol == "-":
                return _subtract(args, ctx)
            if symbol == "let":
                return _let(args, ctx)
            value = _lookup(symbol, ctx)
            if value is None:
                raise UnknownSymbol(symbol)
            return _evaluate(value, ctx)
        return expr

    return _evaluate(source, env)
