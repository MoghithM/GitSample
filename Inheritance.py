#Single Inheritance

class Parent:
    def display(self):
        print("This is the parent class")

class Child(Parent):
    def show(self):
        print("This is the child class")

c = Child()
c.display()
c.show()


#Multiple Inheritance

class Father:
    def father_msg(self):
        print("This is the father")

class Mother:
    def mother_msg(self):
        print("This is the mother")

class Kid(Father, Mother):
    def kid_msg(self):
        print("This is the kid")

k = Kid()
k.father_msg()
k.mother_msg()
k.kid_msg()

#Multilevel Inheritance

class Grandparent:
    def grand_msg(self):
        print("This is the grandparent")

class Parent(Grandparent):
    def parent_msg(self):
        print("This is the parent")

class Child(Parent):
    def child_msg(self):
        print("This is the child")

c = Child()
c.grand_msg()
c.parent_msg()
c.child_msg()

#Hierarchical Inheritance

class Animal:
    def speak(self):
        print("Animals make sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.speak()
d.bark()
c.speak()
c.meow()

#Hybrid Inheritance

class A:
    def msg_a(self):
        print("Class A")

class B(A):
    def msg_b(self):
        print("Class B")

class C:
    def msg_c(self):
        print("Class C")

class D(B, C):  # Inherits from B (which inherits A) and C
    def msg_d(self):
        print("Class D")

d = D()
d.msg_a()
d.msg_b()
d.msg_c()
d.msg_d()
