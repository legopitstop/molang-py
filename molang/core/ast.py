__all__ = ["Node", "Number", "String", "Variable", "Unary", "Binary", "Ternary", "Assign", "Call"]


class Node:
    pass


class Number(Node):
    def __init__(self, value):
        self.value = float(value)


class String(Node):
    def __init__(self, value):
        text = str(value)
        if len(text) >= 2 and text[0] in ("'", '"') and text[-1] == text[0]:
            inner = text[1:-1]
        else:
            inner = text
        # Basic unescape for quotes and backslash
        inner = inner.replace("\\'", "'").replace('\\"', '"').replace("\\\\", "\\")
        self.value = inner


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
