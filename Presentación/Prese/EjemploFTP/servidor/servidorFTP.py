from pyftpdlib.authorizers import DummyAuthorizer   # Autorizaciones
from pyftpdlib.handlers import FTPHandler   # Comandos del usuario
from pyftpdlib.servers import FTPServer # Creacion del servidor
import logging
import os 

def main():
    # Instancia un autorizador dummy para controlar usuarios "virtuales"
    authorizer = DummyAuthorizer()

    # Define un nuevo usuario teniendo todos los permisos y otro para usuarios de solo lectura
    authorizer.add_user('user', '12345', '.', perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())   # Obtener la direcccion del archivo actual

    # Instancia una clase controladora de FTP
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define un string predeterminado que se envia al cliente cuando se conecte
    handler.banner = 'pyftpdlib basado en FTP, listo'

    # Informacion sobre las conexiones y acciones dentro de la carpeta
    # logging.basicConfig(filename='pyftpd.log', level=logging.INFO)
    logging.basicConfig(level=logging.INFO, format='(ServidorTCP) %(message)s',)
    # Instancia una clase servidor FTP
    address = ('127.0.0.1', 2121)   # Direccion IP y puerto de escucha del servidor (puerto por default 21)
    server = FTPServer(address, handler)    # Se crea el socket

    # configura un limite de conexiones
    server.max_cons = 10    # Numero maximo de conexiones simultanesas
    server.max_cons_per_ip = 5  # Numero maximo de conexiones aceptadas por la misma dirección IP (default=0 (sin limite))

    # Inicia el servidor FTP
    server.serve_forever()  # (timeout=None, blocking=True, handle_exit=True)

if __name__ == '__main__':
    print("Servidor a la escucha")
    main()