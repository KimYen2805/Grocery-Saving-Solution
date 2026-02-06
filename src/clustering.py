from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def add_clusters(rfm, n_clusters=4):
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(
        rfm[["order_count", "product_count", "max_order_number"]]
    )

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    rfm["cluster"] = kmeans.fit_predict(rfm_scaled)

    return rfm
