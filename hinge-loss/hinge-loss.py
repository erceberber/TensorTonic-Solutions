import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here

    yt = np.asarray(y_true)
    ys = np.asarray(y_score)

    if yt.shape != ys.shape:
        return None

    if not np.all(np.abs(yt) == 1) or not np.all(np.abs(yt) == 1):
        return None

    result = yt * ys
    result = margin - result 

    if reduction == "mean":
        return np.mean(np.where(result > 0, result, 0))

    if reduction == "sum":
        return np.sum(np.where(result > 0, result, 0))
    pass