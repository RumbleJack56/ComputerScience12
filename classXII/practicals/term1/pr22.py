#6/5/22

#Method1:
GivenList1 = [458,646,64,385,48,364,77,62,43,59,78]
print("List Before Function is", GivenList1)

def OddEven1(Ls):
    for k in range(len(Ls)): 
        if Ls[k] %2==0 : Ls[k]//=2
        else: Ls[k]*=2
OddEven1(GivenList1)

print("List After Method is", GivenList1)

