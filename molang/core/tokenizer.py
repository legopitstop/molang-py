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
        [+\-*/(){}?:<>!;=,]
        )
    """,
    re.VERBOSE,
)


def tokenize(text: str | MolangExpr) -> list[str]:
    source = str(text)
    tokens = []
    pos = 0
    while pos < len(source):
        match = TOKEN_REGEX.match(source, pos)
        if match is None:
            if not source[pos:].strip():
                break
            raise SyntaxError(f"Unexpected character at position {pos}")
        tokens.append(match.group(1))
        pos = match.end()
    return tokens
