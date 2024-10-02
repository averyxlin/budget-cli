from datetime import datetime
from budget.services.client import get_supabase_client
from globals.total_monthly_expenses import get_total_needs, get_total_wants, get_total_savings

def categorize(category, expense_type, planned_amount):
    # Validate inputs
    if not isinstance(category, str):
        print("Error: category must be a string.")
        return
    
    if not isinstance(planned_amount, (float, int)):  # Accept both float and int for planned amount
        print("Error: planned_amount must be a float.")
        return

    if not isinstance(expense_type, str) or expense_type not in ['needs', 'wants', 'savings']:
        print("Error: expense_type must be a string and one of 'needs', 'wants', or 'savings'.")
        return
    
    # Proceed with categorization
    supabase = get_supabase_client()

    today = datetime.now()
    first_day_of_month = today.replace(day=1)
    month = first_day_of_month.strftime("%Y-%m-%d")

    existing_expenses = supabase.table('monthly_expenses').select('*').eq('month', month).execute().data

    if not existing_expenses:
        print(f"No existing monthly expenses found for the month: {month}. Please set your monthly expenses first using the 'divide' command.")
        return
    
    monthly_expenses = existing_expenses[0]

    needs = monthly_expenses['needs']
    wants = monthly_expenses['wants']
    savings = monthly_expenses['savings']

    print(f"Needs: ${needs:.2f}, Wants: ${wants:.2f}, Savings:${savings:.2f}")

    total_needs = get_total_needs()
    total_wants = get_total_wants()
    total_savings = get_total_savings()
    if expense_type == 'needs':
        if total_needs + planned_amount > needs:
            print(f"Error: Exceeds amount allocated for needs this month: ${planned_amount:.2f} exceeds remaining ${(needs - total_needs):.2f}.")
            return

    elif expense_type == 'wants':
        if total_wants + planned_amount > wants:
            print(f"Error: Exceeds amount allocated for wants this month: ${planned_amount:.2f} exceeds remaining ${(wants - total_wants):.2f}.")
            return

    elif expense_type == 'savings':
        if total_savings + planned_amount > savings:
            print(f"Error: Exceeds amount allocated for savings this month: ${planned_amount:.2f} exceeds remaining ${(savings - total_savings):.2f}.")
            return

    # Check if the category already exists
    existing_category = supabase.table('expense_categories').select('*').eq('category', category).execute().data

    if existing_category:
        # Update the existing category
        supabase.table('expense_categories').update({
            'planned_amount': planned_amount,
            'expense_type': expense_type  
        }).eq('category', category).execute()
        print(f"Updated existing category {category} with new planned amount ${planned_amount:.2f} and expense type {expense_type}.")
    else:
        # Insert a new category
        supabase.table('expense_categories').insert({
            'category': category,
            'planned_amount': planned_amount,
            'expense_type': expense_type  
        }).execute()
        print(f"Created new category {category} as {expense_type} with planned amount ${planned_amount:.2f}.")

    if expense_type == 'needs':
        print(f"Total Needs: ${total_needs:.2f}")
        print(f"Remaining amount for needs: ${needs - total_needs:.2f}")

    elif expense_type == 'wants':
        print(f"Total Wants: ${total_wants:.2f}")
        print(f"Remaining amount for wants: ${wants - total_wants}")

    elif expense_type == 'savings':
        print(f"Total Savings: ${total_savings:.2f}")
        print(f"Remaining amount for savings: ${savings - total_savings}")