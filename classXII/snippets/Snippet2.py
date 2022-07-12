def rev(a):
    revword = ""
    for k in a:
        revword = k + revword
    return revword

c = "asodjqwowidhqwi"
print(rev(c))