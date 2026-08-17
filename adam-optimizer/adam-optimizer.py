import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here

    mt = np.asarray(m)
    gt = np.asarray(grad)
    vt = np.asarray(v)
    theta = np.asarray(param)

    mt = beta1 * mt + (1-beta1) * gt
    vt = beta2 * vt + (1-beta2) * gt**2

    mt_hat = mt / (1-(beta1**t))
    vt_hat = vt / (1-(beta2**t))

    theta = theta - ((lr * mt_hat) / ((np.sqrt(vt_hat) + eps)))
    

    return theta, mt, vt
    
    pass