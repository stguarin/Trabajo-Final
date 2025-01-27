import firebase_admin as f_a
from firebase_admin import credentials,db
import random
#configurar el acceso a la base
credencial = credentials.Certificate('pong\pong-92e6d.json')
f_a.initialize_app(credencial, {'databaseURL': 'https://pong-92e6d-default-rtdb.firebaseio.com/'})

posiblesombres_provicionales = ['hector','victor','manuel','pedro','laura','sofia','johanna','esteban','damian','david','ricardo','aluminio','sekiro','a','b','c','d','e','f','g','h','i','j']
nombre_del_jugaor = posiblesombres_provicionales[random.randrange(0,13)]
puntaje_del_jugador = random.randrange(500,1000001)    

def escritura_del_registro( path, data):
        ref = db.reference(path)
        ref.set(data)

def lectura_del_registro(path):
        ref = db.reference(path)
        return ref.get()

def actualizacion_del_registro(path, data):
        ref = db.reference(path)
        ref.update(data)

def borrado_del_registro(path):
        ref = db.reference(path)
        ref.delete()


registro_anterior =lectura_del_registro('puntajes')
print(registro_anterior)
lista_dict= list(registro_anterior)


datos = {
    lista_dict[0]: registro_anterior[lista_dict[0]],
    lista_dict[1]: registro_anterior[lista_dict[1]],
    lista_dict[2]: registro_anterior[lista_dict[2]],
    lista_dict[3]: registro_anterior[lista_dict[3]],
    lista_dict[4]: registro_anterior[lista_dict[4]],
    nombre_del_jugaor:puntaje_del_jugador
}
data = dict(sorted(datos.items(), key=lambda item: item[1]))
print(data)
eliminacion = list(data)
data.pop(eliminacion[0])
print(data)
escritura_del_registro('puntajes',data)
