__all__ = ["evaluate"]

from .ast import Number, Variable, Unary, Binary, Ternary, Assign, Call
from .utils import alias


def evaluate(node, context):
    if isinstance(node, Number):
        return node.value

    if isinstance(node, Variable):
        parts = node.name.split(".")
        parts[0] = alias(parts[0])
        value = context
        for p in parts:
            if p not in value:
                return 0
            value = value[p]
        return value

    if isinstance(node, Call):
        # Evaluate the function from Variable node
        if not isinstance(node.func, Variable):
            raise TypeError("Only variables can be called")
        parts = node.func.name.split(".")
        parts[0] = alias(parts[0])
        func = context
        for p in parts:
            if p not in func:
                raise NameError(f"Function {node.func.name} not found")
            func = func[p]

        if not callable(func):
            raise TypeError(f"{node.func.name} is not callable")

        # Evaluate all arguments
        args = [evaluate(arg, context) for arg in node.args]
        return func(*args)

    if isinstance(node, Assign):
        if not isinstance(node.left, Variable):
            raise TypeError("Left side of assignment must be a variable")
        parts = node.left.name.split(".")
        parts[0] = alias(parts[0])
        val = evaluate(node.right, context)
        target = context
        for p in parts[:-1]:
            if p not in target or not isinstance(target[p], dict):
                target[p] = {}
            target = target[p]
        target[parts[-1]] = val
        return val

    if isinstance(node, Unary):
        val = evaluate(node.expr, context)
        if node.op == "!":
            return not val
        if node.op == "-":
            return -val

    if isinstance(node, Binary):
        left = evaluate(node.left, context)
        right = evaluate(node.right, context)

        try:
            return {
                "+": left + right,
                "-": left - right,
                "*": left * right,
                "/": left / right,
                "&&": left and right,
                "||": left or right,
                "==": left == right,
                "!=": left != right,
                ">": left > right,
                "<": left < right,
                ">=": left >= right,
                "<=": left <= right,
            }[node.op]
        except ZeroDivisionError:
            return 0

    if isinstance(node, Ternary):
        return (
            evaluate(node.true, context)
            if evaluate(node.cond, context)
            else evaluate(node.false, context)
        )
