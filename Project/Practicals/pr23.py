print("Word Count and Substrings")
n,wrds= input("Enter a few lines: \n"),1
for j in n:
    if(j==" "):
        wrds+=1
print("Word Count:",wrds,end="\n")
subs= input("Enter substring: ")
subsAppear, iter = 0 , (len(n)-len(subs)+1)
for count in range(0,iter):
    j=0
    for num in range(count,count+len(subs)):
        if(n[num]!=subs[j]):
            j+=1
            break
    else:
        subsAppear+=1
print("The number of times the substring appears is",subsAppear)
