import tkinter as tk


    
def ventana_un_jugador():
    ventana_de_1_jugador = tk.Tk()
    ventana_de_1_jugador.geometry('1600x900')
    ventana_de_1_jugador.attributes('-fullscreen',1)
    ventana_de_1_jugador.config(bg='black')
    titulo = tk.Label(ventana_de_1_jugador,text='1 JUGADOR',font=('8BIT WONDER',110),bg='#000000',fg='white')
    titulo.place(x=200,y=50)
    Iniciar_juego= tk.Button(ventana_de_1_jugador,text='Iniciar Juego',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised')
    Iniciar_juego.place(x=560,y=400)
    volver= tk.Button(ventana_de_1_jugador,text='Volver',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised',command=ventana_de_1_jugador.destroy)
    volver.place(x=670,y=700)
    ventana_de_1_jugador.mainloop() 
    
def ventana_dos_jugadores():
    ventana_de_2_jugadores = tk.Tk()
    ventana_de_2_jugadores.geometry('1600x900')
    ventana_de_2_jugadores.attributes('-fullscreen',1)
    ventana_de_2_jugadores.config(bg='black')
    titulo = tk.Label(ventana_de_2_jugadores,text='2 JUGADORES',font=('8BIT WONDER',110),bg='#000000',fg='white')
    titulo.place(x=40,y=50)
    Iniciar_juego= tk.Button(ventana_de_2_jugadores,text='Iniciar Juego',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised')
    Iniciar_juego.place(x=560,y=400)
    volver= tk.Button(ventana_de_2_jugadores,text='Volver',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised',command=ventana_de_2_jugadores.destroy)
    volver.place(x=670,y=700)
    ventana_de_2_jugadores.mainloop() 
    
def Brick_Breaker():
    brick_breaker = tk.Tk()
    brick_breaker.geometry('1600x900')
    brick_breaker.attributes('-fullscreen',1)
    brick_breaker.config(bg='black')
    titulo = tk.Label(brick_breaker,text='Brick Breaker',font=('8BIT WONDER',100),bg='#000000',fg='white')
    titulo.place(x=20,y=50)
    Iniciar_juego= tk.Button(brick_breaker,text='Iniciar Juego',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised')
    Iniciar_juego.place(x=560,y=400)
    volver= tk.Button(brick_breaker,text='Volver',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised',command=brick_breaker.destroy)
    volver.place(x=670,y=700)
    brick_breaker.mainloop() 


ventana = tk.Tk()
ventana.geometry('1600x900')
ventana.attributes('-fullscreen',1)
ventana.config(bg='black')
titulo = tk.Label(ventana,text='Pong',font=('8BIT WONDER',150),bg='#000000',fg='white')
titulo.place(x=400,y=50)
single_player= tk.Button(text='1 jugador',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised',command= ventana_un_jugador)
single_player.place(x=600,y=400)
multi_player= tk.Button(text='multijugador',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised',command= ventana_dos_jugadores)
multi_player.place(x=510,y=490)
brick_Breaker= tk.Button(text='Brick Breacker',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised',command=Brick_Breaker)
brick_Breaker.place(x=490,y=580)
salir= tk.Button(text='Salir',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised',command=ventana.quit)
salir.place(x=670,y=700)
ventana.mainloop() 
