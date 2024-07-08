import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as c

def charge() -> int:
    """Returns randomly -1 or 1."""
    return np.random.choice([-1, 1])



def getGitterV2(n) -> np.ndarray:
    """Returns an array with the dimension n*n randomly filled with -1 or 1.
    second version. much faster"""
    return np.random.choice([-1, 1], (n, n))
