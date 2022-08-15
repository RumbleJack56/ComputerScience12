#12-08-22
#list comprehension
#code1
lis2to100 = [x for x in range(2,101)]
print(lis2to100)
#code2
listAlts = lambda lis: [x for x in lis[1::2]]
print(listAlts([1,2,4,4,5,5,6,2,2,4,5,23,1,3,4,1,24,21]))