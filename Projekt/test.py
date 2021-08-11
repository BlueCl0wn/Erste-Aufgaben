def blub(x):
    return x if x > 0 else "wrong"

def blub2(x):
    if x > 0:
        return x
    else:
        return "wrong"

r= 100000

x = False

if x:
    for i in range(r):
        print(blub(-1))
else:
    i=0
    while(i < 10000):
        print(blub(-1))
        i+=1
