import turtle 
import random 
import time 
WIDTH, HEIGHT = 500, 500
COLORS = ["pink", "black", "purple", "blue", "green", "yellow", "orange", "red", "gray", "brown"]

def race(colors):
    turtles = create_many_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x,y = racer.pos()
            if y >= HEIGHT:
                return colors[turtles.index(racer)]
            
        
        

def create_many_turtles(colors):
    turtles = []
    dislocation = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * dislocation , -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
        
        #time.sleep(3)
    return turtles

def create_turtle():
    screen  = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing!")
    time.sleep(5)

def amount_of_racers():
    while True:
       players = input("How many players do you want to create (2-10)?: ") 
       if players.isdigit():
          racers = int(players)
          if 2 <= racers <= 10:
              return racers
          else:
              print("Sorry, invalid number")
       else:
           print("You should type a number")
           
             
    
#amount_of_racers()
#create_turtle()
racers = amount_of_racers()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print("The winner is the turtle with color:", winner)

time.sleep(5)

