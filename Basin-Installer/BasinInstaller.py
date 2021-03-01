# ------------------------------------------------------------------
#______           _           _____          _        _ _           
#| ___ \         (_)         |_   _|        | |      | | |          
#| |_/ / __ _ ___ _ _ __ ______| | _ __  ___| |_ __ _| | | ___ _ __ 
#| ___ \/ _` / __| | '_ \______| || '_ \/ __| __/ _` | | |/ _ \ '__|
#| |_/ / (_| \__ \ | | | |    _| || | | \__ \ || (_| | | |  __/ |   
#\____/ \__,_|___/_|_| |_|    \___/_| |_|___/\__\__,_|_|_|\___|_|   
# ------------------------------------------------------------------
# Made by SamuR4II & gladyouraway
#                                                               
                                                                   
from time import sleep
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import tkinter as tk 
import os

# -------------------------------------

gui = Tk()

# --  Main colors

Main_BG = "black"                         # lime green, lawn green, ivory2, snow3, seashell2, SteelBlue1, gold, SlateBlue2
Main_FG = "gray71"
Main_Extra = "purple3"

# -- Main GUI stuff

gui.title("Basin-Installer")
gui.configure(background= "black") 
gui.attributes('-topmost', True)
gui.resizable(False, False)
gui.update()


w = 600 # width of GUI
h = 400 # height of GUI

# get screen width and height
ws = gui.winfo_screenwidth() # width of the screen
hs = gui.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the GUI
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

gui.geometry('%dx%d+%d+%d' % (w, h, x, y))


# --







# --



# --

gui.mainloop() 