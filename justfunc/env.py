from dataclasses import dataclass, field
from typing import Dict, Any, List

from justfunc import primitives


class UnboundVariableError(RuntimeError):
    pass


Frame = Dict[str, Any]


@dataclass
class Env:
    frames: List[Frame] = field(default_factory=list)

    @classmethod
    def new(cls, initial):
        return cls([initial])

    def lookup_variable_value(self, var):
        for frame in self.frames:
            value = frame.get(var)
            if value is not None:
                return value
        raise UnboundVariableError(f"Unbound variable: {var}")

    def define_variable(self, var, val):
        first, *_ = self.frames
        first[var] = val

    def extend(self, frame):
        return Env([frame] + self.frames)


def setup_env(initial_env=None):
    initial_env = initial_env or dict()
    initial_env.update({
        "+": ["primitive", primitives.add],
        "-": ["primitive", primitives.subtract],
        "*": ["primitive", primitives.multiply],
        "/": ["primitive", primitives.divide],
        "==": ["primitive", primitives.equal],
        "str": ["primitive", primitives.join],
        "not": ["primitive", lambda a: not a[0]],
        "true": True,
        "false": False,
    })
    return Env.new(initial_env)
