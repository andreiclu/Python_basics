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
        # opening and sharing of resources
        self.file = open(self.filename, self.mode)
        if self.tipe == "json":
            json.dump(self.content, self.file)
        return self.file

    def __exit__(self, type, value, traceback):
        # cleaning, release of resources
        self.file.close()

class NoInkForPrint(Exception):
  pass


class PyShirt(Tshirt):
    def __init__(self, material, marime, culoare, model):
        super().__init__(material, marime, culoare, model)
        self.print_capacity = 2000

    def plasareComanda(self, comanda):
        with InventoryManager("listaComenzi", "json", comanda, "w"):
            self.orders.append(comanda)

    def imprimareTxt(self, text):
        if len(text) <= 30:
            iterax = re.match("([a-zA-Z0-9_])", text)
            return True
        else:
            return False

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

    @staticmethod
    def send():
        pass

    def updateOrders(self):
        pass