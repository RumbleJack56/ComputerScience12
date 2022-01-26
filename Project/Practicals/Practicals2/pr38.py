print("List Functions and Methods")
lost = [1,2,3,4,6,7,121,-31.41,2,3,2,2]
print("The list is",lost,"\n")
print("""
You can select from functions to perform on the list:
1) index()
2) append()
3) extend()
4) count()
5) reverse()
6) sort()
7) insert()
8) pop()
""")
while True:
    option = int(input("Enter the Option: "))
    if option==1:
    	print(lost.index(eval(input("index() \nEnter the item (use appropriate variable format): "))))
    elif option==2:
        lost.append(eval(input("append() \nEnter Item to Append (use appropriate variable format): ")))
        print(lost)
    elif option==3:
        lost.extend(eval(input("extend() \nEnter List to Extend (use appropriate variable format): ")))
        print(lost)
    elif option==4:
    	print(lost.count(eval(input("count() \nEnter the Item (use appropriate variable format): "))))
    elif option==5:
        lost.reverse()
        print(lost)
    elif option==6:
        if bool(input("sort() \nIf you want to reverse press 1 else blank: ")) == 0:
            lost.sort() ; print(lost)
        else:
            lost.sort(reverse=True) ; print(lost)
    elif option==7:
        lost.insert(eval(input("count() \nEnter index: ")),eval(input("Enter Item (in format): ")))
        print(lost)
    elif option==8:
        a = lost.pop(int(input("Enter index to pop: ")))
        print(lost)
        print("Removed Item:",a)
    else: continue
    break
