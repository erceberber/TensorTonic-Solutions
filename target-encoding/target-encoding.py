import numpy as np

def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    hashmap = {}
    for i, category in enumerate(categories):
        if category not in hashmap:
            hashmap[category] = [targets[i], 1]
            

        else:
            hashmap[category][0] += targets[i]
            hashmap[category][1] += 1

    result = []

    for category in categories:
        result.append(hashmap[category][0] / hashmap[category][1])


    return result
    
    pass


print(target_encoding(["cat", "dog", "cat", "dog"], targets=[1, 2, 3, 4]))