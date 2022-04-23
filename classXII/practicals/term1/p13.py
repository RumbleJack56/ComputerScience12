#22/4/22
def countvowel(s):
    c=0
    for ch in s:
        if ch in 'aeiouAEIOU':
            c+=1
    return c

sin=input('Enter a string: ')
count=countvowel(sin)
print('Total number of vowels in the string are: ',count)



#alternate method using list comprehension
def vowelcount(st): return len(['' for k in st if st.lower() in "aeiou"])
cos=input('Enter a string: ')
dooku=countvowel(cos)
print('Total number of vowels in the string are: ',dooku)

