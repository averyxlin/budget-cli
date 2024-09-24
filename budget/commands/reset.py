from budget.services.client import get_supabase_client

def reset_base_amount(amount=None):
    supabase_client = get_supabase_client()
    data = supabase_client.table('incomes').select('amount').eq('id', 1).execute()