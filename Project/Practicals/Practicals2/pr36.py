print(" Welcome to List Index Deletion")
LS = 0
while True:
    try: LS = eval(input("  Enter List: "))
    except: pass
    if type(LS)==type([]): break
    print('   Invalid, Try Again')
de = int(input("Enter Index to Delete: "))
LS = [LS[x] for x in range(len(LS)) if x!=de]
print(LS)
