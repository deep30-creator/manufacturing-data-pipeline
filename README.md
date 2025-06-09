# manufacturing-data-pipeline
Simulate manufacturing and sales data of color-coated roofing sheets, store it, transform it using dbt, orchestrate with Airflow, and visualize using Streamlit.

# 🏭 Manufacturing Data Pipeline Project

This project showcases a simple data engineering workflow using **Python**, **PostgreSQL (Supabase)**, and **CSV ingestion** to simulate real-world manufacturing production and sales data.

---

## 📦 Project Overview

We simulate a manufacturing environment with two datasets:
- `production`: Shift-wise quantity of items produced
- `sales`: Customer-wise quantity sold

Data is loaded from CSV into a cloud-hosted **Supabase PostgreSQL** database using Python and `psycopg2`.

---
# 📦 Supabase Manufacturing Data Pipeline

A simple data engineering project that demonstrates how to:
- Store production and sales data in Supabase
- Load data using Python (`pandas`, `psycopg2`)
- Run SQL queries for analysis

---

## 🛠️ Tech Stack

- 🔸 Python (`psycopg2`, `pandas`)
- 🔸 Supabase (PostgreSQL hosting)
- 🔸 SQL (analytics and table creation)

---

## 🚀 How It Works

1. **Create Tables**  
   `production` and `sales` tables are created if not already present.

2. **Load CSV Data**  
   Python script reads and loads data row-by-row into Supabase using `INSERT`.

3. **Query Results**  
   Sample queries are included to calculate total production and top customers.

---

## 📊 Example Queries

```sql
-- Total units produced
SELECT SUM(quantity_produced) FROM production;

-- Customer with highest sales
SELECT customer, SUM(quantity_sold) AS total
FROM sales
GROUP BY customer
ORDER BY total DESC;

