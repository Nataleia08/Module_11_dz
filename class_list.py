import sys
from collections import UserDict


class Field():
    def __init__(self) -> None:
        pass


class Name(Field):
    def __init__(self, name) -> None:
        Field.__init__(self)
        self.name = name


class Phone(Field):
    def __init__(self, phone) -> None:
        Field.__init__(self)
        self.phone = phone


class Record():
    def __init__(self, name, phone) -> None:
        self.name = Name(name)
        self.phone = []
        if type(phone) == str:
            self.phone.append(Phone(phone))
        elif type(phone) == list:
            for p in phone:
                self.phone.append(Phone(p))
        else:
            self.phone.append(Phone(str(phone)))

    def add_phone(self, phone_new):
        self.phone.append(Phone(phone_new))

    def change_phone(self, phone_new):
        self.phone.extend(Phone(phone_new))

    def delete_phone(self, phone_new):
        try:
            self.phone.remove(Phone(phone_new))
        except:
            print("This phone not found!")


class AddressBook(UserDict):
    def __init__(self) -> None:
        UserDict.__init__(self)

    def __setitem__(self, name, phone) -> None:
        self.data[name] = Record(name, phone)

    def add_record(self, name, phone):
        """Функція додання запису"""
        if (name == "") or (phone == ""):
            print("Give me name and phone please!")
            return None
        try:
            self.data[name] = Record(name, phone)
            print("Contact save fine!")
        except:
            print("Error!")

    def change_record(self, name, phone):
        """Функція зміни запису"""
        if (name == "") or (phone == ""):
            print("Give me name and phone please!")
            return None
        try:
            self.data[name].phone.clear()
            self.data[name].phone.append(Phone(phone))
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
            for p in self.data.get(name).phone:
                result.append(p.phone)
            print(" ".join(result))
        except:
            print("There is no user with this name!")

    def show_all(self):
        """Функція відображення списку контактів"""
        try:
            result = []
            for key_name in self.data.keys():
                result.append(key_name.title())
                phone_l = self.data.get(key_name).phone
                for i in phone_l:
                    result.append(i.phone)
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
