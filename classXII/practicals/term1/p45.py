#14-07-2022
#address locationalistation

#project uses custom class student and allows entry and removal of data from the records


#import of libraries
from codecs import utf_16_decode, utf_16_encode
import sd,pickle

#defining required classes
class Student:
    def __init__(self, name, addm, cls , sec):
        self.name = name
        self.addm = addm
        self.cls = cls
        self.sec = sec
    def __dir__(self):
        output , c = [] , 1
        for val in (self.name, self.addm, self.cls , self.sec):
            output.append(str(c)+str(val))
            c+=1
        return output

#defining useful functions

#Import data: parameters: File name , return list of records
def importData(fname):
    #reads data, if cant read data, then assumes file DNE, and creates file, if creation fails, then assumes empty or corrupt file and writes blank list to file, returns blank, or data
    try:
        with open(fname,"rb") as f1:
            data = pickle.load(f1)
            return data
    except:
        try:
            with open(fname,"xb") as f1:
                pass
        except:
            with open(fname,'wb') as f1:
                pickle.dump(list(),f1)
        return []
        
def updateRecords(data, fname):
    #If write successful, returns true else false
    try:

        with open(fname, "wb") as f1:
            pickle.dump(data,f1)
            return True
    except: return False



#working Output Formats
def dataFormat(data):
    #formats data to present in console
    return ["%-15s|%5s|%5s|%-2s"%tuple([x[1:] for x in dir(k)]) for k in data]


#defining useful global variables
Fn = "p45.txt"



#main code
records = importData(Fn)

count = int(input("Number of Students: "))
for _ in range(count):
    a = Student(input("Name: "),
                int(input("Admission Number: ")),
                int(input("Class: ")),
                input("Section: "))
    records.append(a)



if updateRecords(records,Fn):
    for val in dataFormat(importData(Fn)):
        print(val)