import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    ans = np.array(x)
    return np.where(ans < 0, ans * alpha, ans)
    
    pass