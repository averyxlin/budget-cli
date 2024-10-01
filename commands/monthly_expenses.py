from services.client import get_supabase_client
from datetime import datetime

def set_monthly_expenses(needs, wants, savings):
    supabase = get_supabase_client()

    today = datetime.now()
    first_day_of_month = today.replace(day=1)

    # Format the date as a string
    month = first_day_of_month.strftime("%Y-%m-%d")  # Change to string for better compatibility

    # Querying the existing expenses
    existing_expenses = supabase.table('monthly_expenses').select('*').eq('month', first_day_of_month.date()).execute().data

    if existing_expenses:
        prev_needs = existing_expenses[0]['needs_total']
        prev_wants = existing_expenses[0]['wants_total']
        prev_savings = existing_expenses[0]['savings_total']
        
        # Update existing expenses
        supabase.table('monthly_expenses').update({
            'month': month,  
            'needs_total': needs, 
            'wants_total': wants, 
            'savings_total': savings
        }).eq('id', existing_expenses[0]['id']).execute()
        
        print(f"Updated expenses for {month} - Needs: {needs}%, Wants: {wants}%, Savings: {savings}%")
        print(f"Previous expenses - Needs: {prev_needs}%, Wants: {prev_wants}%, Savings: {prev_savings}%")
    else:
        # Insert new expenses
        supabase.table('monthly_expenses').insert({
            'month': month,  
            'needs_total': needs, 
            'wants_total': wants, 
            'savings_total': savings
        }).execute()
        print("No existing monthly expenses found.")
        print(f"Created new expenses for {month} - Needs: {needs}%, Wants: {wants}%, Savings: {savings}%")
