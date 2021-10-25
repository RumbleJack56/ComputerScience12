n , c = input("Enter String: ").lower() , 0
for j in n:
	if j in "aeiou":
		c+=1
print("There are",c,"vowels in the string.")




# n , c = input("Enter String: ") , []
# c = len([c.append('') for j in n if j in 'aeiouAEIOU'])
# print('There are',c,'vowels in the string.')
