import numpy as np
import matplotlib.pyplot as plt

# Returns randomly -1 or 1.
def charge():
    return np.random.choice([-1, 1])

# Fills the array randomly with -1 and 1.
def setCharges(my_arr):
    for i in range(len(my_arr)):
        for j in range(len(my_arr[0])):
            my_arr[i][j] = charge()

# Returns an array with the dimension n*n randomly filled with -1 or 1.
def getGitter(n):
    x = np.zeros((n, n))
    setCharges(x)
    return x

# Plots an array as bunch of small squares.
def plot(my_arr, n):
    # Does fancy stuff. (creating subplot)
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111, aspect='equal')

    # Displays the array as squares.
    mesh = plt.pcolormesh(my_arr)

    # Plots everything
    plt.show()
