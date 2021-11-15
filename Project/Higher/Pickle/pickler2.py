import pickle
u = 0
with open('Project/Snippets/file.pkl','rb') as dat:
    u = pickle.load(dat)


a = [input("Enter Name: "),input("Enter Username: "),input("Enter Password: ")]
u.append(a)
with open('Project/Snippets/file.pkl','wb') as dat:
    pickle.dump(u,dat)
