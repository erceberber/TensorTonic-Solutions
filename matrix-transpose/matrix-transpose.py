import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
        
    rows = len(A)
    cols = len(A[0])

    rows, cols = cols, rows

    AT = np.ndarray((rows, cols))

    for i in range(cols):
        for j in range(rows):
            AT[j, i] = A[i][j]

    return AT
    
    pass
