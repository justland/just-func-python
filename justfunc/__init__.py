import json

from justfunc.env import setup_env
from justfunc.evaluator import evaluate
from justfunc.reader import read


class JustFunc:
    def __init__(self):
        self.env = setup_env()

    def run(self, src):
        return evaluate(read(src), self.env)

    def run_repl(self, prompt=">>> "):
        while line := input(prompt):
            try:
                result = self.run(line)
                print(json.dumps(result))
            except RuntimeError as e:
                print(e.args[0])

    def main(self, _args):
        self.run_repl()
