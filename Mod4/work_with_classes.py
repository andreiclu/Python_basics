class Human():
    def __init__(self, nume, varsta, nat):
        self.nume = nume
        self.varsta = varsta
        self.nat = nat
    def calc_leafa(self):
        return 0

class Student(Human):
    def __init__(self, nume, varsta, nat,bursa):
        super().__init__(nume, varsta, nat)
        self.bursa = bursa

    def calc_leafa(self):
        return self.bursa

    def varsta(self, varsta):
        if varsta >0:
            self.__varsta = varsta
        else:
            print("Age must be greater than 0")

class StudentAngajat(Student):
    def __init__(self, nume, varsta, nat, bursa, salar):
        super().__init__(nume, varsta, nat, bursa)
        self.salar = salar
    def calc_leafa(self):
        return self.salar + self.bursa





om1 = Human("Ion", 30, "roman")
print(om1.calc_leafa())

student1 = Student("Mircea", 18, "roman", 250)

print(student1.calc_leafa())

none1 = StudentAngajat("Mike", 22, "english", 100, 1040)

print(none1.calc_leafa())

student2 = student1

print(student2.calc_leafa())








