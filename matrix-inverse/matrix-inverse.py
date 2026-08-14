import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    a = np.asarray(A)

    if a.ndim != 2 and a.shape[0] != a[1]:
        return None

    try: 
        inv = np.linalg.inv(a)
        return inv
    except:
        return None

    pass
