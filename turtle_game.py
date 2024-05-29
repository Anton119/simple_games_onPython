import turtle 
import time 
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["pink", "pink", "pink", "pink", "gray", "brown", "red", "green", "blue", "orange"]


def race(colors):
    
    racers  = create_many_turtles(colors)
    
    while True:
        for turtle in racers:
            distance = random.randrange(1, 20)
            turtle.forward(distance)
            
            x,y = turtle.pos()
            if y >= HEIGHT - 150:
                return colors[racers.index(turtle)]
    
def create_many_turtles(colors):
    turtles = []
    pinky = []
    spacingx = WIDTH//(len(colors)+1)
    for i, color in enumerate(colors):
        if color == "pink":
            pinky = turtle.Turtle()
            pinky.color(color)
            pinky.shapesize(5)
            pinky.left(90)
            pinky.shape("turtle")
            pinky.penup()
            pinky.setpos(-WIDTH//2 + spacingx * i+1, -HEIGHT//2 + 20)
            pinky.pendown()
            turtles.append(pinky)
        else:
           racer = turtle.Turtle()
           racer.color(color)
           racer.shapesize(1)
           racer.left(90)
           racer.shape("turtle")
           racer.penup()
           racer.setpos(-WIDTH//2 + spacingx * i+1, -HEIGHT//2 + 20)
           racer.pendown()
           turtles.append(racer)
        
        
    return turtles

def init_turtle():
    screen = turtle.Turtle()
    screen = setup(WIDTH, HEIGHT)
    screen.title("Turtle racing!")

def number_of_racers():
    while True:
        racer = input("Enter the number of racers (2-10): ")
        if racer.isdigit():
            racer = int(racer)
            if 2 <= racer <= 10:
                return racer 
            else:
                print("Invalid number")
                
        else:
            print("It's not a number, try again!")
                
racers = number_of_racers()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
time.sleep(3)
print("The color of the winner is:", winner)