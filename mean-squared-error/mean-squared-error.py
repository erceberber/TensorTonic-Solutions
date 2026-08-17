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

    n = yp_np.shape[0]

    mse = 0
    for i in range(n):
        mse += np.power(yp_np[i]-yt_np[i], 2)

    return mse / n
    
    pass
