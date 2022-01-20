# -*- coding: utf-8 -*-
# Python 3.9
import argparse


class Characters:
    def __init__(self, name, age, phone_number, email):
        self.__name = name
        self.__age = age
        self.__phone_number = phone_number
        self.__email = email

    def get_all(self):
        return "Name: " + self.__name + "\nAge: " + self.__age + "\nPhone number: " + self.__phone_number +\
               "\nE-mail: " + self.__email

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email


if __name__ == "__main__":
    all_information = []
    parser = argparse.ArgumentParser(description='Gives you information about someone you requested')
    parser.add_argument(dest='name', type=str,
                        help='The name of the person chosen')
    parser.add_argument(dest='attributs', nargs="+",
                        type=str,
                        help='Information desired (all, name, age, phone_number, email)')

    args = parser.parse_args()
    # print(args.name)
    with open("phoneBook.txt", 'r') as file:
        data = file.readlines()
        # print(data)
        for i in data:
            information = i.split(' ')
            # print(information)
            all_information.append(Characters(information[0], information[1], information[2], information[3]))

    for character in all_information:
        if args.name == character.get_name():
            for j in args.attributs:
                if j == "name":
                    print("Name: " + character.get_name())

                elif j == "age":
                    print("Age: " + character.get_age())

                elif j == "phone_number":
                    print("Phone number: " + character.get_phone_number())

                elif j == "email":
                    print("E-mail: " + character.get_email())

                elif j == "all":
                    print(character.get_all())
