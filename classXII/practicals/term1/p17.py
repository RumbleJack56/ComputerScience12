#22/4/22
def countOddEven(t):
    odd = len(['' for k in t if k%2==1])
    return odd , len(t) - odd
store = tuple()
times = int(input("Number of elements: "))

for _ in range(times):
    store+= (int(input("Enter Element "+str(_+1)+": ")),)

a = countOddEven(store)
print("Odd numbers are",a[0] , "and Even numbers are",a[1])