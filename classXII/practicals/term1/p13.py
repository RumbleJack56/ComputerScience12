#22/4/22

#Method 1:
def countvowel(s):
    c=0
    for ch in s:
        if ch in 'aeiouAEIOU':
            c+=1
    return c

sin=input('Enter a string: ')
count=countvowel(sin)
print('Total number of vowels in the string are: ',count)


#Method 2:
def vowelcount(st): return len(['' for k in st if st.lower() in "aeiou"])
a=input('Enter a string: ')
d=countvowel(a)
print('Total number of vowels in the string are: ',d)

