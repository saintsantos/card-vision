import PIL
from tkinter import *
from PIL import Image, ImageTk


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))



class Board:
    def __init__(self, master):
        self.master = master
        master.title("Card-Vision")
        self.master.attributes("-fullscreen", True)
        for x in range (1,12):
            self.master.columnconfigure(x, weight=1)

        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)

        basewidth = 1790                             # set a base width for resize
        im = Image.open('background.jpg')


        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), PIL.Image.ANTIALIAS)

        background_image = ImageTk.PhotoImage(im)
        self.background_label = Label(master, image=background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.im = background_image

        self.label1 = Label(master, text="1")
        self.label1.grid(row=0, column=0)
        self.label2 = Label(master, text="2")
        self.label2.grid(row=0, column=12)
        self.label3 = Label(master, text="3")
        self.label3.grid(row=12, column=0)
        self.label4 = Label(master, text="4")
        self.label4.grid(row=12, column=12)

        opened = Image.open('BlackLotus.jpg')
        img = ImageTk.PhotoImage(opened)
        self.img_label = Label(master, image=img)
        self.img_label.grid(row=1, column=1)
        self.img_label.img = img

        self.img_label.bind("<Enter>", self.on_enter)
        self.img_label.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        global toplevel
        toplevel = Toplevel()
        toplevel.overrideredirect(1)
    #    center(toplevel)
        im = Image.open('BlackLotus.jpg')
        background_image = ImageTk.PhotoImage(im)
        self.background_label = Label(toplevel, image=background_image)
        self.background_label.im = background_image
        self.background_label.pack()
        print('enter')

    def on_leave(self, enter):
        print('leave')
        toplevel.destroy()



root = Tk()
global my_gui
my_gui = Board(root)
root.mainloop()
