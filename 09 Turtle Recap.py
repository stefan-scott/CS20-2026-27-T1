# Turtle Recap
# Mr. Scott
# Nov 26, 2026

# you MUST NOT save your file as
# turtle.py under ANY CIRCUMSTANCES

import turtle, random  #loads turtle.py (library)

# Boilerplate
# Window/Screen Object
wn = turtle.Screen()
wn.setup(600,400)
wn.bgcolor("LemonChiffon")

# Turtle(s)
t = turtle.Turtle()
t.color("tomato")
t.pensize(3)

turtle.tracer(False) #disables turtle animations
                     #all drawings appear at once
                     #when program concludes...

# Main Program Starts Here
# Choose 6 color strings and add to list
colors = ["MediumPurple","Olive","MidnightBlue",
          "MediumVioletRed","SeaGreen","Thistle"]

def color_line(steps):
    #create a line out of many little lines
    #steps → number of little lines to use
    for i in range(steps): #[0,1,2,3,4...,49] #range makes list with steps things in it
        col = random.choice(colors)
        t.color(col)
        t.fd(5) #.forward(5)

for i in range(360):
    color_line(50)
    t.penup()  #.up()
    t.goto(0,0)
    t.pendown()
    t.left(1)
    if i%5 == 0: #once every 5 times
        turtle.update() #forces an update to the screen
    


wn.exitonclick()