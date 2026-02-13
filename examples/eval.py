import molang

expr = "math.sqrt(16) + variable.x"

ctx = molang.create_context()
ctx["variable"]["x"] = 9
print(molang.eval(expr, ctx))
