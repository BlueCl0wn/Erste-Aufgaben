# Bibliotheken
import time
import matplotlib.pyplot as plt
import numpy as np

# Funktionen
import MakeGitter as MG
import DetermineCharge as DC
import SwitchSpinOptimized as SwSp
import SaveGitter as SG


n = 100
T = 1
r = 10000


gitter = MG.getGitterV2(n)

SG.saveGridIMG(gitter, n, "Projekt/Ergebnis/start_Graph")

SG.saveFile(gitter, "Projekt/Ergebnis/start_Array")

conf_neu, my_graphE, my_akzeptanzVars = SwSp.switchSpin(gitter, n, T, r, distanz=0, akzeptanzrate=False, GraphE=False, Abbruchbedingung=(True, 100))

print("hsdfbsdifb")
print(my_graphE)
print(my_akzeptanzVars)

SG.saveGridIMG(conf_neu, n, "Projekt/Ergebnis/end_Graph")
SG.saveFile(gitter, "Projekt/Ergebnis/end_Array")

# plt.show()



# x = MG.getGitter(n)
# c = DC.getAllCharge(x, n)
# print(c)
