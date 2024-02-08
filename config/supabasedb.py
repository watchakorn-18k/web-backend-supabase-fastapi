import os
from supabase import create_client, Client
import dotenv

dotenv.load_dotenv()


def supabase_db():
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase_client: Client = create_client(url, key)
    return supabase_client
