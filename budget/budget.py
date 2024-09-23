#!/usr/bin/env python3

import argparse

# version
VERSION = "1.0.0"

def main():
    # Create the parser
    parser = argparse.ArgumentParser(prog='budget', description='Budget CLI')

    # --help argument is automatically added
    
    # --version argument
    parser.add_argument('--version', action='version', version=VERSION, help='show the current version of Budget CLI.')

    # parse arguments
    args = parser.parse_args()

if __name__ == '__main__':
    main()
