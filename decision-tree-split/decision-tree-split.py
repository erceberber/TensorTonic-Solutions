import numpy as np

def decision_tree_split(X: list, y: list) -> list:
    """
    Returns the best feature index and threshold.
    """
    # Write code here

    def gini(labels):
        n = len(labels)
        if n == 0:
            return 0.0
        
        classes, counts = np.unique(labels, return_counts=True)
        p = counts / n
        return 1 - np.sum(p ** 2)
    
    X_ = np.asarray(X, dtype=float)
    y_ = np.asarray(y, dtype=int)

    m, n = X_.shape
    parent_gini = gini(labels=y_)

    best_gain = -1 
    best_feature = None
    best_threshold = None

    for i in range(n):
        feature_values = X_[:, i]
        uniq_values = np.sort(np.unique(feature_values))

        thresholds = (uniq_values[1:] + uniq_values[:-1]) / 2.0

        for th in thresholds:
            left = feature_values <= th
            right = ~left

            y_left = y_[left]
            y_right = y_[right]

            if len(y_left) == 0 or len(y_right) == 0:
                continue
            
            gini_left = gini(y_left) * len(y_left) / m
            gini_right = gini(y_right) * len(y_right) / m

            gain = parent_gini - gini_left - gini_right

            if gain > best_gain:
                best_gain = gain
                best_threshold = th
                best_feature = i

    return [best_feature, best_threshold]

    pass