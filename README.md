# molang

[![PyPI](https://img.shields.io/pypi/v/molang)](https://pypi.org/project/molang/)
[![Python](https://img.shields.io/pypi/pyversions/molang)](https://www.python.org/downloads//)
![Downloads](https://img.shields.io/pypi/dm/molang)
![Status](https://img.shields.io/pypi/status/molang)
[![Issues](https://img.shields.io/github/issues/legopitstop/molang)](https://github.com/legopitstop/molang/issues)

Molang to Python Translator & interpreter written in pure Python.

Documentation: https://molang.readthedocs.io/

## Installation

Install the module with pip:

```bat
pip3 install molang
```

Update existing installation: `pip3 install molang --upgrade`

## Features

- Decorator to convert a Python function to Molang.
- Execute .molang files from the command line or using Python. See [Road map](#road-map)

See the docs for more information.

## Example

Convert `my_function` to Molang

```python
from molang import molang

@molang
def my_function(a, b):
    return a + b

print(my_function)

>> return t.a+t.b
```

## Command-line interface

```
usage: molang [-h] [-V]

Run molang files

options:
  -h, --help     show this help message and exit
  -V, --version  print the molang version number and exit.

```

## Road map

- [x] Python function to Molang
- [ ] Interpreter
- [ ] Lexer
- [ ] Parser
- [ ] cli to convert Python code to Molang code (vice versa)
