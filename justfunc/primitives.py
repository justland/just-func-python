from functools import reduce


def add(args):
    return sum(args)


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
