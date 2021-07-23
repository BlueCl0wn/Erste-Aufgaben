import DetermineCharge as DC
import numpy as np
import MakeGitter as MG
import time as t

def deltaE(conf_alt, altE, pos, charge, n):
    n -= 1

    neuE = altE

    neuE -= DC.getCharge(conf_alt, pos[0], pos[1],  n)

    neuE += charge
    neuE += conf_alt[pos[0] - 1][pos[1]] if pos[0] >= 0 else 0
    neuE += conf_alt[pos[0] + 1][pos[1]] if pos[0] <= (n-1) else 0
    neuE += conf_alt[pos[0]][pos[1] - 1] if pos[1] >= 0 else 0
    neuE += conf_alt[pos[0]][pos[1] + 1] if pos[1] <= (n-1) else 0


    return neuE - altE

def switchSpin(conf, n, e, r):
    altE = DC.getAllCharge(conf, n)

    for x in range(r):

        charge = MG.charge()

        pos = np.random.randint(0, n, size=(2))

        dE = deltaE(conf, altE, pos, charge, n)
        if dE <= 0:
            conf[pos[0]][pos[1]] = charge
        elif np.random.rand() < e:
            conf[pos[0]][pos[1]] = charge
        else:
            pass
        altE = altE + dE

    return conf
