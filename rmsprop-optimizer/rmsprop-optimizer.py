import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    wnp = np.asarray(w)
    gnp = np.asarray(g)
    snp = np.asarray(s)

    st = beta * snp + (1-beta) * np.power(gnp, 2)

    wnp = wnp- ((lr / np.sqrt(st + eps)) * gnp)

    return wnp, st
    pass