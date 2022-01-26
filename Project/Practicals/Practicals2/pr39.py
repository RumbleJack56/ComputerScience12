print("List Comprehension")
print("\n\nWithout Comprehension in 5 lines")
lis1 = []
for i in range(5):
    for j in range(2):
        lis1.append([i,j])
print(lis1)
print("\n\nWith comprehension in 2 lines")
lis2 = [[i,j] for i in range(5) for j in range(2)]
print(lis2)
print("\n\nWithout comprehension in 8 lines")
lis3 = []
for i in range(3):
    for j in range(3):
        if (i + j) % 2 ==0:
            lis3.append([i,j,'e'])
        else:
            lis3.append([i,j,'o'])
print(lis3)
print("\n\n With comprehension in 2 lines")
lis4 = [[i,j,'e'] if (i+j)%2==0 else [i,j,'o'] for i in range(3) for j in range(3)]
print(lis4)
