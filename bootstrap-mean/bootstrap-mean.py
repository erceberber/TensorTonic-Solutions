import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here

    xnp = np.asarray(x)

    if rng is None:
        rng = np.random.default_rng()


    boot_means = np.zeros((n_bootstrap,))
    for i in range(n_bootstrap):
        resample = rng.integers(0, xnp.shape[0], size=xnp.shape[0])
        resample = xnp[resample]
        boot_means[i] = np.mean(resample)

    alpha = (1 - ci) / 2
    lower = np.quantile(boot_means, alpha)
    upper = np.quantile(boot_means, 1-alpha)



    return boot_means, lower, upper
    pass
