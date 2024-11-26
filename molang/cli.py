from argparse import ArgumentParser
from molang import __version__

parser = ArgumentParser(prog="molang", description="Run molang files")
# parser.add_argument('file', metavar='<file>', nargs='?', const=None, help='execute the molang code contained in a file.')
# parser.add_argument('-c', type=str, metavar='<cmd>' , dest='cmd', help='execute the molang code in cmd.
#   cmd can be one or more statements separated by newlines, with significant leading whitespace as in normal module code.')
parser.add_argument(
    "-V",
    "--version",
    action="store_true",
    help="print the molang version number and exit.",
)


def main():
    args = parser.parse_args()
    if args.version:
        print(__version__)
    # elif args.file:
    #     run_file(args.file)
    # elif args.cmd:
    #     run('<stdin>', args.cmd)


if __name__ == "__main__":
    main()
