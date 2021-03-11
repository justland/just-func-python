

class BaseError(RuntimeError):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class ArityMismatch(BaseError):
    pass


class TooFewArguments(ArityMismatch):
    def __init__(self, expected, given):
        super().__init__(f"Expected: at least {expected}; given: {given}")


class UnknownSymbol(BaseError):
    def __init__(self, symbol):
        super().__init__(f"Unable to resolve symbol {symbol}")
