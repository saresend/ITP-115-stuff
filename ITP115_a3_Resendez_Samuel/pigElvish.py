# Author: Samuel Resendez
# Date: Tuesday, September 13th, 2016
# ITP 115 
# Assignment 3
# Cheers!



#------ Boilerplate ---------
import random


#------ method implementations -------

def function(word):
    vowels = "aeiou"
    translatedString = word[1:] + word[0]
    if len(word) >= 4:
        translatedString = translatedString + getRandomVowel() + getRandomVowel()
    elif len(word) <= 3:
        translatedString += "en"
    elif translatedString[-1] == "e":
         translatedString = translatedString[:len(translatedString)-1] + "ë"
    translatedString.lower()
    translatedString[0].upper()
    return translatedString

    
def getRandomChar():
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
    charIndex = random.randint(0,25)
    return alphabet[charIndex]
def getRandomVowel():
    vowels = "aeiou"
    vowelIndex = random.randint(0,4)
    return vowels[vowelIndex]



#--- Begin execution -- ---
print("""Elcómewó óten heten Igpén Lvísheá ránslátórtë!
      (Welcome to the Pig Elvish translator!)""")
userWantsToContinue = True
while userWantsToContinue:
    wordToTranslate = input("Please enter a word to translate: ")
    translated = function(wordToTranslate)
    print("'"+wordToTranslate+"' in elvish is: " + translated)
    shouldContinue = input("Would you liek to enter another word?(y/n): ")
    if shouldContinue.lower() == "n":
        userWantsToContinue = False
        print("Oodbyega! Aveha aen icenë ayden!")
    
