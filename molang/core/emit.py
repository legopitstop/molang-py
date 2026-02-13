__all__ = ["to_molang"]

from .ast import Number, Variable, Unary, Binary, Ternary, Assign, Call, Node
from .utils import alias


def to_molang(node: Node, minify: bool = False) -> str:
    if isinstance(node, Number):
        return str(node.value)

    if isinstance(node, Variable):
        return alias(node.name)

    if isinstance(node, Unary):
        return f"{node.op}{to_molang(node.expr)}"

    if isinstance(node, Binary):
        return f"({to_molang(node.left)} {node.op} {to_molang(node.right)})"

    if isinstance(node, Ternary):
        return f"({to_molang(node.cond)} ? {to_molang(node.true)} : {to_molang(node.false)})"

    if isinstance(node, Assign):
        return f"{to_molang(node.left)} = {to_molang(node.right)}"

    if isinstance(node, Call):
        args = ", ".join(to_molang(arg) for arg in node.args)
        return f"{to_molang(node.func)}({args})"

    raise TypeError("Unknown node")
