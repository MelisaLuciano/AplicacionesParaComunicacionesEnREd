import os
import time

os.chdir('user')


class Acciones:
    def signIn(self, usuario, contra):
        perfilU = list();
        sim = False
        f = open("../usuarios.txt", "r")
        for linea in f.readlines():
            perfil = str(linea).split(',')
            if perfil[0] == usuario and perfil[1] == (str(contra) + "\n"):
                sim = True
                break
        f.close()
        return sim

    def logIn(self, usuario, contra):
        sim = False
        try:
            with open("../usuarios.txt", "a") as f:
                f.write(usuario + ':' + contra + '\n')
            os.mkdir(usuario)
            with open("./" + usuario + "/ini.txt", 'w') as f:
                f.write("Bienvenido " + usuario + "al servicio")
            sim = True
        except Exception as e:
            print(e)
            sim = False
        return sim

    def hacerPing(self):
        return 'reconectando...'

    def crearArchivo(self, arch, usuario):
        f.open("./" + usuario + "/" + arch, "w")
        f.close()
        return self.verConten(usuario)

    def oLookUp(self, usuario, ficha):
        encon = "No existe"
        conten = os.listdir(usuario)
        for dd in conten:
            if dd == ficha:
                encon = "Aqui esta"
                break
        return encon

    def leerA(self, usuario, arch):
        enviar = str.encode('')
        with open("./" + usuario + "/" + arch, "rb") as f:
            for linea in f.readlines():
                envio = envio + linea
        return envio.decode()

    def editarA(self, usuario, arch, text):
        with open("./" + usuario + "/" + arch, "a") as f:
            f.write(text + '\n')
        return self.leerA(usuario, arch)

    def renombrarA(self, nomb1, nomb2, usuario):
        os.rename("./" + usuario + "/" + nomb1, "./" + usuario + "/" + nomb2)
        return self.verConten(usuario)

    def borarA(self, nomb, usuario):
        os.remove("./" + usuario + "/" + nomb)
        return self.verConten(usuario)

    def crearC(self, name, usuario):
        os.mkdir("./" + usuario + "/" + name)
        return self.verConten(usuario)

    def borarC(self, name, usuario):
        os.rmdir("./" + usuario + "/" + name)
        return self.verConten(usuario)

    def verConten(self, usuario):
        return str(os.listdir(usuario))

    def infoArch(self, name, usuario):
        mensaje = "\t" + name
        tamanio = os.path.getsize("./" + usuario + "/" + name)
        hora = os.path.getmtime("./" + usuario + "/" + name)
        mensaje += '\n\t Fecha modificiacion: ' + str(time.ctime(hora))
        mensaje += '\n\t Tamaño: ' + str(tamanio) + 'bytes'
        mensaje += '\n\t' + os.getcwd() + "/" + usuario
        return mensaje

    def accederPath(self, usuario):
        requeri = "Acceso a usuario" + usuario
        return requeri

    def verDirec(self, usuario):
        return os.getcwd() + "/" + usuario

    def ayuda(self):
        com = {
            "null": "Hace ping al servidor",
            "create": "Crea archivo",
            "lookUp": "Busca elemento",
            "read": "Lee documento",
            "write": "Editas documento",
            "rename": "Cambiar nombre de documento",
            "remove": "Elimina documento",
            "mkdir": "Creas directorio",
            "rmdir": "Borras directorio",
            "readdir": "Ver todos los archivos",
            "getattr": "Informacion de arvhivo",
            "access": "Acceso al usuario",
            "pwd": "Da la ruta del usuario"
        }
        text = ""
        for c in com:
            text += ("\t" + c + "\t" + com[c] + "\n")
            return text
