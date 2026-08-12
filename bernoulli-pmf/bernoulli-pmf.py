import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    xnp = np.asarray(x)
    
    pmf = np.where(xnp == 1, p, 1-p)

    return (pmf, p, p*(1-p)) 
    
    
    
    pass