times = int(input())
state = 0
err = 0
op = []
for _ in range(times):
    n_inputs = int(input())
    val = input().split()
    val = [x.lower() for x in val]
    for j in val:
        if j == 'start':
            state = 1
        elif j == 'restart' and state==1:
            pass
        elif j == 'restart' and state==0:
            state = 1
        elif j == 'stop' and state==1:
            state = 0
        elif j == 'stop' and state==0:
            err = 1
            break
    if err == 1:
        op.append('404')
    elif err == 0:
        op.append('200')
for j in op:
    print(j)
