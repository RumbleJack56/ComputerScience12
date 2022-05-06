#6/5/22

def avgs(l):
    s=0
    for i in l:
        s+=i
    avg=s/len(l)
    return s,avg

l1=[]
n=int(input('Enter how many numbers: '))
for i in range(n):
    num=int(input('Enter any number: '))
    l1.append(num)

print(l1)
savg=avgs(l1)
print('Sum= ',savg[0],'Average= ',savg[1])