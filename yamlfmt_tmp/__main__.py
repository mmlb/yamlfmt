"""
Arg parsing, calling other functions.
"""
import argparse
import sys

from yamlfmt_tmp.yamlfmt import round_trip, format_and_display, format_and_write

parser = argparse.ArgumentParser()
parser.add_argument('file', help='file to parse', nargs='*')
parser.add_argument('-w', '--write', help='overwrite file with formatted output',
                    action='store_true')
parser.add_argument('-t', '--width', help='set custom width', type=int, required=False, default=80)
parser.add_argument('--use-yaml-1-1', help='force yaml output to version 1.1', action='store_true')
parser.add_argument('-i', '--indent', help='set indent for formatted output', default=2, type=int)
args = parser.parse_args()


def main():
    if args.write and not args.file:
        parser.error('write requires at least one file')

    if not args.file:
        # input is piped in.
        round_trip(sys.stdout, sys.stdin, args.width, args.use_yaml_1_1)
        sys.exit(0)

    for file in args.file:
        if args.write:
            # write to temp file then overwrite
            format_and_write(file, args.width, args.use_yaml_1_1)
        else:
            # write output to standard out
            format_and_display(file, args.width, args.use_yaml_1_1)


if __name__ == '__main__':
    sys.exit(main())
