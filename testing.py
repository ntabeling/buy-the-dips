import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect():
    host='localhost'
    database=os.getenv('POSTGRES_DB')
    user=os.getenv('POSTGRES_USER')
    password=os.getenv('POSTGRES_PASSWORD')

    conn = psycopg2.connect(host=host, dbname=database, user=user, password=password)

    cur = conn.cursor()

    cur.execute('SELECT * from caliber_9mm')

    print(cur.fetchone())

    cur.close()

if __name__ == '__main__':
    connect()