import numpy as np

def clip_gradients(g: list, max_norm: float) -> np.ndarray:
    """Return g clipped by its global L2 norm."""
    # Write code here

    g = np.asarray(g)
    g_norm = np.linalg.norm(g)

    if g_norm > max_norm:
        return g * max_norm / g_norm

    return g
    



    pass

