zigzag = [["o",".",".","."],
          ["o",".",".","."],
          ["o",".",".","."],
          ["o","o","o","o"],
          [".",".",".","o"],
          [".",".",".","o"],
          [".",".",".","o"]]
          
square = [["o","o","o","o"],
          ["o",".",".","o"],
          ["o",".",".","o"],
          ["o",".",".","o"],
          ["o",".",".","o"],
          ["o",".",".","o"],
          ["o","o","o","o"]]


glass = [[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]]
         
         # поле 16 на 16
         # фигура 7(y) на 4(x)      

def turn_the_figure (figure):
    new_figure = []
    for x in range(0, len(figure[0])):
        sub_array = []
        for y in range(0, len(figure)):
            turn.append(figure[y][x])      
     
        new_figure.append(sub_array))


    return new_figure       
        
         
         
def projection(glass, y, x, figure):
    #glass[2+0][4+0] = figure[0][0]
    #glass[2+0][4+1] = figure[0][1]
    #glass[2+1][4+0] = figure[1][0]
    #glass[y+1][x+1] = figure[1][1]
    #glass[y+2][x+0] = figure[2][0]
    #glass[y+2][x+1] = figure[2][1]
    
    
    for v in range(0, len(figure)):
       for h in range(0, len(figure[0])):
           if glass[y+v][x+h] != "o":
              glass[y+v][x+h] = figure[v][h]

    return glass
    
# сделать функц по проверке хода фигуры (возможен ли ход фигурой)    


# подумать о перевороте фигуры 
         
def print_figure (figure):
    fig_el = figure[0]
    for y in range(0, len(figure)):
       print()
       for x in range (0, len(fig_el)):
          print(figure[y][x],end="")
       
def is_move_possible(glass, figure_1, y_1, x_1):
    for v in range (0, len(figure_1)):
        for h in range(0, len(figure_1[0])):
            # остановка у дна стакана
             #  if figure_1[y_1][x_1] == "_" and (y_1+v) >= len(glass[v][0]) and (x_1+h) >= len(glass[0][h])//\\
              # or (y_1+v) >= len(glass[v][0]) and (x_1+h) >= len(glass[v][0])   
               #
               #len(glass) = y 
               #gl = len(glass[0]) 
               #gl = x
               
                   
            if glass[y_1+v][x_1+h] != "o" and figure_1[y_1][x_1] == " " :
               continue
            else:
               return False 
    return True 
    # glass - изменен и записывается в glass_1         

            


#print_figure(projection(glass, 4, 6, zigzag))
##next_move = print_figure(projection(glass, 4, 6, zigzag))
next_move = projection(glass, 2, 4, zigzag)
next_move
print_figure(projection(glass, 9, 12, square))
print()
print(is_move_possible(glass, square, 1, 1))
print_figure(turn_the_figure(zigzag))

##zigzag[0][0]

