class Cook:
    '''
    Director - manages the creation of the object
    '''
    def __init__(self):
        self._builder = None

    def prepare(self, builder):
        self._builder = builder
        self._builder.prepare_dough()
        self._builder.add_extras()
        self._builder.bake()

class PizzaBuilder:
    '''
    Builder - abstract interface for creating target objects
    '''
    def __init__(self):
        self.pizza = Pizza()

    def prepare_dough(self): pass

    def add_extras(self): pass

    def bake(self): pass

class MargeritaBuilder(PizzaBuilder):
    '''
    ConcreteBuilder - a specific builder that creates and combines the components of the created object
    '''
    def prepare_dough(self): pass

    def add_extras(self): pass

    def bake(self): pass

class PepperoniBuilder(PizzaBuilder):
    def prepare_dough(self): pass

    def add_extras(self): pass

    def bake(self): pass

class Pizza:
    '''
    the generated complex object
    '''
    pass

def main():
    cook = Cook()
    # we choose a builder
    baking = PepperoniBuilder()
    cook.prepare(baking)
    pizza = baking.pizza

