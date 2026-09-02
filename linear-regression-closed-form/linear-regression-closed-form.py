import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    m, n = X.shape

    w = np.zeros(n)

    w = (np.linalg.inv(X.T @ X)) @ X.T @ y

    return w


    pass