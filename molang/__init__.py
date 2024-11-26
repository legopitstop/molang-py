from typing import Self, Callable, Type, Any
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema
import inspect
import ast
import os

__version__ = "0.0.3"
__all__ = ["__version__", "molang", "Molang"]


class Molang(str):
    @classmethod
    def from_ast(cls, ast_node: ast.Module) -> Self:
        """
        Converts a Python abstract syntax tree to Molang

        :param ast_node: The ast node to parse
        :type ast_node: ast.Module
        :rtype: Molang
        """
        _globals = []

        def convert(x) -> str:
            if isinstance(x, ast.Return):
                return f"return {convert(x.value)};"
            elif isinstance(x, ast.UnaryOp):
                return convert(x.op) + convert(x.operand)
            elif isinstance(x, ast.BinOp):
                return convert(x.left) + convert(x.op) + convert(x.right)
            elif isinstance(x, ast.BoolOp):
                return convert(x.values[0]) + convert(x.op) + convert(x.values[1])
            elif isinstance(x, ast.Compare):
                return convert(x.left) + convert(x.ops) + convert(x.comparators)
            elif isinstance(x, ast.Assign):
                return f"{convert(x.targets)}={convert(x.value)};"
            elif isinstance(x, ast.AugAssign):
                return f"{convert(x.target)}{convert(x.op)}={convert(x.value)};"
            elif isinstance(x, ast.IfExp):
                return f"{convert(x.body)} ? {convert(x.test)} : {convert(x.orelse)};"
            elif isinstance(x, ast.For):
                if isinstance(x.iter, ast.Call):  # use convert() instead
                    if x.iter.func.id == "range":
                        print(x.iter.func.id, x.iter.args[0].value, x.iter.keywords)
                        inner = "{" + convert(x.body) + "}"
                        return f"loop({convert(x.iter.args[0])}, {inner});"
                else:
                    v = "{" + convert(x.body) + "}"
                    return f"for_each({convert(x.target)}, {convert(x.iter)}, {v});"
                return ""  # unsupported func
            elif isinstance(x, ast.Constant):
                v = x.value
                if v is True:
                    return "true"
                if v is False:
                    return "false"
                if v is None:
                    return "null"
                return str(x.value)
            elif isinstance(x, ast.Name):
                if x.id in _globals:  # Use variable if global
                    return "v." + str(x.id)
                if x.id in ["round", "min", "max"]:
                    return f"math.{x.id}"
                return "t." + str(x.id)
            elif isinstance(x, ast.Not):
                return "!"
            elif isinstance(x, ast.Add):
                return "+"
            elif isinstance(x, ast.Sub):
                return "-"
            elif isinstance(x, ast.Div):
                return "/"
            elif isinstance(x, ast.Mult):
                return "*"
            elif isinstance(x, ast.Eq):
                return "=="
            elif isinstance(x, ast.NotEq):
                return "!="
            elif isinstance(x, ast.Gt):
                return ">"
            elif isinstance(x, ast.GtE):
                return ">="
            elif isinstance(x, ast.Lt):
                return "<"
            elif isinstance(x, ast.LtE):
                return "<="
            elif isinstance(x, ast.And):
                return "&&"
            elif isinstance(x, ast.Or):
                return "||"
            elif isinstance(x, ast.List):
                return "[" + ",".join(convert(v) for v in x.elts) + "]"
            elif isinstance(x, ast.Attribute):
                if x.value.id == "math":
                    return "math." + x.attr
                return ""  # Unsupported attr
            elif isinstance(x, list):
                return "".join(convert(i) for i in x)
            elif isinstance(x, ast.Global):
                _globals.extend(x.names)
                return ""
            elif isinstance(x, ast.Call):
                if x.keywords:
                    raise KeyError(f"keywords are not supported!, line {x.lineno}")
                inner = ",".join([convert(a) for a in x.args])
                return convert(x.func) + f"({inner})" if x.args else ""
            else:
                raise TypeError(f"'{x.__class__.__name__}' is not supported!")

        string = ""
        for func in ast_node.body:
            if not isinstance(func, ast.FunctionDef):
                raise TypeError(
                    f"Expected ast.FunctionDef but got '{func.__class__.__name__}' instead"
                )
            string = convert(func.body)
        return cls(string)

    def append(self, s: str) -> Self:
        """
        Add text to the end of the expression

        :param s: The text to append
        :type s: str
        :rtype: Molang
        """
        self += str(s)
        return self

    def prepend(self, s: str) -> Self:
        """
        Add text to the start of the expression

        :param s: The text to prepend
        :type s: str
        :rtype: Molang
        """
        self = str(s) + self
        return self

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        assert source is Molang
        return core_schema.no_info_after_validator_function(
            cls._validate,
            core_schema.str_schema(),
            serialization=core_schema.plain_serializer_function_ser_schema(
                cls._serialize,
                info_arg=False,
                return_schema=core_schema.str_schema(),
            ),
        )

    @staticmethod
    def _validate(value: str) -> "Molang":
        return Molang(value)

    @staticmethod
    def _serialize(value: "Molang") -> str:
        return str(value)


def molang(func: Callable) -> Molang:
    """
    Convert this function to Molang

    :rtype: Molang
    """

    def wrapper():
        source = inspect.getsource(func)
        ast_node = ast.parse(source, mode="exec")
        return Molang.from_ast(ast_node)

    return wrapper()


def run(fn: str, text: str):
    raise NotImplementedError()


def run_file(fp: str):
    with open(fp, "r") as fd:
        run(os.path.basename(fp), fd.read())
