#6/5/22

def MatrixPrintDiagonal(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i==j:
                print(l[i][j],end='\t')
            else:
                print('',end='\t')
        print()

m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

MatrixPrintDiagonal(m)