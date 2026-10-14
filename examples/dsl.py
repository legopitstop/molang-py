from molang.dsl import query, variable

variable.x = 4
print(variable.x)

expr = query.block_state("minecraft:cardinal_direction") == "north"
print(expr)
