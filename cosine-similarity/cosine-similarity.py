import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    
    A = np.array(a)
    B = np.array(b)

    A_norm = np.linalg.norm(A)
    B_norm = np.linalg.norm(B)

    if A_norm == 0 or B_norm == 0:
        return 0

    return np.dot(A, B) / (A_norm * B_norm)
    
    pass