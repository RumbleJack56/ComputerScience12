t = (1,5,4,2,6,8,4,7,5,234,6,3,534,5,3,45)
print("Tuple is",t)
a = int(input("Enter Element to Search:"))
for k in range(len(t)):
    if a==t[k]:
        print("Element found at index",k)
        print("Search Complete")
        break
else:
    print("Search Failed")
