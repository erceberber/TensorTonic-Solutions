import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    xnp = np.asarray(x)
    return np.where(xnp > 0, xnp, 0)
    pass