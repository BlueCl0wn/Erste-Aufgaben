import MakeGitter as MG
import DetermineCharge as DC
import time



import SwitchSpin as SwSp

import matplotlib.pyplot as plt
import numpy as np

n = 100
T = 1
r = 10000


gitter = MG.getGitterV2(n)

MG.saveGridIMG(gitter, n, "Zweites/Ergebnis/start_Graph")

MG.saveFile(gitter, "Zweites/Ergebnis/start_Array")

conf_neu = SwSp.switchSpin(gitter, n, T, r, distanz=0, akzeptanzrate=False, GraphE=True)

MG.saveGridIMG(conf_neu, n, "Zweites/Ergebnis/end_Graph")
MG.saveFile(gitter, "Zweites/Ergebnis/end_Array")

# plt.show()



# x = MG.getGitter(n)
# c = DC.getAllCharge(x, n)
# print(c)
