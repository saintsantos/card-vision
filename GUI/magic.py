#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

# root = Tk()
# root.title("Card-Vision")
#
# root.mainloop()

class Fullscreen_Window:

    def __init__(self, master):
        self.tk = Tk()
        #self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.cli_button = Button(master, text="Client", command=self.cli)
        self.cli_button.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    w = Fullscreen_Window(master)
    w.tk.mainloop()
