__all__ = ["compile", "eval", "parse"]

from typing import Any

from ..dsl import MolangExpr
from .ast import Node
from .context import create_context
from .emit import to_molang
from .eval import evaluate
from .parse import parse_expression


def parse(expr: str | MolangExpr) -> Node:
    return parse_expression(expr)


def compile(expr: str | MolangExpr, minify: bool = False) -> str:
    return to_molang(parse_expression(expr), minify)


def eval(expr: str | MolangExpr, context: dict[str, Any] | None = None) -> Any:
    return evaluate(parse_expression(expr), context or create_context())
