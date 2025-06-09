import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_production_data(start_date, days):
    dates = [start_date + timedelta(days=i) for i in range(days)]
    data = {
        "date": dates,
        "shift": [random.choice(["A", "B", "C"]) for _ in range(days)],
        "quantity_produced": [random.randint(200, 500) for _ in range(days)],
    }
    return pd.DataFrame(data)

def generate_sales_data(start_date, days):
    dates = [start_date + timedelta(days=i) for i in range(days)]
    data = {
        "date": dates,
        "customer": [random.choice(["ABC Infra", "RoofX", "Sunshade Ltd."]) for _ in range(days)],
        "quantity_sold": [random.randint(150, 450) for _ in range(days)],
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    start_date = datetime(2024, 1, 1)
    days = 60

    df_production = generate_production_data(start_date, days)
    df_sales = generate_sales_data(start_date, days)

    df_production.to_csv("data/raw_production.csv", index=False)
    df_sales.to_csv("data/raw_sales.csv", index=False)

    print("✅ Raw data generated in `data/` folder.")
