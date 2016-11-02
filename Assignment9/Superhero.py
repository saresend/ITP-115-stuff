# Author: Samuel Resendez
# ITP 115 - Fall 2016
# Assignment 9 - Superheroes
# saresend@usc.edu
# Cheers!

# -------- imports -------


#----- classes, defined ----
class Superhero(object):
    def __init__(self,heroName,heroType,attackInt):
        self.__name = heroName
        self.__hType =  heroType
        self.__attack = attackInt
        self.__health = 100

    def getName(self):
        return self.__name
    
    def getAttack(self):
        return self.__attack
    def getHealth(self):
        return self.__health
    def getType(self):
        return self.__hType
    def loseHealth(self,opponentAttack):
        self.__health = self.__health - int(opponentAttack)
        
    def isDead(self):
        if self.__health <= 0:
            return True
        else:
            return False
    def __str__(self):
        descrip = self.__name + " the " + self.__hType + " has " + str(self.__attack) + " attack points\n and currently has " + str(self.__health) + " points of health."
        return descrip
