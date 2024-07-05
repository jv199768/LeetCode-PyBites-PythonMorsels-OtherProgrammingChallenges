import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    date_sales = sales.groupby(by='product_id').agg(min_date=('sale_date', 'min'),max_date=('sale_date','max')).merge(product, on='product_id').query('min_date >= "2019-01-01" and max_date <= "2019-03-31"')[['product_id', 'product_name']]
    return date_sales
