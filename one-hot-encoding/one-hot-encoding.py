import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    result = []
    if num_classes is not None:
        result = []
        for i in range(len(y)):
            out = np.zeros(num_classes)
            out[y[i]] = 1
            result.append(out)


    else:
        K = np.max(y) + 1
        for i in range(len(y)):
            out = np.zeros(K)
            out[y[i]] = 1
            result.append(out)

    return np.asarray(result)
        
    pass