import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """Return population Z-scores along axis."""
    # Write code here
    X = np.asarray(X)
    m = np.mean(X, axis=axis, keepdims=True)
    std = np.std(X, axis=axis, keepdims=True)
    std = np.where(std < eps, 0, std)

    z = np.where(std == 0, 0, (X - m) / std)

    return z
    
    pass
