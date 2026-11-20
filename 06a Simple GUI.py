# Simple GUI
# Mr. Scott
# Nov 19, 2026
# How to install / use an external library

import FreeSimpleGUI as sg

# get a string from the user...like input()
name = sg.popup_get_text("Enter your name: ", "Question!")
if(name == None):
    print("you pressed cancel")

# Display text in a window
sg.popup(f"Hello there, {name}.")