import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

load_dotenv()

host='localhost'
database=os.getenv('POSTGRES_DB')
user=os.getenv('POSTGRES_USER')
password=os.getenv('POSTGRES_PASSWORD')
port = '5432'

def read_records_into_df(table):
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

    df = pd.read_sql_table(table, engine)

    return df

def make_line_graph(table):
    df = read_records_into_df(table)
    fig = px.line(df, x="date", y="cost_per_round", color='casing')
    fig.show()

if __name__ == '__main__':
    make_line_graph('caliber_9mm')