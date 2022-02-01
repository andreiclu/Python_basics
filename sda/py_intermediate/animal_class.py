class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Quadrupeds():
    nr_leg = 4 #class attribute
    #encapsulate behavior below/ encapsulation focuses
    #upon the implementation that gives rise to this behavior
    # encapsulation is most often achieved through information hiding,
    # which is the process of hiding all of the secrets of object
    # that do not contribute to its essential characteristics

    def __init__(self, species):
        self.species = species # instance attribute

    def print_nr_legs(self):
        print("I don't have %s legs" % self.nr_legs)


class Dog(Animal, Quadrupeds): #class attributes
    def __init__(self, name, age, species, abilities):
        Animal.__init__(self, name, age)
        Quadrupeds.__init__(self, species)
        self.abilities = abilities

animal = Animal("Spike", 6)
print("Animalul are numele %s si varsta %s" % (animal.name, animal.age))
print(f"Animalul are numele {animal.name} si varsta {animal.age}")

my_dog = Dog('Rex', 12, "Canis familiars", "tail wagging")

print(f"His name is {my_dog.name} age of {my_dog.age}, family of {my_dog.species} and he's good at {my_dog.abilities}")

my_dog.name = 'Petrica'
print(my_dog.name)


#TODO:
# 1.Print my_dog and your_dog age
# 2. Change my_dog age to 2
# 3. is my_dog == your_dog?
# 4. print number of legs for my_dog object

print(my_dog.age)
my_dog.age = 2
print(my_dog.age)

your_dog = Dog("Rex", 11, "Canis familiars", "barking")

if my_dog == your_dog:
    print(True)
else: print(False)



print(f"My dog will have the number of legs we declare as a class attribute, that would be: {my_dog.nr_leg}")

#________________________________________________________________


