#22/4/22

def marksu(s,nm):
    s['Marks']+=nm
    s["Status"]="Updated"

s1={'Name':'Akash','Marks':56,'Status':'Old'}
s2={'Name':'Chinmay','Marks':60,'Status':'Old'}
s3={'Name':'Chirag','Marks':50,'Status':'Old'}

print("Original data: ")
print(s1)
print(s2)
print(s3)

marksu(s1,70)
marksu(s2,80)
marksu(s3,75)

print("After updating: ")
print(s1)
print(s2)
print(s3)


