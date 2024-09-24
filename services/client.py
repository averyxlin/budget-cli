# services/client.py

import os
from supabase import create_client
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv(dotenv_path='env/.env')

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_supabase_client():
    return supabase
