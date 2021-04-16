from justfunc import primitives
from justfunc.env import Env, UnboundVariableError


class Interpreter:
    def __init__(self):
        self.env = Env.new(global_env())

    def run(self, src):
        return evaluate(src, self.env)


def global_env(initial_env=None):
    env = initial_env or dict()
    env.update({
        "+": ["primitive", primitives.add],
        "-": ["primitive", primitives.subtract],
        "*": ["primitive", primitives.multiply],
        "/": ["primitive", primitives.divide],
        "==": ["primitive", primitives.equal],
        "str": ["primitive", primitives.join],
        "not": ["primitive", lambda a: not a[0]]
    })
    return env


def evaluate(expr, env):
    if is_self_evaluating(expr):
        return expr
    if is_variable(expr):
        return look_up_variable(expr[1], env)
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
    return type(expr) in [str, int, float, bool, dict, None]


def is_variable(expr):
    return (type(expr) == list
            and len(expr) == 2
            and expr[0] == "ret")


def look_up_variable(var, env):
    try:
        value = env.lookup_variable_value(var)
    except UnboundVariableError:
        return None
    return value


def is_mod(expr):
    return (type(expr) == list and
            len(expr) >= 2 and
            expr[0] == "mod")


def eval_mod(exprs, env):
    return [evaluate(expr, env) for expr in exprs][-1]


def is_let(expr):
    return (type(expr) == list
            and len(expr) >= 3
            and expr[0] == "let")


def eval_let(expr, env):
    new_env = {
        evaluate(k, env): create_procedure([], v, env)
        for (k, v) in expr[0]}
    return evaluate(expr[1], env.extend(new_env))


def is_if(expr):
    return (type(expr) == list
            and len(expr) == 4
            and expr[0] == "if")


def eval_if(expr, env):
    predicate, consequent, alternative = expr
    if evaluate(predicate, env):
        return evaluate(consequent, env)
    return evaluate(alternative, env)


def is_fn(expr):
    return (type(expr) == list
            and len(expr) >= 4
            and expr[0] == "fn"
            and type(expr[1]) == str
            and type(expr) == list)


def eval_fn(expr, env):
    name, params, body = expr
    env.define_variable(name, create_procedure(params, body, env))


def create_procedure(params, body, env):
    return ["closure", params, body, env]


def operator(expr):
    return ["ret", expr[0]]


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
            k: create_procedure([], v, env)
            for (k, v) in zip(params, args)}
        return evaluate(body, env.extend(bindings))


def is_primitive_procedure(procedure):
    return type(procedure) == list \
           and len(procedure) == 2 \
           and procedure[0] == "primitive"


def apply_primitive_procedure(proc, args):
    _, primitive_procedure = proc
    return primitive_procedure(args)


def is_closure(procedure):
    return (type(procedure) == list,
            len(procedure) == 4,
            procedure[0] == "closure")
