import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    
    uniq = np.unique(y, return_counts=True)

    unique_class_count = len(uniq[0])
    if unique_class_count  <= 1:
        return 0.0
        
    n = len(y)
    counts = uniq[1]
    p = counts / n

    return -np.sum(p * np.log2(p))
    
    pass
