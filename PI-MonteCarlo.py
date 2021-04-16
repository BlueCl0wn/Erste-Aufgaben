# Importieren von Bibliotheken#
import math
import numpy as np

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
def standardabweichung(n, my_arr):
     mean = np.mean(my_arr)
     x = 0
     for i in range(my_arr.size()):
         x += (my_arr[i] - mean)**2
     return math.sqrt(x/(n-1))

# Fehler des Mittelwert
def fehlerMittelwert(n, my_arr):
    return standardabweichung(n, my_arr)/math.sqrt(n)

# Berechnet Betrag der Differenz zweier Zahlen.
def differenz(a, b):
    return math.abs(a - b)

# Berechnet verschieden statistische Werte eines Zahlenarrays und gibt diese als Liste zurück.
def data(n, my_arr):
    min = my_arr.min()
    max= my_arr.max()
    mean= np.mean(my_arr)
    standardabweichung = standardabweichung(n, my_arr)
    fehlMittel = fehlerMittelwert(n, my_arr)

    # my_arr = np.append(my_arr, my_arr.min())
    # my_arr = np.append(my_arr, my_arr.max())
    # my_arr = np.append(my_arr, np.mean(my_arr))
    return [min, max, mean, standardabweichung, fehlMittel]

# Zusammenfassung der Methoden zur Berechnung von Pi.
def pi(n):
    points = random(n, 2)
    x = count(points)
    pi = calc(x)
    return pi

# Gibt Array aus mit r Wiederholungen der Berechnung von Pi, aber dauerhaft mit der gleichen Anzahl an Punkten.
def repeat(n, r):
    arr = np.zeros(r)
    for i in range(r):
        arr[i] = pi(n)
    #arr = np.append(arr, data(arr))
    return arr

# Erzeugt einen Array, in dem für verschiedenen Wiederholungen mit verschiedenen Anzahl an Punkten gespeicher werden.
def table(nMaxPos, r):
    arr = np.empty((nMaxPos, r+3))
    for i in range(nMaxPos):
        arr[i] = repeat(10**nMaxPos, r)

    return arr

def test(n, r):
    results = repeat(n, r)
    print(results)
    print()
    data = np.empty((r, 5))
    for i in range(r):
        np.append(data[i], data(n, results))
        # data[i] = np.array(1).append(data(n, results))
    print(data)
# def write

# table = table(4, 50)
# print(table)
# print(table(5, 50))
test(100,100)
