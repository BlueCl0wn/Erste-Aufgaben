# Bibliotheken
import math
import numpy as np

# Funktionen
import DetermineCharge as DC
import MakeGitter as MG
import getPosition as GP

"""Es gibt mehrere Versionen dieser Datei. V1, V2 und V3. Die Neueste ist jeweils schneller als die Vorherige."""
import DeltaE.V3 as DeltaE

import matplotlib.pyplot as plt

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


    posAlt = (None, None)
    pos = None

    altE = DC.getAllCharge(conf, n)

    for x in range(r):

        # Eine zufällige mögliche Ladung wird ausgewählt.
        charge = MG.charge()

        # Position des Spinwechsel wird ausgewählt.
        pos = GP.getPosition(posAlt, distanz, n)

        # Zähler für Akzeptanzrate wird erhöht.
        if akzeptanzrate:
            Versuche += 1

        # DeltaE wird als Zwischenvariable gespeichert.
        dE = DeltaE.deltaE(conf, altE, pos, charge, n)

        # DeltaE ist kleiner als 0. Es wird also Energei freigesetzt und dammit ist die Wahrscheinlichkeit fürs Umdrehen 100%.
        if dE <= 0:
            conf[pos[0]][pos[1]] = charge

            if akzeptanzrate:
                akzeptiert += 1
                akzeptiertE += 1

        # DeltaE ist größer als 0. Es wird Energie benötigt. Mit gewisser Wahrscheinlichkeit findest Spinwechsel trotzdem statt.
        elif np.random.rand() < math.exp(-dE): # !!!!!! e ist eingeführt. J und beta kürzen sich aber gegenseitig weg, dadurch immer noch kein T. Ohne J kein sinnvoller Effekt des elifs, da redundant.
            conf[pos[0]][pos[1]] = charge

            # für Akzeptanzrate
            if akzeptanzrate:
                akzeptiert += 1
                akzeptiertW += 1

        else:
            # für Akzeptanzrate
            if akzeptanzrate:
                abgelehnt += 1

            pass

        altE = altE + dE
        yAxis[x] = altE

    # Ausgaben für Akzeptanzrate.
    if akzeptanzrate:
        print("Versuche = " + str(Versuche))
        print("akzeptiert = " + str(akzeptiert))
        print("\tdE < 0 = " + str(akzeptiertE))
        print("\tw < e = " + str(akzeptiertW))
        print("unaccepted = "  + str(abgelehnt))
        print("Akzeptanzrate (akzeptiert/Versuche): " + str(akzeptiert/Versuche))

    if GraphE:
        xAxis = np.arange(0, r, 5)
        MG.saveGraphIMG(xAxis, yAxis, r, n, "EnergieGraph")

        # MG.saveGraphIMG(xAxis, np.fft.fft(yAxis), r, n, "EnergieGraphSMooth")

    return conf
