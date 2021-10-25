a = 'python4csip'
L = len(a)
m = ''
for i in range(L):
	if ((a[i] >='a') and (a[i] <='m')):
		m+=a[i].upper()
	elif ((a[i] >='n') and (a[i] <='z')):
		m+=a[i-1]
	elif (a[i].isupper()):
		m+=a[i].lower()
	else:
		m+='#'
print(m)