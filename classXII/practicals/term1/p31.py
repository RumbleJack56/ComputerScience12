#6/6/22

import sd

myfile = open("p31.txt" , 'r+')
data = [line for line in myfile]
[print(k.rstrip("\n")) for k in data]

myfile.seek(0)
myfile.writelines(data)
myfile.close()