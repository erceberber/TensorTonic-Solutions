import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    true = np.asarray(y_true)
    pred = np.asarray(y_pred)

    if true.shape == 0 or true.shape[0] != pred.shape[0]:
        return None

    matched_probs = pred[np.arange(true.shape[0]), y_true]
    return -1 * np.mean(np.log(matched_probs))
    
    pass

