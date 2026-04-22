def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    ans = np.array(values)

    ans = np.log(1 + ans)

    return ans
    