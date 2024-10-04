from services.client import get_supabase_client

from services.client import get_supabase_client

def track_expense(item, amount):
    supabase = get_supabase_client()

    # Check if the item is already in spendings table
    spendings = supabase.table('spendings').select('*').eq('category', item).execute().data

    if spendings:
        # Item exists in spendings table
        current_amount = spendings[0]['amount']
        if current_amount - amount < 0:
            print(f"Error: Cannot spend more than the allocated amount for {item}.")
        else:
            # Update the amount in the spendings table
            new_amount = current_amount - amount
            supabase.table('spendings').update({'amount': new_amount}).eq('category', item).execute()
            print(f"Successfully updated {item}. Spent ${amount:.2f}, ${new_amount:.2f} remaining.")
    else:
        # Item not in spendings table, check expense_categories
        expense_categories = supabase.table('expense_categories').select('*').eq('category', item).execute().data

        if not expense_categories:
            # Item not found in expense_categories
            all_categories = supabase.table('expense_categories').select('category').execute().data
            category_list = ", ".join([cat['category'] for cat in all_categories])
            print(f"Category '{item}' not found. Did you mean one of these: {category_list}? If not, please use the 'categorize' command to create a new category.")
        
        # Item found in expense_categories
        planned_amount = expense_categories[0]['planned_amount']

        # Initialize the spending table with the category and planned amount
        supabase.table('spendings').insert({'category': item, 'amount': planned_amount}).execute()

        # Subtract the amount spent
        new_amount = planned_amount - amount
        supabase.table('spendings').update({'amount': new_amount}).eq('category', item).execute()

        print(f"Successfully added {item}. Spent ${amount:.2f}, ${new_amount:.2f} remaining.")

    # Print the amount left in the spendings table for that item
    updated_spending = supabase.table('spendings').select('amount').eq('category', item).execute().data
    if updated_spending:
        print(f"Amount left for {item}: ${updated_spending[0]['amount']:.2f}")
    else:
        print(f"Error: Could not retrieve updated amount for {item}")


