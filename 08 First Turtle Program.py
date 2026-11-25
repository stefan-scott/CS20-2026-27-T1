# First Turtle Program
# Mr. Scott
# Nov 25, 2026
# Boilerplate and Basics...

import turtle, random

# TURTLE BOILERPLATE CODE
window = turtle.Screen() #returns a "screen" obj
window.setup(600,400)  #set window dimensions

my_turtle = turtle.Turtle()  #return a "turtle" obj
my_turtle.pensize(3)  #line width
my_turtle.speed(0)  #animation delay,  lower = faster

# Main Program
colors = ["red", "black", "grey", "blue", "orange", "brown"]
color_index = 0

for i in range(0,300,1): #[0,2,4,6,...,296,298]
    my_turtle.color(colors[color_index])
    my_turtle.fd(i)  #.forward()
    my_turtle.rt(60)   #.right()
    color_index += 1 #increase by 1
    if color_index >= len(colors):
        color_index = 0  #color wrap-around


# Program ONE
# my_turtle.forward(150)
# my_turtle.left(90)
# my_turtle.forward(100)



# at the very end
window.exitonclick()


