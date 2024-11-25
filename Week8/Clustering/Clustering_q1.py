from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

# Load data
data = pd.read_csv("iris.csv")
X = data.drop("Name", axis=1)

k_values = [2, 3, 4, 5, 6]
for k in k_values:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inertia = kmeans.inertia_
    silhouette = silhouette_score(X, kmeans.labels_)
    print(f"K={k}, Inertia={inertia}, Silhouette Score={silhouette}")


#(a) How do the inertia and silhouette scores change?
# As k increases, because of the clusters, inertia decreases.
# However, silhouette scores may decrease if k becomes too large since the clusters become less meaningful. 

#(b) What if you don't scale your features?
# If features are not scaled, clustering algorithms like kmeans can be affected by the magnitude of the features. 
# Some features might dominate the clustering process. 
    
#(c) Is there a 'right' k? Why or why not?
# There is no right k. Finding k is more about finding a meaningful number of clusters for the analysis
# k depends on the dataset and methods such as elbow or silhouette scores can guide but can not say it is right. 
