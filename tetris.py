from curses import*

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

# точка фигуры  не может оказаться в стакане, если 
#  точка в стакане  равна "o" 
#  точка другой фигуры не равна "."
glass = [[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]]
         
         # поле 17(x) на 16(y)
         # фигура 7(y) на 4(x)      

# создать алгоритм, чтобы цикл печатал элементы снизу фигуры 
def turn_the_figure (figure):
    new_figure = []
    # проходит по столбику фигуры
    for x in range(0, len(figure[0])):
        sub_array = []
        # проходит по горизонтали фигуры
        for y in range(0, len(figure)):
            sub_array.append(figure[y][x])      
        
        new_figure.append(sub_array[::-1])
        
    

#abcd -> dcba
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
       
def is_move_possible(glass, figure, y, x):
    for v in range (0, len(figure)):
        #print()
        for h in range(0, len(figure[0])):
            # остановка у дна стакана
            #print(figure[v][h], end="")
            #print("x+v-",x+v, " ", "y+h-",y+h, "x+h-", (x+h), "len(glass[v][0]) - ", len(glass[v][0]), "len(glass[0][h]) - ", len(glass[0][h]))
            #print(glass[y+v][x+h], end="")
            
            if figure[v][h] == "o" and (y+h) >= len(glass) and (x+h) >= len(glass[0]) or (y+v) >= len(glass) and (x+h) >= len(glass[0]):   
               #
               #len(glass) = y 
               #gl = len(glass[0]) 
               #gl = x
                return " first False"
               
            if glass[v+y][h+x] == "o" and figure[v][h] == "o":
                return "SECOND False" 
    return True 
    # glass - изменен и записывается в glass_1         

def interface (glass, figure, y ,x):
    screen = initscr()
    screen.addstr( 0, 0, "Hello")
    print_field_interface(screen, glass, 5, 5)
    
    for i in range(0, len(glass)):
        projection(glass, (y+i), x, figure)
        screen.getch()
        print_field_interface(screen, glass, 5, 5)
    
    screen.getch()
    endwin()            

def print_field_interface (screen, glass, y, x):
    for v in range(0, len(glass)):
        for h in range(0, len(glass[0])):
            screen.addstr((y+v), (x+h), glass[v][h])
    
# написать фунцкию для копирования массива 

    






#print_figure(projection(glass, 4, 6, zigzag))
##next_move = print_figure(projection(glass, 4, 6, zigzag))
next_move = projection(glass, 2, 4, zigzag)
next_move
print_figure(projection(glass, 0, 0, zigzag))
print()
print_figure(zigzag)
print()
print("(glass)x-",len(glass[0]), "(glass)y-", len(glass))
print()
interface(glass, zigzag, 0, 0)

#print(is_move_possible(glass, zigzag, 12, 10))
#print()
#print(len(zigzag[0]))
#print()

##zigzag[0][0]

