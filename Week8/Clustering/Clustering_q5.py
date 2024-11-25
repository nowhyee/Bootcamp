from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

# Load food nutrients dataset
data = pd.read_csv("glass.csv")
X = data.drop("Type", axis=1)

# Try different k values
k_values = [2, 3, 4, 5, 6]
for k in k_values:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inertia = kmeans.inertia_
    silhouette = silhouette_score(X, kmeans.labels_)
    print(f"K={k}, Inertia={inertia}, Silhouette Score={silhouette}")
