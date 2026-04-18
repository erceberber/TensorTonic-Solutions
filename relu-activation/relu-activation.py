import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    ans = np.array(x)
    return np.maximum(0, ans)
    pass