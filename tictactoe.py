# игровое поле 
board = [1,2,3,4,5,6,7,8,9]

# количество клеток

board_size = 3

# выводим игровое поле 
def draw_board():
   print("_" * 4 * board_size)
   for i in range(board_size):
      print((" " * 3 + "|") * board_size)
      print("", board[i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print(("_" * 3 + "|") * board_size)
# выполняем ход
def game_step(move, char):
    if (move < 1 and move > 9 or board[move-1] in ("X", "O")):
       return False
    
    board[move-1] = char
    return True  

def check_win():
    win = False
    
    win_combination = (
       (0,1,2), (3,4,5), (6,7,8),# horizontal
       (0,3,6), (1,4,7), (2,5,8),# vertical 
       (0,4,8), (2,4,6)          # diagonale 
    )
    for pos in win_combination:
       if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
           win = board[pos[0]]


    return win


def start_game():
    current_player = 'X'
    # номер шага 
    step = 1
    draw_board()
    
    while (step < 10) and (check_win() == False): 
       move = input("Current player is " + current_player + " | Enter the coordinate to make a move ( 0 - exit ):  ")
       
       if (move  == "0"):
          break
       
       if (game_step(int(move), current_player)):
          print("Successful move!")
              
          if (current_player == "X"):
              current_player = "O"
          else:
              current_player = "X"
         
         
          draw_board()
          #увеличим номер хода
          step += 1
          
       else:
          print("Invalid number, try again!")
          
       if (step == 10):
          print("Tie!")
       else:
          if check_win() == False: # if check_win == false
             continue
          else:
             print( check_win() + " won!")
       
       
print("Welcome to Tictactoe game!")   

start_game()


