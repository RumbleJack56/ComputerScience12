d={'p':43,'q':13,'r':4,'s':100}
vals = sorted([d[x] for x in d])
for k in d:
    if d[k]==vals[0]:
        print("Minimum Value",d[k],"at index",k)
    if d[k]==vals[-1]:
        print("Maximum Value",d[k],"at index",k)
