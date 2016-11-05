import select
import socket
import sys
import _thread
from tkinter import Tk, Label, Button

global sv

class Network:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Select if you'd like to listen or connect:")
        self.label.pack()

        self.cli_button = Button(master, text="Client", command=self.cli)
        self.cli_button.pack()

        self.serv_button = Button(master, text="Server", command=self.serv)
        self.serv_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def cli(self):
        _thread.start_new_thread( client, ('8.37.55.41',12345) )

        print("You are now a client!")

    def serv(self):
        _thread.start_new_thread( server, (12345,) )
        print("You are now the server!")

def client(ip, port):
    size = 1024
    print('You are the client')
    sv = socket.socket()
    sv.connect((ip, port))
    print('Connected to server')
    while(True):
        sv.recv(size)

def server(port):
    print ('You are the server')
    sv = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    #hostip = '127.0.0.1'
    hostip = socket.gethostbyname(host)
    print('Your ip is: ', hostip)
    port = 12345                # Reserve a port for your service.
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
my_gui = Network(root)
#_thread.start_new_thread( server, (1234,) )
#_thread.start_new_thread( root.mainloop, () )
#server()
root.mainloop()
