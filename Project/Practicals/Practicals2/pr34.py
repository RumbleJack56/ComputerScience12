print(" Welcome to List Size and Indexing")
lis = 0
while True:
    try: lis = eval(input("  Enter List: "))
    except: pass
    if type(lis)==type([]): break
    print('   Invalid, Try Again')
print(' Length of List is',len(lis),end="\n\n")
for j in range(len(lis)):
    print("  Element",j+1,":",lis[j])
    print("   Index from Front:",j)
    print("   Index from Back:" ,j-len(lis),end="\n\n")
