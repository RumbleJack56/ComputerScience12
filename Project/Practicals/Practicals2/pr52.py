d = {'m':3 , 'n':6 , 'o':2 , 'p':3 , 'q':2}
dn = {}
print(d)
for k in d:
    if d[k] not in dn.values():
        dn[k]=d[k]
print(dn)
