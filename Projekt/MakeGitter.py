import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as c

def charge():
    """Returns randomly -1 or 1."""
    return np.random.choice([-1, 1])

def setAllCharges(my_arr):
    """Fills the array randomly with -1 and 1."""
    for i in range(len(my_arr)):
        for j in range(len(my_arr[0])):
            my_arr[i][j] = charge()

def getGitterV1(n):
    """First version of getGitter"""
    x = np.zeros((n, n))
    setAllCharges(x)
    return x


def getGitterV2(n):
    """Returns an array with the dimension n*n randomly filled with -1 or 1.
    second version. much faster"""
    return np.random.choice([-1, 1], (n, n))

def plot(my_arr, n):
    """Plots an array as bunch of small squares."""
    # Does fancy stuff. (creating subplot)
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111, aspect='equal')

    # Displays the array as squares.
    mesh = plt.pcolormesh(my_arr)

    # Plots everything
    plt.show()

def saveGridIMG(my_arr, n, string):
    """
    Speichert Array als Bilddatei.
    Funktioniert nur für Gitterdarstellung.
    """

    # Does fancy stuff. (creating subplot)
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111, aspect='equal')
    ax.set_title(string)

    # Colormap for specific colors.
    cMap = c.ListedColormap(["Black", 'White'])

    # Displays the array as squares.
    mesh = plt.pcolormesh(my_arr, cmap=cMap)

    # Speicehrt plot als .png
    fig.savefig(string, dpi=200)

def saveGraphIMG(xAxis, yAxis, r, n, T, filename):
    """
    Speichert Array als Bilddatei.
    Funktioniert nur für Darstellung von Graphen.
    """

    # Erzeugung des Graphen
    fig, ax = plt.subplots()
    xAxis = np.arange(0, r, 1)
    ax.plot(xAxis, yAxis)

    # Überschrift und Unterüberschrift
    fig.suptitle("Energie über r")
    ax.set_title("r = " + str(r) + " ; n = " + str(n) + " ; T = " + str(T))

    # Achsenbeschriftung
    ax.set_ylabel("Energie")
    ax.set_xlabel("r")

    # Formatiert plot
    ax.set_xlim(0, r)

    # Speicehrt plot als .png
    fig.savefig(filename + "_r=" + str(r) + "_n=" + str(n) + "_T=" + str(T))

def saveFile(my_arr, string):
    """Sepeichert Array als Textdatei."""
    with open(string, 'w') as file:
        file.write(np.array2string(my_arr, threshold=100))

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth
