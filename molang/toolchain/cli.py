import time
from argparse import ArgumentParser
from typing import Any

import molang

parser = ArgumentParser(prog="molang", description="Run molang files")
parser.add_argument(
    "file",
    metavar="<file>",
    nargs="?",
    const=None,
    help="execute the molang code contained in a file.",
)
parser.add_argument(
    "-c",
    type=str,
    metavar="<cmd>",
    dest="cmd",
    help="execute the molang code in cmd. cmd can be one or more statements separated by newlines,\
        with significant leading whitespace as in normal module code.",
)
parser.add_argument(
    "-V",
    "--version",
    action="store_true",
    help="print the molang version number and exit.",
)


def main() -> Any:
    args = parser.parse_args()
    if args.version:
        return f"molang {molang.__version__}"

    if args.file:
        result = molang.eval_file(args.file)
        return str(result)

    if args.cmd:
        result = molang.eval(args.cmd)
        return str(result)

    start = time.time()
    ctx = molang.create_context()
    ctx["query"]["anim_time"] = 0
    while True:
        try:
            code = input(">> ")
            if code == "exit" or code == "exit()":
                break
            ctx["query"]["anim_time"] = round(time.time() - start, 3)
            result = molang.eval(code, ctx)
            print(result)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
