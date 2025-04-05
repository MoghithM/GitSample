class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
a=Animal("Generic Animal") #init method

d=Dog("Buddy")

#Accessing attributes and methods
print(a.name) #Output: Genric Animal
print(d.name) #Output:Buddy
print(d.sound()) #output"Woof!     