
# Samuel Resendez
# ITP115, Fall 2016
# Lab Practical L3
# saresend@usc.edu

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Would you like to:")
print("a) See the ASCII code for the alphabet")
print("b) Translate a word into its ASCII code")
choiceOne = input("a or b: ")
while choiceOne.lower() != "a" and choiceOne.lower() != "b":
    choiceOne = input("a or b: ")

if choiceOne.lower() == "a":
    upperOrLower = input("Would you like to see the alphabet in upper (u) or lower (l) case?: ")
    if upperOrLower.lower() != "l" and upperOrLower.lower() != "u":
        upperOrLower = input("Would you like to see the alphabet in upper (u) or lower (l) case?: ")
    if upperOrLower.lower() == "l":
        alphabet = alphabet.lower()
    for char in alphabet:
        print(ord(char), end = " ")
        print(char)
elif choiceOne.lower() == "b":
    userString = input("Enter the word you would like to turn into ASCII:")
    for char in userString:
        print(char + ":", end=" ")
        print(ord(char))



