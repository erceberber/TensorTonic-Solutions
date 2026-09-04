import numpy as np

def k_means_centroid_update(points: list, assignments: list, k: int) -> list:
    """
    Returns one updated centroid for each cluster.
    """
    # Write code here
    p = np.asarray(points, dtype=float)
    a = np.asarray(assignments, dtype=int)

    new_centroids = []
    for i in range(k):
        curr_cluster = p[np.where(a == i)]
        
        if len(curr_cluster) > 0:
            new_centroids.append(np.mean(curr_cluster, axis=0).tolist())
        else:
            new_centroids.append(np.zeros(p.shape[1]).tolist())

    return new_centroids
        






    pass

print(k_means_centroid_update(k = 2, points = [[1,1],[2,2]], assignments = [0,0]))