#!/usr/bin/python3

import socket

def banner_grabber(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(str(s.recv(1024)).strip('b'))

def main():
    print("Banner Grabber Automation tool")

    ip = input("Enter the IP address: ")
    port = input("Enter the port number: ")

    banner_grabber(ip, port)

main()