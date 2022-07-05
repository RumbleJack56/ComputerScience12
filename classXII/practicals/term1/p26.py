#19/5/22   


def j(s):
    sn1=''
    for i in range(len(s)):
        if sn1[i].islower: sn1+=s[i].upper()
        elif sn1[i].isupper: sn1+=s[i].lower()
        elif sn1[i].isdigit: sn1+="*"
        else: sn1+='@'
    return sn1
    