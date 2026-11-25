# Turtle Graphics Basics
# Mr. Scott
# Nov 25, 2026
# Boilerplate + Basics...

# you MAY NOT save your file as
# turtle.py
# under any circumstances

import turtle  #loads "turtle.py"

# TURTLE BOILERPLATE CODE:
   
# create a window (Screen Object)
window = turtle.Screen() #returns a window obj
window.setup(600,400) #set window dimensions

# make a turtle (or more)
my_turtle = turtle.Turtle() #returns turtle obj
my_turtle.pensize(3) #pen width
my_turtle.speed(0) #animation delay.  lower = faster

# Main Program


# Program Two
#            0       1       2       3       4       5(X)
colors = ["maroon","red","orange","yellow","green"]
c_index = 0

for i in range(0,300,2): #[0,2,4,...,296,298] 
    my_turtle.color(colors[c_index])
    my_turtle.fd(i) #.forward()  .fd()
    my_turtle.rt(72) #.right()   .rt()
    c_index += 1 #increase by 1
    if c_index >= 5:
        c_index = 0





# Program ONE
# my_turtle.forward(100)
# my_turtle.left(60)
# my_turtle.forward(50)


# AT VERY END
window.exitonclick()






