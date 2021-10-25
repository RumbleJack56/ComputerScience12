a = "h ;4 t akos"
out = ''
for j in a:
    if j.isspace():
        out+=j
    elif j.isdigit():
        out+=str(int(j) - 1)
    else:
        if j in 'aeiou':
            out+=j
        else:
            out+=chr( ord(j) + 1 )
print(out)
