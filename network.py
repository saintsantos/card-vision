import select
import socket
import sys
import _thread
from tkinter import *

global sv


class Network:
    def __init__(self, master):
        self.master = master
        master.title("Card-Vision")

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


root = Tk()
global my_gui
my_gui = Network(root)
#_thread.start_new_thread( server, (1234,) )
#_thread.start_new_thread( root.mainloop, () )
#server()
root.mainloop()
