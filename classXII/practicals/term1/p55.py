#10/8/22


#functions
def emp(S):
    if len(S)==0:
        return True
    else:
        return False


def push(S,a):
    S.append(a)
    top=len(S)-1


def pop(S):
    if emp(S):
        return "Underflow"
    else:
        val=S.pop()
        if len(S)==0:
            top=None
        else:
            top=len(S)-1
        return val

def peek(S):
    if emp(S):
        return 'Underflow'
    else:
        top=len(S)-1
        return S[top]


def show(S):
    if emp(S):
        print("Sorry, empty stack")
    else:
        t=len(S)-1
        print('(Top)',end='')
        while(t>=0):
            print((S[t]))
            t-=1
        print()


#main program        

S=[]
top=None
while True:
    print("STACKS FUNCTIONS")
    print("1) PUSH")
    print("2) POP")
    print("3) PEEK")
    print("4) SHOW STACK")
    print("5) EXIT")

    ch=int(input("Enter your choice:" ))\
    
    if ch==1:
        v=int(input("Enter item to add: "))
        push(S,v)

    elif ch==2:
        v=pop(S)
        if v=='Underflow':
            print('Stack empty')
        else:
            print("Deleted item: ",v)
    
    elif ch==3:
        v=peek(S)
        if v=='Underflow':
            print('Stack empty')
        else:
            print("Top item: ",v)
    
    elif ch==4:
        show(S)

    elif ch==5:
        print("Bye")
        break
