import pandas as pd
from matplotlib import pyplot as plt
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load CSV
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'Superstore.csv'), encoding="latin1")

# Upload raw data
df.to_sql("orders_raw", engine, if_exists="replace", index=False)
print("raw data loaded successfully")

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Fix data types
df["order_date"] = pd.to_datetime(df["order_date"], format="%d/%m/%Y")
df["ship_date"] = pd.to_datetime(df["ship_date"], format="%d/%m/%Y")

# Upload clean data
df.to_sql("orders_clean", engine, if_exists="replace", index=False)
print("clean data loaded successfully")