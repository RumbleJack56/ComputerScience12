#27-07-2022
#csv working
import sd , csv

with open("p51.csv",'r') as f1:
    dat = csv.reader(f1)
    dat = [line for line in dat]
    maxl = max([len(line) for line in dat])
    for line in dat:
        while len(line)!=maxl:
            line.append('')
    print(dat)

    maxlist = []
    for times in range(len(line)):    
        maxval = 0
        for line in dat:
            if len(line[times]) > maxval:
                maxval = len(line[times])
        maxlist.append(maxval)
    strR = "|"
    for length in maxlist:
        strR = strR + r"%-"+str(length)+"s|"
    print("_"*(sum(maxlist)+len(maxlist)+1))
    for line in dat:
        # print(line)
        print(str(strR)%tuple(line))
    print("‾"*(sum(maxlist)+len(maxlist)))

# ___‾‾‾
        
