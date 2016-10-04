
# Author: Samuel Resendez
# Date: Tuesday, September 18th, 2016
# ITP 115

# ------- begin execution ---------
#### vars ####
userWantsToContinue = True
minValue = -10
userInput = -1337
while userWantsToContinue:
    print("Input an integer greater than or equal to 0 or -1 to quit: ")
    while userInput != "-1":
        userInput = input(">> ")
        if(userInput == "-1"):
            print("The largest number is " + str(minValue))
        if int(userInput) >  minValue:
            minValue = int(userInput)
    wantToGo = input("Would you like to find the largest number again?(y/n): ")
    if wantToGo.lower() == "n":
        userWantsToContinue = False
    userInput = -1337
print("Goodbye!")
