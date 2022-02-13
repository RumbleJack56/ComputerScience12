#Basic
def renameKey( dic , existKey , newKey ):
    if newKey not in dic.keys():
        dic[newKey] = dic[existKey]
        del dic[existKey]
        return dic
    else: print("New Key already exists") ; return None

print(renameKey({1:'a', 2:'b' , 3:'c'} , 2 , 6))




#Semi Advanced
def renameKey2(dic , oldKey , newKey):
    a = dict([(newKey,k[1]) if k[0]==oldKey else (k[0],k[1]) for k in dic.items()])
    return a

print(renameKey2({1:'a', 2:'b' , 3:'c'} , 2 , 6))




#Advanced
renameKey3 = lambda d , k1 , k2 : dict([(k2,x[1]) if x[0]==k1 else (x[0],x[1]) for x in d.items()])
print(renameKey3({1:'a', 2:'b' , 3:'c'} , 2 , 6))



# print("LOL")