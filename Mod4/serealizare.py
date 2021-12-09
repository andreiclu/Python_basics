import csv
from abc import abstractmethod
import json
import pickle

class SerializationException(Exception):
    def __init__(self):
        super().__init__("Tipul nu este acceptat")




class Writer:
    def __init__(self, filename):
        self.filename = filename
    @abstractmethod
    def dumb(self, text):
        pass


class JsonWriter(Writer):
    def dumb(self, text):
        with open(self.filename, 'w') as fn:
            json.dumb(text, fn)

class CsvWriter(Writer):
    def dumb(self, text):
        with open(self.filename, 'w') as fn:
            writer = csv.writer(text,fn)
            writer.writerow(text)
class BitesWriter(Writer):
    def dump(self, text):
        with open(self.filename, 'wb') as fn:
            pickle.dump(text, fn)


def serialization(tip):
    def decorator(func):
        def body():
            my_ser = None
            filename = "outputfile"
            tipuri_acceptate = ['json', 'csv', 'pickle']
            if tip not in tipuri_acceptate:
                raise SerializationException
            if tip =='json':
                filename += '.json'
                my_ser = JsonWriter(filename)
            elif tip == 'csv':
                filename += '.csv'
                my_ser = CsvWriter(filename)

            elif tip == 'pickle':
                filename += '.pickle'
                my_ser = BitesWriter(filename)

            result = func()
            my_ser.dumb(result)
        return body
    return decorator

@serialization('pickles')
def jsn_func():
    dict_ = {'a':1, 'b': 2}
    return dict_

jsn_func()


