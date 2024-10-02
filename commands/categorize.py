from datetime import datetime
from budget.services.client import get_supabase_client
from globals.total_montly_expenses import get_total_needs, get_total_wants, get_total_savings

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

    if expense_type == 'needs':
        total_needs = get_total_needs()
        print(f"Total Needs: {total_needs}")
        if total_needs + planned_amount > needs:
            print(f"Error: Exceeds amount allocated for needs this month: {planned_amount} exceeds remaining {needs - total_needs}.")
            return

    elif expense_type == 'wants':
        total_wants = get_total_wants()
        print(f"Total Wants: {total_wants}")
        if total_wants + planned_amount > wants:
            print(f"Error: Exceeds amount allocated for wants this month:{planned_amount} exceeds remaining {wants - total_wants}.")
            return

    elif expense_type == 'savings':
        total_savings = get_total_savings()
        print(f"Total Savings: {total_savings}")
        if total_savings + planned_amount > savings:
            print(f"Error: Exceeds amount allocated for savings this month: {planned_amount} exceeds remaining {savings - total_savings}.")
            return
