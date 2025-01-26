import firebase_admin
from firebase_admin import credentials, db
cred = credentials.Certificate("brick-c588e-firebase-adminsdk-fbsvc-819dcc811c.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://brick-c588e-default-rtdb.firebaseio.com/"})


def registrar_jugador():
    jugador= input('¿ingrese su nombre de usuario')
    referencia= db.reference(f'jugadores/{jugador}')
    if referencia.get():
        print('el jugador ya esta registrado')
        return

    clave= input('ingrese la clave con la que se va a loguear')
    marcador = input('ingrese el marcador')

    referencia.set({'contraseña':clave, 'marcador':marcador})
    print(referencia.get)
    print(f'el jugador{jugador}fue registrado exitosamente')
def ingresar():
    jugador= input('ingrese su usuario')
    clave= input('ingrese su contraseña')
    referencia= db.reference(f'jugadores/ {jugador}')

    dato_jugador=referencia.get()
    

    if dato_jugador:
     
        if (dato_jugador.get('contraseña')== clave):
            marcador=dato_jugador.get('marcador')
            print(f'bievenido {jugador} su marcador es {marcador}')
        else :
            print('clave incorracta')
    else:
        print(f'el {jugador} no existe')
def borrar():
    print('desea eliminar su usuario?')
    sino=input('presione 1 para si 2 para no')
    si=1
    if(sino == si):
        print('ok')
        jugador=input('ingrese el nombre de jugador')
        clave=input('ingrese su contr2aseña')
        referencia= db.reference(f'jugadores/ {jugador}') 
        dato_jugador=referencia.get()
        if dato_jugador:
     
            if (dato_jugador.get('contraseña')== clave):  
                referencia.delete 
    else:
        print('gracias por participar')            
def leer_datos():
    referencia = db.reference('jugadores')  # Nodo principal que deseas leer
    datos = referencia.get()  # Obtiene los datos del nodo
    print(datos)




print('bienvenido \ndigite 1 para registrarse\ndigite 2 para ingresar \ndigite 3 para borrar')
Opcion= int(input('ingrese un nimero\t'))
if Opcion == 1:
    registrar_jugador()
elif Opcion==2:    
    ingresar()
elif Opcion==3:
    borrar()
elif Opcion==4:
    leer_datos()
else:
    print('no hay opcion')


