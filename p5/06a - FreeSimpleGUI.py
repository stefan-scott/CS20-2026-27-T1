# Using External Libraries
# Mr. Scott
# Nov 19, 2026
# Installing/Using FreeSimpleGUI
# GUI - graphical user interface

import FreeSimpleGUI as sg

# Get a string from user... like input()
#                           prompt              title
name = None
while name == None:
    name = sg.popup_get_text("Enter your name: ", "Question")
    if name==None:
        print("No Cancelling!")

# Printing Text on a Window
sg.popup(f"Hi There, {name}")

