

def evaluate(source, env=None):
    def _add(args, ctx):
        if not args:
            return 0
        return sum(_evaluate(arg, ctx) for arg in args)

    def _evaluate(expr, ctx):
        if type(expr) == tuple:
            symbol, *args = expr
            if symbol == "+":
                return _add(args, ctx)
            value = ctx.get(symbol)
            if value is not None:
                return _evaluate(value, ctx)
        return expr
    return _evaluate(source, env if env else dict())
