import argparse
import json

# Python 2 support.
from io import open
from wubi import to_wubi, from_wubi


def wubi():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t",
                        help="chinese2wubi: cw, wubi2chinese: wc",
                        default='cw')
    parser.add_argument("-d",
                        help="delimiter",
                        default=" ")
    parser.add_argument("-i", help="Input file", required=True)
    parser.add_argument("-o", help="Output file", required=True)
    parser.add_argument("-custom", help="A JSON file containing a dictionary "
                                        "specifying custom relations")
    args = parser.parse_args()

    if args.t not in ['wc', 'cw']:
        parser.print_help()
        return
    if args.custom:
        d = json.loads(open("args.custom"))
    else:
        d = None
    out = open(args.o, 'w')
    if args.t == "wc":
        func = from_wubi
    elif args.t == "cw":
        func = to_wubi
    else:
        raise ValueError("-t must be either 'wc' or 'cw', "
                         "was now {}".format(args.t))
    for line in open(args.i):
        out.write("{}\n".format(func(line, delimiter=args.d, dictionary=d)))


if __name__ == '__main__':
    wubi()
