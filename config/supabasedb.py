import settings as ENV
from supabase import create_client, Client


def supabase_db():
    supabase_client: Client = create_client(ENV.SUPABASE_URL, ENV.SUPABASE_KEY)
    return supabase_client
