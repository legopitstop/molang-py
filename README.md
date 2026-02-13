# molang

![Tests](https://github.com/legopitstop/molang/actions/workflows/tests.yml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/molang)](https://pypi.org/project/molang/)
[![Python](https://img.shields.io/pypi/pyversions/molang)](https://www.python.org/downloads//)
![Downloads](https://img.shields.io/pypi/dm/molang)
![Status](https://img.shields.io/pypi/status/molang)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Issues](https://img.shields.io/github/issues/legopitstop/molang)](https://github.com/legopitstop/molang/issues)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Molang to Python Translator & interpreter written in pure Python.

## Installation

Install the module with pip:

```bat
pip3 install molang
```

Update existing installation: `pip3 install molang --upgrade`

## Links

- [Documentation](https://docs.lpsmods.dev/molang)
- [Source Code](https://github.com/legopitstop/molang)

## Requirements

| Name                                             | Description                             |
| ------------------------------------------------ | --------------------------------------- |
| [`pydantic`](https://pypi.org/project/pydantic/) | Data validation using Python type hints |

## Features

- Pure-Python Molang parser and AST representation
- Interpreter: evaluate Molang expressions against a runtime context
- Compiler / emitter: convert parsed AST back to Molang source
- DSL convenience objects: `query`, `variable`, `math`, `temp`, `array`, etc.
- Assignment support for dotted variables (e.g. `variable.x = 1`, `temp.a.b = 2`)
- Full `math.*` function implementations and callable math functions (e.g. `math.sqrt(4)`)
- Function-call support in expressions and argument evaluation
- CLI to run Molang files or execute inline Molang code

See the docs for more information.

## Example

### Parse / Compile / Eval

Parse, compile and evaluate with a context

```python
import molang

expr = "math.sqrt(16) + variable.x"
node = molang.parse(expr)
print(molang.compile(expr))
ctx = molang.create_context()
ctx['variable']['x'] = 9
print(molang.eval(expr, ctx))  # prints 13.0
```

### DSL usage

```python
from molang.dsl import variable, math

variable.x = 4
print(variable.x)           # Expr("variable.x = 4;") when used as assignment
print(math.sqrt(variable.x))

expr = query.block_state("minecraft:cardinal_direction") == "north"
print(expr) # Expr("query.block_state('minecraft:cardinal_direction') == 'north'")
```

### Assignment to dotted variables

```python
import molang

ctx = molang.create_context()
molang.eval('variable.health = 20', ctx)
print(ctx['variable']['health'])  # 20.0
```

### Function calls and math helpers

```python
import molang

ctx = molang.create_context()
print(molang.eval('math.lerp(0, 10, 0.5)', ctx))  # 5.0
```

## Command-line interface

```
usage: molang [-h] [-c <cmd>] [-V] [<file>]

Run molang files

positional arguments:
  <file>                execute the molang code contained in a file.

options:
  -h, --help            show this help message and exit
  -c <cmd>              execute the molang code in cmd. cmd can be one or more statements separated by newlines, with significant leading whitespace as in normal module code.
  -V, --version         print the molang version number and exit.
```
