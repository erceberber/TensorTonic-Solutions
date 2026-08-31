import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    # Write code here
    X = np.asarray(X)
    X_imputed = X.copy()
    if strategy == "mean":
        mean = np.nanmean(X, axis=0)
        mean = np.nan_to_num(mean, nan=0.0)
        X_imputed = np.where(np.isnan(X_imputed), mean, X_imputed)

    if strategy == "median":
        median = np.nanmedian(X, axis=0)
        median = np.nan_to_num(median, nan=0.0)
        X_imputed = np.where(np.isnan(X_imputed), median, X_imputed)
   
    
    return X_imputed




    pass
