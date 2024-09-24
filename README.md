# budget-cli

## description
a simple python and supabase cli. i kind of have a spending problem, but i can't possibly be bothered to download a budgeting app or use a spreadsheet. however, i'm always using my terminal, so i thought this would be an easy way for me to log things without being overwhelmed by the ui.

### usage
available commands:
1. default `--version` and `--help`

## technologies
- the cli itself is built with python
- supabase is used for data storage

### database overview
the database is designed to track budgeting information, consisting of five main tables:

- **incomes**: stores the base amount made every month
- **budgets**: stores the total amount remaining to be allocated
- **categories**: stores high-level categories (e.g., "needs", "wants", "savings")
- **subcategories**: stores subcategories under each category (e.g., "groceries", "entertainment")
- **allocations**: stores the amount allocated to each category and subcategory