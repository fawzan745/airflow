import pandas as pd
import sqlite3

def to_sqlite():
    input_path = "data/extracted_data.csv"
    df = pd.read_csv(input_path) 
    conn = sqlite3.connect("data/extracted_data.db")
    df.to_sql("data", conn, if_exists="replace", index=False)