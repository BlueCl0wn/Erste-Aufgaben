import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as c

def plot(my_arr, n) -> None:
    """Plots an array as bunch of small squares."""
    # Does fancy stuff. (creating subplot)
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111, aspect='equal')

    # Displays the array as squares.
    mesh = plt.pcolormesh(my_arr)

    # Plots everything
    plt.show()

def saveGridIMG(my_arr, n, string) -> None:
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

def saveGraphIMG(yAxis, r, n, T, filename, ptp) -> None:
    """
    Speichert Array als Bilddatei.
    Funktioniert nur für Darstellung von Graphen.
    """

    # Erzeugung des Graphen
    fig, ax = plt.subplots()
    # xAxis = np.arange(0, r, 1)
    ax.plot(yAxis)

    # Überschrift und Unterüberschrift
    fig.suptitle("Energie über r")
    ax.set_title("r = %(r)s ; n = %(n)s ; T = %(T)s ; ptp=%(ptp)s" % locals())

    # Achsenbeschriftung
    ax.set_ylabel("Energie")
    ax.set_xlabel("r")

    # Formatiert plot
    ax.set_xlim(0, r)

    # Speicehrt plot als .png
    fig.savefig(filename + "_r=%(r)s_n=%(n)s_T=%(T)s_ptp=%(ptp)s" % locals())

def saveMeanGraphIMG(yAxese, yAxisMean, r, n, T, reps, filename) -> None:
    """
    Plottet den Durschnitts-Array und dazu die einzelnen Arrays dünn in grau und speichert als Bilddatei.
    Funktioniert nur für Darstellung von Graphen.
    """

    # Erzeugung des Graphen
    fig, ax = plt.subplots()
    # xAxis = np.arange(0, r, 1)
    for i in yAxese:
        ax.plot(i,  color='grey', linewidth='0.3')
    ax.plot(yAxisMean, linewidth='3')

    # Überschrift und Unterüberschrift
    fig.suptitle("gemittelte Energie über r")
    ax.set_title("r = %(r)s ; n = %(n)s ; T = %(T)s ; reps=%(reps)s" % locals())

    # Achsenbeschriftung
    ax.set_ylabel("Energie")
    ax.set_xlabel("r")

    # Formatiert plot
    ax.set_xlim(0, r)

    # Speicehrt plot als .png
    fig.savefig(filename + "_r=%(r)s_n=%(n)s_T=%(T)s_reps=%(reps)s" % locals())

def saveFile(my_arr, string) -> None:
    """Sepeichert Array als Textdatei."""
    with open(string, 'w') as file:
        file.write(np.array2string(my_arr, threshold=100))
