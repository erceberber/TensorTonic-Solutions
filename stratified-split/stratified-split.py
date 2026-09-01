import numpy as np

def stratified_split(X: list, y: list, test_size: float = 0.2, seed: int = 42) -> dict:
    """
    Returns a dictionary with X_train, X_test, y_train, and y_test.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    values, n_class = np.unique(y, return_counts=True)
    rng = np.random.default_rng(seed=seed)

    result = {}
    x_train, x_test = [], []
    y_train, y_test = [], []
    for c in values:
        class_indices = np.flatnonzero(y == c)
        class_indices = rng.permutation(class_indices)

        x_shuffled = X[class_indices]
        y_shuffled = y[class_indices]

        n_c = len(class_indices)
        n_c_test = round(n_c * test_size)

        test_idx = class_indices[:n_c_test]
        train_idx = class_indices[n_c_test:]
        test_idx.sort()
        train_idx.sort()

        x_test.append(X[test_idx])
        x_train.append(X[train_idx])
        y_test.append(y[test_idx])
        y_train.append(y[train_idx])


    x_train = np.concatenate(x_train)
    x_test = np.concatenate(x_test)
    y_train = np.concatenate(y_train)
    y_test = np.concatenate(y_test)
    
    result = {
        "X_train": x_train,
        "X_test": x_test,
        "y_train": y_train,
        "y_test": y_test
    }

    return result

    pass
