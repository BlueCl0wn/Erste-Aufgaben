import numpy as np

def position(posAlt, distanz, n):
    """
    Sucht anhand von der vorherigen Position des Spinwechsels und der angegeben Variable 'distanz' eine neue Position heraus.
    Diese neue Position ist abhängig von einigen Faktoren.
    """

    # Wenn distanz = 0 ist, wird bei jeder Iteration eine komplett zufälliger Spin aus dem gesamten System ausgewählt.
    if distanz == 0:
        return np.random.randint(0, n, size=(2))
    # Wenn die Distanz größer als 0 ist, liegt der nächste ausgewählte Spin maximal so weit von Vorherigen entfernt, wie groß 'distanz' ist.
    elif distanz > 0 & distanz <= n:
        if posAlt == (None, None):
            return np.random.randint(0, n, size=(2))
        else:
            return (posAlt[0] + np.random.randint(-distanz, distanz, size=(1))[0], posAlt[1] + np.random.randint(-distanz, distanz, size=(1))[0])
    # 'distanz' darf dabei selbstverständnlich nicht kleiner als 0 und nicht größer als der Array (n) sein.
    else:
        print("'Distanz' muss im Berreich [0; n] liegen. 0 für keine Beeinflussung.")
