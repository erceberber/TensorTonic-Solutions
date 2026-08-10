import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    ans = np.array(x)
    ans *= -1
    ans = np.exp(ans)
    ans += 1
    ans = 1 / ans
    return ans
    # Write code here
    pass