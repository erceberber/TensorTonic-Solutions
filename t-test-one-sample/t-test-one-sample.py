import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x_ = np.asarray(x)
    mean = np.mean(x_)
    s = np.std(x_, ddof=1)
    n = x_.shape[0]

    t = mean - mu0
    t /= s / np.sqrt(n)

    return t



    pass