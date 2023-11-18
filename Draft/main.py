import pickle
import copy
from copy import deepcopy, copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        new_copy = Person(self.name, self.email, self.phone, self.favorite)
        new_copy.name = copy (self.name)
        new_copy.email = copy (self.email)
        new_copy.phone = copy (self.phone)
        new_copy.favorite = copy (self.favorite)
        return new_copy
        

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.contacts = contacts
        self.filename = filename
        self.count_save = 0
        self.is_unpacking = False
        

    def save_to_file(self):
        with open(self.filename, "wb") as fh:
            pickle.dump(self, fh)
            

    def read_from_file(self):
        with open(self.filename, "rb") as fh:
            unpacked = pickle.load(fh)
        return unpacked

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['fh'] = None
        attributes["count_save"] += 1
        return attributes
    
    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        new_copy = Contacts(self.filename, self.contacts)
        new_copy.contacts = copy (self.contacts)
        new_copy.filename = copy (self.filename)
        new_copy.count_save = copy (self.count_save)
        new_copy.is_unpacking = copy (self.is_unpacking)
        return new_copy
    
    def __deepcopy__(self, memo):
        copy_obj = Contacts(self.filename, self.contacts)
        memo[id(copy_obj)] = copy_obj
        copy_obj.contacts = deepcopy(self.contacts)
        copy_obj.filename = deepcopy(self.filename)
        copy_obj.count_save = deepcopy(self.count_save)
        copy_obj.is_unpacking = deepcopy(self.is_unpacking)
        return copy_obj

        

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True