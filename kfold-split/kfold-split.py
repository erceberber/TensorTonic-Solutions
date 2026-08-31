import numpy as np

def kfold_split(N: int, k: int, shuffle: bool = True, seed: int = 0) -> list:
    """
    Returns a list of dictionaries with train_idx and val_idx.
    """
    # Write code here
    idx = np.arange(N)
    if shuffle:
        rng = np.random.default_rng(seed=seed)
        idx = rng.permutation(idx)

    idx = np.array_split(idx, k)
    result = []
    for i in range(k):
        val_idx = idx[i]
        train_idx = np.concatenate([idx[j] for j in range(k) if j != i])
        result.append({"train_idx": train_idx, "val_idx": val_idx})


    return result
        
    pass
