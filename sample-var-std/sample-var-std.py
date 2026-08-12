def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here

    xnp = np.asarray(x)
    std = np.std(xnp, ddof=1)
    var = np.power(std, 2)

    return (var, std)
    pass