#Author: Samuel Resendez
# ITP 115, Fall 2016
# Lab 9
# saresend@usc.edu

# ---- method declarations -----
def main():
    dictionaryPath = input("Enter dictionary file name: ")
    errorPath = input("Enter error passage file name: ")
    dictionaryList = readDictionaryFile(dictionaryPath)
    textList = readTextFile(errorPath)
    misspelledWords = findErrors(dictionaryList,textList)
    printErrors(misspelledWords)

def readDictionaryFile(dictionaryPath):
    dictionaryList = []
    dictionaryFile = open(dictionaryPath,"r")
    for line in dictionaryFile:
        line = line.strip()
        dictionaryList.append(line)
    dictionaryFile.close()
    return dictionaryList

def readTextFile(textPath):
    textList = []
    textFile = open(textPath, "r")
    for line in textFile:
        line=line.strip()
        line=line.strip(".,:;?\"")
        textList.append(line)
    textFile.close()
    return textList
def findErrors(dictionarylist,textList):
    misspelledWords = []
    for word in textList:
        if word not in dictionaryList:
            misspelledWords.append(word)
    return misspelledWords

def printErrors(misspelledWordList):
    for word in misspelledWordList:
        print(word)

# ---- method calls -----
if __name__ == "__main__":
    main()
