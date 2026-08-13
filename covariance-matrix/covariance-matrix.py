import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here

    xnp = np.asarray(X)

    shape = xnp.shape

    if shape[0] < 2 or len(shape) < 2:
        return None

    mean = np.mean(xnp, axis=0)

    xnp = xnp - mean

    cov = xnp.T @ xnp

    cov = cov / (shape[0] - 1)

    return cov

    
    pass