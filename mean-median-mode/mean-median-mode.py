import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    xnp = np.asarray(x)

    mean = np.mean(xnp)
    median = np.median(xnp)
    mode = Counter(xnp).most_common(1)[0][0]

    return (mean, median, mode)
    
    # Write code here
    pass