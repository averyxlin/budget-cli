# budget/budget.py

# import ssl

# ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL

import argparse
from commands.income import set_income

# version
VERSION = "1.0.0"

def main():
    # Create the parser
    parser = argparse.ArgumentParser(prog='budget', description='Budget CLI')

    # --help flag is automatically added
    
    # --version flag
    parser.add_argument('--version', action='version', version=VERSION, help='Show the current version of Budget CLI.')

    # Add income subparser
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    income_parser = subparsers.add_parser('income', help='Log income')
    income_parser.add_argument('category', help='Income category')
    income_parser.add_argument('amount', type=float, help='Income amount')
    
    # Parse arguments
    args = parser.parse_args()

    if args.command == 'income':
        set_income(args.category, args.amount)

if __name__ == '__main__':
    main()
