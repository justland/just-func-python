class ArityError(RuntimeError):
    def __init__(self, msg):
        super().__init__(msg)


class TooFewArgumentsError(ArityError):
    def __init__(self, expected, given):
        super().__init__(f"Expected: at least {expected}; given: {given}")