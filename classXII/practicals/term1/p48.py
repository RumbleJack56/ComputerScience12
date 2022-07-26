import sd
from pickle import *

<<<<<<< HEAD
# class student:
#     def assignrno(self,cls, sec, col):


<<<<<<< HEAD
#     def __init__(self,):
=======
    def __init__(self):
>>>>>>> 166080a2bc6a89198e6ce26a1dbb69de0e91f650
        
=======
class student:
    def __init__(self, name, cls, per , admno):
        self.name = name
        self.cls = cls
        self.per = per
        self.admno = admno

>>>>>>> 9a9157de152c51104ad258185825705f185d49d5
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
            
        else


                



students = Collection('p48.txt')

<<<<<<< HEAD
students.add('lol')
=======




students.add(student("Ujjwal",12,99.999,1))
>>>>>>> 9a9157de152c51104ad258185825705f185d49d5
print(students.data)
students.remove(rno=1)
