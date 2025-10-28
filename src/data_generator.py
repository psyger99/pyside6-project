# ─────────────────────────────────────────────────────────────
# data_generator.py — Generate fake employee data 
# ─────────────────────────────────────────────────────────────

import pandas as pd
import random
from faker import Faker
from datetime import date

fake = Faker()

departments = ["IT", "HR", "Operations", "Administration", "Finance"]

def generate_employee_data(n: int) -> pd.DataFrame:
    """
    Generate synthetic employee data for n employees.

    Args:
        n (int): Number of employees to generate.

    Returns:
        pd.DataFrame: A DataFrame containing columns:
            - emp_id: Auto-incrementing integer starting at 1
            - full_name: Random realistic name
            - department: Randomly chosen from predefined list
            - salary: Random integer between 25,000 and 120,000
            - hire_date: Random date between 2020-01-01 and today
    """
    
    data = []
    for i in range(1, n + 1):
        data.append({
            "emp_id": i,
            "full_name": fake.name(),
            "department": random.choice(departments),
            "salary": round(random.randint(25000, 120000), -2),
            "hire_date": fake.date_between(start_date=date(2020, 1, 1), end_date=date.today()).strftime("%Y-%m-%d")
        })
    return pd.DataFrame(data)