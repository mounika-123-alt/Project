# utils/clv.py

def calculate_metrics(df):
    total_revenue = df["revenue"].sum()
    total_orders = df.shape[0]
    total_customers = df["customer_id"].nunique()

    purchase_frequency = total_orders / total_customers
    aov = total_revenue / total_orders

    return purchase_frequency, aov


def calculate_clv(df, lifespan=2):
    pf, aov = calculate_metrics(df)
    clv = pf * aov * lifespan
    return clv, pf, aov