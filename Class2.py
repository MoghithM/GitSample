class Dog:
    species ="Canine" #Class attribute
    def __init__(self,name,age):
        self.name = name #Instance attribute
        self.age = age #Instance attribute
        
        #Creating an object of the Dog class
dog1=Dog()
dog1=Dog("Buddy", 3)
print(dog1.name) #Output: Buddy
print(dog1.species) #Output: Canine
        
        #Self parameter is a reference to the current instance of the class
        #It allows us to accress the attributes and methods of the object