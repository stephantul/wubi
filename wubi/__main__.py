import os
import argparse
import json
from wubi import get


def wubi():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", help="chinese2wubi:cw, wubi2chinese wc")
    parser.add_argument("-c", help="Input chinese words")
    parser.add_argument("-i", help="Input file", required=True)
    parser.add_argument("-o", help="Output file", required=True)
    parser.add_argument("-custom", help="A JSON file containing a dictionary "
                                        "specifying custom relations")
    args = parser.parse_args()

    if args.t not in ['wc', 'cw']:
        parser.print_help()
        return
    if not args.c:
        parser.print_help()
        return
    if args.custom:
        d = json.loads(open("args.custom"))

    if os.path.file.exists(args.o):
        raise ValueError("File {} already exists. Aborting".format(args.o))
    out = open(args.o, 'w')
    for line in open(args.i):
        out.write("{}\n".format(get(args.c, args.t, d)))


if __name__ == '__main__':
    wubi()
