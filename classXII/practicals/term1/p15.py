#22/4/22
def countChar(s,ch):
    c=0
    for i in s:
        if i==ch:
            c+=1
    return c

sin=input('Enter a string: ')
ch1=input('Enter the character to count: ')
f=countChar(sin,ch1)

if f==0:
    print(ch1, "does not exist.")
else:
    print(ch1,'exist',f,'times.')

#Alernate Method
chCount = lambda x,y : len(["" for k in x if k == y])
v = chCount(input("Enter String: "),input("Enter character: "))
if v!=0: print("Character found",v,"times")
else: print("Character not found")