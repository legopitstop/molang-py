__all__ = ["parse", "compile", "eval"]

from typing import Dict, Any, Optional
from ..dsl import MolangExpr
from .ast import Node
from .parse import parse_expression
from .emit import to_molang
from .eval import evaluate
from .context import create_context


def parse(expr: str | MolangExpr) -> Node:
    return parse_expression(expr)


def compile(expr: str | MolangExpr, minify: bool = False) -> str:
    return to_molang(parse_expression(expr), minify)


def eval(expr: str | MolangExpr, context: Optional[Dict[str, Any]] = None) -> Any:
    return evaluate(parse_expression(expr), context or create_context())
