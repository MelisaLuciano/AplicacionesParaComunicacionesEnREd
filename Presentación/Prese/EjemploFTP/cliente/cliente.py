"""
ftplib define la clase FTP 
la clase FTP implementa el lado del cliente del protocolo FTP
Puede dulicar otros servidores FTP 
"""
from ftplib import FTP   #de ftplib se importa FTP
import os
import sys
import time  #tiempo


class Cliente():
    def __init__(self,usu,contra):
        self.HOST="127.0.0.1"
        self.PORT=2121

        ftp = FTP()  # Conexión al host
        ftp.connect(self.HOST, self.PORT) # Se hace la conexión a los parametros definidos
        ftp.login(usu, contra, "noaccount") # Se inicia con los parametros que se piden en init
        #inicia try 
        try:
            with open('README_COPIA.txt', 'wb') as f: # Ayuda a abrir y cerrar alguna estancia, cuando se acabe todo lo que esta dentro 
                ftp.retrbinary('RETR README.txt', f.write) # Recuperar un archivo en modo de transferencia binaria.
                f.write(str.encode(time.strftime("%H:%M:%S"))) 
            a=input("Nombre de la carpeta nueva: ") 
            ftp.mkd(a) #Crear una carpeta, directorio dentro de la carpeta donde está el servidor
        except Exception as e: #error
            print(e) # imprime el error y se sale
        finally:
            print("Tarea finalizada")
            ftp.quit() #Cerrar la conexión

print("Hola\nQuiere ingresar usuario y contrasenia?\n[S]i\t[N]o")
op=input("Opcion: ")
if op=="S" or op=='s':
    name=input("Usuario: ")
    contra=input("Contrasenia: ")
    c=Cliente(name, contra)   
else:
    c=Cliente('anonymous','')
