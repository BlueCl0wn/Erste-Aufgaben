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

def meanGraph(n, beta, r, reps) -> None:
    listOfGraphs = Wiederholung.repeatE_Graph(reps, n, beta, r)
    print(listOfGraphs)

    avgGraph = B.tolerant_meanArray(listOfGraphs)

    SG.saveMeanGraphIMG(listOfGraphs, avgGraph, r, n, beta, reps,  "EGraphGemittelt")

def graph(n, beta, r):
    gitter = MG.getGitterV2(n)

    # SG.saveGridIMG(gitter, n, "Projekt/Ergebnis/start_Graph")
    # SG.saveFile(gitter, "Projekt/Ergebnis/start_Array")

    conf_neu, my_graphE, my_akzeptanzVars, infos = SwSp.switchSpin(gitter, n, beta, r, distanz=0, akzeptanzrate=False, GraphE=True, Abbruchbedingung=(True, 100))

    print("hsdfbsdifb")
    # print(conf_neu)
    print(my_graphE)
    # print(my_akzeptanzVars)

    # SG.saveGridIMG(conf_neu, n, "Projekt/Ergebnis/end_Graph")
    SG.saveGraphIMG(my_graphE, n, beta,  "EGraph", int(infos[3]))
    # SG.saveFile(gitter, "Projekt/Ergebnis/end_Array")
