import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y = np.asarray(y)

    if num_classes is None:
        num_classes = np.max(y) + 1

    result = np.zeros((y.size, num_classes))
    result[np.arange(y.size), y] = 1

    return result
        
    pass

