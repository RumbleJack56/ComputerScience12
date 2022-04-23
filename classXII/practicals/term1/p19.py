#23/4/22

def freq(l,d):
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d

l1=[1,2,31,4,1,4,6,2,1,6,6,2]
d1={}
freq(l1,d1)
print(d1)

