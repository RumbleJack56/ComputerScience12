import pickle
path = 'file.pkl'
users , accPresent= [] , 0

with open(path,'rb') as dat:
    users = pickle.load(dat)

#print(users)

while True:
    accPresent = input("Do you have an account?\n   Press 1 for Yes \n   Press 2 for No\n   ")
    if accPresent in ['1','2']:
        accPresent = int(accPresent)
        break
    else:
        print("Invalid Input, Please Try Again\n\n")

if accPresent == 1:
    user = 0
    uID , pwd , breaker = 0 , 0 , 0
    while True:
        uID = input("Enter Username: ")
        for j in users:
            if j[1] == uID:
                breaker = 1
                break
        else:
            print("Username Not Found, Please try Again \n\n")
        if breaker == 1:
            breaker = 0
            break
    while True:
        pwd = input("Password: ")
        for j in users:
            if j[1] == uID and pwd==j[2]:
                user = j
                breaker = 1
                break
        else:
            print('Incorrect Password, Please try again \n\n')
        if breaker == 1:
            breaker = 0
            break
    print("Hi," , user[0] , "You are now logged in from account",user[1])
if accPresent == 2:
    name = input("Enter Your Name: ")
    username = 0
    while True:
        username = input("\nEnter Username: ")
        for j in users:
            if j[1] == username:
                print("Username Already Taken, Try Again")
                break
        else:
            break
    password = input("Enter Your Password: ")
    user = [name, username,password]
    users.append(user)

    with open(path,'wb') as dat:
        pickle.dump(users,dat)
