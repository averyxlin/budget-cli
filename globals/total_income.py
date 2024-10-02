# globals/total_income.py

__all__ = ['get_total_income']

def get_total_income():
    from services.client import get_supabase_client
    supabase = get_supabase_client()

    response = supabase.table('income').select('amount').execute()
    
    total = sum(entry['amount'] for entry in response.data if 'amount' in entry)
    
    return total

