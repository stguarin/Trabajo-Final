import tkinter as tk
ventana = tk.Tk()
ventana.geometry('1600x900')
ventana.attributes('-fullscreen',1)
ventana.config(bg='black')

titulo = tk.Label(ventana,text='Pong',font=('8BIT WONDER',150),bg='#000000',fg='white')
titulo.place(x=400,y=50)
single_player= tk.Button(text='1 jugador',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised')
single_player.place(x=600,y=400)
single_player= tk.Button(text='multijugador',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised')
single_player.place(x=510,y=490)
brick_Breaker= tk.Button(text='Brick Breacker',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised')
brick_Breaker.place(x=490,y=580)
salir= tk.Button(text='Salir',font=('8BIT WONDER',30),bg='#000000',fg='white',relief='raised',command=ventana.quit)
salir.place(x=670,y=700)

ventana.mainloop()  