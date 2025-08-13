# kmeans_model.py
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def perform_kmeans(data, k):
    kmeans = KMeans(n_clusters=k, random_state=0)
    clusters = kmeans.fit_predict(data)
    data['Cluster'] = clusters

    # Plot
    plt.figure(figsize=(8, 6))
    for cluster in range(k):
        clustered_data = data[data['Cluster'] == cluster]
        plt.scatter(clustered_data.iloc[:, 0], clustered_data.iloc[:, 1], label=f'Cluster {cluster}')
    plt.xlabel(data.columns[0])
    plt.ylabel(data.columns[1])
    plt.title('Customer Segmentation using K-Means')
    plt.legend()
    plt.savefig('static/plot.png')
    plt.close()
    
    return data
