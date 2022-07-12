def rev(k):
    string = ""
    for j in k:
        string = j + string
    return string

c = "ace race"
print(rev(c))