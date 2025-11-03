import numpy as np

def european_call(S_T, K):
    return np.maximum(S_T - K, 0)
