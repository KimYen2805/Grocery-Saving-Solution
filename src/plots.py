import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def top_products_pie(df, n=10):
    top = (
        df["product_name"]
        .value_counts()
        .head(n)
        .reset_index()
    )
    top.columns = ["product_name", "order_count"]

    fig = px.pie(
        top,
        names="product_name",
        values="order_count",
        hole=0.4  
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        showlegend=True,
        margin=dict(t=60, b=20, l=20, r=20)
    )

    return fig

def boxplot_orders_by_cluster(rfm):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(
        data=rfm,
        x="cluster",
        y="order_count",
        ax=ax
    )
    ax.set_title("Order Frequency by Customer Segment")
    ax.set_xlabel("Cluster")
    ax.set_ylabel("Number of Orders")
    return fig


def users_per_cluster(rfm):
    fig, ax = plt.subplots()
    rfm["cluster"].value_counts().sort_index().plot(
        kind="bar", ax=ax
    )
    ax.set_title("Users per Cluster")
    ax.set_xlabel("Cluster")
    ax.set_ylabel("Number of Users")
    return fig

def orders_distribution(rfm):
    fig, ax = plt.subplots()
    ax.hist(rfm["order_count"], bins=50)
    ax.set_title("Distribution of Number of Orders per User")
    ax.set_xlabel("Number of Orders")
    ax.set_ylabel("Number of Users")
    return fig


