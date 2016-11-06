import select
import socket
import sys
import _thread
import PIL
from tkinter import *
from PIL import ImageTk, Image
from PIL import Image


global sv

class BState:
    def __init__(self):
        self.my_life = 20
        self.my_poison = 0
        self.op_life = 20
        self.op_poison = 0
        self.cards = []

class Network:
    def __init__(self, master):
        self.master = master
        master.title("Card-Vision")

        self.state = False
        self.master.bind("<F10>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)

        self.label = Label(master, text="Select if you'd like to listen or connect:")
        self.label.pack()


        self.cli_button = Button(master, text="Client", command=self.cli)
        self.cli_button.pack()

        self.serv_button = Button(master, text="Server", command=self.serv)
        self.serv_button.pack()

        self.ip_entry = Entry(master, width=24)
        self.port_entry = Entry(master, width=24)
        self.ip_label = Label(master, text="Peer IP:")
        self.port_label = Label(master, text="Peer Port:")
        self.connect_button = Button(master, text="Connect", command=self.con)

        self.port_listen_label = Label(master, text="Listen on port:")
        self.listen_button = Button(master, text="Listen", command=self.lis)

        self.listening_label = Label(master, text="You are listening for your peer...")
        self.cancel_button = Button(master, text="Cancel", command=self.canc)

        self.connected_label = Label(master, text="You are connected!")

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        global m
        m = master


    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.master.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"

    def greet(self):
        print("Greetings!")

    def cli(self):
        #_thread.start_new_thread( client, (self.ip_entry.get(),int(self.port_entry.get()) ))

        print("You are now a client!")
        self.label.pack_forget()
        self.cli_button.pack_forget()
        self.serv_button.pack_forget()
        self.close_button.pack_forget()

        self.ip_label.pack()
        self.ip_entry.pack()
        self.port_label.pack()
        self.port_entry.pack()
        self.connect_button.pack()
        self.close_button.pack()

    def con(self):
        _thread.start_new_thread( client, (self.ip_entry.get(),int(self.port_entry.get()) ))

    def serv(self):
        #_thread.start_new_thread( server, (12345,) )
        print("You are now the server!")
        for widget in self.master.winfo_children():
            widget.pack_forget()


        self.port_listen_label.pack()
        self.port_entry.pack()
        self.listen_button.pack()
        self.close_button.pack()

    def lis(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
        _thread.start_new_thread( server, (int(self.port_entry.get()),) )
        self.listening_label.pack()
        self.cancel_button.pack()
        self.close_button.pack()

    def canc(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()

        self.label.pack()
        self.cli_button.pack()
        self.serv_button.pack()
        self.close_button.pack()

    def connected(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
        self.connected_label.pack()
        GUI(Toplevel())
        #self.master.destroy()


class GUI:
    def __init__(self, master):
        self.bstate = BState()
        self.toplevel = Toplevel()
        self.toplevel.destroy()
        #Keeps track of how many cards are on the board for while adding cards
        self.card_count = 0
        self.land_count = 0

        self.images = []

        self.master = master
        master.title("Card-Vision")

        #self.master.configure(background='grey')

        # This is full screen stuff
        self.state = True
        self.master.attributes("-fullscreen", self.state)
        self.master.bind("<F10>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)


        for x in range(0, 100):
            self.master.columnconfigure(x,weight=1)

        for y in range(0, 50):
            self.master.rowconfigure(y,weight=1)

        basewidth = 1920                             # set a base width for resize
        im = Image.open('../background.jpg')


        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), PIL.Image.ANTIALIAS)

        background_image = ImageTk.PhotoImage(im)
        self.background_label = Label(master, image=background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.im = background_image



        self.my_life_label = Label(master, text='Life', font=("Courier", 33), borderwidth=5, bg='grey').grid(row=0,column=0,columnspan=3)
        self.my_life_number = Label(master, text='20', font=("Courier", 44), borderwidth=5, bg='grey' )
        self.my_life_number.grid(row=1,column=1)
        self.life_plus = Button(master, text="+", command= lambda: self.adjust_counters(1,0,1), bg='grey').grid(row=1,column=0)
        self.life_minus = Button(master, text="-", command=lambda: self.adjust_counters(1,0,0), bg='grey').grid(row=1,column=2)

        self.my_poison_label = Label(master, text='Poison', font=("Courier", 33), borderwidth=5, bg='grey' ).grid(row=3,column=0,columnspan=3)
        self.my_poison_number = Label(master, text='0', font=("Courier", 44), borderwidth=5, bg='grey' )
        self.my_poison_number.grid(row=4,column=1)
        self.poison_plus = Button(master, text="+", command=lambda: self.adjust_counters(0,0,1)).grid(row=4,column=0)
        self.poison_minus = Button(master, text="-", command=lambda: self.adjust_counters(0,0,0)).grid(row=4,column=2)



        self.op_life_label = Label(master, text='Life', font=("Courier", 28), borderwidth=5, bg='grey').grid(row=45,column=0,columnspan=3)
        self.op_life_number = Label(master, text='20', font=("Courier", 33), borderwidth=5 , bg='grey')
        self.op_life_number.grid(row=46,column=1)
        self.life_plus = Button(master, text="+", command=lambda: self.adjust_counters(1,1,1)).grid(row=46,column=0)
        self.life_minus = Button(master, text="-", command=lambda: self.adjust_counters(1,1,0)).grid(row=46,column=2)

        self.op_poison_label = Label(master, text='Poison', font=("Courier", 28), borderwidth=5 , bg='grey').grid(row=47,column=0,columnspan=3)
        self.op_poison_number = Label(master, text='0', font=("Courier", 33), borderwidth=5 , bg='grey')
        self.op_poison_number.grid(row=48,column=1)
        self.poison_plus = Button(master, text="+", command=lambda: self.adjust_counters(0,1,1)).grid(row=48,column=0)
        self.poison_minus = Button(master, text="-", command=lambda: self.adjust_counters(0,1,0)).grid(row=48,column=2)

        landnum = 0
        cardnum = 0

        for x in range(0,11):
            self.add_card("Afterlife","CMD",0,0)
        self.add_card("Attrition", "CMD", 1, 1)
        self.add_card("Attrition", "CMD", 1, 0)
        self.add_card("Attrition", "CMD", 1, 1)


        global m
        m = master

    def adjust_counters(self, life, opponent, add):
        if life:
            if opponent:
                if add:
                    self.bstate.op_life += 1
                else:
                    self.bstate.op_life -= 1
            else:
                if add:
                    self.bstate.my_life += 1
                else:
                    self.bstate.my_life -= 1
        else:
            if opponent:
                if add:
                    self.bstate.op_poison += 1
                else:
                    self.bstate.op_poison -= 1
            else:
                if add:
                    self.bstate.my_poison += 1
                else:
                    self.bstate.my_poison -= 1
        print('hullo!')
        self.op_life_number.config(text=(self.bstate.op_life))
        self.op_poison_number.config(text=(self.bstate.op_poison))
        self.my_life_number.config(text=(self.bstate.my_life))
        self.my_poison_number.config(text=(self.bstate.my_poison))


        #should take in the card name and three set code and form file name from that, then boolian for if it's a land
    def add_card(self, card, setn, land, isTapped):

        basewidth = 120

        img = Image.open(setn+"/"+card+".full.jpg")
        if isTapped:
            img = img.rotate(90, expand=True)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.ilabel = Label(self.master, image = img)

        if land:
            self.land_count += 1
            if self.land_count > 9:
                self.ilabel.grid(row=0,column=10*self.land_count%9)
            else:
                self.ilabel.grid(row=0,column=10*self.land_count, rowspan=2)

        else:
            self.card_count += 1
            if self.card_count > 9:
                self.ilabel.grid(row=5*(1+ self.card_count//9),column=10*(self.card_count%9), rowspan=8)
            else:
                self.ilabel.grid(row=3,column=10*self.card_count, rowspan=8)
        self.ilabel.bind("<Enter>", lambda event: self.on_enter(setn+"/"+card+".full.jpg"))
        self.ilabel.bind("<Leave>", self.on_leave)


        #img = img.ImageOps.fit(img, 50, Image.ANTIALIAS)
        self.ilabel.img = img


    def on_enter(self, path):
        self.toplevel = Toplevel()
        hs = root.winfo_screenheight()
        h = 285
        w = 199
        y = (hs/2) - (h/2)
        self.toplevel.geometry('%dx%d+%d+%d' % (w, h, 0, y))
        self.toplevel.overrideredirect(1)
    #    center(toplevel)
        im = Image.open(path)
        background_image = ImageTk.PhotoImage(im)
        self.background_label = Label(self.toplevel, image=background_image)
        self.background_label.im = background_image
        self.background_label.pack()
        print('enter')

    def on_leave(self, enter):
        print('leave')
        self.toplevel.destroy()

    # Function for toggling fullscreen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.master.attributes("-fullscreen", self.state)
        return "break"

    # Function for exiting fullscreen
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"



    def cli(self):
        #_thread.start_new_thread( client, (self.ip_entry.get(),int(self.port_entry.get()) ))

        print("You are now a client!")
        self.label.pack_forget()
        self.cli_button.pack_forget()
        self.serv_button.pack_forget()
        self.close_button.pack_forget()

        self.ip_label.pack()
        self.ip_entry.pack()
        self.port_label.pack()
        self.port_entry.pack()
        self.connect_button.pack()
        self.close_button.pack()

    def con(self):
        _thread.start_new_thread( client, (self.ip_entry.get(),int(self.port_entry.get()) ))

    def serv(self):
        #_thread.start_new_thread( server, (12345,) )
        print("You are now the server!")
        for widget in self.master.winfo_children():
            widget.pack_forget()


        self.port_listen_label.pack()
        self.port_entry.pack()
        self.listen_button.pack()
        self.close_button.pack()

    def lis(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
        _thread.start_new_thread( server, (int(self.port_entry.get()),) )
        self.listening_label.pack()
        self.cancel_button.pack()
        self.close_button.pack()

    def canc(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()

        self.label.pack()
        self.cli_button.pack()
        self.serv_button.pack()
        self.close_button.pack()

    def connected(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
        self.connected_label.pack()




def client(ip, port):
    size = 1024
    print('You are the client')
    sv = socket.socket()
    sv.connect((ip, port))
    print('Connected to server')
    my_gui.connected()
    while(True):
        sv.recv(size)

def server(port):
    print ('You are the server')
    sv = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    #hostip = '127.0.0.1'
    hostip = socket.gethostbyname(host)
    print('Your ip is: ', hostip)
    print('You are listening on port: ', port)
    sv.bind((hostip, port))        # Bind to the port
    #port = 50000
    #backlog = 5
    size = 1024
    #server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server.bind((host,port))
    #server.listen(backlog)
    sv.listen(5)
    input = [sv,sys.stdin]
    running = 1
    while running:
        inputready,outputready,exceptready = select.select(input,[],[])
        for s in inputready:
            if s == sv:
                # handle the server socket
                client, address = sv.accept()
                input.append(client)
                print("New connection: ", address)
                my_gui.connected()
            elif s == root:
                root.mainloop()
            elif s == sys.stdin:
                # handle standard input
                junk = sys.stdin.readline()
                running = 0

            else:
                # handle all other sockets
                data = s.recv(size)
                print('Recieved: ', data.decode())
                if data:
                    s.send(data)
                else:
                    s.close()
                    input.remove(s)
    sv.close()

global root
root = Tk()
global my_gui
my_gui = Network(root)
#_thread.start_new_thread( server, (1234,) )
#_thread.start_new_thread( root.mainloop, () )
#server()
root.mainloop()
