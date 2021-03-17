from functools import reduce


def is_self_evaluating(expr):
    return type(expr) in [str, int, float, bool, dict, None]


def is_application(expr):
    return type(expr) == list and len(expr) >= 1


def add(args):
    if not args:
        return 0
    return reduce(lambda x, y: x + y, args, 0)


def subtract(args):
    if len(args) == 1:
        return -args[0]
    return reduce(lambda x, y: x - y, args[1:], args[0])


def multiply(args):
    return reduce(lambda x, y: x * y, args, 1)


def divide(args):
    if len(args) == 1:
        return 1 / args[0]
    return reduce(lambda x, y: x / y, args)


def join(args):
    return "".join(args)


def equal(args):
    return reduce(lambda x, y: x == y, args)


primitive_procedures = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "==": equal,
    "str": join
}


def is_primitive_procedure(procedure):
    return procedure in primitive_procedures


def apply_primitive_procedure(procedure, args):
    return primitive_procedures.get(procedure)(args)


def apply(procedure, args):
    if is_primitive_procedure(procedure):
        return apply_primitive_procedure(procedure, args)


def is_variable(expr, env):
    return type(expr) == list and len(expr) == 1 and expr[0] in env


def look_up_variable(var, env):
    return env.get(var)


def is_let(expr):
    return type(expr) == list and len(expr) >= 3 and expr[0] == "let"


def eval_let(expr, env):
    bindings, exprs = expr
    new_env = {evaluate(k, env): evaluate(v, env) for (k, v) in bindings}
    return evaluate(exprs, dict(**env, **new_env))


def is_if(expr):
    return type(expr) == list and len(expr) == 4 and expr[0] == "if"


def eval_if(expr, env):
    predicate, consequent, alternative = expr
    if evaluate(predicate, env):
        return evaluate(consequent, env)
    return evaluate(alternative, env)


def evaluate(expr, env=None):
    env = env if env else dict()
    if is_self_evaluating(expr):
        return expr
    if is_variable(expr, env):
        return look_up_variable(expr[0], env)
    if is_let(expr):
        return eval_let(expr[1:], env)
    if is_if(expr):
        return eval_if(expr[1:], env)
    if is_application(expr):
        operator, *operands = expr
        return apply(
            evaluate(operator, env),
            [evaluate(op, env) for op in operands])
