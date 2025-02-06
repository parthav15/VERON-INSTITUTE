import pandas as pd
import numpy as np

np.random.seed(42)

start_date = "2023-01-01"
end_date = "2024-01-01"
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

num_days = len(date_range)
sales_units = np.random.randint(50, 200, size=num_days)
price_per_candle = 20
revenue = sales_units * price_per_candle

raw_material_used = sales_units * 0.5

df = pd.DataFrame({
    "date": date_range,
    "sales_units": sales_units,
    "revenue": revenue,
    "raw_material_used": raw_material_used
})

df.to_csv("synthetic_candle_sales.csv", index=False)

print("Synthetic data generated and saved as 'synthetic_candle_sales.csv'!")

