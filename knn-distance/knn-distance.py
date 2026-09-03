import numpy as np

def knn_distance(X_train: list, X_test: list, k: int = 0) -> np.ndarray:
    """
    Returns a NumPy array with shape (n_test, k).
    """
    # Write code here
    train = np.asarray(X_train)
    test = np.asarray(X_test)

    if train.ndim == 1:
        train = train.reshape(-1, 1)

    if test.ndim == 1:
        test = test.reshape(-1, 1)

    distances = np.sum((train[None, :, :] - test[:, None, :]) ** 2, axis=2)
    print(distances)

    if k <= train.shape[0]:
        closest = np.argsort(distances, axis=1, kind="stable")[:, :k]

    else:
        closest = np.full(shape=(test.shape[0], k), fill_value=-1) 
        closest[:, :train.shape[0]] = np.argsort(distances, axis=1, kind="stable")[:, :train.shape[0]]


    return closest.astype(int)

    pass

print(knn_distance(X_train=[1, 3, 5], X_test=[2], k=2))