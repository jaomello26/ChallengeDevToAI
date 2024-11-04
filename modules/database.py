import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_connection():
    conn = psycopg2.connect(dsn=os.environ["TIMESCALE_SERVICE_URL"])
    return conn
