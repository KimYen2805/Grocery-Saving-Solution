def build_rfm(df):
    rfm = (
        df.groupby("user_id")
        .agg(
            order_count=("order_id", "nunique"),
            product_count=("product_id", "count"),
            max_order_number=("order_number", "max"),
        )
        .reset_index()
    )
    return rfm
