# commands/set.py
from services.supabase_client import get_supabase_client

def set_base_amount(amount):
    supabase = get_supabase_client()
    
    # insert or update the budget record
    response = supabase.table("budgets").insert({"base_amount": amount}).execute()
    if response.status_code == 201:
        print(f"Monthly base set to: ${amount:.2f}")
    else:
        print("Error setting base amount:", response.data)
