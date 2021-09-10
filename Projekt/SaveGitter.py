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

def plotPoints(x, ymain, filename="filename", ysub=None, title="title", suptitle="suptitle", labels=("x-Axis", "y-Axis"), show=False) -> None:
    """
    """

    # Erzeugung des Graphen
    fig, ax = plt.subplots()

    # xAxis = np.arange(0, r, 1)
    if ysub == None:
        # x = np.array([[1, 2, 3], [10, 20, 30], [100, 200, 300]])
        for i in ysub:
            ax.scatter(x, i, color='b', linewidths=0.5, marker='x')

    ax.plot(x, ymain)

    # ax.plot(yAxisMean, linewidth='2.5')

    # Definiert Titel und Überschrift dieser Speicherung
    # if title != "title":
    #     title = "r = %(r)s ; n = %(n)s ; beta = %(beta)s ; reps=%(reps)s" % locals()

    # Entfernt alle Punkte aus dem Titel und ersetzt sie mit Kommata, damit keine Fehler bei der Speicherung entstehen.
    title = title.replace(".", ",")

    # Überschrift und Unterüberschrift
    fig.suptitle(suptitle)
    ax.set_title(title)

    # Achsenbeschriftung
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])

    # Formatiert plot
    # ax.set_xlim(0, r)

    if show:
        # Zeigt plot in neuem Fenster an.
        plt.show()
    else:
        # Speichert plot als .png
        fig.savefig(filename + title)

plotPoints(np.flip(np.arange()), [0.1, 0.2, 0.3], ysub=None, title="title", suptitle="suptitle", labels=("x-Axis", "y-Axis"), show=True)

def saveList(string, my_list) -> None:
    """Speichert Liste als Textdatei."""
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
