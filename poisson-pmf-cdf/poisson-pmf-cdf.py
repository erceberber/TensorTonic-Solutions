import numpy as np
from math import factorial

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    def compute_pmf(lam, k):
        return (np.exp(-1*lam) * np.power(lam, k)) / factorial(k)

    cdf = 0
    for i in range(k+1):
        cdf += compute_pmf(lam, i)



    return compute_pmf(lam, k), cdf
    pass