class Dog:
    species = "Canis Familiaris"
    alive = True
    
    def __init__(self, breed, age, hair):
        self.breed , self.age , self.hair = breed , age , hair
    def birthday(self):
        self.age+=1
        return str(self.age-1)+" to "+str(self.age)
    def died(self):
        self.alive = False
    def temper(self, temp):
        self.temper = temp



tommy = Dog("German Shepherd",8,"furry")
rocky = Dog("Pug" , 4 , "smooth")

tommy.temper("angry")


print(tommy.temper)

print(tommy.age)
tommy.birthday()
print(tommy.age)

print(rocky.age)
print(rocky.alive)
rocky.birthday()
print(rocky.age)
rocky.died()
print(rocky.alive)



