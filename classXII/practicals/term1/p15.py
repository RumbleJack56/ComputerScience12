#22/4/22

def cch(s,ch):
    c=0
    for i in s:
        if i==ch:
            c+=1
    return c

sin=input('Enter a string: ')
ch1=input('Enter the character to count: ')
f=cch(sin,ch1)

if f==0:
    print(ch1, "does not exist.")
else:
    print(ch1,'exist',f,'times.')