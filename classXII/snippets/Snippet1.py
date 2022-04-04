class Teacher:
    retired = False
    
    def __init__(self, subject=None, age=None , designation=None):
        self.subject = subject
        self.age = age
        self.designation = designation

rajni = Teacher("science",33,"idiot")
shyamal = Teacher("Maths", 912, "Voldemort")
gurjeet_maam = Teacher("CS" , 34 , "PGT")

for x in dir():
    y = eval(x)
    if type(y) == type(Teacher()):
        print("Teacher is",x,"who is a",y.subject,"teacher and is aged",y.age,".",
        
        "Their designation is",y.designation,".")

