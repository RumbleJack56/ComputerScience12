#25/7/22

import sd
from pickle import *

class student:
    def __init__(self, name, cls, per , admno):
        self.name = name
        self.cls = cls
        self.per = per
        self.admno = admno

class Collection:
    def __init__(self,dirpath):
        self.dirpath = dirpath


        def filecheck(location):
            try: a = load(open(location,'rb'))
            except: a = open(location,'wb') ; dump([],a) ; print("Exception occurs")
        filecheck(dirpath)


        #basis filerefresh
        with open(dirpath,"rb") as f1:
            self.data = load(f1)
            self.totalnum = len(self.data)

    def filerefresh(self):
        with open(self.dirpath,"rb") as f1:
            self.data = load(f1)
            self.totalnum = len(self.data)

    def add(self,info):
        self.data+=[info]
        with open(self.dirpath,'wb') as f1:
            dump(self.data,f1)
        self.filerefresh()

    def remove(self,name = "", admno = ""):
        if name == "" and admno=="":
            return False
        elif name == "":
            for k in self.data:
                if k.amdno == admno:
                    self.data.remove(k)
        else:
            for k in self.data:
                if k.name == name:
                    self.data.remove(k)
        with open(self.dirpath,'wb') as f1:
            dump(self.data,f1)
    def edit(self, admno):
        if admno in [k.admno for k in self.data]:
            k.name,k.cls,k.per = input("Enter Name: "), input("Enter Class: "),input("Enter Percentage: ")
            return True
        else:
            return False
    


students = Collection('p48.txt')


students.add(student("Ujjwal",12,99.999,1))
print(students.data)
students.remove(rno=1)
