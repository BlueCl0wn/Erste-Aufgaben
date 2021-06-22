import DetermineCharge as DC
import numpy as np
import MakeGitter as MG

def deltaE(conf_alt, conf_neu, n):
    return DC.getAllCharge(conf_neu, n) - DC.getAllCharge(conf_alt, n)

def switchSpin(conf_alt, n, e):
    for x in range(1000):
        # altE = getAllCharge(conf_alt, n)
        pos = np.random.randint(0, n, size=(2))
        conf_neu = conf_alt
        conf_neu[pos[0]][pos[1]] = MG.charge()
        # neuE = getAllCharge(conf_neu, n)
        # if neuE < altE:
        if deltaE(conf_alt, conf_neu, n) <= 0:
            conf_al = conf_neu
        elif np.random.rand() < e:
            conf_alt = conf_neu
        else:
            pass
    return conf_alt
