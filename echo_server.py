# Imports the socket library
import socket

# Control for the main loop for our server
running = True

# We need to bind the HOST and the PORT later
HOST = 'localhost'
PORT = 6060

# Simple reverse message function without using [::-1]
def reverse_message(message):
    reversed_message = ""
    for char in message:
        reversed_message = char + reversed_message
    return reversed_message

# The socket is for IPv4 and since it is TCP, we use SOCK_STREAM
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Server waits to receive a connection from a client
server.listen()

# Server accepts a connection from client
communication_socket, address = server.accept()
print("Connected to Client...")

# Receives any messages and replies with the message in reverse until client decides to end the connection
while running:
    message = communication_socket.recv(1024).decode('ascii')
    print("Message Recieved:", message)

    reply = reverse_message(message)
    print("Message Sent Back:", reply)
    communication_socket.send(reply.encode('ascii'))

    if(message == 'end'):
        running = False

# Closes connection
communication_socket.close()
print("Connection ended...")
input("Press Enter to exit...")