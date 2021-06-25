import MakeGitter as MG
import DetermineCharge as DC

# Es gibt zwei verschiedenen Versionen dieser Datei. V1 und V2. V2 ist schneller.
# import DeltaEV2 as DeltaE
import DeltaE.V2 as DeltaE
import matplotlib.pyplot as plt

n = 100
e = 0.5
r = 10000

gitter = MG.getGitterV2(n)
MG.saveIMG(gitter, n, "Zweites/start_Graph")
MG.saveFile(gitter, "Zweites/start_Array")
conf_neu = DeltaE.switchSpin(gitter, n, e, r)
MG.saveIMG(conf_neu, n, "Zweites/end_Graph")
MG.saveFile(gitter, "Zweites/end_Array")

# x = MG.getGitter(n)
# c = DC.getAllCharge(x, n)
# print(c)
