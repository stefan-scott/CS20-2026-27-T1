# Turtle Recap
# Mr. Scott
# Nov 26, 2026

import turtle, random
# Turtle Boilerplate
# Create a screen/window object
wn = turtle.Screen()
wn.setup(600,400)
wn.bgcolor("DARKSEAGREEN")

# Create one or more turtles
t = turtle.Turtle()
t.color("DarkOrchid")
t.pensize(5)
t.speed(0)

# Second control over drawing speed
turtle.tracer(False) #disable drawing animations
                     #instead all instructions
                     #are drawn at once when
                     #the program ends

# Main Program Starts Here
# add four color strings
colors = ["gold", "goldenrod", "lemonchiffon", "linen"]

def color_line(steps):
    #create one line out of many
    #steps → how many mini-lines used
    for i in range(steps):
        col = random.choice(colors)
        t.color(col)
        t.fd(5)

for i in range(360): #[0,1,2,3,4...
    color_line(50)
    t.penup()    #.up()
    t.goto(0,0)
    t.pendown()  #.down()
    t.left(1)
    if i%10 == 0:  #redraw every 10th line 
        turtle.update() #force a screen draw
    

wn.exitonclick()