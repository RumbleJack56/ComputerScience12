print("Words Occurence")
n= input("Enter a few lines: \n")
subs , count = input("Enter Word to find: ") , 0
for j in range(len(n)-len(subs)+1):
    if subs+" " == n[j:(j+len(subs)+1)]:
        count += 1
print("The number of times the word appears is",count)
