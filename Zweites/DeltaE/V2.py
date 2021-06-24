import DetermineCharge as DC
import numpy as np
import MakeGitter as MG

def deltaE(conf_alt, altE, pos, charge, n):
    n -= 1

    neuE = altE

    neuE -= DC.getCharge(conf_alt, pos[0], pos[1], n)

    neuE += charge
    neuE += conf_alt[pos[0] - 1][pos[1]] if pos[0] >= 0 else 0
    neuE += conf_alt[pos[0] + 1][pos[1]] if pos[0] <= (n-1) else 0
    neuE += conf_alt[pos[0]][pos[1] - 1] if pos[1] >= 0 else 0
    neuE += conf_alt[pos[0]][pos[1] + 1] if pos[1] <= (n-1) else 0

    return neuE - altE

def switchSpin(conf, n, e, r):
    for x in range(r):
        altE = DC.getAllCharge(conf, n)
        charge = MG.charge()

        pos = np.random.randint(0, n, size=(2))

        if deltaE(conf, altE, pos, charge, n) <= 0:
            conf[pos[0]][pos[1]] = charge
        elif np.random.rand() < e:
            conf[pos[0]][pos[1]] = charge
        else:
            pass

    return conf
