from supabase import create_client
from config.settings import settings
supabase = create_client(settings.supabase_url, settings.supabase_key)
def save_digest(d): return supabase.table("talent_digests").insert(d).execute().data
