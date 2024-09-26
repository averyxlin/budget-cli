# budget/budget.py

import ssl

ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL

import argparse
from commands.income import set_income

# version
VERSION = "1.0.0"

def main():
    # Create the parser
    parser = argparse.ArgumentParser(prog='budget', description='Budget CLI')

    # --help argument is automatically added
    
    # --version argument
    parser.add_argument('--version', action='version', version=VERSION, help='Show the current version of Budget CLI.')

    # Add --income argument
    parser.add_argument('--income', nargs=2, metavar=('<category>', '<amount>'), help="Log income. Usage: --income <category> <amount>")
    
    # Parse arguments
    args = parser.parse_args()

    if args.income:
        # Extract the category and amount
        category = args.income[0]  # This is directly the string
        amount = float(args.income[1])  # Convert amount to float
        set_income(category, amount)

if __name__ == '__main__':
    main()
