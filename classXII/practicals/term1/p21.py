#4/6/22
#using functions as objects and combining them
name = "Madam"
print(name.replace('m','nna').upper())
print(name.upper().replace("M",'NNA'))

name="Vikram"
print(name.replace('im','nt').upper()) 

#finding number of numbers with a conditional : odd, divisible by 7, leaves remainder 3 on dividing by 5, less than 5000
print(len([x for x in range(5000+1) if x%2==1 and x%7==0 and x%5==3]))