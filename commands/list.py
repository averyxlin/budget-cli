from services.client import get_supabase_client
from globals.total_income import get_total_income

def list_data(table):
    supabase = get_supabase_client()
    response = supabase.table(table).select('*').execute()
    
    data = response.data if response.data else []

    print(f"\n--- {table.upper()} ---")
    if not data:
        print(f"No data found for {table}")
        print() 
        return

    if table == 'income':
        for entry in data:
            if 'category' in entry:
                print(f"Category: {entry['category']}")
            if 'amount' in entry:
                print(f"Amount: {entry['amount']}")
        total_income = get_total_income()
        print(f"TOTAL INCOME: {total_income}")
    elif table == 'monthly_expenses':
        for entry in data:
            if 'needs_total' in entry:
                print(f"Needs: {entry['needs_total']}")
            if 'wants_total' in entry:
                print(f"Wants: {entry['wants_total']}")
            if 'savings_total' in entry:
                print(f"Savings: {entry['savings_total']}")
    
    elif table == 'expense_categories':
        for entry in data:
            if 'expense_type' in entry:
                print(f"{entry['expense_type']}: {entry.get('planned_amount', '')}")
    
    elif table == 'items':
        for entry in data:
            if 'title' in entry:
                print(f"{entry['title']}: {entry.get('amount', '')}")
    
    print()  