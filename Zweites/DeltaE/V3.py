import DetermineCharge as DC
import numpy as np
import MakeGitter as MG
import math

"""Definition der Boltzmann-Konstanten"""
kBoltzmann = 1.380649e-23

tries = 0
accepted = 0
unaccepted = 0


def beta(T):
    """Berechnet beta."""
    return 1/(kBoltzmann * T)

def deltaE(conf_alt, altE, pos, charge, n):
    """Berechnet den Energieunterschied des Systems nach dem Umdrehen eines Spins."""
    n -= 1

    neuE = altE

    neuE -= DC.getCharge(conf_alt, pos[0], pos[1],  n)

    neuE += charge
    neuE += conf_alt[pos[0] - 1][pos[1]] if pos[0] >= 0 else 0
    neuE += conf_alt[pos[0] + 1][pos[1]] if pos[0] <= (n-1) else 0
    neuE += conf_alt[pos[0]][pos[1] - 1] if pos[1] >= 0 else 0
    neuE += conf_alt[pos[0]][pos[1] + 1] if pos[1] <= (n-1) else 0


    return neuE - altE

def switchSpin(conf, n, T, r):
    """Wählt einen zufälligen Spin aus, wechselt diesen und überprüft, ob dieser Wechsel beibehalten oder rückgängig gemacht wird."""

    # Variabeln für Akzeptanzrate.
    global tries
    global accepted
    global unaccepted

    altE = DC.getAllCharge(conf, n)

    for x in range(r):

        charge = MG.charge()

        pos = np.random.randint(0, n, size=(2))
        #
        tries += 1

        dE = deltaE(conf, altE, pos, charge, n)
        # print("dE(T) = " + str(dE))

        #
        if dE <= 0:
            conf[pos[0]][pos[1]] = charge
            # print("flipped")
            accepted += 1
        elif np.random.rand() < math.exp(-dE): # e ist eingeführt. J und beta kürzen sich aber gegenseitig weg, dadurch immer noch kein T. Ohne J kein sinnvoller Effekt des elifs, da redundant.
            conf[pos[0]][pos[1]] = charge
            accepted += 1
            # print("beta(T) = " + str(beta(T)))
            # print("flipped")
        else:
            unaccepted += 1
            # print("beta(T) = " + str(beta(T)))
            # print("not flipped")
            pass

        # print("---------------------------")

        altE = altE + dE

    # Ausgaben für Akzeptanzrate.
    print("tries = " + str(tries))
    print("accepted = " + str(accepted))
    print("unaccepted = "  + str(unaccepted))

    return conf
