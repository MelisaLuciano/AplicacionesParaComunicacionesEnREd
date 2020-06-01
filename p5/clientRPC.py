import sys
import getpass
import datetime
import xmlrpc.client

HOST=sys.argv[1]; PORT=sys.argv[2]
addr=HOST+':'+PORT
s=xmlrpc.client.ServerProxy('http://'+addr)
orden=""; instruccion=list()

print("\Service RPC")
nueva=input('Presione [Y] si tiene perfil, [N] para crear nuevo: ')
user=input("usuario: ")
password=getpass.getpass("Contraseña: ")

if nueva.upper()=='Y':
    ingr=s.signIn(user,password)
else:
    ingr=s.logIn(user,password)

if ingr:
    print('\t Sesion lista\n')
    while True:
        orden=input("user@"+user+">> ")
        instruccion=orden.lower().split()
        try:
            if instruccion[0] == 'null':
                print(s.hacerPing())
            elif instruccion[0] == 'create':
                print(s.crearArchivo(instruccion[1], user))
            elif instruccion[0] == 'lookup':
                print(s.oLookUp(user, instruccion[1]))
            elif instruccion[0] == 'read':
                print(s.leerA(user, instruccion[1]))
            elif instruccion[0] == 'write':
                dato=input('Ingrese texto: \n')
                print(s.editarA(user, instruccion[1], dato))
            elif instruccion[0] == 'rename':
                print(s.renombrarA(instruccion[1], instruccion[2], user))
            elif instruccion[0] == 'remove':
                print(s.borarA(instruccion[1],user))
            elif instruccion[0]=='mkdir':
                print(s.crearC(instruccion[1],user))
            elif instruccion[0]=='rmdir':
                print(s.crearC(instruccion[1],user))
            elif instruccion[0]=='readdir':
                print(s.verConten(user))
            elif instruccion[0]=='getattr':
                print(s.infoArch(instruccion[1],user))
            elif instruccion[0]=='access':
                print (s.accederPath(user))
            elif instruccion([0])=='pwd':
                print (s.verDirec(user))
            elif instruccion[0]=='help' or instruccion[0]=='?':
                print (s.ayuda())
            elif instruccion[0]=='exit':
                print ("\n\t Sesion cerrada"+ user +"\n")
                break
            else:
                print ("Intentar de nuevo\n")
        except Exception as e:
            print(e)
else:
    print ("Usuario o contraseña incorrectas")