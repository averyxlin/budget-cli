from datetime import datetime
from services.client import get_supabase_client
from globals.total_income import get_total_income
from globals.total_monthly_expenses import get_total_needs, get_total_wants, get_total_savings
def list_data(table):
    supabase = get_supabase_client()
    response = supabase.table(table).select('*').execute()
    
    data = response.data if response.data else []

    if table == 'income':
        if data:
            print(f"\n--- INCOME ---")
            total_income = get_total_income()
            print(f"TOTAL INCOME: ${total_income}")
            for entry in data:
                if 'category' in entry:
                    print(f"Category: {entry['category']} (${entry['amount']})")\
                    
    elif table == 'monthly_expenses':
        print(f"\n--- MONTHLY EXPENSES BREAKDOWN ---")
        today = datetime.now()
        first_day_of_month = today.replace(day=1)
        month = first_day_of_month.strftime("%Y-%m-%d")
        existing_expenses = supabase.table('monthly_expenses').select('*').eq('month', month).execute().data
        if existing_expenses:
            for entry in existing_expenses:
                total_income = get_total_income()
                if 'needs' in entry:
                    print(f"Needs: ${entry['needs']} ({entry['needs'] / total_income * 100:.2f}%)")   
                if 'wants' in entry:
                    print(f"Wants: ${entry['wants']} ({entry['wants'] / total_income * 100:.2f}%)")
                if 'savings' in entry:
                    print(f"Savings: ${entry['savings']} ({entry['savings'] / total_income * 100:.2f}%)")
        else:
            print(f"No expenses found for {month}")
    
    elif table == 'expense_categories':
        needs = False
        wants = False
        savings = False
        if data:        
            print(f"\n--- EXPENSE CATEGORY BREAKDOWN ---")
            for entry in data:
                if 'expense_type' in entry:
                    if entry['expense_type'] == 'needs':
                        if not needs:
                            print("NEEDS:")
                            needs = True
                        print(f"{entry['category']}: ${entry['planned_amount']}")
                    elif entry['expense_type'] == 'wants':
                        if not wants:
                            print("WANTS:")
                            wants = True
                        print(f"{entry['category']}: ${entry['planned_amount']}")
                    elif entry['expense_type'] == 'savings':
                        if not savings:
                            print("SAVINGS:")
                            savings = True
                        print(f"{entry['category']}: ${entry['planned_amount']}")
    elif table == 'items':
        print(f"\n--- ITEMS PURCHASED ---")
        if data:
            for entry in data:  
                if 'title' in entry:
                        print(f"{entry['title']}: ${entry.get('amount', '')}")

    if not data:
        print(f"No data found for {table}")
        print() 
        return
    
    print()  