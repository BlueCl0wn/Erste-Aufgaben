import MakeGitter as MG
import DetermineCharge as DC

# Es gibt zwei verschiedenen Versionen dieser Datei. V1 und V2. V2 ist schneller.
# import DeltaEV2 as DeltaE
import DeltaE.V2 as DeltaE
import matplotlib.pyplot as plt

n = 100
e = 0.001
r = 100000

# print(DC.getAllCharge(x, n))
def bla(n):
    print(DC.getAllCharge(MG.getGitter(n), n))

gitter = MG.getGitter(n)
MG.save(gitter, n, "alt")
conf_neu = DeltaE.switchSpin(gitter, n, e, r)
MG.save(conf_neu, n, "neu")

# x = MG.getGitter(n)
# c = DC.getAllCharge(x, n)
# print(c)
