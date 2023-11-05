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
    def check_phone (self, phone):
        try:
            if phone.isnumeric() and len (phone) == 10:
                return phone
            else:
                raise ValueError
        except ValueError:
            print ("The tel. number must be 10 digit length")
            phone = ""
            return phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        check_phone = Phone(self)
        phone = check_phone.check_phone (phone)
        if phone:
            self.phones.append(phone)
    
    def add_phone_simple(self,phone):
            tel = ""
            key = 0
            for char in phone:
                if char.isnumeric():
                    tel += char
                    key = 1
                elif key == 1:
                    self.phones.append(tel)
                    key = 0
                    tel = ""
            self.phones.append(tel)

    def find_phone (self, phone):
        list = []
        list = self.phones
        for value in list:
            if value == phone:
                return phone
        return None
            
    def edit_phone (self, phone_orig, phone_edited):
        list = []
        list = self.phones
        check_phone = Phone(self)
        phone_edited = check_phone.check_phone (phone_edited)
        if phone_edited:
            for value in list:
                try:
                    if value == phone_orig:
                        index = list.index(value)
                        self.phones[index] = phone_edited
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print ("no such phone")

    
    def remove_phone(self, phone_2_remove):
        list = []
        list = self.phones
        found = 0
        try:
            for value in list:
                if value == phone_2_remove:
                    index = list.index(value)
                    self.phones.pop(index)
                    book.add_record(self)
                    found = 1
                    break
            if found == 0:
                raise ValueError
        except ValueError:
                print ("no such phone")

    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):

    # book = {}
    # name = ""
    # addr_phone = ""

    def add_record(self, record):

        name = record.name
        book [name] = record.phones


    def find (self, search_name):
        for name, record in book.data.items():
            if search_name == str(name):
                search_rec = Record (search_name)
                search_rec.phones = record
                return search_rec
        else:
            return None

            
    def delete (self, name):
        try:
            del book[name]
        except KeyError:
            print ("no such name")


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


    # Видалення запису Jane
book.delete("Jane")

for name, record in book.data.items():
    print(name, record)
