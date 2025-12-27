#!/usr/bin/python3
"""Module for Client-Server Application"""


import socket
import json

def start_server():
    """Server side"""
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 5050
    ADDR = (HOST, PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(ADDR)
        s.listen()

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)

                if not data:
                    break

                print(json.load(data))



def send_data(sample_dict):
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 5050
    ADDR = (HOST, PORT)


    with socket.socket(socket.AT_INET, socket.SOCK_STREAM) as s:
        s.connect(ADDR)
        s.sendall(json.dumps(sample_dict))

