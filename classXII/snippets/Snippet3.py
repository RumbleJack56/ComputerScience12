a = 10
print(a , id(a) , type(a))

def func(x):
    a = 12
    p = (a,)
    print(a , id(a) , type(a))
    print(p , id(p) , type(p))
    print(x , id(x) , type(x))
    x += 4
    print(x , id(x) , type(x))
    x -=4
    print(x , id(x) , type(x))

func(a)

print(a , id(a) , type(a))