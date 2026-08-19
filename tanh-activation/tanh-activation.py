import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    xnp = np.asarray(x)

    result = np.exp(xnp) - np.exp(-1 * xnp)
    result /= np.exp(xnp) + np.exp(-1 * xnp)
    return result
    pass