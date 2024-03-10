# Когда законится луп gameRunning?
import random 
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None 
gameRunning = True 


# printing the game board 

def printBoard (board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8])

# take player input 
def playerInput(board):
    inp = int(input("Entre a coordinate to make a move: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    elif inp < 1 or inp > 9:
            print("This spot doesn't exist!")
    else:
        print("You cannot make a move, the spot is occupied")



# check for win or tie
def checkHorizontale(board):
    global winner 
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRows(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonale(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[6] == board [4] == board[2] and board[6] != "-":
        winner = board[6]
        return True 
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Tie!")
        gameRunning = False 

def checkforWin():
    if checkDiagonale(board) or checkHorizontale(board) or checkRows(board):
        print(f"The winner is {winner}")
        gameRunning = False 


# switch the player 
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O" 
    else: 
        currentPlayer = "X"
        
# computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

# check for win or tie again


# game
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkforWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    # check for win or tie again
    checkforWin()
    checkTie(board)
