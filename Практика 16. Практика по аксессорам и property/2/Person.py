class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def fullname(self):
        return f"{self._name} {self._surname}"

    @fullname.setter
    def fullname(self, value):
        self._name, self._surname = value.split()




person = Person('Mike', 'Pondsmith')
print(person.name)
print(person.surname)
print(person.fullname)

person.name = 'Troy'
print(person.fullname)

person.surname = 'Baker'
print(person.fullname)

person.fullname = 'John Doe'
print(person.name)
print(person.surname)
