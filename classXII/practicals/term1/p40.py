#8/7/22

import sd
from pickle import *

with open('p40.txt', 'w+b') as f:
    dump({1:'p',2:'b',3:'c',4:'d'},f)
    f.seek(0)
    data = load(f)
    print(data)