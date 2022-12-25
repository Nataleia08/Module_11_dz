import sys
from collections import UserDict
from class_list import Field, Name, Phone, Record, AddressBook, User


address_book = AddressBook()
user_1 = User()
command_list = ["hello", "add", "change",
                "phone", "show all", "close", "exit", "good bye"]
while True:
    # ----------------------------Розпізнавання введених даних-----------------------
    command_string = input("Enter command:").lower()
    if command_string == ".":
        break
    find_command = False
    for k in command_list:
        if k in command_string:
            input_com = k
            attribute_sring = command_string.replace(input_com, "").strip()
            find_command = True
            break
    if not find_command:
        print("Command undefined! Try again!")
        continue
    input_list = attribute_sring.split(" ")
    # if "" in input_com:
    #     input_list.remove("")
    for i in input_list:
        if i.isalpha():
            name = i
            input_list.remove(i)
            phone = " ".join(input_list)
            new_record = Record(name, phone)
            break
    # ----------------------------Виконання команди--------------------------------------
    if input_com == "hello":
        user_1.command_hello()
    elif (input_com == "close") or (input_com == "exit") or (input_com == "good bye"):
        user_1.command_exit()
    elif input_com == "add":
        try:
            address_book.add_record(new_record)
        except:
            print("Give me name and phone please!")
    elif input_com == "change":
        try:
            address_book.change_record(new_record)
        except:
            print("Give me name and phone please!")
    elif input_com == "phone":
        try:
            address_book.search_phone(name)
        except:
            print("Enter user name!")
    elif input_com == "show all":
        address_book.show_all()
    else:
        print("Command undefined! Try again!")
