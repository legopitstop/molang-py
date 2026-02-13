__all__ = ["Node", "Number", "Variable", "Unary", "Binary", "Ternary", "Assign", "Call"]


class Node:
    pass


class Number(Node):
    def __init__(self, value):
        self.value = float(value)


class Variable(Node):
    def __init__(self, name):
        self.name = name


class Unary(Node):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr


class Binary(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Ternary(Node):
    def __init__(self, cond, true, false):
        self.cond = cond
        self.true = true
        self.false = false


class Assign(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Call(Node):
    def __init__(self, func, args):
        self.func = func
        self.args = args
