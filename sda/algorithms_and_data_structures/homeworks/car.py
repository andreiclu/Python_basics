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
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return str.format("Brand: {}, Model: {}, Year: {}", self.brand, self.model, self.year)



def merge_sort(car_list, left_index, right_index, comparison_function):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(car_list, left_index, middle, comparison_function)
    merge_sort(car_list, middle + 1, right_index, comparison_function)
    merge(car_list, left_index, right_index, middle, comparison_function)



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

sorted_by_method = sorted(car_array,key= attrgetter('brand'))
print("This one is sorted with lambda function: ")

sorted_by_lamnda = sorted(car_array, key=lambda x: x.brand)
print(sorted_by_lamnda)
print("____________________________________")



print(f"This one is sorted by sorted method : {sorted_by_method}")


class NewCar(Car):
    sort_by = 'year'
    def __init__(self, brand, model, year):
        super().__init__(brand,model,year)





    def __lt__(self, other):
        if self.sort_by == 'year':
            return self.year < other.year
        else:
            return self.model < other.model
    def __gt__(self, other):
        if self.sort_by == 'year':
            return self.year > other.year
        else:
            return self.model > other.model
    def __eq__(self, other):
        if self.sort_by == 'year':
            return self.year == other.year
        else:
            return self.model == other.model



child_car1 = NewCar("Skoda", "Octavia", 2015)
child_car2 = NewCar("Lancia", "Musa", 2011)
child_car3 = NewCar("Kia", "Cee’d", 2013)
child_array = [child_car1, child_car2, child_car3]
print("___________________________")
print("This list of objects is sorted by year:")
print(sorted(child_array))

print("This list of objects is sorted by model: ")
NewCar.sort_by = 'model'
print(sorted(child_array))





