import random

# Global variables
board = ["-" for _ in range(9)]
currentPlayer = "X"
winner = None
gameRunning = True


# Print the game board
def printBoard(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# Take player input
def playerInput(board):
    while True:
        try:
            inp = int(input("Enter a number (1-9): "))

            if 1 <= inp <= 9:
                if board[inp - 1] == "-":
                    board[inp - 1] = currentPlayer
                    break
                else:
                    print("That position is already taken!")
            else:
                print("Please enter a number between 1 and 9.")

        except ValueError:
            print("Please enter a valid number!")


# Check horizontal win
def checkHorizontal(board):
    global winner

    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True

    if board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True

    if board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True

    return False


# Check vertical win
def checkVertical(board):
    global winner

    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True

    if board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True

    if board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True

    return False


# Check diagonal win
def checkDiagonal(board):
    global winner

    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True

    if board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True

    return False


# Check for winner
def checkWin():
    global gameRunning

    if (
        checkHorizontal(board)
        or checkVertical(board)
        or checkDiagonal(board)
    ):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False


# Check for tie
def checkTie(board):
    global gameRunning

    if "-" not in board and winner is None:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False


# Switch player
def switchPlayer():
    global currentPlayer

    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# Computer move
def computer(board):
    while currentPlayer == "O" and gameRunning:
        position = random.randint(0, 8)

        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


# Main game loop
while gameRunning:
    printBoard(board)

    playerInput(board)
    checkWin()
    checkTie(board)

    if not gameRunning:
        break

    switchPlayer()
    computer(board)

    checkWin()
    checkTie(board)