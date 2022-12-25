import re
import sys
from collections import UserDict
from datetime import datetime, date


class Field():
    def __init__(self) -> None:
        pass


class Name(Field):
    def __init__(self) -> None:
        Field.__init__(self)
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if (new_value != None) and (new_value != ""):
            self.__value = new_value
        else:
            print("Enter value!")


class Phone(Field):
    def __init__(self, value) -> None:
        Field.__init__(self)
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        result = re.find(
            r"[+380]?[(]?[0-9]{2}[)]?[0-9]{3}[-][0-9]{1,2}[-][0-9]{2,3}\b", new_value)
        if result != -1:
            return result
        else:
            print("This is not a phone!")


class Birthday(Field):
    def __init__(self, value):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if (type(new_value) == datetime) or (type(new_value) == date):
            self.value = new_value
        elif type(new_value) == str:
            try:
                if "-" in new_value:
                    d_list = new_value.split("-")
                elif "/" in new_value:
                    d_list = new_value.split("/")
                elif "." in new_value:
                    d_list = new_value.split(".")
                if len(d_list[0]) == 4:
                    self.value = datetime(
                        year=int(d_list[0]), month=int(d_list[1]), day=int(d_list[2]))
                else:
                    self.value = datetime(
                        year=int(d_list[-1]), month=int(d_list[-2]), day=int(d_list[-3]))
            except:
                print("This is not a date!")


class Record():
    def __init__(self, name: Name, phone, data: Birthday = None) -> None:
        self.name = name
        self.data = data
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
        self.current_page = 0
        self.on_pages = 50

    def __next__(self):
        max_page = len(self.data)/50
        if self.current_page <= max_page:
            self.current_page +=
            return  # генератор!!!
        raise StopIteration

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


class AddressBookPage:
    def __iter__(self):
        return AddressBook()


class User():
    def __init__(self):
        pass

    def command_hello(self):
        """Функція привітання"""
        print("How can I help you?")

    def command_exit(self):
        """Функція виходу"""
        sys.exit("Good bye!")
