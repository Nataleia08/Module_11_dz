import sys
from collections import UserDict
from datetime import datetime, date


class Field():
    def __init__(self) -> None:
        pass


class Name(Field):
    def __init__(self, value: str) -> None:
        Field.__init__(self)
        self.value = value


class Phone(Field):
    def __init__(self, value: str) -> None:
        Field.__init__(self)
        self.value = value


class Birthday():
    def __init__(self, value):
        self.value = datetime(value)


class Record():
    def __init__(self, name, phone, data=None) -> None:
        if type(name) == Name:
            self.name = name
        else:
            self.name = Name(str(name))
        self.phone = []
        if type(phone) == Phone:
            self.phone.append(phone)
        elif type(phone) == str:
            p_list = phone.strip().split(" ")
            for p in p_list:
                self.phone.append(Phone(p))
        elif type(phone) == list:
            for p in phone:
                self.phone.append(Phone(p))
        else:
            self.phone.append(Phone(str(phone)))
        if type(data) == Birthday:
            self.data = data
        else:
            self.data = Birthday(data)

    def add_phone(self, phone_new):
        self.phone.append(Phone(phone_new))

    def change_phone(self, phone_new):
        self.phone.extend(Phone(phone_new))

    def delete_phone(self, phone_new):
        try:
            self.phone.remove(Phone(phone_new))
        except:
            print("This phone not found!")

    def days_to_birthday(self):
        if self.data == None:
            print("Birthday not entering!")
            return None
        else:
            now_day = datetime.now().date()
            self.data.value.year = 2023
            days_count = now_day - self.data.value
            return days_count


class AddressBook(UserDict):
    def __init__(self) -> None:
        UserDict.__init__(self)

    def __setitem__(self, name: str, phone) -> None:
        self.data[name] = Record(name, phone)

    def add_record(self, record: Record):
        """Функція додання запису"""
        key = str(record.name.value)
        if (key == "") or (len(record.phone) == 0):
            print("Give me name and phone please!")
            return None
        try:
            self.data[key] = record
            print("Contact save fine!")
        except:
            print("Error!")

    def change_record(self, record: Record):
        """Функція зміни запису"""
        key = str(record.name.value)
        if (key == "") or (len(record.phone) == 0):
            print("Give me name and phone please!")
            return None
        try:
            self.data[key] = record
            print("Contact save fine!")
        except:
            print("There is no user with this name!")

    def search_phone(self, name):
        """Функція пошуку телефону за ім'ям"""
        if (name == ""):
            print("Give me name please!")
            return None
        try:
            result = []
            for p in self.data[name].phone:
                result.append(str(p.value))
            print(" ".join(result))
        except:
            print("There is no user with this name!")

    def show_all(self):
        """Функція відображення списку контактів"""
        try:
            result = []
            for key_name in self.data.keys():
                k = key_name.title()
                result.append(k)
                phone_l = self.data[key_name].phone
                for i in phone_l:
                    result.append(str(i.value))
                result.append("\n")
            print(" ".join(result))
        except Exception as e:
            print("Error!", e.args)


class User():
    def __init__(self):
        pass

    def command_hello(self):
        """Функція привітання"""
        print("How can I help you?")

    def command_exit(self):
        """Функція виходу"""
        sys.exit("Good bye!")
