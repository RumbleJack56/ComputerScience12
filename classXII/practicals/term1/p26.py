#19/5/22   


def j(s):
    sn1=''
    for i in range(len(s)):
        if s[i].islower(): sn1+=s[i].upper()
        elif s[i].isupper(): sn1+=s[i].lower()
        elif s[i].isdigit(): sn1+="*"
        else: sn1+='@'
    return sn1
print(j("LumberiNATIONi5aster*2001*11*09"))
