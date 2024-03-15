#!/usr/bin/env python3
from players import Players
import os

# class player:
#     # property: name, symbol

#     def set_symbol():
#     def get_symbol():
#     def set_name():
#     def get_name():

# class board:
#     #property: list (board 1 to 9)
#     # winning state:
#         # xxx --- ---
#         # --- xxx ---
#         # --- --- xxx
#         # x-- x-- x--
#         # -x- -x- -x-
#         # --x --x --x
#         # x-- -x- --x
#         # --x -x- x--

#     def print_board():
#         # update board with new position set
#     def set_board_position():
#         # board position taken
#     def check_game_state():
#         # win
#         # lose
#         # draw

def check_game_state(board, symbol):
    if (board[0] == symbol and board[1] == symbol and board[2] == symbol) \
        or (board[3] == symbol and board[4] == symbol and board[5] == symbol) \
        or (board[6] == symbol and board[7] == symbol and board[8] == symbol) \
        or (board[0] == symbol and board[3] == symbol and board[6] == symbol) \
        or (board[1] == symbol and board[4] == symbol and board[7] == symbol) \
        or (board[2] == symbol and board[5] == symbol and board[8] == symbol) \
        or (board[0] == symbol and board[4] == symbol and board[8] == symbol) \
        or (board[2] == symbol and board[4] == symbol and board[6] == symbol):
        return False
    else:
        return True


def printBoard(board):
    row1 = "A  {} | {} | {} ".format(board[0], board[1], board[2])
    row2 = "B  {} | {} | {} ".format(board[3], board[4], board[5])
    row3 = "C  {} | {} | {} ".format(board[6], board[7], board[8])

    print("   1   2   3 ")
    print (row1)
    print("  -----------")
    print (row2)
    print("  -----------")
    print (row3)


if __name__ == '__main__':

    # Initialize the board
    board = [" " for x in range(9)]
    state = True
    symbol = "X"
    os.system('clear')
    printBoard(board)

    while state:
        playerTextNumber = "One" if symbol == "X" else "Two"
        playerChosenPosition = input(f"Player {playerTextNumber}, please pick your spots using the format like this: A1, B2. \n")
        if playerChosenPosition == "A1" and board[0] == " ":
            board[0] = symbol
        elif playerChosenPosition == "A2" and board[1] == " ":
            board[1] = symbol
        elif playerChosenPosition == "A3" and board[2] == " ":
            board[2] = symbol
        elif playerChosenPosition == "B1" and board[3] == " ":
            board[3] = symbol
        elif playerChosenPosition == "B2" and board[4] == " ":
            board[4] = symbol
        elif playerChosenPosition == "B3" and board[5] == " ":
            board[5] = symbol
        elif playerChosenPosition == "C1" and board[6] == " ":
            board[6] = symbol
        elif playerChosenPosition == "C2" and board[7] == " ":
            board[7] = symbol
        elif playerChosenPosition == "C3" and board[8] == " ":
            board[8] = symbol
        else:
            os.system('clear')
            printBoard(board)
            print("Spot taken!")
            continue

        os.system('clear')
        printBoard(board)
        state = check_game_state(board, symbol)

        if state == False:
            print(f"Player {playerTextNumber} has won!")
            break

        #Switch players
        symbol = "O" if symbol == "X" else "X"

    listOfPlayers = []
    totalNumberOfPlayers = 0

    playerResponse = input("Hi, this is a game of tic-tac-toe. Will you play against a bot? Y/N ")
    print(playerResponse)

    hasAnswered = False

    while not hasAnswered:
        if playerResponse.lower() == 'n' or playerResponse.lower() == 'no':
            
            totalNumberOfPlayers = 2

            # Create and add players into list

            for playerNumber in range(totalNumberOfPlayers):
                playerTextNumber = "One" if playerNumber == 0 else "Two"

                playerName = input(f"Player {playerTextNumber}, please enter your name: ")
                listOfPlayers.append(Players())
                listOfPlayers[playerNumber].name = playerName

                playerSymbol = "X" if playerNumber == 0 else "O"
                listOfPlayers[playerNumber].symbol = playerSymbol

            hasAnswered = True

        elif playerResponse.lower() == 'y' or playerResponse.lower() == 'yes':
            playerOneName = input("Player one, please enter your name: ")

            totalNumberOfPlayers = 1

            # Create players
            for playerNumber in range(totalNumberOfPlayers):
                playerTextNumber = "One" if playerNumber == 0 else "Two"

                playerName = input(f"Player {playerTextNumber}, please enter your name: ")
                listOfPlayers.append(Players())
                listOfPlayers[playerNumber].name = playerName

                playerSymbol = "X" if playerNumber == 0 else "O"
                listOfPlayers[playerNumber].symbol = playerSymbol
        else:
            playerResponse = input("I'm sorry. I did't quite understand. Will you play against a bot? Y/N ")
            hasAnswered = False






    # playerTwo = Players(playerTwoName, "O")

    print(f"Player one, {listOfPlayers[0].name} is using {listOfPlayers[0].symbol}")
    print(f"Player two, {listOfPlayers[1].name} is using {listOfPlayers[1].symbol}")


    # while repeatSentence:
    #     # end when no grade is entered
    #     repeatSentence = input("Enter a word to repeat: ")
    #     print(repeatSentence)
        
