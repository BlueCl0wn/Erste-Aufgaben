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
import Berechnungen as B


n = 100
T = 10
r = 1000000
reps = 10


def meanGraph() -> None:
    listOfGraphs = Wiederholung.repeat(reps, n, T, r)
    print(listOfGraphs)

    avgGraph = B.tolerant_meanArray(listOfGraphs)
    print(avgGraph)

    SG.saveMeanGraphIMG(listOfGraphs, avgGraph, r, n, T, reps,  "EGraphGemittelt")

def graph():
    gitter = MG.getGitterV2(n)

    # SG.saveGridIMG(gitter, n, "Projekt/Ergebnis/start_Graph")
    # SG.saveFile(gitter, "Projekt/Ergebnis/start_Array")

    conf_neu, my_graphE, my_akzeptanzVars, infos = SwSp.switchSpin(gitter, n, T, r, distanz=0, akzeptanzrate=False, GraphE=True, Abbruchbedingung=(True, 100))

    print("hsdfbsdifb")
    # print(conf_neu)
    print(my_graphE)
    # print(my_akzeptanzVars)

    # SG.saveGridIMG(conf_neu, n, "Projekt/Ergebnis/end_Graph")
    SG.saveGraphIMG(my_graphE, n, T,  "EGraph", int(infos[3]))
    # SG.saveFile(gitter, "Projekt/Ergebnis/end_Array")

# graph()
meanGraph()
