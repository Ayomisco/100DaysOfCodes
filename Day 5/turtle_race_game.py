import os
import time
import turtle
import random

# SPECIFIC THE SCREEN OF THE GRAPHICS IN CONSTANT
WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'brown', 'pink', 'cyan']

# constant def
def timing():
    time.sleep(2)
    print('===='*8)

# This function ask player of the numbers of tortoise they we be playing with
def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ') 
        if racers.isdigit():
            timing()
            racers = int(racers)
        else:
            timing()
            print('Input is not numeric... Try again!')
            time.sleep(6)
            os.system('cls')
            continue
            

        if 2 <= racers <= 10:
            return racers
        else:
            timing()
            print('Number not in range 2-10. Try again!')
            time.sleep(2)
            os.system('cls')

# Creating turtle using the color properties
def race(colors):

    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # Set Position
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles
    
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle racing Game!')


racers = get_number_of_racers()
# print(racers)

init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)
