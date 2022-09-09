"""
In object-oriented programming, the open–closed principle states "software entities
(classes, modules, functions, etc.) should be open for extension, but closed for modification";
that is, such an entity can allow its behaviour to be extended without modifying its source code.
"""

from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage(ABC):
    @abstractmethod
    def save(self, human):
        pass


class PersonDB(PersonStorage):
    def save(self, human):
        print(f'Save the {human} to database')


class PersonJSON(PersonStorage):
    def save(self, human):
        print(f'Save the {human} to a JSON file')


class PersonXML(PersonStorage):
    def save(self, human):
        print(f'Save the {human} to a XML file')


if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonXML()
    storage.save(person)
    storage = PersonJSON()
    storage.save(person)
    storage = PersonDB()
    storage.save(person)
