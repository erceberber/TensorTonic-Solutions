import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    xnp = np.asarray(x)
    xnp *= -1
    xnp = np.exp(xnp)
    xnp += 1

    return 1 / xnp
    
    pass