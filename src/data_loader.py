import pandas as pd

def load_data(data_path="data"):
    orders = pd.read_csv(f"{data_path}/orders.csv")
    order_products = pd.read_csv(f"{data_path}/order_products__prior.csv")
    products = pd.read_csv(f"{data_path}/products.csv")

    df = orders.merge(order_products, on="order_id")
    df = df.merge(products, on="product_id")

    return df
