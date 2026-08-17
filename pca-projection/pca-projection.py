import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here
    x = np.asarray(X)
    x = x - np.mean(x, axis=0)
    cov = (x.T @ x) / (x.shape[0] - 1)

    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]

    w = eigenvectors[:, :k]
    """for j in range(k):
        max_idx = np.argmax(np.abs(w[:, j]))
        if w[max_idx, j] < 0:
            w[:, j] *= -1"""
    
    return x @ w
    
    


