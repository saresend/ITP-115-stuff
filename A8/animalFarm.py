#Author: Samuel Resendez
#ITP 115 A8 - Animal Daycare
# Monday, October 24th, 2016
# Cheers!

# --- import statements ----

# ----- class Declarations ----

class Animal:
    
# ----- attributes ----
    hunger = 0
    happiness = 0
    health = 0
    energy = 0
    age = 0
    name = ""
    species = ""

    
# ---- methods -----
    def __init__(self,hungerNum,happinessNum,healthNum,EnergyNum,ageNum,nameStr,speciesStr):
        self.hunger = hungerNum
        self.happiness = happinessNum
        self.health = healthNum
        self.energy = EnergyNum
        self.age = ageNum
        self.name = nameStr
        self.species = speciesStr

    def play(self):
        self.happiness += 10
        self.hunger += 5

    def feed(self):
        self.hunger -= 10

    def giveMedicine(self):
        self.happiness -= 20
        self.health += 20

    def sleep(self):
        self.energy += 20
        self.age += 1

    def __str__(self):
        string = "Name: " + self.name + "\n"
        string += "Health: " + str(self.health) + "\n"
        string += "Species: " + self.species + "\n"
        string += "Age: " + str(self.age) + "\n"
        string += "Energy: " + str(self.energy) + "\n"
        string += "Happiness: " + str(self.happiness) + "\n"
        string += "Hunger: " + str(self.hunger) + "\n"
        string += "********************************"
        return string

    
#----- begin implementation ----
def main():
    userInput = 0
    animalArray = loadAnimals("animals.csv")
    while(userInput != 7):
        displayMenu()
        userInput = int(input("Please make a selection: "))
        while userInput > 7 or userInput < 1:
            print("*Invalid input, please try again.")
            userInput = int(input("Please make a selection: "))
        if userInput == 1:
            selectedAnimal = selectAnimal(animalArray)
            selectedAnimal.play()
            print("You played with "+selectedAnimal.name+"!")
        elif userInput == 2:
            selectedAnimal = selectAnimal(animalArray)
            selectedAnimal.feed()
            print("You fed "+selectedAnimal.name+"!")
        elif userInput==3:
            selectAnml = selectAnimal(animalArray)
            selectAnml.giveMedicine()
            print("You gave "+selectAnml.name+" medicine!")
        elif userInput == 4:
            selAn = selectAnimal(animalArray)
            selAn.sleep()
            print(selAn.name+ " fell asleep!")
        elif userInput == 5:
            selAn = selectAnimal(animalArray)
            print(selAn)
        elif userInput == 6:
            for animal in animalArray:
                print(animal)

    
def loadAnimals(filename):
    fileIn = open(filename,"r")
    animalArray = []
    for line in fileIn:
        vars = line.split(",")
        animal = Animal(int(vars[0]),int(vars[1]),int(vars[2]),int(vars[3]),int(vars[4]),vars[5],vars[6])
        animalArray.append(animal)
    fileIn.close()
    return animalArray

def displayMenu():
    print("1) Play")
    print("2) Feed")
    print("3) Give Medicine")
    print("4) Sleep " )
    print("5) Print an Animal's stats" )
    print("6) View All Animals")
    print("7) Exit")


# takes an animal array, and returns a selected animal!
def selectAnimal(animalArray):
    for animal in animalArray:
        print(animal.name)
    userSelection = int(input("Please make a selection(1 - "+str(len(animalArray))+"): "))
    while userSelection < 1 or userSelection > len(animalArray):
        print("Invalid Input, give it another go.")
        userSelection = int(input("Please make a selection: "))
    return animalArray[userSelection - 1]

#----- begin execution
main()
