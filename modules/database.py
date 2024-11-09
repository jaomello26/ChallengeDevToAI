# modules/database.py
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        dbname=os.environ.get("PGDATABASE"),
        user=os.environ.get("PGUSER"),
        password=os.environ.get("PGPASSWORD"),
        host=os.environ.get("PGHOST"),
        port=os.environ.get("PGPORT"),
        sslmode=os.environ.get("PGSSLMODE", "require")
    )
    return conn

def set_ollama_host():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT set_config('ai.ollama_host', 'http://ollama:11434', false);
        """)
        conn.commit()
    conn.close()

def create_tables():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS interactions (
                id SERIAL PRIMARY KEY,
                user_input TEXT,
                ai_response TEXT
            );
        """)
        conn.commit()
    conn.close()

def save_interaction(user_input, ai_response):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO interactions (user_input, ai_response)
            VALUES (%s, %s);
        """, (user_input, ai_response))
        conn.commit()
    conn.close()
