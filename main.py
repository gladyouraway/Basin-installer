# Imports

import time
from colored import fg, bg, attr
from appJar import gui
import os
import sys
from os import system, name

# definitions

def clear():
    if name == 'nt': 
        _ = system('cls')

    else: 
        _ = system('clear') 







# ================================================== - THA ANIMATION



def load():
    print (" " * 34 + '%sLoading Program%s    V_1.0' % (fg(1), attr(0)))
    time.sleep(2)

    print("                                     __________     ")
    print("                              ______/ ________ \______")
    print("                            _/      ____________      \_")
    print("                          _/____________    ____________\_")
    print("                         /  ___________ \  / ___________  \ ")
    print("                        /  /%sXXXXXXXXXXX%s\ \/ /%sXXXXXXXXXXX%s\  \ " % (fg(1), attr(0),fg(1), attr(0)))
    print("                       /  /%s000000000000%s/    \%s000000000000%s\  \ " % (fg(1), attr(0),fg(1), attr(0)))
    print("                       |  \%sXXXXXXXXXXX%s/ _  _ \%sXXXXXXXXXXX%s/  |" % (fg(1), attr(0),fg(1), attr(0)))
    print("                     __|\_____   ___   //  \\   ___   _____/|__")
    print("                     [_       \     \  X    X  /     /       _]")
    print("                     __|     \ \                    / /     |__")
    print("                     [____  \ \ \   ____________   / / /  ____]")
    print("                          \  \ \ \/||.||.||.||.||\/ / /  /")
    print("                           \_ \ \  ||.||.||.||.||  / / _/")
    print("                             \ \   ||.||.||.||.||   / /")
    print("                              \_   ||_||_||_||_||   _/")
    print("                                \     ........     /")
    print("                                 \________________/  ")


    
    print("")
    print(" %s                     - - - - - - - - - - - - - - - - - - -  %s" % (fg(3), attr(0)))
    
    
    animation = "|/-\\"

    for i in range(50):
        time.sleep(0.01)
        sys.stdout.write("\r" + "                       " +animation[i % len(animation)] + "               Loading ... ")
        sys.stdout.flush()

    for i in range(11):
        time.sleep(0.1)
        sys.stdout.write("\r" + "                       " +animation[i % len(animation)] + "               Done !             ")
        sys.stdout.flush()

    
        
# ================================================== - THA GUI

def Gui():

    app = gui("AfroPony", "400x200")
    app.setBg("Gray") # black, grey, red, orange, white, green, blue, yellow ....
    app.setFg("white")
    app.setFont(16)
    
    

    # Labels
    app.addLabel("title", "Please Login",)
    app.setLabelBg("title", "Black")
    app.setLabelFg("title", "white")

    # LOgin
    app.addLabelEntry("User" + " " * 8)
    app.addLabelSecretEntry("Password")

    def press(button):
        if button == "Cancel":
            app.stop()
        else:
            usr = app.getEntry("Username")
            pwd = app.getEntry("Password")
            print("User:", usr, "Pass:", pwd)

    app.addButtons(["Submit", "Cancel"], press)




    app.go()


# ================================================== 


load()
Gui()
