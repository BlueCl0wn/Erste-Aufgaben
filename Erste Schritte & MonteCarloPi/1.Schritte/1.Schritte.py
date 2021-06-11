# Importieren von Bibliotheken
import math
import numpy as np

# Funktion distance berechnet den Betrag des Distanzvektors von Punkt A zu Punkt B.
def distance(punktA, punktB):
    # Gibt die Wurzel aus den addierten Differenzen der Dimensionswerte aus.
  return math.sqrt((punktB[0]-punktA[0])**2 + (punktB[1]-punktA[1])**2)


# Festlegung der Anzahl der später vorhandene Punkte.
length = 10

# Kreieren eines zweidimensionalen Arrays mit (length, 2).
my_arr = np.random.random((length, 2))

# Kreieren eines neuen Arrays, welches die Distanzen der Punkte zum Punkt (0.5, 0.5) speichert.
distances = np.zeros(length)

# Loopt über den Array my_arr, berechnet die Distanz des Punktes zum Punkt (0.5, 0.5) und speichert diese Information im Array distances.
for i in range(length):
    distances[i] = distance(my_arr[i], (0.5, 0.5))

# Fügt die beiden Arrays so zusammen, dass hinter den beiden Koordinaten der Punkte nun der Abstand zum Punkt (0.5, 0.5) steht.
data = np.column_stack((my_arr, distances))

# Speichert den Array data in der Datei "points.dat".
np.savetxt("points.dat", data, header="X, Y, Distanz")

# Lädt den Array in der Datei "points.dat".
data = np.loadtxt("points.dat")

# Erzeugt eine Liste, die die Werte der erneuten Berechnung der Abstände speichern wird.
newDis = []

# Erneutes berechnen der Abstände und anfügen and Lsite newDis.
for i in range(length):
    newDis.append(distance(my_arr[i], (0.5, 0.5)))
