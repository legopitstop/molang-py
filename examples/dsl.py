from molang.dsl import variable, query

variable.x = 4
print(variable.x)

expr = query.block_state("minecraft:cardinal_direction") == "north"
print(expr)
