import MakeGitter as MG
import DetermineCharge as DC
import time



# import SwitchSpinOptimized as SwSp
import SwitchSpin as SwSp


import matplotlib.pyplot as plt
import numpy as np

n = 100
T = 1
r = 1000000


gitter = MG.getGitterV2(n)

MG.saveGridIMG(gitter, n, "Projekt/Ergebnis/start_Graph")

MG.saveFile(gitter, "Projekt/Ergebnis/start_Array")

conf_neu = SwSp.switchSpin(gitter, n, T, r, distanz=0, akzeptanzrate=False, GraphE=True)

MG.saveGridIMG(conf_neu, n, "Projekt/Ergebnis/end_Graph")
MG.saveFile(gitter, "Projekt/Ergebnis/end_Array")

# plt.show()



# x = MG.getGitter(n)
# c = DC.getAllCharge(x, n)
# print(c)
