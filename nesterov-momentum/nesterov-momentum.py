import numpy as np

def nesterov_momentum_step(w, v, grad, lr=0.01, momentum=0.9):
    """
    Perform one Nesterov Momentum update step.
    """
    # Write code here

    wnp = np.asarray(w, dtype=float)
    vnp = np.asarray(v, dtype=float)
    grad = np.asarray(grad, dtype=float)

    vnp *= momentum
    vnp += lr * grad

    return (wnp - vnp), vnp

    pass