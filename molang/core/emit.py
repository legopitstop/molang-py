__all__ = ["to_molang"]

from .ast import (
    Assign,
    Binary,
    Block,
    Call,
    Node,
    Number,
    Program,
    String,
    Ternary,
    Unary,
    Variable,
)
from .utils import alias


def to_molang(node: Node, minify: bool = False) -> str:
    if isinstance(node, Program):
        separator = "" if minify else " "
        source = separator.join(
            to_molang(statement, minify) + ";" for statement in node.statements
        )
        return "{" + source + "}" if isinstance(node, Block) else source

    if isinstance(node, Number):
        return str(node.value)

    if isinstance(node, String):
        escaped = node.value.replace("\\", "\\\\").replace("'", "\\'")
        return f"'{escaped}'"

    if isinstance(node, Variable):
        return alias(node.name)

    if isinstance(node, Unary):
        return f"{node.op}{to_molang(node.expr, minify)}"

    if isinstance(node, Binary):
        return f"({to_molang(node.left, minify)} {node.op} {to_molang(node.right, minify)})"

    if isinstance(node, Ternary):
        return f"({to_molang(node.cond, minify)} ? {to_molang(node.true, minify)} : {to_molang(node.false, minify)})"

    if isinstance(node, Assign):
        return f"{to_molang(node.left, minify)} = {to_molang(node.right, minify)}"

    if isinstance(node, Call):
        args = ", ".join(to_molang(arg, minify) for arg in node.args)
        return f"{to_molang(node.func, minify)}({args})"

    raise TypeError("Unknown node")
