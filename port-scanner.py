#!/usr/bin/python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = "137.74.187.104"
# port = 443

def port_scanner(host, port):
    if s.connect_ex((host, port)):
        print("Port is closed")
    else:
        print("Port is open")

port_scanner("137.74.187.104", 3306)