import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    if len(x) != len(y):
        raise ValueError
    
    X = np.array(x)
    Y = np.array(y)

    return np.dot(X, Y)
    
    # Write code here
    pass