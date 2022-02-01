class Student:
    def __init__(self):
        print('Student class constructor called')

    def get_full_name(self):
        pass

    def get_contact_details(self):
        pass

    def is_adult(self):
        pass

    def get_results(self):
        pass


class Favorite:
    def __init__(self, first_name, last_name, email, age, grades):
        print('Favorite class constructor called')
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._age = age
        self._grades = grades

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_age(self):
        return self._age

    def get_grades(self):
        return self._grades

class FavoriteAdapter(Favorite, Student):
    def __init__(self, first_name, last_name, email, age, grades):
        super().__init__( first_name, last_name, email, age, grades)
        # Student.__init__(self)

    def get_full_name(self):
        return self.get_first_name() + " " + self.get_last_name()

    def get_contact_details(self):
        return self.get_email()

    def is_adult(self):
        return self.get_age() >= 18

    def get_results(self):
        return self.get_grades()

def main():
    students = [FavoriteAdapter('Steven', 'Morgan', 'sm@gmail.com', 19, [3, 4, 5]),
                FavoriteAdapter('Maria', 'Smith', 'mk@hotmail.com', 17, [4, 5, 4]),
                FavoriteAdapter('Joanna', 'Noris', 'jn@yahoo.com', 21, [2, 4, 6])]

    for s in students:
        print(f"{'Adult' if s.is_adult() else 'Child'} {s.get_full_name()} [{s.get_contact_details()}]: {s.get_results()}")


if __name__ == '__main__':
    main()



