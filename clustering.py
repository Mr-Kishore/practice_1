from numpy import where
from numpy import unique
from sklearn.datasets import make_classification
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plot

# Initializing data
train_data, _ = make_classification(n_samples=1000,
                                       n_features=2,
                                       n_informative=2,
                                       n_redundant=0,
                                       n_clusters_per_class=1,
                                       random_state=4)

agg_mdl = AgglomerativeClustering(n_clusters=4)

# each data point assigned to cluster
agg_result = agg_mdl.fit_predict(train_data)

# Obtain all clusters which are unique
agg_clusters = unique(agg_result)

# plot clusters
for agg_cluster in agg_clusters:
    # fetch data point that fall in this clstr
    index = where(agg_result == agg_cluster)

    plot.scatter(train_data[index, 0], train_data[index,1])

# Agglomerative hierarchy plot
plot.show()