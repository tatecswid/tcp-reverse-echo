# Imports the socket library
import socket

# Control for the main loop for the client
running = True

# We will connect to the server with the HOST and the PORT later
HOST = 'localhost'
PORT = 6060

# The socket is for IPv4 and since it is TCP, we use SOCK_STREAM
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Client requests connection to the server
client.connect((HOST, PORT))
print("Connected to Server...")

# Sends messages to server and prints responses back until client types 'end'
while running:
    message = input("Client Input: ")

    client.send(message.encode('ascii'))

    reversed_message = client.recv(1024).decode('ascii')
    print("Server Reply:", reversed_message)

    if(message == "end"):
        running = False

# Connection ends and client is closed
client.close()
print("Connection ended...")
input("Press Enter to exit...")