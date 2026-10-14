__all__ = ["compile_file", "eval_file", "parse_file"]

from os import PathLike
from typing import Any

from .ast import Node
from .context import create_context
from .emit import to_molang
from .eval import evaluate
from .parse import parse_expression


def parse_file(path: str | PathLike[str], *, encoding: str = 'utf-8') -> Node:
    with open(path, encoding=encoding) as fd:
        return parse_expression(fd.read())


def compile_file(path: str | PathLike[str], minify: bool = False, *, encoding: str = 'utf-8') -> str:
    with open(path, encoding=encoding) as fd:
        return to_molang(parse_expression(fd.read()), minify)


def eval_file(path: str | PathLike[str], context: dict[str, Any] | None = None, *, encoding: str = 'utf-8') -> Any:
    with open(path, encoding=encoding) as fd:
        return evaluate(parse_expression(fd.read()), context or create_context())
