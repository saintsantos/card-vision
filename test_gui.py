from tkinter import *


class Board:
    def __init__(self, master):
        self.master = master
        master.title("Card-Vision")
        self.master.attributes("-fullscreen", True)
        for x in range (1,12):
            self.master.columnconfigure(x, weight=1)

        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)

        background_image = PhotoImage(file="background.jpg")
        background_label = Label(master, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label1 = Label(master, text="1")
        self.label1.grid(row=0, column=0)
        self.label2 = Label(master, text="2")
        self.label2.grid(row=0, column=12)
        self.label3 = Label(master, text="3")
        self.label3.grid(row=12, column=0)
        self.label4 = Label(master, text="4")
        self.label4.grid(row=12, column=12)


root = Tk()
global my_gui
my_gui = Board(root)
root.mainloop()