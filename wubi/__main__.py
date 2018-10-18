import os
import argparse
import json
from wubi import chinese2wubi, wubi2chinese


def wubi():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t",
                        help="chinese2wubi: cw, wubi2chinese: wc",
                        default='cw')
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
    if args.t == "wc":
        func = wubi2chinese
    elif args.t == "cw":
        func = chinese2wubi
    else:
        raise ValueError("-t must be either 'wc' or 'cw', "
                         "was now {}".format(args.t))
    for line in open(args.i):
        out.write("{}\n".format(func(line, args.t, d)))


if __name__ == '__main__':
    wubi()
