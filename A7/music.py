#Author:  Samuel Resendez
# ITP 115 Assignment 7
# October 23rd, 2016

#------ imports ------
import pickle


# ----- begin declaration -----
def main():
    musicLib = loadLibrary("music_library.dat")
    userChoice = ""
    while(userChoice != 7):
        displayMenu()
        userChoice = int(input("> "))
        if userChoice == 1:
            displayLibrary(musicLib)
        elif userChoice == 2:
            displayArtists(musicLib)
        elif userChoice == 3:
            addAlbum(musicLib)
        elif userChoice == 7:
            saveLibrary("music_library.dat",musicLib)
        elif userChoice == 4:
            deleteAlbum(musicLib)
        elif userChoice == 6:
            searchLibrary(musicLib)
        elif userChoice == 5:
            deleteArtist(musicLib)

def loadLibrary(libraryFileName):
    fileIn = open(libraryFileName, "rb")
    val = pickle.load(fileIn)
    val = dict(val)
    return val
    
def saveLibrary(libraryFileName, musicLibDct):
    fileIn = open(libraryFileName, "wb")
    
    pickle.dump(musicLibDct,fileIn)
    
def displayMenu():
    print("Welcome to the music player, what would you like to do? ")
    print("Options:")
    print("\t 1) Display Library")
    print("\t 2) Display all artists")
    print("\t 3) Add an album")
    print("\t 4) Delete an album")
    print("\t 5) Delete an artist")
    print("\t 6) Search Library")
    print("\t 7) Exit")

def displayLibrary(musicLibDct):
    for key in musicLibDct:
        print("Artist: " + key)
        print("Albums: ")
        for album in musicLibDct[key]:
            print("\t- " + album)

def displayArtists(musicLibDct):
    print("Displaying all artists:")
    for key in musicLibDct:
        print(" - " + key)

def addAlbum(musicLibDct):
    nameOfArtist = input("Please enter the name of the artist you would like: ")
    nameOfAlbum = input("Please enter the name of the album you would want to add: ")
    if nameOfArtist in musicLibDct.keys():
        musicLibDct[nameOfArtist].append(nameOfAlbum)
    else:
        musicLibDct[nameOfArtist] = [nameOfAlbum]

def deleteAlbum(musicLibDct):
    relevantArtist = input("Please enter name of artist: ")
    albumToRemove = input("Please enter album to remove: ")
    if relevantArtist in musicLibDct.keys():
        if albumToRemove in musicLibDct[relevantArtist]:
            musicLibDct[relevantArtist].remove(albumToRemove)
            return True
        else:
            return False
    else:
        return False

def deleteArtist(musicLibDct):
    relevantArtist = input("Please enter name of artist to remove: ")
    if relevantArtist in musicLibDct.keys():
        del musicLibDct[relevantArtist]
        return True
    else:
        return False
def searchLibrary(musicLibDct):
    searchTerm = input("Please enter a search: ")
    searchTerm = searchTerm.lower()
    print("Artists that matched your search: ")
    for key in musicLibDct.keys():
        if searchTerm.lower() in key.lower():
            print("\t - ", end="")
            print(key)
    print("Albums which matched your search: ")
    
    for key in musicLibDct.keys():
        for album in musicLibDct[key]:
            if searchTerm in album.lower():
                print("\t - ",end="")
                print(album)
    
# ----- begin execution ----
main()
