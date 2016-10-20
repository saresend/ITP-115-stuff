# Author: Samuel Resendez
# ITP 116 Assignment 6
# October 16th, 2016
# saresend@usc.edu
# Cheers!


def main():
    print("Welcome to EPA Mileage Calculator")
    year = input("What year would you like to view data for? (2008 or 2009) ")
    year = int(year)
    print(year)
    while(year != 2008 and  year != 2009):
        year = int(input("*Invalid input, please try again: "))
    filename = input("Enter the filename to save results to: ")
    inputFilename = "epaVehicleData"+str(year)+".csv"
    vehicleType = 
    fileIn = open(inputFilename, "r")
    counter = 0
    minMPG = 1000000
    maxMPG = 0
    maxMPGModels = []
    minMPGModels = []
    for line in fileIn:
        if counter != 0 and "van" not in line[0] and "pickups" not in line[0]:
            line = line.split(",")
            if int(line[9]) > maxMPG:
                maxMPGModels = []
                maxMPG = int(line[9])
                maxMPGModels.append(line[2])
            elif int(line[9]) == maxMPG:
                maxMPGModels.append(line[2])
            if int(line[9]) < minMPG:
                minMPGModels = []
                minMPG = int(line[9])
                minMPGModels.append(line[2])
            elif int(line[9]) == minMPG:
                minMPGModels.append(line[2])
        counter += 1
    fileO = open(filename,"w+")
    fileO.write("EPA Highway MPG Calculator ("+str(year)+")\n")
    fileO.write("--------------------------------------------\n")
    fileO.write("Maximum mileage (highway): " + str(maxMPG)+"\n")
    for car in maxMPGModels:
        fileO.write("\t" + car+"\n")
    fileO.write("Minimum mileage (highway): " + str(minMPG)+"\n")
    for car in minMPGModels:
        fileO.write("\t"+car+"\n")
    print("Operation has been a success. Check out " + filename + " for results.")
    fileO.close()


# ----- begin execution ------
main()
