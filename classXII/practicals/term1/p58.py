#12-08-2022
#count odd-even

def SumOddEven(L):
    od , ev = list() , list()
    [od.append(k) if k%2==1 else ev.append(k) for k in L]
    return len(od),len(ev)
lis = [8,12,17,19,25,28,33,32,56,90]
print(SumOddEven(lis))