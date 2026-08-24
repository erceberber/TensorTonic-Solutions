import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    N = X.shape[0]
    w = np.zeros(X.shape[1])
    b = 0.0
    
    for _ in range(steps):
        z = X @ w + b
        predicted = _sigmoid(z)
        err = predicted - y
        gradients = (X.T @ err) / N 
        _b = np.mean(err)
        w = w - lr * gradients
        b = b - lr * _b
        

    return w, b
    
    pass

print(train_logistic_regression(X=[[0],[1],[2],[3]], y=[0,0,1,1]))