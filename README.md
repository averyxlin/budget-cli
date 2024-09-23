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

the database for the budget cli application consists of three main tables:

1. **budgets**
2. **categories**
3. **subcategories**

#### 1. budgets table

the **budgets** table stores the overall budgeting information, including the user's base amount for the month.

**schema:**
- `id`: unique identifier for the budget.
- `base_amount`: the monthly take-home salary.
- `created_at`: timestamp of when the budget record was created.

**example data:**

| id | base_amount | created_at          |
|----|-------------|---------------------|
| 1  | 5000        | 2023-10-01 10:00:00 |

#### 2. categories table

the **categories** table categorizes the spending into fundamental areas like needs, wants, and savings. each category is linked to a specific budget.

**schema:**
- `id`: unique identifier for the category.
- `name`: name of the category (e.g., "needs," "wants," "savings").
- `budget_id`: foreign key linking to the budgets table.

**example data:**

| id | name    | budget_id |
|----|---------|-----------|
| 1  | needs   | 1         |
| 2  | wants   | 1         |
| 3  | savings | 1         |

#### 3. subcategories table

the **subcategories** table allows for more granular tracking of expenses within each category. this could include different types of needs (like groceries and utilities) and different types of wants (like entertainment).

**schema:**
- `id`: unique identifier for the subcategory.
- `name`: name of the subcategory (e.g., "groceries," "entertainment").
- `amount`: amount allocated for this subcategory.
- `category_id`: foreign key linking to the categories table.

**example data:**

| id | name          | amount | category_id |
|----|---------------|--------|--------------|
| 1  | groceries     | 300    | 1            |
| 2  | utilities     | 150    | 1            |
| 3  | entertainment  | 200    | 2            |
| 4  | emergency fund | 500    | 3            |

### how it works

- when you set your base amount using the cli, it gets saved in the **budgets** table
- you can categorize your expenses into **categories** such as needs, wants, and savings
- each category can have multiple **subcategories** that detail specific expenses, helping you keep track of where your money is going

### example workflow

1. **set base amount**:
   - command: `budget set 5000`
   - this will create a new record in the **budgets** table with a `base_amount` of 5000

2. **add categories**:
   - you can add categories like "needs," "wants," and "savings" through specific cli commands

3. **log subcategories**:
   - add subcategories under "needs" for precise tracking, such as "groceries" with an amount of 300