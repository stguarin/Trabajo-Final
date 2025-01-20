import firebase_admin as f_a
from firebase_admin import credentials,db
#configurar el acceso a la base
credencial = credentials.Certificate('pong\pong-92e6d.json')
f_a.initialize_app(credencial, {'databaseURL': 'https://pong-92e6d-default-rtdb.firebaseio.com/'})

# referenciando al nodo en la base de datos
referencia = db.reference('/puntajes')
#escribir los datos en tiempo real
referencia.set({
    'Kafka':100
})

#escucha los cambios en tiempo real
def escuchar_eventos(event):
    print(f'cambio detectado: {event.data}')
referencia.listen(escuchar_eventos)