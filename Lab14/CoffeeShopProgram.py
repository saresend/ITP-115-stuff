"""
FA 16: Lab 14 OOP (Barista lab)
Main program
    - creates a Barista
    - Barista takes orders
    - when the barista is done taking orders, make the drinks
    - Continue taking orders until user chooses to exit
"""
from Barista import Barista


def main():
    name = input("Please enter your name:\n> ")
    barista = Barista(name)
    print("\n~Welcome to the Coffee Shop!~\n")

    cont = True
    while cont:
        # Take 5 orders
        while barista.isAcceptingOrders():
            barista.takeOrder()
            # Make drinks
            barista.makeDrinks()

            # Ask to continue
            response = input("Would you like to continue? (y/n)\n> ")
            while response.lower() != "y" and response.lower() != "n":
                print("*Invalid input, please try again!")
                response = input("Would you like to continue? (y/n)\n> ")
            cont = (response.lower() == "y")

    print("Goodbye, please come again!")

main()
                                                                                                                                    
