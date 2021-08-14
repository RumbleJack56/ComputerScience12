def sorter(variable_type_list=[]):
    lis = variable_list
    lisLen=len(lis)
    for a in range(0,lisLen):
        for iter in range(a+1,lisLen):
            if  lis[a] > lis[iter]:
                lis[a],lis[iter] = lis[iter],lis[a]
    print(lis)

toArrange = [123,4353,232,434,9948,18,1,43,56,234]
sorter(toArrange)
