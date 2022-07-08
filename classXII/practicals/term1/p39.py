#8/7/22

import sd
from pickle import *

mf=open('p39.txt','r+b')
val=load(mf)
print(val)
d={1:'p',2:'b',3:'c',4:'d'}
mf.seek(0)
dump(d,mf)

mf.close()
