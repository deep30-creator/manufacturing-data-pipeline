import psycopg2
import pandas as pd

# PostgreSQL connection settings
conn_params = {
    "dbname": "postgres",
    "user": "postgres.xuxdfohhcilfxvrowyxq",
    "password": "creator@2025",
    "host": "aws-0-ap-south-1.pooler.supabase.com",  # or your RDS/public IP
    "port": 5432 ,
}

def create_tables():
    create_production = """
    CREATE TABLE IF NOT EXISTS production (
        id SERIAL PRIMARY KEY,
        date DATE NOT NULL,
        shift VARCHAR(1),
        quantity_produced INTEGER
    );
    """
    create_sales = """
    CREATE TABLE IF NOT EXISTS sales (
        id SERIAL PRIMARY KEY,
        date DATE NOT NULL,
        customer VARCHAR(100),
        quantity_sold INTEGER
    );
    """
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(create_production)
            cur.execute(create_sales)
        conn.commit()
    print("✅ Tables created or verified.")

def load_csv_to_table(csv_file, table_name):
    df = pd.read_csv(csv_file)

    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            for _, row in df.iterrows():
                if table_name == "production":
                    cur.execute(
                        "INSERT INTO production (date, shift, quantity_produced) VALUES (%s, %s, %s)",
                        (row["date"], row["shift"], row["quantity_produced"])
                    )
                elif table_name == "sales":
                    cur.execute(
                        "INSERT INTO sales (date, customer, quantity_sold) VALUES (%s, %s, %s)",
                        (row["date"], row["customer"], row["quantity_sold"])
                    )
        conn.commit()
    print(f"✅ Loaded data into '{table_name}'.")

if __name__ == "__main__":
    create_tables()
    load_csv_to_table("data/raw_production.csv", "production")
    load_csv_to_table("data/raw_sales.csv", "sales")
