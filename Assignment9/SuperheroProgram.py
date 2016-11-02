# Author: Samuel Resendez
# ITP 115 - Assignment 9
# saresend@usc.edu
# Cheers!

#---- imports ----
from Superhero import Superhero


# ---- method declaration -----
def main():
    userWantsToContinue = "y"
    while(userWantsToContinue != "n"):
        fighterOneName = input("Enter fighter #1's name: ")
        fighterOneType = input("Is fighter #1 a hero or a villain?: ")
        fighterOneAtk = int(input("Enter fighter #1's attack points: "))
        fighterTwoName = input("Enter superhero #2's name: ")
        fighterTwoType = input("Is fighter #2 a hero or villain?: ")
        fighterTwoAtk = input("Enter fighter #2's attack points: ")
        fighterOne = Superhero(fighterOneName,fighterOneType,fighterOneAtk)
        fighterTwo = Superhero(fighterTwoName,fighterTwoType,fighterTwoAtk)
        print("FIGHTERS")
        print("")
        print("")
        print(fighterOne)
        print(fighterTwo)
        print("")
        print("BEGINNING BATTLE!")
        print("")
        numRounds = 1
        while(not fighterOne.isDead() and not fighterTwo.isDead()):
            print("============ Round",str(numRounds),"==============")
            fighterOne.loseHealth(fighterTwo.getAttack())
            fighterTwo.loseHealth(fighterOne.getAttack())
            print(fighterOne)
            print(fighterTwo)
            numRounds += 1
        if(fighterOne.isDead() and fighterTwo.isDead()):
            print("Tie. Both died.")
        elif(fighterOne.isDead()):
            print(fighterTwo.getName(),"won!")
        else:
            print(fighterOne.getName(),"won!")
        userWantsToContinue = input("Would you like to play again?(y/n): ")


#-------begin execution ----
main()
