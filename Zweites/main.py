import MakeGitter as MG
import DetermineCharge as DC
import time

"""Es gibt mehrere Versionen dieser Datei. V1, V2 und V3. Die Neueste ist jeweils schneller als die Vorherige."""
import DeltaE.V3 as DeltaE

import matplotlib.pyplot as plt
import numpy as np

n = 100
T = 10
r = 10000

gitter = MG.getGitterV2(n)

MG.saveIMG(gitter, n, "Zweites/start_Graph")

MG.saveFile(gitter, "Zweites/start_Array")

conf_neu = DeltaE.switchSpin(gitter, n, T, r)

MG.saveIMG(conf_neu, n, "Zweites/end_Graph")

MG.saveFile(gitter, "Zweites/end_Array")

# x = MG.getGitter(n)
# c = DC.getAllCharge(x, n)
# print(c)
