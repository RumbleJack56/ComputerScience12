#4/4/22

def drawline(sym,t=20):
    for i in range(t):
        print(sym,end='')
    print()

drawline(sym='@')
drawline('#')
drawline('*',60)
drawline(t=80 ,sym='^')