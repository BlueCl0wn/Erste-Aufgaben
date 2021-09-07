# Bibliotheken
import time
import matplotlib.pyplot as plt
import numpy as np

# Funktionen
import MakeGitter as MG
import DetermineCharge as DC
import SwitchSpinOptimized as SwSp
import SaveGitter as SG
import Wiederholung


n = 100
T = 1
r = 10000
reps = 10

listOfGraphs = Wiederholung.repeat(reps, n, T, r)
avgGraph = Wiederholung.averageArray(listOfGraphs)

SG.saveMeanGraphIMG(listOfGraphs, avgGraph, r, n, T, reps,  "EGraphGemittelt")



# gitter = MG.getGitterV2(n)

# SG.saveGridIMG(gitter, n, "Projekt/Ergebnis/start_Graph")
# SG.saveFile(gitter, "Projekt/Ergebnis/start_Array")

# conf_neu, my_graphE, my_akzeptanzVars, infos = SwSp.switchSpin(gitter, n, T, r, distanz=0, akzeptanzrate=False, GraphE=True, Abbruchbedingung=(True, 100))

# print("hsdfbsdifb")
# print(conf_neu)
# print(my_graphE)
# print(my_akzeptanzVars)

# SG.saveGridIMG(conf_neu, n, "Projekt/Ergebnis/end_Graph")
# SG.saveGraphIMG(my_graphE[0], my_graphE[1], r, n, T,  "EGraph", int(infos[3]))
# SG.saveFile(gitter, "Projekt/Ergebnis/end_Array")

# plt.show()



# x = MG.getGitter(n)
# c = DC.getAllCharge(x, n)
# print(c)
