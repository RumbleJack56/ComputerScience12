print("Elemental Frequency")
tup = tuple(sorted(list(eval(input("Enter values in tuple form: ")))))
sel = ()
for x in tup:
    if x not in [y[0] for y in sel]:
        sel+=((x,tup.count(x)),)
for x in sel: print("%-5s - %-5s"%(x[0],x[1]))


print("Elemental Frequency")
tup,sel= tuple(sorted(list(eval(input("Enter values in tuple form: "))))),[]
sel = [(x,tup.count(x)) for x in tup if x not in [y[0] for y in sel]]
for x in sel: print("%-3s-%-3s"%(x[0],x[1]))