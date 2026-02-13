__all__ = [
    "MolangExpr",
    "array",
    "geometry",
    "material",
    "math",
    "query",
    "temp",
    "texture",
    "variable",
    "context",
]

from typing import Any, Dict
from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

from .core.ast import Node
import molang


class MolangExpr:
    def __init__(self, expr: Any):
        self.expr = MolangExpr.convert(expr)

    def eval(self, context: Dict[str, Any]) -> Any:
        return molang.eval(self.expr, context)

    def parse(self) -> Node:
        return molang.parse(self.expr)

    def compile(self) -> str:
        return molang.compile(self.expr)

    @staticmethod
    def convert(value: str | bool | float | int) -> str:
        if isinstance(value, bool):
            return "1" if value else "0"
        text = str(value)
        match text.lower():
            case "true":
                return "1"
            case "false":
                return "0"
        return text

    @staticmethod
    def value(value: Any) -> "str|MolangExpr":
        if isinstance(value, MolangExpr):
            return value
        x = repr(value)
        return MolangExpr.convert(x)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls,
            core_schema.union_schema(
                [
                    core_schema.is_instance_schema(cls),
                    core_schema.chain_schema(
                        [
                            core_schema.str_schema(),
                            core_schema.no_info_plain_validator_function(
                                lambda v: cls(v)
                            ),
                        ]
                    ),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda instance: str(instance),
                return_schema=core_schema.str_schema(),
            ),
        )

    def _bin(self, op: str, other: Any) -> "MolangExpr":
        return MolangExpr(f"({self} {op} {MolangExpr.value(other)})")

    def _log(self, op: str, other: Any) -> "MolangExpr":
        return MolangExpr(f"{self} {op} {MolangExpr.value(other)}")

    def __str__(self) -> str:
        return self.expr

    def __repr__(self) -> str:
        return self.expr

    def __call__(self, *args) -> "MolangExpr":
        return MolangExpr(
            f"{self}({', '.join([str(MolangExpr.value(x)) for x in args])})"
        )

    def __invert__(self) -> "MolangExpr":
        return MolangExpr(f"!{self}")

    def __or__(self, other: Any) -> "MolangExpr":
        return self._log("||", other)

    def __and__(self, other: Any) -> "MolangExpr":
        return self._log("&&", other)

    def __gt__(self, other: Any) -> "MolangExpr":
        return self._log(">", other)

    def __lt__(self, other: Any) -> "MolangExpr":
        return self._log("<", other)

    def __ge__(self, other: Any) -> "MolangExpr":
        return self._log(">=", other)

    def __le__(self, other: Any) -> "MolangExpr":
        return self._log("<=", other)

    def __ne__(self, other: Any) -> "MolangExpr":  # type: ignore
        return self._log("!=", other)

    def __eq__(self, other: Any) -> "MolangExpr":  # type: ignore
        return self._log("==", other)

    def __add__(self, other: Any) -> "MolangExpr":
        return self._bin("+", other)

    def __sub__(self, other: Any) -> "MolangExpr":
        return self._bin("-", other)

    def __mul__(self, other: Any) -> "MolangExpr":
        return self._bin("*", other)

    def __truediv__(self, other: Any) -> "MolangExpr":
        return self._bin("/", other)

    def __floordiv__(self, other: Any) -> "MolangExpr":
        return self._bin("/", other)

    def __getitem__(self, name: "float|int|MolangExpr") -> "MolangExpr":
        return MolangExpr(f"{self}[{name}]")

    def if_(self, true_v: Any, false_v: Any) -> "MolangExpr":
        return MolangExpr(
            f"({self} ? {MolangExpr.value(true_v)} : {MolangExpr.value(false_v)})"
        )

    @staticmethod
    def for_each(
        variable: "MolangExpr", array: "MolangExpr", expression: "MolangExpr"
    ) -> "MolangExpr":
        return MolangExpr(f"for_each({variable}, {array}, {{{expression}}});")

    @staticmethod
    def loop(count: "int|MolangExpr", expression: "MolangExpr") -> "MolangExpr":
        return MolangExpr(f"loop({count}, {{{expression}}});")


class ArrayNamespace:
    def __getattr__(self, name: str) -> MolangExpr:
        return MolangExpr(f"array.{name.lower()}")


class VariableNamespace:
    _assignments: Dict[str, Any] = {}

    def __call__(self, name: str, *args) -> MolangExpr:
        if len(args) == 0:
            return MolangExpr(f"{self._prefix}.{name.lower()}")
        return MolangExpr(f"{self._prefix}.{name.lower()}")(*args)

    def __init__(self, prefix: str):
        self._prefix = prefix

    def __getattr__(self, name: str) -> MolangExpr:
        name = name.lower()
        if name in self._assignments:
            v = self._assignments[name]
            return MolangExpr(f"{self._prefix}.{name} = {MolangExpr.value(v)};")
        return MolangExpr(f"{self._prefix}.{name}")

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_"):
            object.__setattr__(self, name, value)
            return
        self._assignments[name.lower()] = value


class MathNamespace(VariableNamespace):
    pass


class QueryNamespace(VariableNamespace):
    pass


variable = VariableNamespace("variable")
temp = VariableNamespace("temp")
context = VariableNamespace("context")
geometry = VariableNamespace("geometry")
texture = VariableNamespace("texture")
material = VariableNamespace("material")
query = QueryNamespace("query")
math = MathNamespace("math")
array = ArrayNamespace()
