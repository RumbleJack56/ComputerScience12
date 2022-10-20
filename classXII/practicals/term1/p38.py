#07-07-2022
#line cursor setter
import sd

def lineset(filen):
    chars = [len(line) for line in filen.readlines()]
    filen.seek(0,0)
    for k in chars:
        print(k, filen.tell())
        filen.seek(filen.tell() + k-2)
        filen.write("*")
        filen.seek(filen.tell()+3)

with open('p38.txt','r+') as file1:
    lineset(file1)
    file1.seek(12,0)
    file1.write("1")