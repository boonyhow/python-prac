import pandas as pd

df = pd.read_csv('data/orders.csv', nrows=10)


print(df.order_status.to_string())
