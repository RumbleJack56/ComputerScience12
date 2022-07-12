#07-07-2022
#line cursor setter
import sd

def lineset(filen,Lnum,pos):
    chars = [len(line) for line in filen.readlines()]

with open('p38.txt','r+') as file1:
    file1.seek(12)
    file1.write("1") 