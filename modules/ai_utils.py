from modules.database import get_connection


def vectorize_content(content):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT pgai.embed($$%s$$)
        """, (content,))
        embedding = cur.fetchone()[0]
    conn.close()
    return embedding


def insert_story_element(content):
    embedding = vectorize_content(content)
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO story_elements (content, embedding)
            VALUES (%s, %s)
        """, (content, embedding))
        conn.commit()
    conn.close()


def generate_response(prompt):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT pgai.generate_text($$%s$$)
        """, (prompt,))
        response = cur.fetchone()[0]
    conn.close()
    return response
