from pathlib import Path
from unittest.mock import Mock

from molang import compile, compile_file, eval_file, parse_file
from molang.core.ast import Assign, Binary, Block, Call, Number, Ternary, Variable
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

    b = parse_file(FILES / "multiline.molang")
    assert isinstance(b, Ternary)
    assert isinstance(b.cond, Variable)
    assert b.cond.name == "t.RANDOMISE_SE_WALLS"
    assert isinstance(b.true, Block)
    assert isinstance(b.true.statements[0], Assign)
    assert isinstance(b.true.statements[0].left, Variable)
    assert b.true.statements[0].left.name == "t.WALL_SOUTH"
    assert isinstance(b.true.statements[0].right, Binary)
    assert isinstance(b.true.statements[0].right.left, Call)
    assert isinstance(b.true.statements[0].right.left.func, Variable)
    assert b.true.statements[0].right.left.func.name == "math.random_integer"
    assert isinstance(b.true.statements[0].right.left.args[0], Number)
    assert b.true.statements[0].right.left.args[0].value == 1
    assert isinstance(b.true.statements[0].right.left.args[1], Number)
    assert b.true.statements[0].right.left.args[1].value == 5
    assert isinstance(b.true.statements[0].right.op, str)
    assert b.true.statements[0].right.op == "<"
    assert isinstance(b.true.statements[0].right.right, Number)
    assert b.true.statements[0].right.right.value == 3.0

    assert isinstance(b.true.statements[1], Assign)
    assert isinstance(b.true.statements[1].left, Variable)
    assert b.true.statements[1].left.name == "t.WALL_EAST"
    assert isinstance(b.true.statements[1].right, Binary)
    assert isinstance(b.true.statements[1].right.left, Call)
    assert isinstance(b.true.statements[1].right.left.func, Variable)
    assert b.true.statements[1].right.left.func.name == "math.random_integer"
    assert isinstance(b.true.statements[1].right.left.args[0], Number)
    assert b.true.statements[1].right.left.args[0].value == 1
    assert isinstance(b.true.statements[1].right.left.args[1], Number)
    assert b.true.statements[1].right.left.args[1].value == 5
    assert isinstance(b.true.statements[1].right.op, str)
    assert b.true.statements[1].right.op == "<"
    assert isinstance(b.true.statements[1].right.right, Number)
    assert b.true.statements[1].right.right.value == 3.0

    assert isinstance(b.false, Block)
    assert isinstance(b.false.statements[0], Assign)
    assert isinstance(b.false.statements[0].left, Variable)
    assert b.false.statements[0].left.name == "t.WALL_SOUTH"
    assert isinstance(b.false.statements[0].right, Number)
    assert b.false.statements[0].right.value == 0

    assert isinstance(b.false.statements[1], Assign)
    assert isinstance(b.false.statements[1].left, Variable)
    assert b.false.statements[1].left.name == "t.WALL_EAST"
    assert isinstance(b.false.statements[1].right, Number)
    assert b.false.statements[1].right.value == 0


def test_compile_file():
    a = compile_file(FILES / "simple.molang")
    assert a == "(5.0 + 5.0)"

    b = compile_file(FILES / "multiline.molang")
    assert (
        b
        == "(temp.RANDOMISE_SE_WALLS ? {temp.WALL_SOUTH = (math.random_integer(1.0, 5.0) < 3.0); temp.WALL_EAST = (math.random_integer(1.0, 5.0) < 3.0);} : "
        "{temp.WALL_SOUTH = 0.0; temp.WALL_EAST = 0.0;})"
    )


def test_compile_file_minify():
    a = compile_file(FILES / "simple.molang", minify=True)
    assert a == compile("5 + 5", minify=True)

    b = compile_file(FILES / "multiline.molang", minify=True)
    assert b == compile(
        "(temp.RANDOMISE_SE_WALLS ? {temp.WALL_SOUTH = (math.random_integer(1.0, 5.0) < 3.0); temp.WALL_EAST = (math.random_integer(1.0, 5.0) < 3.0);} : "
        "{temp.WALL_SOUTH = 0.0; temp.WALL_EAST = 0.0;})",
        minify=True,
    )


def test_eval_file():
    ctx = create_context()
    ctx["query"]["log"] = print

    assert eval_file(FILES / "simple.molang", ctx) == 10

    random_integer = Mock(side_effect=[1, 5])
    ctx["math"]["random_integer"] = random_integer

    # True branch: 1 < 3 is true; 5 < 3 is false.
    ctx["temp"]["RANDOMISE_SE_WALLS"] = 1
    eval_file(FILES / "multiline.molang", ctx)

    assert ctx["temp"]["WALL_SOUTH"] == 1
    assert ctx["temp"]["WALL_EAST"] == 0
    assert random_integer.call_count == 2

    # False branch must overwrite both variables without calling random.
    random_integer.reset_mock()
    ctx["temp"].update(
        RANDOMISE_SE_WALLS=0,
        WALL_SOUTH=1,
        WALL_EAST=1,
    )
    eval_file(FILES / "multiline.molang", ctx)

    assert ctx["temp"]["WALL_SOUTH"] == 0
    assert ctx["temp"]["WALL_EAST"] == 0
    random_integer.assert_not_called()
