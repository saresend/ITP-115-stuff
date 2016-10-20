#Author: Samuel Resendez
# ITP 115 Assignment 5
# October 3rd, 2016
# Cheers!!

# ------- add imports -----
import TicTacToeHelper
import random


# ---- begin implementation -----
def main():
    wouldLikeToPlayAgain = True
    while(wouldLikeToPlayAgain):
        playGame()
        wouldLikeToPlay = input("Would you like to play again?(y/n): ")
        if wouldLikeToPlay.lower() == "n":
            wouldLikeToPlayAgain = False



def printPrettyBoard(board):
    for x in range(3):
        for y in range(3):
            properIndex = 3*x + y
            if y != 2:
                print(" " + str(board[properIndex]) + " |", end = "")
            else:
                print(" " + str(board[properIndex]), end = "")
        print("\n",end="")
        if x != 2:
            print("------------")
def isValidMove(board_list,spot):
    if board_list[spot] == "x" or board_list[spot] == "o":
        return False
    else:
        return True
def updateBoard(board_list, spot, player_letter):
    board_list[spot] = player_letter

        
def playGame():
    moveCounter = 0
    isXmove = True
    board = ["0","1","2","3","4","5","6","7","8"]
    boardState = "n"
    while(boardState=="n"):
        printPrettyBoard(board)
        if(isXmove):
            userXmove = int(input("Player X, please enter your move: "))
            moveCounter += 1
            while not isValidMove(board,userXmove):
                print("That space is not available!")
                userXmove = int(input("Player X, please enter your move: "))
            updateBoard(board,userXmove,"x")
            isXmove = False
        else:
            isValidInput = False
            userMove =int(input("Player O, please enter your move: "))
            isValidInput = isValidMove(board,userMove)
            moveCounter += 1
            while not isValidInput:
                print("That space is not available!")
                userMove = int(input("Player O, please enter your move: "))
                isValidInput = isValidMove(board,userMove)
            isXmove = True
            updateBoard(board,userMove,"o")
        boardState = TicTacToeHelper.checkForWinner(board,moveCounter)
    if boardState == "s":
        print("It seems you are evenly matched, stalemate!")
    elif boardState == "x":
        print("Congratulations, X wins!")
    elif boardState == "o":
        print("Congratulations, O wins!")
        
# ---- begin execution ----
if __name__ == "__main__":
    main()
