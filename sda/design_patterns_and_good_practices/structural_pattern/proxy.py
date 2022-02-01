# similar to decorator design pattern
# wrapps functionality

from abc import ABCMeta, abstractmethod
class IPerson(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def person_method():
        """ Ieterface Method"""

class Person(IPerson):

    def person_method(self):
        print("I am a person")

class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy functionality!")
        self.person.person_method()

p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()


