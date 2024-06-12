import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame({'customer_number': []})
    df = orders.groupby('customer_number').count().reset_index()
    df.sort_values(by='order_number', ascending=False, inplace=True)
    return df[['customer_number']][0:1]
