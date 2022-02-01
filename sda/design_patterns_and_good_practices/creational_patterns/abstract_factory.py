class Car:
    def get_type(self):
        pass

    def get_model_name(self):
        pass

    def get_cylinders_num(self):
        pass

    def get_producer(self):
        pass

    def get_engine_volume(self):
        pass

    def get_trunk_size(self):
        pass

class AbstractCar(Car):
    def __str__(self):
        return (
            f"Car: {self.get_producer()} {self.get_model_name()} {self.get_type()} has {self.get_cylinders_num()} "
            f"cylinders and engine {self.get_engine_volume()} and trunk size {self.get_trunk_size()} litres")

class ToyotaCorolla(AbstractCar):
    def get_model_name(self):
        return "Corolla"

    def get_producer(self):
        return "Toyota"

class ToyotaCorollaWagon(ToyotaCorolla):
    def get_type(self):
        return "Wagon"

    def get_cylinders_num(self):
        return 4

    def get_engine_volume(self):
        return 1.6

    def get_trunk_size(self):
        return 540

class ToyotaCorollaHatchback(ToyotaCorolla):
    def get_type(self):
        return "Hatchback"

    def get_cylinders_num(self):
        return 4

    def get_engine_volume(self):
        return 2.0

    def get_trunk_size(self):
        return 350

class ToyotaCorollaSedan(ToyotaCorolla):
    def get_type(self):
        return "Sedan"

    def get_cylinders_num(self):
        return 4

    def get_engine_volume(self):
        return 1.8

    def get_trunk_size(self):
        return 420

class AudiA4(AbstractCar):
    def get_model_name(self):
        return "A4"

    def get_producer(self):
        return "Audi"

class AudiA4Wagon(AudiA4):
    def get_type(self):
        return "Wagon"

    def get_cylinders_num(self):
        return 4

    def get_engine_volume(self):
        return 1.8

    def get_trunk_size(self):
        return 520

class AudiA4Hatchback(AudiA4):
    def get_type(self):
        return "Hatchback"

    def get_cylinders_num(self):
        return 6

    def get_engine_volume(self):
        return 2.4

    def get_trunk_size(self):
        return 300

class AudiA4Sedan(AudiA4):
    def get_type(self):
        return "Sedan"

    def get_cylinders_num(self):
        return 4

    def get_engine_volume(self):
        return 2.0

    def get_trunk_size(self):
        return 450

class CarFactory:
    def create_Wagon(self):
        pass

    def create_hatchback(self):
        pass

    def create_sedan(self):
        pass

class ToyotaCorollaFactory(CarFactory):
    def create_Wagon(self):
        return ToyotaCorollaWagon()

    def create_hatchback(self):
        return ToyotaCorollaHatchback()

    def create_sedan(self):
        return ToyotaCorollaSedan()

class AudiA4Factory(CarFactory):
    def create_Wagon(self):
        return AudiA4Wagon()

    def create_hatchback(self):
        return AudiA4Hatchback()

    def create_sedan(self):
        return AudiA4Sedan()

class FactoryProvider:
    @staticmethod
    def create_factory(factory_type):
        if factory_type == 'T':
            return ToyotaCorollaFactory()
        elif factory_type == 'A':
            return AudiA4Factory()
        else:
            return None

def main():
    factory_type = input('What car do you want to produce - choose A or T: ')
    factory = FactoryProvider.create_factory(factory_type)

    if factory:
        hatchback = factory.create_hatchback()
        print(hatchback)


if __name__ == '__main__':
    main()