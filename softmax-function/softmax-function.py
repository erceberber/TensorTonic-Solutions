import numpy as np

def softmax(x: list) -> np.ndarray:
    """Return stable softmax probabilities with the same shape as x."""
    # Write code here

    x = np.asarray(x)
    if len(x.shape) == 1:
        m = np.max(x)
        p = np.exp(x - m)
        p /= np.sum(p)

    else:
        p = []
        for i in range(len(x)):
            m = np.max(x[i])
            s = np.sum(np.exp(x[i]))
            p_i = np.exp(x[i]) / s
            p.append(p_i)

    return np.asarray(p)

        
    pass