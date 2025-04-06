class Student:
    def __init__(self):
        self.name = "John"        # Public
        self._age = 20            # Protected
        self.__marks = 90         # Private

    def show(self):
        print("Marks:", self.__marks)

s = Student()
print(s.name)        # Public
print(s._age)        # Protected (can access, but not recommended)
s.show()             # Accessing private via method
