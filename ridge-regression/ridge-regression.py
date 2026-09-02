import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    # Write code here

    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    m, n = X.shape

    w = np.linalg.inv((X.T @ X) + lam * np.identity(n=n)) @ X.T @ y 
    return w
    pass

