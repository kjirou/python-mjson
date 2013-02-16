r"""Command-line tool to validate and pretty-print JSON

@author python json module

Usage::

"""
import sys
import json
from optparse import OptionParser

def main():

    parser = OptionParser()
    parser.add_option('-i', '--indent', dest='indent', type='int', action='store', default=4)
    options, args = parser.parse_args()

    if len(args) == 0:
        infile = sys.stdin
        outfile = sys.stdout
    elif len(args) == 1:
        infile = open(args[0], 'rb')
        outfile = sys.stdout
    elif len(args) == 3:
        infile = open(args[0], 'rb')
        outfile = open(args[1], 'wb')
    else:
        raise SystemExit(sys.argv[0] + " [infile [outfile]]")
    try:
        obj = json.load(infile)
    except ValueError as e:
        raise SystemExit(e)
    json.dump(obj, outfile, sort_keys=True, indent=options.indent)
    outfile.write('\n')


if __name__ == '__main__':
    main()
