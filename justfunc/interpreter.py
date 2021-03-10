from functools import reduce


def evaluate(source, env=None):
    def _add(args, ctx):
        if not args:
            return 0
        return sum(_evaluate(arg, ctx) for arg in args)

    def _subtract(args, ctx):
        if len(args) == 1:
            return -_evaluate(args[0], ctx)
        return reduce(
            lambda x, y: x - y,
            (_evaluate(arg, ctx) for arg in args))

    def _evaluate(expr, ctx):
        if type(expr) == tuple:
            symbol, *args = expr
            if symbol == "+":
                return _add(args, ctx)
            if symbol == "-":
                return _subtract(args, ctx)
            value = ctx.get(symbol)
            if value is not None:
                return _evaluate(value, ctx)
        return expr
    return _evaluate(source, env if env else dict())
