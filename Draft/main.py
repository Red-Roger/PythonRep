from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def input_name(self):
        self.names = []
        self.names.append (self.value)
        return self.names

class Phone(Field):
    def __init__(self, value):
        
        self.checked = value
        self.check()

    def check(self):
        if self.checked.isnumeric() and len (self.checked) == 10:
            self.value = self.checked
            return self
        else:
            self.value = None
            raise  Error (("The tel. number must be 10 digit length"))

            
class Error(ValueError):
    def __init__(self, message):
        super().__init__(message)
        self.msg = message

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        new_phone = Phone (phone)
        if new_phone.value:
            self.phones.append(new_phone)

    def find_phone (self, phone):
        
        for value in self.phones:
            if value.value == phone:
                return value
        return None
            
    def edit_phone (self, phone_orig, phone_edited):
        
        phone_orig = Phone(phone_orig)
        phone_edited = Phone(phone_edited)
        key = 0
        if phone_orig.value and phone_edited.value:
                for value in self.phones:
                    if value.value == phone_orig.value:
                        index = self.phones.index(value)
                        self.phones[index] = phone_edited
                        key = 1
                        break
                if key == 0:
                    raise Error ("no such phone")

    
    def remove_phone(self, phone_2_remove):
        list = []
        list = self.phones
        found = 0
        for value in list:
            if value == phone_2_remove:
                index = list.index(value)
                self.phones.pop(index)
                found = 1
                break
        if found == 0:
            raise ValueError ("no such phone")

    
    def __str__(self):
       return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):


    def add_record(self, record):

        self.data [record.name.value] = record


    def find (self, search_name):
        for name, record in self.data.items():
            if search_name == name:
                return record

            
    def delete (self, search_name):
        for name in self.data.keys():
            if search_name == str(name):
                del self.data[name]
                break


# Створення нової адресної книги
book = AddressBook()


    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)


    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")


print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555


    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555



    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(name, record)

    # Видалення запису Jane
book.delete("Jane")



