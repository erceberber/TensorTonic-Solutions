import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """Return exact GELU values with the same shape as x."""
    # Write code here
    
    xnp = np.asarray(x, dtype=float)

    return (xnp / 2) * (1 + np.vectorize(math.erf)(xnp / np.sqrt(2)))

    pass

