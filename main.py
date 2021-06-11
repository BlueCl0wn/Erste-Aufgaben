import MakeGitter as MG
import DetermineCharge as DC

n = 10000

# print(DC.getAllCharge(x, n))
def bla(n):
    print(DC.getAllCharge(MG.getGitter(n), n))

x = MG.getGitter(n)
c = DC.getAllCharge(x, n)
print(c)
