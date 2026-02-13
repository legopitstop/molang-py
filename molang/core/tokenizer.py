__all__ = ["tokenize"]

import re
from typing import List
from ..dsl import MolangExpr

TOKEN_REGEX = re.compile(
    r"""
    \s*
    (
        \d+(\.\d+)? |
        [A-Za-z_][A-Za-z0-9_\.]* |
        &&|\|\||==|!=|>=|<=|
        [+\-*/()?:<>!;=,]
        )
    """,
    re.VERBOSE,
)


def tokenize(text: str | MolangExpr) -> List[str]:
    tokens = TOKEN_REGEX.findall(str(text))
    return [t[0] for t in tokens]
