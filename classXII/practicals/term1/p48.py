import sd
from pickle import *

class student:
    def __init__(self):
        pass
class Collection:

    def __init__(self,dirpath):
        self.dirpath = dirpath

        def filecheck(location):
            try: a = load(open(location,'rb')); a.close()
            except: a = open(location,'wb') ; dump([],a)
        
        filecheck(dirpath)
        def filerefresh():
            with open(dirpath,"rb") as f1:
                self.data = load(f1)
                self.totalnum = len(self.data)
        filerefresh()

    def add(self,info):
        self.data+=[info]
        with open(self.dirpath,'wb') as f1:
            dump(self.data,f1)


students = Collection('p48.txt')
students.add('Ujjwal')
students.add("Hardik")
print(students.data)
        
