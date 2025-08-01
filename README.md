# Simple TPC Client-Server Reverse Echo Communication

*** This is a Simple Data Communication Project created by Tate Swidorski in SUMMER SEMESTER 2025 ***

--------------------------------------------

## Project Description

The assignment was to create a server and a client that used TCP. The project specified that I would 
create a client that takes input from the user and sends it to server. When the server receives the 
message it replies back with the same message but in reverse.

--------------------------------------------

##  How To Use

To clone repository:
    git clone https://github.com/tatecswid/tcp-reverse-echo
    cd tcp-reverse-echo


[Windows]
Open up two command prompts and run these commands respectively:
    python echo_server.py
    python echo_client.py


[Linux] Note: Run 'sudo apt install python3' if you don't have it yet
Open two terminals and run these commands respectively:
    python3 echo_server.py
    python3 echo_client.py

--------------------------------------------

## Modification

Depending on the devices that will communicate you may want to modify the HOST and PORT to fit your needs.
The HOST should be the ip address that is running the server (on both echo_client.py & echo_server.py).
This setup only works for LAN. However if you port forward then this will work across different networks.