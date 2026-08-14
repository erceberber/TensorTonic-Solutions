import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    xnp = np.asarray(X)
    means = np.mean(xnp, axis=0)
    X_centered = xnp - means
    cov = (X_centered.T @ X_centered) / (X_centered.shape[0] - 1)
    stds = np.std(X_centered, axis=0, ddof=1)
    corr = cov / np.outer(stds, stds)

    return corr
    
    pass


