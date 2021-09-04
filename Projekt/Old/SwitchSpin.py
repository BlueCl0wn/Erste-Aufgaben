# Bibliotheken
import math
import numpy as np

# Funktionen
import DetermineCharge as DC
import MakeGitter as MG
import GetPosition as GP

"""Es gibt mehrere Versionen dieser Datei. V1, V2 und V3. Die Neueste ist jeweils schneller als die Vorherige."""
import DeltaE.V3 as DeltaE

import matplotlib.pyplot as plt

# beta = J/1.380649e-23*T


def switchSpin(conf, n, T, r, distanz=0, akzeptanzrate=False, GraphE=False):
    """
    Wählt einen zufälligen Spin aus, wechselt diesen und überprüft, ob dieser Wechsel beibehalten oder rückgängig gemacht wird.
    Beinhaltet Code zum berechnen der Akzeptanzrate.

    """

    # Variabeln für Akzeptanzrate. ALle Codeblöcke, die mit der Akzeptanzrate zu tun haben, werden nur ausgeführt, wenn der Paramter 'akzeptanzrate' 'True' ist. Dieser ist standardmäßig 'False'.
    if akzeptanzrate:
        Versuche = 0
        akzeptiert = 0
        akzeptiertE = 0
        akzeptiertW = 0
        abgelehnt = 0

    yAxis = np.zeros(r)

    beta = 1/T

    posAlt = (None, None)
    pos = None

    altE = DC.getAllCharge(conf, n)

    for x in range(r):

        # Eine zufällige mögliche Ladung wird ausgewählt.
        # charge = MG.charge()

        # Position des Spinwechsel wird ausgewählt.
        pos = GP.getPosition(posAlt, distanz, n)

        # Zähler für Akzeptanzrate wird erhöht.
        if akzeptanzrate:
            Versuche += 1

        # DeltaE wird als Zwischenvariable gespeichert.
        dE = DeltaE.deltaE(conf, altE, pos, -conf[pos[0]][pos[1]], n)
        # Vorher:
        # dE = DeltaE.deltaE(conf, altE, pos, -conf[pos[0]][pos[1]], n)

        # DeltaE ist kleiner als 0. Es wird also Energei freigesetzt und dammit ist die Wahrscheinlichkeit fürs Umdrehen 100%.
        if dE <= 0:
            conf[pos[0]][pos[1]] *= -1
            altE = altE + dE
            # print(conf[pos[0]][pos[1]])
            # print(-conf[pos[0]][pos[1]])
            # print("------")

            # Vorher:
            # conf[pos[0]][pos[1]] = charge
            # print(conf[pos[0]][pos[1]])
            # print(charge)
            # print("------")

            if akzeptanzrate:
                akzeptiert += 1
                akzeptiertE += 1

        # DeltaE ist größer als 0. Es wird Energie benötigt. Mit gewisser Wahrscheinlichkeit findest Spinwechsel trotzdem statt.
        elif np.random.rand() < math.exp(-beta*dE):
            conf[pos[0]][pos[1]] *= -1
            altE = altE + dE

            # für Akzeptanzrate
            if akzeptanzrate:
                akzeptiert += 1
                akzeptiertW += 1

        else:
            # für Akzeptanzrate
            if akzeptanzrate:
                abgelehnt += 1

            pass

        yAxis[x] = altE

    # For-schleife zuende

    # Ausgaben für Akzeptanzrate.
    if akzeptanzrate:
        print("Versuche = " + str(Versuche))
        print("akzeptiert = " + str(akzeptiert))
        print("\tdE < 0 = " + str(akzeptiertE))
        print("\tw < e = " + str(akzeptiertW))
        print("unaccepted = "  + str(abgelehnt))
        print("Akzeptanzrate (akzeptiert/Versuche): " + str(akzeptiert/Versuche))

    if GraphE:
        xAxis = np.arange(0, r, 1)
        MG.saveGraphIMG(xAxis, yAxis, r, n, T,  "EGraph")

        # MG.saveGraphIMG(xAxis, np.fft.fft(yAxis), r, n, "EnergieGraphSMooth")

    return conf
