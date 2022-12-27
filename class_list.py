import re
import sys
from collections import UserDict
from datetime import datetime, date, timedelta


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
    def __init__(self) -> None:
        Field.__init__(self)
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value: str):
        try:
            result = re.search(
                r"[+380]?[(]?[0-9]{2}[)]?[0-9]{3}[-]?[0-9]{1,2}[-]?[0-9]{2,3}\b", new_value).string
            if result != None:
                self.__value = str(result)
            else:
                print("This is not a phone!")
        except ValueError as e:
            print(e.error)


class Birthday(Field):
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if (type(new_value) == datetime) or (type(new_value) == date):
            self.__value = new_value
        elif type(new_value) == str:
            try:
                if "-" in new_value:
                    d_list = new_value.split("-")
                elif "/" in new_value:
                    d_list = new_value.split("/")
                elif "." in new_value:
                    d_list = new_value.split(".")
                if len(d_list[0]) == 4:
                    self.__value = datetime(
                        year=int(d_list[0]), month=int(d_list[1]), day=int(d_list[2]))
                else:
                    self.__value = datetime(
                        year=int(d_list[-1]), month=int(d_list[-2]), day=int(d_list[-3]))
            except:
                print("This is not a date! Date not save!")


class Record():
    def __init__(self, name: Name, phone, date: Birthday = None) -> None:
        self.name = name
        self.date = date
        self.phone = phone

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
        if self.date == None:
            print("Birthday not entering!")
            return None
        else:
            now_day = datetime.now().date()
            birthday_now = datetime(
                year=2023, month=self.date.value.month, day=self.date.value.day).date()
            days_count = birthday_now - now_day
            if days_count.days > 365:
                days_count = days_count - timedelta(days=365)
            return days_count


class AddressBook(UserDict):
    def __init__(self) -> None:
        UserDict.__init__(self)
        self.current_page = 1
        self.on_pages = 5
        self.number_record = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (len(self.data) % self.on_pages) == 0:
            max_page = int(len(self.data)/self.on_pages)
        else:
            max_page = int(len(self.data)//self.on_pages + 1)
        try:
            result = []
            for key_name in self.data.keys():
                k = key_name.title()
                result.append(k)
                self.number_record += 1
                phone_l = self.data[key_name].phone
                for i in phone_l:
                    result.append(str(i.value))
                result.append("\n")
                if self.current_page*self.on_pages >= self.number_record:
                    yield (" ".join(result))
            if self.current_page <= max_page:
                self.current_page += 1
            else:
                self.current_page = 1
        except Exception as e:
            print("Error!", e.args)
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

    def search_phone(self, name) -> str:
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

    def show_all(self) -> str:
        """Функція відображення списку контактів"""
        try:
            result = []
            for key_name in self.data.keys():
                k = key_name.title()
                result.append(k)
                if self.data[key_name].date.value != None:
                    d = str(self.data[key_name].date.value.date())
                    result.append(d)
                phone_l = self.data[key_name].phone
                for i in phone_l:
                    result.append(str(i.value))
                result.append("\n")
            print(" ".join(result))
        except Exception as e:
            print("Error!", e.args)

    def search_record(self, name) -> Record:
        for key_name in self.data.keys():
            if key_name == name:
                return self.data[key_name]


class User():
    def __init__(self):
        pass

    def command_hello(self):
        """Функція привітання"""
        print("How can I help you?")

    def command_exit(self):
        """Функція виходу"""
        sys.exit("Good bye!")
