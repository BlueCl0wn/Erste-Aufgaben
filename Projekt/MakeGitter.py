import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as c

def charge() -> int:
    """Returns randomly -1 or 1."""
    return np.random.choice([-1, 1])


# def setAllCharges(my_arr):
#     """Fills the array randomly with -1 and 1."""
#     for i in range(len(my_arr)):
#         for j in range(len(my_arr[0])):
#             my_arr[i][j] = charge()
#
# def getGitterV1(n):
#     """First version of getGitter"""
#     x = np.zeros((n, n))
#     setAllCharges(x)
#     return x


def getGitterV2(n) -> np.ndarray:
    """Returns an array with the dimension n*n randomly filled with -1 or 1.
    second version. much faster"""
    return np.random.choice([-1, 1], (n, n))
