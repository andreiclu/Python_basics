from abc import ABC, abstractmethod
import re
import json


class Tshirt:
    def __init__(self, material, marime, culoare, model):
        self.material = material
        self.marime = marime
        self.culoare = culoare
        self.model = model
        self.orders = []

    @abstractmethod
    def plasareComanda(self, comanda):
        pass

    @abstractmethod
    def imprimareTxt(self, text):
        pass

    @abstractmethod
    def imprimareModel(self, model):
        pass

    @abstractmethod
    def getRaport(self):
        pass

    @staticmethod
    def send():
        pass

    @abstractmethod
    def updateOrders(self):
        pass


class InventoryManager:
    def __init__(self, filename, tipe, content, mode):
        self.filename = filename
        self.tipe = tipe
        self.content = content
        self.mode = mode
        self.file = None

    def __enter__(self):
        extendetfilename = self.filename + "." + self.tipe
        self.file = open(extendetfilename, self.mode)
        if self.tipe == "json":
            json.dump(self.content, self.file)

    def __exit__(self, type, value, traceback):
        self.file.close()

from datetime import date

today = date.today()
print("Today's date:", today)

class NoInkForPrint(Exception):
  pass

def birthday(data_cand_e_nascut):
    def dec(func):
        def wrapper(*args, **kwargs):
            print("Hai sa vedem daca e ziua cuiva")
            if data_cand_e_nascut == date.today():
                func(*args, **kwargs)
        return wrapper
    return dec


class PyShirt(Tshirt):
    def __init__(self, material, marime, culoare, model):
        super().__init__(material, marime, culoare, model)
        self.print_capacity = 2000

    def imprimareTxt(self, text):
        pattern = r'^Python[6-9]{1}[0-9]{4}'
        if re.search(pattern, text):
            self.print_capacity -= len(text)
            print("S-a printat tricoul cu textul %s " % text)
        else:
            print("Textul %s nu este corespunzator" % text)

    def imprimareModel(self, model):
        self.model = model
        modell = len(self.model)
        if modell < self.print_capacity:
            self.print_capacity -= modell
            print(f"S-a printat: {model}")
        else:
            raise NoInkForPrint()
        print(f"Capacitatea de printare este: {self.print_capacity}")

    def getRaport(self):
        for order in self.orders:
            print(order)

    def addOrder(self, order):
        with InventoryManager("listaComenzi", "json", order, "w"):
            self.orders.append(order)

    @staticmethod
    def send():
        pass


tricou1 = PyShirt("bumbac",42,"rosu","tricou")
model = 'carouri'
model2 = model*2

# test imprimareModel
tricou1.imprimareModel(model)
tricou1.imprimareModel(model2)

#test ridica excp
try:
  tricou1.imprimareModel("A"*1980)
except NoInkForPrint as e:
  print("Imprimanta a ramas fara tus, schimba tonnerul")

#testimprimareTxt
tricou1.imprimareTxt("mytextadsasdadsada")
tricou1.imprimareTxt("Python12")
tricou1.imprimareTxt("Python60000")
