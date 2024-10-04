# budget-cli

## description
a simple python and supabase cli. i kind of have a spending problem, but i can't possibly be bothered to download a budgeting app or use a spreadsheet. however, i'm always using my terminal, so i thought this would be an easy way for me to log things without being overwhelmed by the ui.

## usage
### installation
1. clone the repo
2. `python3 -m venv env`
3. `source env/bin/activate`
4. `pip install .`
5. call any of the following commands in the format `budget <command> <flags>`

### available commands and flags
1. `--version`: shows the current version of the budget cli
2. `--help`: displays help information about the cli
3. `--list`: lists data from a specified table. if no table is specified, it lists all tables.
4. `income <category> <amount>`: logs income, taking a category (like ‘salary’) and an amount as input. if the category already exists, it updates the amount; otherwise, it creates a new entry
5. `divide <needs> <wants> <savings>`: divides the total income into needs, wants, and savings based on the percentages provided
6. `categorize <category> <expense_type> <planned_amount>`: categorizes an expense (e.g. groceries, rent, etc.) under a specific type (needs, wants, savings) and specifies the planned amount for that expense.
7. `track <item> <amount>`: tracks an expense by itemizing it, taking the item and amount as input. if the item already exists, it updates the amount; otherwise, it creates a new entry.

### future features
- [ ] a flag to undo and redo actions. especially useful for track, since it's easy to accidentally track the same thing more than once
- [ ] delete functionality to income, divide, categorize (and track? but that can be done through undo. not sure yet)
- [ ] a summary command that takes in a month and year and shows the breakdown of where the money went

## technologies + database overview
the cli uses supabase to store and manage budget-related data. the database structure is designed to track income and monthly expenses with clear categorizations.

1. **tables:**
   - **income table**: stores entries for different sources of income (e.g., salary, other).
      - fields: `id`, `category`, `amount`, `date`.

   - **monthly expenses table**: tracks expenses on a monthly basis.
      - fields: `id`, `month`, `needs`, `wants`, `savings`.

   - **expense categories table**: categorizes expenses into expense types (needs, wants, savings) with a planned amount for each type.
      - fields: `id`, `expense_type`, `category`, `planned_amount`.

   - **items table**: tracks amount spent on the items categorized in expense categories.
      - fields: `id`, `category`, `amount`

2. **technologies**:
   - the cli itself is built with python
   - supabase is used for data storage