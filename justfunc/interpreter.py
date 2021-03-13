from functools import reduce

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
            return _expression(value, ctx)
        return expr

    return _expression(source, env if env is not None else dict())
