# Author: Samuel Resendez
# Date: September 20th, 2016
# ITP 115 - Assignment 4
# Cheers!

# -- imports --
import random

#begin implementation
def main():
    print("Welcome to the caesar cypher")
    stringToEncode = input("Enter a message: ")
    shiftValue = input("Enter a value between 0 and 25: ")
    encryptedMessage = encryptMessage(int(shiftValue),stringToEncode)
    print("Encrypting message.....")
    print(encryptedMessage)
    print("Decrypting message...")
    decryptedMessage = encryptMessage(25 - int(shiftValue),encryptedMessage)
    print(decryptedMessage)
    print("Original message: ")
    print(stringToEncode)




def encryptMessage(shiftValue,stringToEncode):
    encodedString = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetList = list(alphabet)
    isUppercase = False
    for char in stringToEncode:        
        index = 0
        if char.lower() in alphabetList:
            if (alphabetList.index(char.lower()) + shiftValue) > 25:
                index = alphabetList.index(char.lower())+shiftValue - 25;
            else: # this may reference the first if statement
                index = alphabetList.index(char.lower())+shiftValue;
            encodedString += alphabetList[index]
        else:
            encodedString += char
    return encodedString

# --- ensures execution if main ----
if __name__ == "__main__":
    main()
