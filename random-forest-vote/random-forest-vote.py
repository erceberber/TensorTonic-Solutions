

def random_forest_vote(predictions: list) -> list:
    """
    Returns the majority-vote label for every sample.
    """
    # Write code here
    
    T = len(predictions)
    N = len(predictions[0])
    decisions = []
    for i in range(N):
        votes = {}
        for t in range(T):
            v = predictions[t][i]
            votes[v] = votes.get(v, 0) + 1

        max_val = max(votes.values())
        decisions.append(min(k for k, v in votes.items() if v == max_val))

    return decisions
        
        
    pass