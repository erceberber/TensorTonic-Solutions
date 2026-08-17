import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    yp_np = np.asarray(y_pred)
    yt_np = np.asarray(y_true)

    if yp_np.shape != yt_np.shape:
        return None

    return np.mean(np.power(yp_np - yt_np, 2))
    
    pass
