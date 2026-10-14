__all__ = ["tokenize"]

import re
from ..dsl import MolangExpr

TOKEN_REGEX = re.compile(
    r"""
    \s*
    (
        '(?:[^'\\]|\\.)*' |
        "(?:[^\"\\]|\\.)*" |
        \d+(?:\.\d+)? |
        [A-Za-z_][A-Za-z0-9_\.]* |
        &&|\|\||==|!=|>=|<=|
        [+\-*/()?:<>!;=,]
        )
    """,
    re.VERBOSE,
)


def tokenize(text: str | MolangExpr) -> list[str]:
    tokens = TOKEN_REGEX.findall(str(text))
    # findall returns list[str] when only one group is present,
    # but keep compat if regex ever gains inner groups.
    if tokens and isinstance(tokens[0], tuple):
        return [t[0] for t in tokens]
    return list(tokens)
