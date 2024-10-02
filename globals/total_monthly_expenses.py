# globals/total_needs.py

__all__ = ['get_total_needs', 'get_total_wants', 'get_total_savings']

def get_total_needs():
    from services.client import get_supabase_client
    supabase = get_supabase_client()

    needs = supabase.table('expense_categories').select('*').eq('expense_type', 'needs').execute().data 
    total_needs = sum(need['planned_amount'] for need in needs)
    
    return total_needs

def get_total_wants():
    from services.client import get_supabase_client
    supabase = get_supabase_client()

    wants = supabase.table('expense_categories').select('*').eq('expense_type', 'wants').execute().data 
    total_wants = sum(want['planned_amount'] for want in wants)
    
    return total_wants

def get_total_savings():
    from services.client import get_supabase_client
    supabase = get_supabase_client()

    savings = supabase.table('expense_categories').select('*').eq('expense_type', 'savings').execute().data 
    total_savings = sum(saving['planned_amount'] for saving in savings)
    
    return total_savings

    