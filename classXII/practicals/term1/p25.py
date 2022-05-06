#6/5/22

#Method 1:
def OEcount(mytuple):
    even = len(["" for k in mytuple if k%2==0])
    odd = len(mytuple) - even
    return odd,even

n = int(input("Number of Numbers: "))
tup = ()
for _ in range(n): tup += (int(input("Enter Number: ")),)
o,e = OEcount(tup)
print("Odd in tuple is",o,"and even in tuple is",e)



