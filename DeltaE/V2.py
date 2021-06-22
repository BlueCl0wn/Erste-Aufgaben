import DetermineCharge as DC
import numpy as np
import MakeGitter as MG

def deltaE(conf_alt, altE, pos, charge, n):
    i = pos[0]
    j= pos[1]

    n -= 1

    neuE = altE

    neuE -= DC.getCharge(conf_alt, i, j, n)

    neuE += charge
    neuE += conf_alt[i - 1][j] if i >= 0 else 0
    neuE += conf_alt[i + 1][j] if i <= (n-1) else 0
    neuE += conf_alt[i][j - 1] if j >= 0 else 0
    neuE += conf_alt[i][j + 1] if j <= (n-1) else 0

    return neuE - altE

def switchSpin(conf_alt, n, e):
    for x in range(1000):
        altE = DC.getAllCharge(conf_alt, n)
        charge = MG.charge()

        pos = np.random.randint(0, n, size=(2))

        if deltaE(conf_alt, altE, pos, charge, n) <= 0:
            conf_alt[pos[0]][pos[1]] = charge
        elif np.random.rand() < e:
            conf_alt[pos[0]][pos[1]] = charge
        else:
            pass

    return conf_alt
