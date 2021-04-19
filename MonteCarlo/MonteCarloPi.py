# Importieren von Bibliotheken#
import math
import numpy as np
import matplotlib.pyplot as plt

# Funktion distance berechnet den Betrag des Distanzvektors von Punkt A zu Punkt B.
def distance(punktA, punktB):
    # Gibt die Wurzel aus den addierten Differenzen der Dimensionswerte aus.
  return math.sqrt((punktB[0]-punktA[0])**2 + (punktB[1]-punktA[1])**2)

# Funktion zum erzeugen eines zufällig gefüllten Arrays mit den Dimensionen (x, y)
def random(x, y):
    return np.random.random((x, y))

# Methode, die zählt wie viele Punkte im Kreis sind und wie viele außerhalb.
def count(my_arr):
    In = 0
    Out = 0
    for i in range(my_arr.shape[0]):
        if distance(my_arr[i], (0, 0)) <= 1:
            In += 1
        else:
            Out += 1
    return (In, Out)

# Methode zum Berechnen von Pi.
def calc(numbers):
    fourth = numbers[0] / (numbers[0]+numbers[1])
    return (4 * fourth)

# Berechnet Standardabweichung.
def standardabweichung(varianz):
    return np.std(varianz)


# OLD - Berechnet Standardabweichung.
# def standardabweichung(varianz):
#     return math.sqrt(varianz)

# Berechnet Varianz.
def varianz(my_arr):
    return np.var(my_arr)

# OLD - Berechnet Varianz.
# def varianz(n, my_arr):
#      mean = np.mean(my_arr)
#      x = 0.0
#      print(my_arr)
#      for i in range(my_arr.size):
#          z = (my_arr[i] - mean)**2
#          x += z
#      return x/n

# Berechnet Betrag der Differenz zweier Zahlen.
def differenz(a, b):
    return math.abs(a - b)

# Berechnet verschieden statistische Werte eines Zahlenarrays und gibt diese als Liste zurück.
def data(n, my_arr):
    length = my_arr.size
    max = my_arr.max()
    min = my_arr.min()
    mean = np.mean(my_arr)
    var = varianz(my_arr)
    standAbweichung = standardabweichung(my_arr)
    diff = mean - math.pi
    return [length, min, max, mean, standAbweichung, var, diff]

# Zusammenfassung der Methoden zur Berechnung von Pi.
def pi(n):
    points = random(n, 2)
    x = count(points)
    pi = calc(x)
    return pi

# Plottet die Punkte auf einer Grafik.
def piPlot(n):
    points = random(n, 2)
    x = count(points)
    pi = calc(x)
    x, y = points.T

    # Zeichnet den Viertelkreis im Quadrat.
    circle=plt.Circle((0,0),1, color="r", fill=False)
    fig, ax = plt.subplots()
    ax.add_patch(circle)

    # Setzt die Größe des Quadrats auf 1x1.
    ax.set_xlim((0 , 1))
    ax.set_ylim((0, 1))

    # Zeichnet die Punkte in dem Quadrat.
    ax.scatter(x, y, s=2)

    # Zeigt die Zeichnung an.
    fig.savefig('plotcircles.png')
    plt.show()

# Gibt Array aus mit r Wiederholungen der Berechnung von Pi, aber dauerhaft mit der gleichen Anzahl an Punkten.
def repeat(n, r):
    arr = np.zeros(r)
    for i in range(r):
        arr[i] = pi(n)
    #arr = np.append(arr, data(arr))
    return arr


# Erzeugt einen Array, in dem für verschiedenen Wiederholungen mit verschiedenen Anzahl an Punkten gespeicher werden.
def table(nMaxPos, r):
    arr = np.empty((nMaxPos, r))
    for i in range(nMaxPos):
        arr[i] = repeat(10**nMaxPos, r)
    return arr

# Gibt einen Array mit verschiedenen Informationen über einen Array mit n Punkten und r Wiederholungen zurück.
def test(n, r):
    results = repeat(n, r)
    print(results)
    print()
    information = np.empty((r, 5))
    information = data(n, results)
    return information

# Schreibt statistische Informationen in einer Datei mit dem Format csv.
def infoTable(name, my_arr):
    f = open(name, "w")
    text = "n, r, min, max, avg, Standardabweichung, Varianz, Differenz\n"
    for i in range(np.ma.size(my_arr, 0)):
        text += str(10**(i+1))
        text += ","
        x = data(10**i, my_arr[i])
        for j in range(7):
            if j == 0:
                text += str(x[j])
            else:
                text += ","
                text += str(x[j])
        text += "\n"
    print(text)
    f.write(text)
    f.close()

def Datei(nMaxPos, r):
    tabelle = table(nMaxPos, r)
    name = "MonteCarlo\Daten\Daten" + str(r) + ".csv"
    infoTable(name, tabelle)

Datei(4, 1000)
# piPlot(5000)
