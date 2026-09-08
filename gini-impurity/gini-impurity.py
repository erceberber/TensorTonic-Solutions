import numpy as np

def gini_impurity(y_left: list, y_right: list) -> float:
    """
    Returns the impurity as a float.
    """
    # Write code here
    left = np.asarray(y_left)
    right = np.asarray(y_right)
    

    #print(left, right)

    left_uniq, left_counts = np.unique(left, return_counts=True)
    right_uniq, right_counts = np.unique(right, return_counts=True)

    if len(left_counts) == 1:
        gsl = 0.0

    if len(right_counts) == 1:
        gsr = 0.0

    #print(left_uniq, left_counts)
    #print(right_uniq, right_counts)

    left_n = len(left)
    right_n = len(right)
    n = left_n + right_n

    if n == 0:
        return 0.0

    #print(left_n, right_n)

    p_left = left_counts / left_n
    p_right = right_counts / right_n

    #print(p_left, p_right)

    gsl = 1 - np.sum(p_left ** 2)
    gsr = 1- np.sum(p_right ** 2)

    return ((left_n / n) * gsl) + ((right_n / n) * gsr)
    
    pass

print(gini_impurity(y_left = [0, 0, 0], y_right = [1, 1, 1]))