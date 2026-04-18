import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    ans = np.array(x)
    ans = -1*ans
    ans = np.exp(ans)
    ans = ans + 1
    ans = 1 / ans
    return ans
    pass