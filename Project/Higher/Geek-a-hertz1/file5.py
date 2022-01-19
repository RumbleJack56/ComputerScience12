n_cycles , qry = int(input()) , []
values = []
op = []
for _ in range(n_cycles):
    qry.append(input().split())
for a in qry:
    if int(a[0]) == 1:
        values.append(a[1])
    if int(a[0]) == 2:
        for k in range(int(a[1])): 
            try: values.pop()
            except: pass
    try: op.append(values[-1])
    except: op.append('Nil')
for k in op: 
    print(k)