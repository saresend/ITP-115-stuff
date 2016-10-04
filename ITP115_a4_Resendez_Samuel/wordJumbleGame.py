# Author: Samuel Resendez
# Date: September 20th, 2016
# ITP 115 - Assignment 4

#Imports
import random

# --- main execution -----
def main():
    userWantsToContinue = True
    counter = 0
    print("Welcome to the jumble word game!")
    while userWantsToContinue:
        guess = ""
        selectedWord = selectRandomWord()
        print("The jumbled word is: " + jumbleWord(selectedWord))
        while guess != selectedWord:
            guess = input("Please enter your guess: ")
            if guess == selectedWord:
                print("You got it!")
                print("It took you " + str(counter) + " tries!")
                userThing = input("Would you like to play again?(y/n) ")
                if userThing.lower() == "n":
                    userWantsToContinue = False
                    counter = 0
            else:
                print("Try Again!")
                counter += 1
    print("goodbye!")
    






def selectRandomWord():
    wordList = ["Bonobos","Orangutans","Chimpanzees","Harambe","Gorillas","Apes","Humans","Macaques","Monkeys"]
    return random.choice(wordList)

def jumbleWord(word):
    letterList = list(word)
    for x in range(len(word)):
        temp = letterList[x]
        randomNumber = random.randint(0,len(letterList)-1)
        letterList[x] = letterList[randomNumber]
        letterList[randomNumber] = temp
    returnString = "".join(letterList)
    return returnString



















# ---- executes if main -----
if __name__ == "__main__":
    main()
