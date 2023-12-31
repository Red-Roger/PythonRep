from collections import UserDict
import datetime


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value  (self, value):
        self._value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
    #def input_name(self):
    #    self.names = []
    #    self.names.append (self.value)
    #    return self.names

class Phone(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance (value, str):
            if value.isnumeric() and len (value) == 10:
                self.__value = value
            else:
                raise  Error (("The tel. number must be 10 digit length"))
        
class Birthday(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, birthday):
        if  birthday:
            try:
                self.__value = datetime.datetime.strptime (birthday, "%Y-%m-%d")
                self.__value = self.__value.date()
            except ValueError:
                self.__value = None
                print (f"Birthday format for {self.name} doesnt't match (YYYY-MM-DD)")


class Error(ValueError):
    def __init__(self, message):
        super().__init__(message)
        self.msg = message

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)


    def add_phone(self,phone):
        new_phone = Phone (phone)
        self.phones.append(new_phone)


    def find_phone (self, phone):
        phone = Phone (phone)
        for value in self.phones:
            if value == phone:
                return value
        return None
            
    def edit_phone (self, phone_to_find, phone_for_replace):
        
        phone = self.find_phone(phone_to_find)
        if phone:
            phone.value = phone_for_replace
        else:
            raise Error ("no such phone")
 
    
    def remove_phone(self, phone):

        phone = self.find_phone(phone)
        if phone:
            self.phones.remove(phone)
        else:
            raise Error ("no such phone")
                
    def days_to_birthday(self):

        if self.birthday:
            today = datetime.date.today()
            user_birth_norm = self.birthday.value.replace (year = today.year)
            if (user_birth_norm - today).days < 0: 
                user_birth_norm = self.birthday.value.replace (year = today.year+1)
            birth_diff = user_birth_norm - today
            return birth_diff.days
        else:
            return f"No valid birthdate for {self.name} to compare"


    def __str__(self):
        line = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        if self.birthday.value:
            line += f"; Birthday: {self.birthday.value}"
        return line
    
    
class AddressBook(UserDict):
    
    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        self.index = 0

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
    
    def __iter__(self):
        return self
    
    
    def __next__(self):
        if self.index < len(self.data):
            start = self.index
            end = min(self.index + self.max_recs, len(self.data))
            result = dict(list(self.data.items())[start:end])
            self.index += self.max_recs
            return result
        else:
            self.index = 0
            raise StopIteration


# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John", "1974-11-25")
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
vv_record = Record("VV", "1974-01-25")
vv_record.add_phone("9874443210")
book.add_record(vv_record)

pp_record = Record("PP")
pp_record.add_phone("9876543111")
book.add_record(pp_record)

print (john_record.days_to_birthday())
print (jane_record.days_to_birthday())

book.iterator(2)

for name, phones in book.data.items():
    print (name, phones)
    
for part in book:
    print(part)