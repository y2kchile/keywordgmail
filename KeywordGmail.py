## Codigo desarrollado en Python3
## Por Marcelo Gonzalez C.

import imaplib
import email
import getpass			# es necesario instalar esta libreria ---- pip install getpass
import stdiomask		# es necesario instalar esta libreria ---- pip install stdiomask




# Funcion para tomar el cuerpo de los correos 
def get_body(msg): 
    if msg.is_multipart(): 
        return get_body(msg.get_payload(0)) 
    else: 
        return msg.get_payload(None, True) 
  
# Funcion para buscar el patron definido en alguna parte del correo, SUBJECT o BODY  
def search(key, value, mail):  
    result, data = mail.search(None, key, '"{}"'.format(value)) 
    return data 
 
# Funcion para tomar el listado de correos que cumplen con el patron 
def get_emails(result_bytes): 
    msgs = [] 
    for num in result_bytes[0].split(): 
        typ, data = mail.fetch(num, '(RFC822)') 
        msgs.append(data)  
    return msgs 


mail = imaplib.IMAP4_SSL('imap.gmail.com')
correo = input ('Por favor ingrese el correo a revisar: ')
pwd = stdiomask.getpass (f"Ingresar la contraseña de {correo}: ")
mail.login(correo, pwd)
mail.list()
mail.select('inbox')


typ, data = mail.search(None, 'ALL')
ids = data[0]
id_list = ids.split()
latest_email_id = int( id_list[-1] )

print (f"\nEn la bandeja de {correo} actualmente hay {latest_email_id} correos")


msgs = get_emails(search('BODY','risk',mail))
for msg in msgs:
    print ('\nEl cuerpo de los correos que tienen la palabra Risk dentro, son: \n')
    print(get_body(email.message_from_bytes(msg[0][1])))
    print ('\nEl encabezado de los correos que tienen la palabra Risk dentro de cuerpo, son: \n')
    print(msg[0][1])


mail.logout()
