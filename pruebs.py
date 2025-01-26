import tkinter as tk
import random
from tkinter import font


##crear una ventana principal
ventana = tk.Tk()
ventana.title("ventana principal")
##ventana.geometry('1600x900')
##definir tamaño de la ventana a tamaño completo
ventana.attributes('-fullscreen',1)
##definir el color del fondo de la ventana
ventana.config(bg='black')
#"definir la fuente para botones y titulo"
fuentebotones=font.Font(family="Arcade Classic", size=30, weight="bold")
fuentetitulo=font.Font(family="Arcade Classic", size=150, weight="bold")
fuentebotonesventanas=font.Font(family="Arcade Classic", size=15, weight="bold")
# Configuración inicial
COLOR_LADRILLOS = ["red", "orange", "yellow", "green", "blue"]



#funcion crear ventana 1 jugador
def crear_ventana_1jugador():
       
    ventana_1jugador=tk.Toplevel(ventana)
    ventana_1jugador.title("ventana 1 jugador")
    ventana_1jugador.attributes('-fullscreen',1)
    ventana_1jugador.config(bg='black')
    
    titulo1jugador=tk.Label(ventana_1jugador,text='1 Jugador',font=(fuentetitulo),bg='#000000',fg='white')
    titulo1jugador.place(x=200,y=40)
    boton_volver=tk.Button(ventana_1jugador,text='volver',font=(fuentebotonesventanas),bg='#000000',fg='white',relief='raised',command=ventana_1jugador.destroy)
    boton_volver.place(x=1180,y=20)
    titulo1jugador
    boton_volver

    

def crear_ventana_multiplayer():
    ventana_multi=tk.Toplevel(ventana)
    ventana_multi.title("ventana multijugador")
    ventana_multi.attributes('-fullscreen',1)
    ventana_multi.config(bg='black')
    boton_volver=tk.Button(ventana_multi,text='volver',font=(fuentebotonesventanas),bg='#000000',fg='white',relief='raised',command=ventana_multi.destroy)
    boton_volver.place(x=1180,y=20)
    boton_volver 









def crear_ventana_brick():
    ventana_brick=tk.Toplevel(ventana)
    ventana_brick.title("ventana multijugador")
    ventana_brick.attributes('-fullscreen',1)
    ventana_brick.config(bg='black')
    boton_volver=tk.Button(ventana_brick,text='volver',font=(fuentebotonesventanas),bg='#000000',fg='white',relief='raised',command=ventana_brick.destroy)
    boton_volver.place(x=1180,y=20)
    boton_volver 


#ventana principal
titulo = tk.Label(ventana,text='Pong',font=(fuentetitulo),bg='#000000',fg='white')
titulo.place(x=400,y=40)
single_player= tk.Button(ventana,text='1 Jugador',font=fuentebotones,bg='#000000',fg='white',relief='raised',command=crear_ventana_1jugador)
single_player.place(x=530,y=350)
multi_player= tk.Button(text='Multijugador',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=crear_ventana_multiplayer)
multi_player.place(x=510,y=440)
brick_Breaker= tk.Button(text='Brick Breacker',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=crear_ventana_brick)
brick_Breaker.place(x=490,y=530)
salir= tk.Button(text='Salir',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=ventana.quit)
salir.place(x=600,y=620)

ventana.mainloop()  