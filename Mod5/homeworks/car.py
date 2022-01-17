"""
Create a car class which has as members:
- brand
- model
- year
a)	Implement __str__() method to show its brand, model, and year and print this information to the console
b)	Adapt bubble sort, and merge sort algorithms class to sort a list of car objects by year.
c)	Use Python built in method to sort these objects by model alphabetically (tip: use "key" parameter in built in sorted() method to achieve that).
d)	Create a child class called NewCar. Use sorted() method directly to sort our list of objects by year and then by brand alphabetically
without the “key” parameter (tip: implement methods __eq__ __gt__ and __ls__ in class NewCar to achieve that. Also, implement those methods in such a way so you can easily switch between comparing by year to comparing by brand).


"""





from operator import attrgetter

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return str.format("Make: {}, Model: {}, Year: {}", self.make, self.model, self.year)

    def __lt__(self, other):
        return (self.make, self.model, self.year) < (other.make, other.model, other.year)
    def __gt__(self, other):
        return (self.make, self.model, self.year) > (other.make, other.model, other.year)
    def __eq__(self, other):
        return (self.make, self.model, self.year) == (other.make, other.model, other.year)





def merge(car_list, left_index, right_index, mid, compare_func):
    left_copy = car_list[left_index:mid + 1]
    right_copy = car_list[mid + 1:right_index + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # We use the comparison_function instead of a simple comparison operator, method without magic methods
        if compare_func(left_copy[left_copy_index], right_copy[right_copy_index]):
            car_list[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
        else:
            car_list[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1


        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        car_list[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        car_list[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_sort(car_list, left_index, right_index, comparison_function):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(car_list, left_index, middle, comparison_function)
    merge_sort(car_list, middle + 1, right_index, comparison_function)
    merge(car_list, left_index, right_index, middle, comparison_function)

def bubble_sort(car_list, comp_func):
    n = len(car_list)
    for i in range(0,n-1):
        for j in range(0, n-1):
            if comp_func(car_list[j], car_list[j + 1]):
                aux = car_list[j]
                car_list[j] = car_list[j + 1]
                car_list[j + 1] = aux
    return car_list




car1 = Car("Alfa Romeo", "33 SportWagon", 1988)
car2 = Car("Chevrolet", "Cruze Hatchback", 2011)
car3 = Car("Corvette", "C6 Couple", 2004)
car4 = Car("Lincoln", "Navigator SUV", 2015)
car5 = Car("Cadillac", "Seville Sedan", 1995)
car_array = [car1, car2, car3, car4, car5]

merge_sort(car_array, 0, len(car_array)-1, lambda car1,car2: car1.year > car2.year) #Method without magic methods xD


print("Cars sorted by year with merge sort: ")
for car in car_array:
    print(car)
print("_____________________________")
print("Car sorted by year with bubble sort: ")

sorted_car_array = bubble_sort(car_array, lambda car1,car2: car1.year > car2.year)
for item in sorted_car_array:
    print(str(item))
print("__________________________")

sorted_by_method = sorted(car_array,key= attrgetter('make'))



print(f"This one is sorted by sorted method : {sorted_by_method}")


class NewCar(Car):
    def __lt__(self, other):
        return (self.year, self.make) < (other.year, other.make)
    def __gt__(self, other):
        return (self.year, self.make) > (other.year, other.make)
    def __eq__(self, other):
        return (self.year, self.make) == (other.year, other.make)


car1 = NewCar("Alfa Romeo", "33 SportWagon", 1988)
car2 = NewCar("Chevrolet", "Cruze Hatchback", 2011)
car3 = NewCar("Corvette", "C6 Couple", 2004)
car4 = NewCar("Lincoln", "Navigator SUV", 2015)
car5 = NewCar("Cadillac", "Seville Sedan", 1995)
car6 = NewCar("Boalfa Romeo", "33 SportWagon", 1988)
car_array = [car1,car2, car3, car4, car5, car6]

print(sorted(car_array))
