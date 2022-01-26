print(" Welcome to List Slicing")
LS = 0
while True:
    try: LS = eval(input("  Enter List: "))
    except: pass
    if type(LS)==type([]): break
    print('   Invalid, Try Again')
print('Enter the Index range-')
s=int(input('Start Index: '))
e=int(input('End   Index: '))
print(LS[s:e])
