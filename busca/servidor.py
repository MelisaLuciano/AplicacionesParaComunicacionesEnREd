import socket
import time
import sys
import os
from buscaminas import *

HOST = "127.0.0.1"
PORT = 8080
bufferSize = 1024
juego = 0
k = 0
seguir = True
sigue = False
timeIni = 0; timeFin = 0
gana=False; #Variable para ver si sigue jugando

with  socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPServerSocket:  # Abrir conexión
    UDPServerSocket.bind((HOST, PORT))

    print("Servidor UDP a la escucha")

    msgFromServer = "Bienvenido a buscaminas\nElige la dificultad del juego\n1. Facil\n2. Dificil"
    bytesToSend = str.encode(msgFromServer) # Codifica mensaje
    data,address = UDPServerSocket.recvfrom(bufferSize) # Detecta datos enviados por el cliente
    print("\nMensaje del cliente: "+str(data.decode()))
    UDPServerSocket.sendto(bytesToSend, address) # Manda Mensaje al cliente
    data,address = UDPServerSocket.recvfrom(bufferSize) # Detecta datos enviados por el cliente
    if int(str(data.decode()))==1:
    	k=9; juego=Buscaminas(k)      # Dif es el valor de 
    elif int(str(data.decode()))==2:
        k=16; juego=Buscaminas(k)


#    msgFromServer = juego.verBuscaminas()
    bytesToSend = str.encode(msgFromServer)
    UDPServerSocket.sendto(bytesToSend, address)
    juego.llenoVista() #Llenar el buscaminas para el usuario
    timeIni=time.time()

    while(True):
        print("\nMensaje del cliente: "+str(data.decode()))
        msgFromServer=juego.verBuscaminas()
        bytesToSend=str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend,address)

        msgFromServer='Sigue'
        bytesToSend=str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend,address)

        data,address = UDPServerSocket.recvfrom(bufferSize)

        siguele=juego.ocup(str(data.decode()),1)

        if siguele:

            if gana:
                msgFromServer=juego.verBuscaminas()
                bytesToSend=str.encode(msgFromServer)
                UDPServerSocket.sendto(bytesToSend, address) #Manda mensaje al tablero
                msgFromServer="\n\t Ganaste \n"
                bytesToSend=str.encode(bytesToSend, address)
                msgFromServer="exit"
                bytesToSend=str.encode(msgFromServer)
                UDPServerSocket.sendto(bytesToSend, address) #manda mensaje de cerrar
                break
            
            else: 
                pass
        else:
            msgFromServer="Ocupado" 
            bytesToSend=str.encode(msgFromServer)
            UDPServerSocket.sendto(bytesToSend, address)

        if siguele==2:
            msgFromServer=juego.verBuscaminas()
            bytesToSend=str.encode(msgFromServer)
            UDPServerSocket.sendto(bytesToSend,address)
            msgFromServer="\n\t\t Has perdido TTwTT \t\t\n"
            bytesToSend=str.encode(msgFromServer)
            UDPServerSocket.sendto(bytesToSend, address)
            break
        else:
            pass

    timeFin=time.time()
    print("\nMensaje del cliente: " + str(data.decode()))
    msgFromServer = juego.tiempoPar(timeFin-timeIni)
    bytesToSend=str.encode(msgFromServer)
    UDPServerSocket.sendto(bytesToSend, address) #Manda mensaje turn
