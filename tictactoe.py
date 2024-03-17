def main():
   print("Welcome to tictactoe game!")
   start_game()



## игровое поле 
board = [1,2,3,4,5,6,7,8,9]

## количество клеток 
board_size = 3

## вывод игрового поля 
def draw_board():
   print("_" * 4 * board_size)
   for i in range(board_size):
      print((" " * board_size + "|")*3)
      print("",board[i*board_size], "|", board[1+i*board_size],"|",  board[2+i*board_size],"|")
      print(("_" * board_size + "|")*board_size)

## выполняем ход
def game_step():
    pass 
    
    
def check_win():
    pass 


def start_game():
    currentPlayer = "X"
    # номре шага
    step = 1
    draw_board()
    
    while (step<10):
       indexx = input("Current player is " + currentPlayer + 
       ". Type the number of the coordinate where you want to make a move (0 - exit the game): ")
       step+=1
    

main()