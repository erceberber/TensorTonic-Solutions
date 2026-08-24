import numpy as np

def softmax(x: list) -> np.ndarray:
    """Return stable softmax probabilities with the same shape as x."""
    # Write code here

    x = np.asarray(x)
    if len(x.shape) == 1:
        m = np.max(x)
        p = np.exp(x - m)
        p /= np.sum(p)
        return p

    else:
        m = np.max(x, axis=1, keepdims=True)
        x_norm = x - m
        x_norm = np.exp(x_norm)
        s = np.sum(x_norm, axis=1, keepdims=True)
        x_norm /= s
        return x_norm
   
    pass