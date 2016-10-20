#Author:  Samuel Resendez
# ITP 115 Assignment 7
# October 23rd, 2016

#------ imports ------
import pickle


# ----- begin declaration -----
def main():
    loadLibrary("music_library.dat")

def loadLibrary(libraryFileName):
    fileIn = open(libraryFileName, "rb")
    val = pickle.load(fileIn)
    val = dict(val)
    return val
    
def saveLibrary(libraryFileName, musicLibDct):
    print("Place")
def displayMenu():
    print("death")
def displayLibrary(musicLibDct):
    print("hi")
def displayArtists(musicLibDct):
    print("hey")
def addAlbum(musicLibDct):
    print("this is a lot")
def deleteAlbum(musicLibDct):
    print("holy")
def deleteArtist(musicLibDct):
    print("what")
def searhLibrary(musicLibDct):
    print("satan")
    
# ----- begin execution ----
main()
