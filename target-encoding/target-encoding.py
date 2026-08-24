import numpy as np

def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    sums = {}
    counts = {}

    for cat, tar in zip(categories, targets):
        sums[cat] = sums.get(cat, 0.0) + tar
        counts[cat] = counts.get(cat, 0) + 1

    means = {cat: sums[cat] / counts[cat] for cat in categories}

    return [means[cat] for cat in categories]
    
    pass


print(target_encoding(["cat", "dog", "cat", "dog"], targets=[1, 2, 3, 4]))