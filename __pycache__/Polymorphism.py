class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

# Common interface
def animal_sound(animal):
    animal.sound()

# Create objects
d = Dog()
c = Cat()

animal_sound(d)
animal_sound(c)
