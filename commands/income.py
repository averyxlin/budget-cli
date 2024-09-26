# commands/income.py

from budget.services.client import get_supabase_client
from globals.total_income import update_total_income

def set_income(category, amount):
    supabase = get_supabase_client()

    # check if the category already exists
    existing_income = supabase.table('income').select('*').eq('category', category).execute().data

    if existing_income:
        # update the existing entry
        existing_id = existing_income[0]['id']
        supabase.table('income').update({'amount': amount}).eq('id', existing_id).execute()
        if amount == 0:
            supabase.table('income').delete().eq('id', existing_id).execute()
            print(f"Deleted {category}.")
        else:
            print(f"Updated {category} to {amount}.")
    else:
        # insert new entry
        supabase.table('income').insert({'category': category, 'amount': amount}).execute()
        print(f"Logged new income: {category} = {amount}.")

    update_total_income()