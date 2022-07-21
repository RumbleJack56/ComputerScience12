import sd
from pickle import *

class student:
    def assignrno(self,cls, sec, col):


    def __init__(self,):
        
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
            print(self.data)

    def filerefresh(self):
        with open(self.dirpath,"rb") as f1:
            self.data = load(f1)
            self.totalnum = len(self.data)

    def add(self,info):
        self.data+=[info]
        with open(self.dirpath,'wb') as f1:
            dump(self.data,f1)
        self.filerefresh()


students = Collection('p48.txt')

students.add('Ujjwal')
print(students.data)
        
