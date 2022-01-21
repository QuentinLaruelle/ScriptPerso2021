# -*- coding: utf-8 -*-
# Python 3.9
import argparse


class Characters:
    def __init__(self, name, age, phone_number, email):
        self.__original_name = name
        list_name = list(name)
        beginning = True
        counter = 0
        for letter in list_name:
            if beginning:
                list_name[counter] = list_name[counter].upper()
            if letter == ".":
                list_name[counter+1] = list_name[counter+1].upper()
                beginning = False
            counter += 1
        self.__name = ''.join([str(each_letter) for each_letter in list_name])# convert into string
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

    def get_original_name(self):
        return self.__original_name


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
    args.name = args.name.lower()
    with open("phoneBook.txt", 'r') as file:
        data = file.readlines()
        # print(data)
        for i in data:
            information = i.split(' ')
            # print(information)
            all_information.append(Characters(information[0], information[1], information[2], information[3]))

    for character in all_information:
        # print(character.get_name())
        if args.name == character.get_original_name():
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
