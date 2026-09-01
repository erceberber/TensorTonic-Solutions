import numpy as np
def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    # Write code here
    dim = len(points[0])
    result = []
    for i in range(len(points)):
        minDist = np.inf
        minDist_idx = 0
        for j in range(len(centroids)):
            dist = 0
            for k in range(dim):
                dist += (points[i][k] - centroids[j][k])**2

            if dist < minDist:
                minDist = dist
                minDist_idx = j
        result.append(minDist_idx)


    return result