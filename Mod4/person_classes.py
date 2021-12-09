

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): #setter
        return f"{self.name} is {self.age} years old"

class Student(Person):

    def __init__(self, name, age, scholarship):
        Person.__init__(self,name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

    @classmethod
    def create_from_sentence(cls, sentence):
        name, age, scholarship = sentence.split()
        age, scholarship = int(age), float(scholarship)
        if cls.is_name_correct(name):
            return cls(name, age, scholarship)

    @staticmethod
    def is_name_correct(name):
        if name[0].isupper and len(name) > 3:
            return True
        return False

stud1 = Student("Margaret", 32, 0)
stud2 = Student.create_from_sentence("Max 21 600")
print(stud1)
print(stud2)
print(Student.is_name_correct("Alice"))

stud3 = Student("Margareta", 32, 0)



