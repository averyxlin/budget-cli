import argparse
from commands.income import set_income
from commands.list import list_data
# version
VERSION = "1.0.0"

def main():
    # Create the parser
    parser = argparse.ArgumentParser(prog='budget', description='Budget CLI')

    # --help flag is automatically added
    
    # --version flag
    parser.add_argument('--version', action='version', version=VERSION, help='Show the current version of Budget CLI.')

    parser.add_argument('--list', nargs='?', const='all', choices=['all', 'income', 'monthly_expenses', 'expense_categories', 'items'], help='List data for all tables or a specific table')

    # add income subparser
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    income_parser = subparsers.add_parser('income', help='Log income')
    income_parser.add_argument('category', help='Income category')
    income_parser.add_argument('amount', type=float, help='Income amount')
    
    # parse arguments
    args = parser.parse_args()

    if args.command == 'income':
        set_income(args.category, args.amount)

    if args.list:
        if args.list == 'all':
            for table in ['income', 'monthly_expenses', 'expense_categories', 'items']:
                list_data(table)
        else:
            list_data(args.list)

if __name__ == '__main__':
    main()
