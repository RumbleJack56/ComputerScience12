print("Summation of Series whose nth term is -(x)^(n-1)/n!")
n,x=int(input("Enter Sequence Terms: ")),int(input("Enter x: "))
seq,fac=0,1
for j in range(1,n+1):
    for i in range(1,j+1):
        fac*=i
    seq+=  ((-x)**(j-1))/fac
print(seq)
