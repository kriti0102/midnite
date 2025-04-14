import pandas as pd
from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:postgres@postgres:5432/analytics"
engine = create_engine(DB_URL)

def insert_bets(df):
    df.to_sql("bet", con=engine, schema="raw", if_exists="append", index=False)
