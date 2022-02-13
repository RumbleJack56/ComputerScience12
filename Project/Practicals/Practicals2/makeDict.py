#Method 1 : Basic
def lisToDict(L1 , L2):
    d1 = {}
    for j in range(len(L1)):
        d1[L1[j]] = L2[j]
    return d1

print(lisToDict([100,-2,300],['a','b','c']))






#Method 2 : Slightly Advanced

def DictCreate(Lis1, Lis2):
    join = [ ( Lis1[x] , Lis2[x] ) for x in range(len(Lis2))]
    join = dict(join)
    return join

print(DictCreate([100,-2,300],['a','b','c']))





#Method 3 : Efficient but very Advanced

LD = lambda L1 , L2 : dict([ (L1[k],L2[k]) for k in range(len(L1))])

print(LD([100,-2,300],['a','b','c']))
