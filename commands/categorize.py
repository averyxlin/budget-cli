from datetime import datetime
from budget.services.client import get_supabase_client

def categorize(category, expense_type, planned_amount):
    # print(f"Categorizing {category} as {expense_type} with planned amount {planned_amount}")

    supabase = get_supabase_client()

    today = datetime.now()
    first_day_of_month = today.replace(day=1)
    month = first_day_of_month.strftime("%Y-%m-%d")

    existing_expenses = supabase.table('monthly_expenses').select('*').eq('month', month).execute().data

    if not existing_expenses:
        print(f"No existing monthly expenses found for the month: {month}. Please set your monthly expenses first using the 'divide' command.")
        return
    
    monthly_expenses = existing_expenses[0]

    if expense_type not in ['needs', 'wants', 'savings']:
        print(f"Invalid expense type: {expense_type}. Please specify 'needs', 'wants', or 'savings'.")
        return
    
    needs = monthly_expenses['needs']
    wants = monthly_expenses['wants']
    savings = monthly_expenses['savings']

    print(f"Needs: {needs}, Wants: {wants}, Savings: {savings}")

        