class Singleton:
    # variabila protected
    _instance = None

    def __init__(self, name=''):
        print(f'Instance initialization name: {name}')
        self.name = name


    def __new__(cls, *args, **kwargs):
        # ne aloca memorie pentru o noua instanta
        # ce facem aici, este sa ne asiguram ca alocam memorie pentru instanta noastra, doar o singura data
        # la  instantieri ulterioare, vom returna direct cls._instance care este deja creat
        if cls._instance is None:
            print('Creating a new instance')
            cls._instance = object.__new__(cls)
        print('Returning existing instance')
        return cls._instance


if __name__ == "__main__":
    # putem considera ca obk_1 si obj_2 sunt aliasuri pentru acelasi obiect
    obj_1 = Singleton("obj_1")
    print('obj_1 name: ', obj_1.name)
    obj_2 = Singleton("obj_2")
    print("id of obj_1: ", id(obj_1))
    print("id of obj_2: ", id(obj_2))
    print('obj_1 name: ', obj_1.name)
    print('obj_2 name: ', obj_2.name)


    obj_1 = Singleton("obj_1")
    obj_1.name = "obj_2"