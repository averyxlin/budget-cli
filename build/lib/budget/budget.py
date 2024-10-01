import argparse
from commands.income import set_income
from commands.list import list_data
from commands.monthly_expenses import set_monthly_expenses
from commands.categorize import categorize

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

     # add divide subparser
    divide_subparser = subparsers.add_parser('divide', help='Divide total income into needs, wants, and savings')
    divide_subparser.add_argument('percentages', type=int, nargs='*', help='Percentages for needs, wants, and savings in order')

    # add categorize subparser
    categorize_subparser = subparsers.add_parser('categorize', help='Categorize expenses')
    categorize_subparser.add_argument('category', help='Category to categorize the expense under')
    categorize_subparser.add_argument('expense_type', choices=['needs', 'wants', 'savings'], help='Type of expense to categorize')
    categorize_subparser.add_argument('planned_amount', type=float, help='Planned amount for the expense')

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

    if args.command == 'divide':
        if args.percentages:
            if len(args.percentages) != 3:
                parser.error("You must provide exactly 3 percentages, with each position corresponding to <needs>, <wants>, and <savings>.")
            needs, wants, savings = args.percentages
        else:
            needs = args.needs
            wants = args.wants
            savings = args.savings

        if needs + wants + savings != 100:
            parser.error(f"The percentages must add up to 100%. \n"
                        f"CURRENT TOTAL: {needs + wants + savings}%. \n"
                        f"NEEDS: {needs}%, WANTS: {wants}%, SAVINGS: {savings}%")

        set_monthly_expenses(needs, wants, savings)

    if args.command == 'categorize':
        categorize(args.category, args.expense_type, args.planned_amount)

if __name__ == '__main__':
    main()
