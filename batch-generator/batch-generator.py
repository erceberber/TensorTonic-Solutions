import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    rng = np.random.default_rng(seed=seed)
    idx = rng.permutation(len(X))

    X = X[idx]
    y = y[idx]

    for i in range(0, len(X), batch_size):
        X_batch = X[i: i + batch_size]
        y_batch = y[i: i + batch_size]

        if drop_last and len(X_batch) < batch_size:
            break

        yield(X_batch, y_batch)
    pass

