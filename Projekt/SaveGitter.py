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

def saveGraphIMG(yAxis, n, beta, filename, ptp) -> None:
    """
    Speichert Array als Bilddatei.
    Funktioniert nur für Darstellung von Graphen.
    """

    # Definiert Titel und Überschrift dieser Speicherung
    title = "r = %(r)s ; n = %(n)s ; beta = %(beta)s ; ptp=%(ptp)s" % locals()
    title = title.replace(".", ",")

    r = yAxis.shape[0]

    # Erzeugung des Graphen
    fig, ax = plt.subplots()
    # xAxis = np.arange(0, r, 1)
    ax.plot(yAxis)

    # Überschrift und Unterüberschrift
    fig.suptitle("Energie über r")
    ax.set_title(title)

    # Achsenbeschriftung
    ax.set_ylabel("Energie")
    ax.set_xlabel("r")

    # Formatiert plot
    ax.set_xlim(0, r)

    # Speicehrt plot als .png
    fig.savefig(filename + "r = %(r)s ; n = %(n)s ; beta = %(beta)s ; ptp=%(ptp)s" % locals())

def saveMeanGraphIMG(yAxese, yAxisMean, r, n, beta, reps, filename) -> None:
    """
    Plottet den Durschnitts-Array und dazu die einzelnen Arrays dünn in grau und speichert als Bilddatei.
    Funktioniert nur für Darstellung von Graphen.
    """

    # Erzeugung des Graphen
    fig, ax = plt.subplots()
    # xAxis = np.arange(0, r, 1)
    for i in yAxese:
        ax.plot(i,  color='grey', linewidth='0.1')
    ax.plot(yAxisMean, linewidth='2.5')

    # Definiert Titel und Überschrift dieser Speicherung
    title = "r = %(r)s ; n = %(n)s ; beta = %(beta)s ; reps=%(reps)s" % locals()
    title = title.replace(".", ",")

    # Überschrift und Unterüberschrift
    fig.suptitle("gemittelte Energie über r")
    ax.set_title(title)

    # Achsenbeschriftung
    ax.set_ylabel("Energie")
    ax.set_xlabel("r")

    # Formatiert plot
    ax.set_xlim(0, r)

    # Speicehrt plot als .png
    # fig.savefig(filename + "_r=%(r)s_n=%(n)s_T=%(beta)s_reps=%(reps)s".replace(".", ",") % locals())
    fig.savefig(filename + title)

def saveList(string, my_list) -> None:
    """Sepeichert Liste als Textdatei."""
    with open(string, 'w') as file:
        file.write(my_list)

def saveArray(string, my_arr, delimiter=' ') -> None:
    """Speichert Array als Textdatei."""
    np.savetxt(string, my_arr)

def loadArray(string, delimiter=None) -> np.ndarray:
    """Lädt Array aus einer Textdatei."""
    try:
        return np.loadtxt(string, delimiter)
    except:
        print("Eine Datei mit diesem Namen existiert nicht.")
