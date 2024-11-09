# modules/ai_utils.py
from modules.database import get_connection

def generate_response(prompt):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT ai.ollama_chat_complete(
                'llama2',
                jsonb_build_array(
                    jsonb_build_object('role', 'system', 'content', 'You are a useful game assistant.'),
                    jsonb_build_object('role', 'user', 'content', %s)
                )
            )->'message'->>'content' AS response;
        """, (prompt,))
        result = cur.fetchone()
        response = result[0] if result else "Sorry, I couldn't generate a response."
    conn.close()
    return response
