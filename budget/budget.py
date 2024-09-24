#!/usr/bin/env python3

import argparse
from budget.commands.reset import reset_base_amount

# version
VERSION = "1.0.0"

def main():
    # Create the parser
    parser = argparse.ArgumentParser(prog='budget', description='Budget CLI')

    # --help argument is automatically added
    
    # --version argument
    parser.add_argument('--version', action='version', version=VERSION, help='show the current version of Budget CLI.')

    # --reset
    parser.add_argument('--reset', nargs='?', type=float, metavar='NEW_AMOUNT', help='reset the budget to an optional new monthly base amount. if not provided, resets to the existing base amount.')

    # parse arguments
    args = parser.parse_args()

    if args.reset is not None:
        reset_base_amount(args.reset)
    elif args.reset is not None and args.reset == '':
        reset_base_amount()

if __name__ == '__main__':
    main()