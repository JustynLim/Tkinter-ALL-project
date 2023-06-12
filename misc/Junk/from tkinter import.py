from tkinter import *

wind = Tk()
wind.geometry("400x200")

def entry_focus_in(event):
    if entry1.get() == "Enter message...":
        entry1.delete(0,'end')
        entry1.config(fg="Black")
    
def entry_focus_out(event):
    if entry1.get() == "":
        entry1.insert(0,"Enter message...")
        entry1.config(fg="gray")