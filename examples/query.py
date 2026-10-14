from typing import Any

import molang

expr = "query.block_state('facing')=='north'"


def block_state(name: str) -> Any:
    return "north"


ctx = molang.create_context()
ctx['query']['block_state'] = block_state
print(molang.eval(expr, ctx))
