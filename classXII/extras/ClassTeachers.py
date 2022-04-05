class Teacher:
    retired = False
    classes = []
    alive = True
    def __init__(self, subject=None, age=None , designation=None):
        self.subject = subject
        self.age = age
        self.designation = designation

    def giveClass(self,newClass,section):
        self.classes.append([newClass,section])

    def birthday(self, dd, mm, yyyy):
        self.birthDate = str(dd)+" / "+str(mm)+" / "+str(yyyy)
        self.age+=1

    def murdered(self):
        self.alive = False






rajni = Teacher("science",420,"idiot")
shyamal = Teacher("Maths", 912, "Voldemort")
gurjeet_maam = Teacher("CS" , 34 , "PGT")





rajni.giveClass(10,'F')
rajni.giveClass(9,'B')
print(rajni.classes)

rajni.birthday(11, 9 , 1675)
print(rajni.birthDate)



print("Rajni is Alive, True/False")
print(rajni.alive)
rajni.murdered()
print("Rajni is Alive, True/False")
print(rajni.alive)


for x in dir():
    y = eval(x)
    if type(y) == type(Teacher()):
        print("Teacher is",x,"who is a",y.subject,"teacher and is aged",y.age,".",
        
        "Their designation is",y.designation,".")