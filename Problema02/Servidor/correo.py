import os
import zipfile
import re
import smtplib
import sys
import email
import imaplib
import imaplib_connect
import email.parser
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
#Para python2
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEBase import MIMEBase
#from email import Encoders

class Correo():
    def __init__(self):
        self.dir="servicios/correo"

    def mandarComprimido(self,usua,nomComp,destino):
        direc=self.dir+"/"+usua
        exitoso = "Se ha enviado el correo"
        comp_zip=zipfile.ZipFile(direc+"/"+nomComp+".zip", 'w') # creacion del archivo comprimido
        # Recorremos todo el directorio carpetas,subcarpetas,archivos
        for folder, subfolders, files in os.walk(direc):
            for file in files:  # Recorrer todos los archivos
                if not str(file)==nomComp+".zip": # Si el archivo no es igual al nombre del archivo zip, comprimirlo
                    comp_zip.write(os.path.join(folder, file), 
                                    os.path.relpath(os.path.join(folder,file),direc),
                                    compress_type = zipfile.ZIP_DEFLATED)
        comp_zip.close()    # Cerramos el archivo comprimido
        #Variables del correo a enviar
        SUBJECT = "Melisa es la mejor!"
        RECIPIENTS = destino #Correo al que se envia
        
        server = "smtp.gmail.com"
        port = 587
        username = "ayudaNanoMXSur@gmail.com" #Aqui va el correo desde el que se envia DEBE ser GMAIL
        password = "Nanowrimo18"
        sender = username
        isGMAIL = True
        
        
        msg = MIMEMultipart()
        msg['Subject'] = SUBJECT
        msg['From'] = sender
        msg['To'] = RECIPIENTS
        
        part = MIMEBase("application", "octet-stream")
        part.set_payload(open(direc+"/"+nomComp+".zip", "rb").read()) #archivo zip que se creo antes
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename=\""+nomComp+".zip\"")# file.zip es el mismo del comentario de arriba
        msg.attach(part)
        
        smtp = smtplib.SMTP(server, port)
        
        
        if isGMAIL:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
        smtp.login(username,password)
        smtp.sendmail(sender, RECIPIENTS, msg.as_string())
        smtp.close()
        
        return exitoso

    def ayudameCorr(self):                              # help or ?
        coma={
            "sendzip":"Mandar un correo con un zip (sendzip nombreArchivo correoDestino)"
            "imap: Muestra lo enviado"
        }
        texto=""
        for c in coma:
            texto+=("\t"+c+"\t"+coma[c]+"\n")
        return texto
        
    def mostrarImap(self):
        with imaplib_connect.mostrarImap() as c:
            c.select('INBOX', readonly=True)
            typ, msg_data = c.fetch('1', '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    email_parser = email.parser.BytesFeedParser()
                    email_parser.feed(response_part[1])
                    msg = email_parser.close()
            for header in ['subject', 'to', 'from']:
                print('{:^8}: {}'.format(
                    header.upper(), msg[header]))