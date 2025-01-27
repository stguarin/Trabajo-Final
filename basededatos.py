import firebase_admin
from firebase_admin import credentials, db
cred = credentials.Certificate("brick-c588e-firebase-adminsdk-fbsvc-c12480d74d.json")
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
    referencia= db.reference(f'jugadores/{jugador}')

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
    sino=int(input('presione 1 para si 2 para no'))
    si=1
    if(sino == si):
        print('ok')
        jugador=input('ingrese el nombre de jugador')
        clave=input('ingrese su contr2aseña')
        referencia= db.reference(f'jugadores/{jugador}')
        dato_jugador=referencia.get()
        print(dato_jugador)
        if dato_jugador:
     
            if (dato_jugador.get('contraseña')== clave):
                print(f'hola {jugador} se borrara toda tu informacion')  
                referencia.delete()
                print('el usuario ha sido eliminado')
    else:
        print('gracias por participar')            
def leer_datos():
    jugador=input('ingrese su nombre de ususario')
    referencia = db.reference(f'jugadores/{jugador}')  # Nodo principal que deseas leer
    datojugador=referencia.get()
    if datojugador:
        print(f'hola {jugador}')
        clave=input('ingrese su contreseña')
        if (datojugador.get('contraseña')== clave):
            print(f'binevenido {jugador}')
            datos = datojugador.get('marcador')  # Obtiene los datos del nodo
            print(datos)
def cambiar_marcador():
    jugador=input('ingrese su nombre de usuario')
    referencia= db.reference(f'jugadores/{jugador}')
    datojugador=referencia.get()
    if datojugador:
        clave=input('ingrese su contraseña')
        if datojugador.get('contraseña')==clave:
            sino=int(input('si desea cambiar su marcador presione 1'))
            if sino==1:
                refmarcador=db.reference(f'jugadores/{jugador}/marcador')
                nuevomarcadir=input('ingrese su nuevo marcador')
                #datojugador.delete('marcador')
                #refmarcador.delete()
                refmarcador.update({'marcador':None})
                refmarcador.update({'marcador':nuevomarcadir})
                #datojugador.update(f'marcador{nuevomarcadir}')
                #print(datojugador)



print('bienvenido \ndigite 1 para registrarse\ndigite 2 para ingresar \ndigite 3 para borrar \ndikite 4 buscar mis datos \ndigite5 para cambiar marcador')
Opcion= int(input('ingrese un nimero\t'))
if Opcion == 1:
    registrar_jugador()
elif Opcion==2:    
    ingresar()
elif Opcion==3:
    borrar()
elif Opcion==4:
    leer_datos()
elif Opcion==5:
    cambiar_marcador()
else:
    print('no hay opcion')


