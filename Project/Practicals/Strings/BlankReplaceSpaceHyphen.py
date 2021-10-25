# print(input("Enter String: ").replace(' ','-'))


n = input("Enter String: ")
for j in range(len(n)):
    if n[j] == " ":
        print('-',end="")
    else:
        print(n[j],end="")
