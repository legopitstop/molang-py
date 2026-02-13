from pydantic import BaseModel
from molang.dsl import MolangExpr, query


class Test(BaseModel):
    condition: MolangExpr


x = Test(condition=query.block_state("facing") == "north")
print(x.model_dump())
