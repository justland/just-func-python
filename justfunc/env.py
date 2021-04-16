from dataclasses import dataclass, field
from typing import Dict, Any, List


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
