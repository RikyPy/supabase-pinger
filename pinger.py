import os
from supabase import create_client, Client

def fetch_songs():
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("Errore: le variabili d'ambiente SUPABASE_URL e SUPABASE_KEY non sono impostate.")
        return
    
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    response = supabase.table("songs").select("*").execute()
    songs = response.data
    for song in songs:
        print(song)
        
if __name__ == "__main__":
    fetch_songs()