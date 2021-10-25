#Len compare print
m , n , c , d= input("Enter String 1: ") , input("Enter String 2: ") , 0 , 0
for j in m:
	c+=1
for j in n:
	d+=1
if(c>d):
	print(m)
elif(d>c):
	print(n)
else:
	print("both are equal")
