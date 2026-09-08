import numpy as np

def information_gain(y: list, split_mask: list) -> float:
    """
    Returns the information gain as a float.
    """
    # Write code here
    ynp = np.asarray(y)
    sm = np.asarray(split_mask)

    true_indices = np.flatnonzero(sm)
    false_indices = np.flatnonzero(~sm)

    y_left = ynp[true_indices]
    y_right = ynp[false_indices]

    n_left = len(y_left)
    n_right = len(y_right)
    n = n_left + n_right
    if n == 0:
        return 0.0

    y_uniq, y_counts = np.unique(ynp, return_counts=True)
    left_uniq, left_counts = np.unique(y_left, return_counts=True)
    right_uniq, right_counts = np.unique(y_right, return_counts=True)

    p_y = y_counts / n
    p_left = left_counts / n_left
    p_right = right_counts / n_right

    h_y = -np.sum(np.where(p_y > 0, p_y * np.log2(p_y), 0))
    h_left = -np.sum(np.where(p_left > 0, p_left * np.log2(p_left), 0))
    h_right = -np.sum(np.where(p_right > 0, p_right * np.log2(p_right), 0))

    return h_y - ((n_left / n) * h_left) - ((n_right / n) * h_right)


    pass