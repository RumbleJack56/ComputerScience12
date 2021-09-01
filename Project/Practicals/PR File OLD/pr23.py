print("Word Count and Substrings")
n,wrds= input("Enter a few lines: \n"),1
for j in n:
    if(j==" "):
        wrds+=1
print("Word Count:",wrds,end="\n")
subs , count = input("Enter substring: ") , 0
for j in range(len(n)-len(subs)+1):
    if subs == n[j:(j+len(subs))]:
        count += 1
print("The number of times the substring appears is",count)
