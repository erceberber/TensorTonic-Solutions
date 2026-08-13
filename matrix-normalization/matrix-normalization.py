import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here

    M = np.asarray(matrix)
    if M.ndim != 2:
        return None

    if axis is not None and axis >= M.ndim:
        return None

    if norm_type == "l2":
        s = np.sqrt(np.sum(M**2, axis=axis, keepdims=True))

    elif norm_type == "l1":
        s = np.sum(np.abs(M), axis=axis, keepdims=True)
        

    elif norm_type == "max":
        s = np.max(M, axis=axis, keepdims=True)

    else:
        return None

    return np.divide(M, s, out=np.zeros_like(M, dtype=float), where= s != 0)

    pass