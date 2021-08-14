print("Multiples between 2 and 100")
num = int(input("Enter a number between 2 and 100: "))
if (num>2 and num<100):
    print("The multiples of",num,"are :")
    for j in range(3,100):
        if((j%num)==0):
            print('\t',j)
else:
    print("Invalid input.")
