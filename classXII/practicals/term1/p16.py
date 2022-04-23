#22/4/22

#passing immutable tuple to a function

def ttl(A):
    A=list(A)
    A[0]=A[0]*2
    A[1]=A[1]+10
    print(A)

t=(100,200)
print(t)
ttl(t)