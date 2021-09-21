n , c = input("Average Word Length \nEnter String: ").split() , 0
for j in n:
    c+=len(j)
print("Average Word Length =",(c*100//len(n))/100)
