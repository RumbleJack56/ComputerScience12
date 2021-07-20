def Hi(name="Human"):
    print("Hello,",name,"I am Python interpreter")

p=5%2            #1
q=p**4           #1
r=p//q           #1
p+=p+q+r         #1 + 1 + 1+1 =4
r+=p+q+r         #1 + 4 + 1+ 1 = 7
q-=p+q*r         #1 - 4 - 7 = -10
print(p,q,r)
