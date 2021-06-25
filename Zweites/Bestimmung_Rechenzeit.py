import MakeGitter as MG
import DetermineCharge as DC


n = 12500
x=MG.getGitterV2(n)
print(x)
print(DC.getAllCharge(x, n))
