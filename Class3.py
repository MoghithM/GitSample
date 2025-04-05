class Dog:
    species= "Canine"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old" #Correcyt: Returning a string
    
dog1=Dog("Buddy", 3)
dog2=Dog("Charlie", 5)

print(dog1.species) #_str_
print(dog2.name) 
print(dog2.name)

dog1.name="Max"
print(dog1.name)