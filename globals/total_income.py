# globals/total_income.py

__all__ = ['get_total_income', 'update_total_income']

total_income = None  # initialize total income as None for uncached state

def update_total_income():
    global total_income
    
    from services.client import get_supabase_client  # Import here to avoid circular imports
    supabase = get_supabase_client()

    # fetch all income entries and calculate the total
    incomes = supabase.table('income').select('amount').execute().data
    total_income = sum(income['amount'] for income in incomes)
    print(f"Updated total income: {total_income}")

def get_total_income():
    if total_income is None:
        update_total_income()  # call to update if not already cached
        print(f"Total income: {total_income}")
    return total_income

