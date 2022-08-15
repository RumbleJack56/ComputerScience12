#15-08-22
#end7 summer


Mylist = [10,27,15,107,97,5,7,81,47]
listofsevens = lambda L: [x for x in L if str(x)[-1]=="7" ]
print(Mylist)
print(listofsevens(Mylist))
print(sum(listofsevens(Mylist)))
