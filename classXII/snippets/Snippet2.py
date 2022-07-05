import manage

ar = open("Datafiles.txt", 'r')
for z in ar.readlines():
    print(z[:-1])

ar = open("Datafiles.txt", 'r')
for str in ar:
    print(str,end="")

aw = open("DataFiles.txt", "w")
aw.writelines([k+'\n' for k in ("hi","hello","Vartika","<3")])
aw.close()