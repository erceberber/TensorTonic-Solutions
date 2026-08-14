import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    
    try:
        x = np.asarray(matrix)
    except:
        return None

    if x.ndim != 2 or x.shape[0] != x.shape[1]:
        return None

    eigenvalues = np.linalg.eigvals(x)
    #eigenvalues = np.lexsort(eigenvalues)
    return eigenvalues
    pass
