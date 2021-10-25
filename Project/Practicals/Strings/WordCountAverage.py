#count words length and average mean
n , charCount = input("Enter Sentence: ").split() , 0
for j in n:
	charCount+=len(j)
print("The Average word length is ",round((charCount/len(n)),2),'.',sep='')
