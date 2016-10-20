#Author: Samuel Resendez
# ITP 115, Fall 2016
# Lab L11
# saresend@usc.edu

def main():
    story = "story.txt"
    storyDictionary = concordance(story)
    storyKeys = sortKeys(storyDictionary)

    print("Heres the concordance for the file \'"+story+"\'")
    for key in storyKeys:
        print(key + ": " + str(storyDictionary[key]))


def sortKeys(unsortDict):
    sortList = unsortDict.keys()
    print(sortList)
    sorted(sortList)
    return sortList
def concordance(filename):
    concordDict = {}
    fileRead = open(filename, "r")
    lineNum = 0
    for line in fileRead:
        lineNum += 1
        for word in line.split():
            word = word.replace(".","")
            word = word.replace("'","")
            word = word.replace("-","")
            word = word.replace("?","")
            word = word.replace(",","")
            word = word.replace(":","")
            if word not in concordDict.keys():
                concordDict[word] = [lineNum]
            elif word in concordDict.keys():
                concordDict[word].append(lineNum)
    return concordDict
            
main()    
              
#input: a filename
#output: dictionary
