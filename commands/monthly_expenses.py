from services.client import get_supabase_client
from datetime import datetime
from globals.total_income import get_total_income

def set_monthly_expenses(needs, wants, savings):
    supabase = get_supabase_client()

    today = datetime.now()
    first_day_of_month = today.replace(day=1)
    
    # Format the date as a string
    month = first_day_of_month.strftime("%Y-%m-%d")

    # Get the total income
    total_income = get_total_income()
    print(f"Total Income: ${total_income:.2f}")

    # Calculate the actual amounts based on percentages
    needs_amount = total_income * (needs / 100)
    wants_amount = total_income * (wants / 100)
    savings_amount = total_income * (savings / 100)

    # Querying the existing expenses
    existing_expenses = supabase.table('monthly_expenses').select('*').eq('month', month).execute().data

    if existing_expenses:
        prev_needs = existing_expenses[0]['needs']
        prev_wants = existing_expenses[0]['wants']
        prev_savings = existing_expenses[0]['savings']
        
        # Update existing expenses
        supabase.table('monthly_expenses').update({
            'month': month,  
            'needs': needs_amount, 
            'wants': wants_amount, 
            'savings': savings_amount
        }).eq('id', existing_expenses[0]['id']).execute()
        
        print(f"Updated expenses for {month}:")
        print(f"Needs: {needs}% (${needs_amount:.2f})")
        print(f"Wants: {wants}% (${wants_amount:.2f})")
        print(f"Savings: {savings}% (${savings_amount:.2f})")
        print(f"Previous expenses - Needs: ${prev_needs:.2f}, Wants: ${prev_wants:.2f}, Savings: ${prev_savings:.2f}")
    else:
        # Insert new expenses
        supabase.table('monthly_expenses').insert({
            'month': month,  
            'needs': needs_amount, 
            'wants': wants_amount, 
            'savings': savings_amount
        }).execute()
        print("No existing monthly expenses found.")
        print(f"Created new expenses for {month}:")
        print(f"Needs: {needs}% (${needs_amount:.2f})")
        print(f"Wants: {wants}% (${wants_amount:.2f})")
        print(f"Savings: {savings}% (${savings_amount:.2f})")
