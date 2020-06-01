#!/usr/bin/env python3
import time
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8080  # The port used by the server
buffer_size = 1024

print("Leer archivo")
elije = input("Elija alguna opcion: 1.-Biblia 2.-Hamlet 3.-MobyDick")

if elije=="1":
	archivo = open("/home/melisa/Escritorio/p3/TCP/Bibla.txt", "r")
	libro = "Biblia"
elif elije=="2":
	archivo = open("/home/melisa/Escritorio/p3/TCP/hamlet.txt", "r")
	libro = "Hamlet"
elif elije=="3":
	archivo = open("/home/melisa/Escritorio/p3/TCP/MobyDick.txt", "r")
	libro = "MobyDick"
else:
	print("Opcion no valida")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))

    for linea in archivo.readlines():
        	var = str.encode(libro + " --->"+str(linea))
        	TCPClientSocket.sendall(var)
        	time.sleep(0.1)