import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """
    # Write code here
    wnp = np.asarray(w)
    mnp = np.asarray(m)
    vnp = np.asarray(v)
    gradnp = np.asarray(grad)

    mt = beta1 * mnp + (1-beta1) * gradnp
    vt = beta2 * vnp + (1-beta2) * gradnp**2
    wt = wnp - (lr * weight_decay * wnp) - lr * mt / (np.sqrt(vt) + eps)

    return wt, mt, vt
    pass