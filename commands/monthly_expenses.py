# commands/monthly_expenses.py

from services.client import get_supabase_client
from datetime import datetime

def set_monthly_expenses(needs, wants, savings):
    total = needs + wants + savings

    supabase = get_supabase_client()
    