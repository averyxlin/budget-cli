# services/client.py

import ssl
from supabase import create_client
from dotenv import load_dotenv
import os
import certifi

# Load environment variables
load_dotenv(dotenv_path='env/.env')

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Create SSL context
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_supabase_client():
    return supabase
