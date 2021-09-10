# Bibliotheken
import time
import matplotlib.pyplot as plt
import numpy as np

# Funktionen
import MakeGitter as MG
import DetermineCharge as DC
import SwitchSpinOptimized as SwSp
from DetermineMagnetisierung import getAllMag
import SaveGitter as SG
import Wiederholung
import Berechnungen as B
import Functions

n = 100
# T = 10
beta = 0.5 # 0 <= beta <= 1
r = 10000
reps = 3



def blub(reps, n, beta, r,) -> list:
    # x = Wiederholung.repeatChoose(reps, n, beta, r, 0)
    # y = map(getAllMag, x)
    return list(map(getAllMag, Wiederholung.repeatChoose(reps, n, beta, r, 0)))

def testBeta(d) -> list:
    betas = np.flip(np.arange(1.0, 0.0, -1.0/d))
    return [blub(reps, n, beta, r,) for beta in betas]

x = testBeta(5)
print(x)

y = B.avgArraySameLength(x, axis=1)
print(y)

# bla = [beta for beta in np.arange(1.0, 0.0, -1.0/50)]
# print(np.flip(bla))


# y = map(getAllMag, x)
# print(list(y))
# SG.saveArray("test", x)


# Functions.meanGraph(n, beta, r, reps)
