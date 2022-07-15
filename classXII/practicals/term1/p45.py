#14-07-2022
#address locationalistation
import sd,pickle

def importData(fname):
    try:
        open(fname,'xb')
        a = open(fname,'wb')
        pickle.dump([],a)
        a.close()
    except: pass

    with open(fname,"rb") as f1:
        data = pickle.load(f1)
        return data

def updateRecords(records, fname):



class Student:
    def __init__(self, name, addm, cls , sec):
        self.name = name
        self.addm = addm
        self.cls = cls
        self.sec = sec

a = Student("Ujjwal Kakar", 1, 12,"F")


records = importData('p45.txt')
records.append(a)
