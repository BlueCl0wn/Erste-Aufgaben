import MakeGitter as MG
import DetermineCharge as DC
import time

# Es gibt zwei verschiedenen Versionen dieser Datei. V1 und V2. V2 ist schneller.
# import DeltaEV2 as DeltaE
import DeltaE.V3 as DeltaE
import matplotlib.pyplot as plt
import numpy as np

n = 100
e = 0.1
r = 100000

gitter = MG.getGitterV2(n)

MG.saveIMG(gitter, n, "Zweites/start_Graph")

MG.saveFile(gitter, "Zweites/start_Array")

conf_neu = DeltaE.switchSpin(gitter, n, e, r)

MG.saveIMG(conf_neu, n, "Zweites/end_Graph")

MG.saveFile(gitter, "Zweites/end_Array")

# x = MG.getGitter(n)
# c = DC.getAllCharge(x, n)
# print(c)
