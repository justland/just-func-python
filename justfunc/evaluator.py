from justfunc.env import UnboundVariableError
from justfunc.reader import Symbol


def evaluate(expr, env):
    if is_self_evaluating(expr):
        return expr
    if is_variable(expr):
        return look_up_variable(expr, env)
    if is_mod(expr):
        return eval_mod(expr[1:], env)
    if is_let(expr):
        return eval_let(expr[1:], env)
    if is_fn(expr):
        return eval_fn(expr[1:], env)
    if is_if(expr):
        return eval_if(expr[1:], env)
    if is_application(expr):
        return apply(
            evaluate(operator(expr), env),
            [evaluate(op, env) for op in operands(expr)])


def is_self_evaluating(expr):
    return type(expr) in [str, int, float, None, dict]


def is_variable(expr):
    return type(expr) == Symbol


def look_up_variable(symbol, env):
    try:
        value = env.lookup_variable_value(symbol.value)
    except UnboundVariableError as e:
        raise e
    return value


def is_mod(expr):
    return (type(expr) == list and
            len(expr) >= 2 and
            expr[0] == Symbol("mod"))


def eval_mod(exprs, env):
    return [evaluate(expr, env) for expr in exprs][-1]


def is_let(expr):
    return (type(expr) == list
            and len(expr) >= 3
            and expr[0] == Symbol("let"))


def eval_let(expr, env):
    bindings, body = expr
    new_env = {
        symbol.value: evaluate(v, env)
        for (symbol, v) in bindings}
    return evaluate(body, env.extend(new_env))


def is_if(expr):
    return (type(expr) == list
            and len(expr) == 4
            and expr[0] == Symbol("if"))


def eval_if(expr, env):
    predicate, consequent, alternative = expr
    if evaluate(predicate, env):
        return evaluate(consequent, env)
    return evaluate(alternative, env)


def is_fn(expr):
    return (type(expr) == list
            and len(expr) >= 4
            and expr[0] == Symbol("fn")
            and type(expr[1]) == Symbol
            and type(expr) == list)


def eval_fn(expr, env):
    symbol, params, body = expr
    env.define_variable(symbol.value, create_procedure(params, body, env))


def create_procedure(params, body, env):
    return ["closure", params, body, env]


def operator(expr):
    return expr[0]


def operands(expr):
    return expr[1:]


def is_application(expr):
    return type(expr) == list and len(expr) >= 1


def apply(procedure, args):
    if is_primitive_procedure(procedure):
        return apply_primitive_procedure(procedure, args)
    if is_closure(procedure):
        params, body, env = procedure[1:]
        bindings = {
            symbol.value: v
            for (symbol, v) in zip(params, args)}
        return evaluate(body, env.extend(bindings))


def is_primitive_procedure(procedure):
    return type(procedure) == list \
           and len(procedure) == 2 \
           and procedure[0] == "primitive"


def apply_primitive_procedure(proc, args):
    _, primitive_procedure = proc
    return primitive_procedure(args)


def is_closure(procedure):
    return type(procedure) == list \
           and len(procedure) == 4 \
           and procedure[0] == "closure"
