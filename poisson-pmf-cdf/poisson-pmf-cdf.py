import numpy as np
from math import factorial

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    def compute_pmf(lam, k):
        logp = -1*lam + k*np.log(lam) - np.sum(np.log(np.arange(1, k+1)))
        p = np.exp(logp)
        return p

    cdf = 0
    for i in range(k+1):
        cdf += compute_pmf(lam, i)



    return compute_pmf(lam, k), cdf
    pass