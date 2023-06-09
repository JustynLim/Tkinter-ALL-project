## Required lib ##
from tkinter import *
from PIL import Image, ImageTk


### Button config ###                                                                                           -- Declare in global
button_mode = True
button_on = PhotoImage(file=global_path+"resources/light_mode.png")                                             ## Locate image ##
button_off = PhotoImage(file=global_path+"resources/dark_mode.png")                                             ##  resources   ##


########################################### Function ###########################################                -- Declare in local
def system_theme():
    global button_mode

    if button_mode:
        #messagebox.showerror('Dark',"Dark Mode")
        toggle_mode.config(image = button_off,bg = '#26242f',activebackground = "#26242f")
        root.config(bg = "#26242f"); frame.config(bg = "#26242f")                                               ## << This line should base on what is available on ur code (frame,root,label,etc.)
        button_mode = False

    else:
        #messagebox.showerror('Light',"Light Mode")
        toggle_mode.config(image = button_on, bg = "white", activebackground = "white")
        root.config(bg="white"); frame.config(bg = "white")                                                     ## << This line should base on what is available on ur code (frame,root,label,etc.)
        button_mode = True
##################################################################################################


toggle_mode = Button(root, width=173,height = 69, pady=7, image = button_on, bd=0, bg = "white", command = system_theme)
toggle_mode.place(x=752,y=431)