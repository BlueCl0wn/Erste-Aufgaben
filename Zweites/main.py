import MakeGitter as MG
import DetermineCharge as DC
import time

"""Es gibt mehrere Versionen dieser Datei. V1, V2 und V3. Die Neueste ist jeweils schneller als die Vorherige."""
import SwitchSpin as SwSp

import matplotlib.pyplot as plt
import numpy as np

n = 100
T = 1000
r = 1000

gitter = MG.getGitterV2(n)

MG.saveGridIMG(gitter, n, "Zweites/Ergebnis/start_Graph")

MG.saveFile(gitter, "Zweites/Ergebnis/start_Array")

conf_neu = SwSp.switchSpin(gitter, n, T, r, distanz=0, akzeptanzrate=True)

MG.saveGridIMG(conf_neu, n, "Zweites/Ergebnis/end_Graph")
MG.saveFile(gitter, "Zweites/Ergebnis/end_Array")

plt.show()



# x = MG.getGitter(n)
# c = DC.getAllCharge(x, n)
# print(c)
