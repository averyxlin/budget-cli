
from budget.services.client import get_supabase_client

def reset_base_amount(amount=None):
    supabase = get_supabase_client()
    
    # retrieve the existing base amount from Supabase
    response = supabase.table("budgets").select("id", "base_amount").order("created_at", desc=True).limit(1).execute()

    # if response.data and len(response.data) > 0:
    #     # we found an existing base amount
    #     existing_base_amount = response.data[0]["base_amount"]
    #     existing_id = response.data[0]["id"]
        
    #     if amount is not None:
    #         # if a new amount is provided, update the base amount
    #         update_response = supabase.table("budgets").update({"base_amount": amount}).eq("id", existing_id).execute()
    #         if update_response.data: # NOTE: supabase responses don't have status codes, e.g. 200. we can only check if the data attribute exists
    #             print(f"Monthly base updated to: ${amount:.2f}")
    #             return True
    #         else:
    #             print("Error updating base amount")
    #             return False
    #     else:
    #         # if no amount is provided, reset to the existing base amount
    #         print(f"Resetting budget to existing base amount: ${existing_base_amount:.2f}")
    #         return True
    # else:
    #     # no existing base amount; prompt for input
    #     print("No base amount found. Please rerun with --reset <amount> to set a new monthly base amount.")
    #     return False