# -*- coding: utf-8 -*-
# Python 3.10

class Product:
    def __init__(self, name, price, stock):
        """
        Function called when creating a new class

        :param name: str with the name of the item
        :param price: str with the price of the item
        :param stock: str with the stock of the item
        """
        self.__name = name
        self.__price = price
        self.__stock = stock

    def __str__(self):
        """
        Function called when displaying a class

        :return:str representing the name of the item
        """
        return self.__name

    def change_name(self, name_new):
        """
        Function used to change the name of an item

        :param name_new: str with the new name of the class
        """
        if type(name_new) == str :
            self.__name = name_new
        else :
            return False

    def change_price(self, price_new):
        """
        Function used to change the price of an item

        :param price_new: str with the new price
        """
        if type(price_new) == str :
            self.__price = price_new
        else :
            return False

    def change_stock(self, stock_new):
        """
        Function used to change the stock of an item

        :param stock_new: str with the new stock
        """
        if type(stock_new) == str :
            self.__stock = stock_new
        else :
            return False

    def get_stock(self):
        """
        Function used to get the actual stock of an item

        :return: str with the stock of the item
        """
        return int(self.__stock)


    def get_price(self):
        """
        Function used to get the actual price of an item

        :return: The price of the item
        """
        return int(self.__price)

    def get_name(self):
        """
        Function used to get the actual name of an item

        :return: The name of the item
        """
        return self.__name




if __name__ == "__main__":
    product_tab = [Product("Titi's back n2", "25", "123"), Product("Call of Witcher", "60", "5")]
    shopping_cart = []
    choice = 0
    while choice != "q":
        print("Welcome to MediaToys\nPlease select one of the options available:"
              "\n1)Add an item on the marketplace (admin)\n2)Modify an item (admin)\n"
              "3)Add an item into the shopping cart\n4)Go to purchase\n"
              "5)To see all the products with their information\n"
              "6)aide")
        choice = input("Your choice(to exit press q): ")
        if choice == "1":
            if input("Admin password: ") == "admin":
                print("What is the name of the item you want to add?")
                alias = input("The name: ")
                print("What is the price of the item you want to add?")
                gold = input("The price: ")
                while not gold.isdigit():
                    print("Error: try using an integer instead of anything else")
                    print("What is the price of the item you want to add?")
                    gold = input("The price: ")
                print("How many items you want to add?")
                number = input("How many: ")
                while not number.isdigit():
                    print("Error: try using an integer instead of anything else")
                    print("How many items you want to add?")
                    number = input("How many: ")
                product_tab.append(Product(alias, gold, number))
                print("The product " + alias + " was successfully added in the marketplace\n\n\n")
            else:
                print("Wrong password !!!\n\n\n")
        elif choice == "2":
            counter = 1
            if input("Admin password: ") == "admin":
                if not product_tab:
                    print("The store is actually empty\n\n\n")
                else:
                    for product in product_tab:
                        print(str(counter) + " - " + str(product))
                        counter += 1
                    number_item = input("Number of the item: ")
                    while not number_item.isdigit() or counter <= int(number_item) or int(number_item) <= 0:
                        print("Error the number you wrote does not exist in this list, try an already existing one")
                        number_item = input("Number of the item: ")
                    print("What do you want to change? (name, price, stock, q to quit) ")
                    response = input("Your answer: ")
                    while response != "name" and response != "price" and response != "stock" and response != "q":
                        print("Wrong value, please try again ")
                        response = input("Your answer: ")

                    if response == "name":
                        new_name = input("What is the new name of the product ? ")
                        product_tab[int(number_item)-1].change_name(new_name)
                        print("The new name of the product is " + new_name + "\n\n\n")

                    elif response == "price":
                        new_price = input("What is the new price of the item?")
                        product_tab[int(number_item)-1].change_price(new_price)
                        print("The new price of the product is " + new_price + "\n\n\n")

                    elif response == "stock":
                        new_stock = input("What is the new quantity of this product?")
                        product_tab[int(number_item) - 1].change_stock(new_stock)
                        print("The new number of items is now " + new_stock + "\n\n\n")

                    elif response == "q":
                        print("You successfully went back to the main menu\n\n\n")

        elif choice == "3":
            counter = 1
            if not product_tab:
                print("The store is actually empty")
            else:
                for product in product_tab:
                    print(str(counter) + " - " + str(product.get_name()) + " " + str(product.get_price()) + "€ " +
                          str(product.get_stock()) + " available")
                    counter += 1
                add_item = input("Which item do you want to pick ?")
                while not add_item.isdigit() or counter < int(add_item) or int(add_item) <= 0:
                    print("Wrong value, please try again ")
                    add_item = input("Which item do you want to pick ?")
                how_many = input("How many items do you want to add ?")
                if product_tab[int(add_item)-1].get_stock() == 0:
                    print("There is not enough stock of the item you asked for.")
                else:
                    while not how_many.isdigit() or product_tab[int(add_item)-1].get_stock() < int(how_many) or \
                            int(how_many) <= 0:
                        print("Wrong value, please try again ")
                        how_many = input("How many items do you want to add ?")
                    shopping_cart.append([add_item, how_many])
                    print("The item requested was successfully added to you shopping cart")
            print("\n\n\n")

        elif choice == "4":
            total_price = 0
            if not shopping_cart:
                print("Your shooping cart is empty")
            else:
                for curser in shopping_cart:
                    if int(curser[1]) <= product_tab[int(curser[0])-1].get_stock():
                        total_price += product_tab[int(curser[0])-1].get_price() * int(curser[1])
                        print("\n" + curser[1] + " x " + product_tab[int(curser[0])-1].get_name() + " (one for "
                              + str(product_tab[int(curser[0])-1].get_price()) + ")\n")
                    else:
                        print("The item " + product_tab[int(curser[0])-1].get_name() +
                              " is not available in this quantity anymore")
                        shopping_cart.remove(curser)
                print("The total price is " + str(total_price) + "€\n")
                print("Do you want to purchase the items in your basket")
                confirmation = input("Confirm (Y/N):")
                if confirmation == "Y":
                    for i in shopping_cart:
                        new_stock = product_tab[int(i[0])-1].get_stock() - int(i[1])
                        product_tab[int(i[0])-1].change_stock(new_stock)
                    print("Thank you for your purchase(s)")
                    shopping_cart = []
                elif confirmation == "N":
                    print("Purchase canceled !\n")
                else:
                    print("Wrong choice, please try again !\n")
            print("\n\n\n")

        elif choice == "5":
            if not product_tab:
                print("The store is actually empty")
            else:
                print("\n\nName|Price|Stock")
                for i in product_tab:
                    print(str(i.get_name()) + "|" + str(i.get_price()) + "€| " + str(i.get_stock()))
            print("\n\n\n")

        elif choice == "6" :
            help()

        elif choice == "q":
            print("See you soon!")
        else:
            print("\nWrong option try one of these ones instead: 1 - 2 - 3 - 4 - 5 - q")
