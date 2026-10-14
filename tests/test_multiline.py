import pytest

from molang import (
    Block,
    Program,
    Ternary,
    compile,
    compile_file,
    create_context,
    eval,
    eval_file,
    parse,
    parse_file,
)


WALLS = """
t.RANDOMISE_SE_WALLS ? {
  t.WALL_SOUTH = math.random_integer(1,5)<3;
  t.WALL_EAST = math.random_integer(1,5)<3;
}:{
  t.WALL_SOUTH = 0;
  t.WALL_EAST = 0;
};
"""


def wall_context(enabled):
    ctx = create_context()
    ctx["temp"]["RANDOMISE_SE_WALLS"] = enabled
    values = iter([1, 5])
    calls = []

    def random_integer(low, high):
        calls.append((low, high))
        return next(values)

    ctx["math"]["random_integer"] = random_integer
    return ctx, calls


@pytest.mark.parametrize("enabled", [False, True])
def test_conditional_blocks(enabled):
    ctx, calls = wall_context(enabled)
    eval(WALLS, ctx)
    assert ctx["temp"]["WALL_SOUTH"] == int(enabled)
    assert ctx["temp"]["WALL_EAST"] == 0
    assert calls == ([(1, 5), (1, 5)] if enabled else [])


def test_block_ast():
    node = parse(WALLS)
    assert isinstance(node, Ternary)
    assert isinstance(node.true, Block)
    assert isinstance(node.false, Block)
    assert len(node.true.statements) == len(node.false.statements) == 2


@pytest.mark.parametrize("minify", [False, True])
def test_block_compile_round_trip(minify):
    source = compile(WALLS, minify=minify)
    assert compile(source, minify=minify) == source
    ctx, calls = wall_context(True)
    eval(source, ctx)
    assert ctx["temp"]["WALL_SOUTH"] == 1
    assert ctx["temp"]["WALL_EAST"] == 0
    assert len(calls) == 2


def test_multiline_file(tmp_path):
    path = tmp_path / "walls.molang"
    path.write_text(WALLS, encoding="utf-8")
    assert isinstance(parse_file(path), Ternary)
    assert compile_file(path) == compile(WALLS)
    ctx, calls = wall_context(True)
    eval_file(path, ctx)
    assert ctx["temp"]["WALL_SOUTH"] == 1
    assert ctx["temp"]["WALL_EAST"] == 0
    assert len(calls) == 2


def test_statement_sequence():
    source = "t.x = 2;\nt.y = t.x + 3;\nt.y;"
    assert isinstance(parse(source), Program)
    ctx = create_context()
    assert eval(source, ctx) == 5
    assert ctx["temp"]["x"] == 2
    assert ctx["temp"]["y"] == 5
    assert eval(compile(source)) == 5


def test_nested_and_empty_blocks():
    ctx = create_context()
    assert eval("1 ? {0 ? {t.x = 1;} : {t.x = 2;}; t.y = t.x + 1;} : {};", ctx) == 3
    assert ctx["temp"]["x"] == 2
    assert ctx["temp"]["y"] == 3
    assert eval("{}") == 0
    assert eval("5 +\n5;") == 10


@pytest.mark.parametrize(
    "source",
    [
        "{t.x = 1;",
        "t.x = 1; }",
        "t.x = 1 t.y = 2;",
        "1 ? {t.x = 1;} :",
        "{t.x = ;}",
        "5 @ 5",
    ],
)
def test_invalid_multiline_source(source):
    with pytest.raises(SyntaxError):
        parse(source)
