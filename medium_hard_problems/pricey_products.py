"""
You will be given a dictionary with various products and their respective prices. Return a list of the products with a minimum price of 500 in descending order.

Examples
pricey_prod({"Computer" : 600, "TV" : 800, "Radio" : 50}) ➞ ["TV", "Computer"]

pricey_prod({"Bike1" : 510, "Bike2" : 401, "Bike3" : 501}) ➞ ["Bike1", "Bike3"]

pricey_prod({"Loafers" : 50, "Vans" : 10, "Crocs" : 20}) ➞ []
"""

def pricey_prod(dict_):
    sorted_dict = sorted(dict_.items(), key=lambda x:x[1], reverse=True)
    lst = []
    for item in sorted_dict:
        if item[1] < 500:
            return lst
        else:
            lst.append(item[0])

    return lst

print(pricey_prod({"Computer" : 600, "TV" : 800, "Radio" : 50}))

print(pricey_prod({"Bike1" : 510, "Bike2" : 401, "Bike3" : 501}))


print(pricey_prod({"Loafers" : 50, "Vans" : 10, "Crocs" : 20}))