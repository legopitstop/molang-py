from pathlib import Path

from molang import compile, compile_file, eval_file, parse_file
from molang.core.ast import Binary, Number
from molang.core.context import create_context

FILES = Path(__file__).parent / "files"


def test_parse_file():
    a = parse_file(FILES / "simple.molang")
    assert isinstance(a, Binary)
    assert a.op == "+"
    assert isinstance(a.left, Number)
    assert a.left.value == 5.0
    assert isinstance(a.right, Number)
    assert a.right.value == 5.0


def test_compile_file():
    a = compile_file(FILES / "simple.molang")
    assert a == "(5.0 + 5.0)"


def test_compile_file_minify():
    result = compile_file(FILES / "simple.molang", minify=True)
    assert result == compile("5 + 5", minify=True)


def test_eval_file():
    ctx = create_context()
    ctx['query']['log'] = print
    a = eval_file(FILES / "simple.molang", ctx)
    assert a == 10
