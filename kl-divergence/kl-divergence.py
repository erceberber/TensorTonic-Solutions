import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """Return KL divergence from p to q."""
    # Write code here
    P = np.asarray(p)
    Q = np.asarray(q)

    pos = np.where(P > 0)
    P = P[pos]

    qhat = np.clip(Q[pos], eps, None)

    return float(np.sum(P * np.log(P / qhat)))
    
    pass

print(kl_divergence(p=[0.4,0.6], q=[0.5, 0.5]))