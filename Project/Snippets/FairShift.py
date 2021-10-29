"""Extract two list-slices of a given list of numbers. Display and print the  sum of elements of first list slice which contain every other elements between index 5 to 15. program should also display the average of second sliced list which contains every fourth elements of list. The list contains 20 elements"""



val , a1 , sum1 , a2 , sum2= [10,20,30,40,1,2,3,100,200,10,20,30,11,12,15,17,19,90,77,] , [] , 0 , [] , 0
[a1.append(val[a]) for a in range(5,15) if a%2==1]
for j in a1:
    sum1+=j
print('Sum of every other element between 5 and 15 is',sum1)
[a2.append(val[x]) for x in range(len(val)) if x%4==0]
for j in a2:
    sum2+=j
print('The average of list 2 is',sum2/len(a2))