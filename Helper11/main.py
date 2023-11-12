from collections import UserDict
import datetime


class Field:
    def __init__(self, value):
        self.value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value  (self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def input_name(self):
        self.names = []
        self.names.append (self.value)
        return self.names

class Phone(Field):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value.isnumeric() and len (value) == 10:
            self.__value = value
        else:
            self.__value = None
            raise  Error (("The tel. number must be 10 digit length"))

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
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        
        if  birthday:
            try:
                self.__birthday = datetime.datetime.strptime (birthday, "%Y-%m-%d")
                self.__birthday = self.__birthday.date()
            except ValueError:
                self.__birthday = None
                print (f"Birthday format for {self.name} doesnt't match (YYYY-MM-DD)")


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

    
    def remove_phone(self, phone):

        remove_phone = Phone(phone)
        key = 0
        if remove_phone.value:
                for value in self.phones:
                    if value.value == remove_phone.value:
                        index = self.phones.index(value)
                        self.phones.pop (index)
                        key = 1
                        break
                if key == 0:
                    raise Error ("no such phone")
                
    def days_to_birthday(self):
        def __str__(self):
            line = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
            try:
                if self.birthday:
                    line += f"; Birthday: {self.birthday}"
            except AttributeError:
                pass
            return line

        if self.birthday:
            today = datetime.date.today()
            user_birth_norm = self.birthday.replace (year = today.year)
            if (user_birth_norm - today).days < 0: 
                user_birth_norm = self.birthday.replace (year = today.year+1)
            birth_diff = user_birth_norm - today
            return birth_diff.days
        else:
            return f"No valid birthdate for {self.name} to compare"



    def __str__(self):
        line = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        try:
            if self.birthday:
                line += f"; Birthday: {self.birthday}"
        except AttributeError:
            pass
        return line
    
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
    
    def iterator (self, max_recs):
        self.max_recs = max_recs
        index = 0
        for record in book.data.items():
            if index < max_recs:
                yield (record)
                index +=1


# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John", "1974-11-27")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane", "1974-01-25")
jane_record.add_phone("9876543210")
book.add_record(jane_record)


    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")


print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555


    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555


    # Видалення запису Jane
#book.delete("Jane")

print (john_record.days_to_birthday())
print (jane_record.days_to_birthday())

book.iterator(3)
