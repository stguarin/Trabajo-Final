import tkinter as tk
from tkinter import messagebox, simpledialog
ventana = tk.Tk()
ventana.geometry('1600x900')
ventana.attributes('-fullscreen',1)
ventana.config(bg='black')

ventana.title("menuprincipak")
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

def salir():
    ##messagebox= caja de texto .askquestion= pedir una informacion cons respuesta de si o no
    resp= messagebox.askquestion("salir" ,"desea salir de menu")
    if resp== 'yes':
        ##ventana.destroy= cierre de la ventana principal
        ventana.destroy
def acerca_de():
    ##  .showinfo= mostrar texto
    messagebox.showinfo("acerca de", "dasearrollado por arnosl")
def restar():
    ##funciona como un input que pide un numero entero,
    #  abre una pestaña en la que pide el dato
    num1=simpledialog.askinteger("resta","primer nomero")
    num2=simpledialog.askinteger("resta","segundo nomero")
    rest= num1-num2
    messagebox.showinfo(f'el resultado es{rest}')

##funcion para crear una nueva ventana 
def nueva_ventana_sumar():
    ##toplevel para crear una ventana inndependiente
    v1=tk.Toplevel
    v1.title('sumar')
    ##label etiquetas que se ponen en python
    titulo=tk.Label(v1, text="sumar dos numeros")
    v1.geometry("250*250")
    def sumar():
        #hacer un campo de texto dentro de la ventana
        num1=int(txt1.get())
        num2=int(txt2.get())
        suma= num1+num2
        messagebox.showinfo(f'el resultado es{suma}')
        ##entradas de texto asignados a la ventana v1
    txt1=tk.Entry(v1)
    txt2=tk.Entry(v1)
    ##se asigna un nombre al boton y se dice que con ese 
    # boton se va a llamar la funcion sumar
    btn1= tk.Button(v1,'sumar',command=sumar)
    titulo.pack()
    txt1.pack()
    txt2.pack()
    btn1.pack()
#tearoff el menu siempre permanece fijo
menu_inicio = tk.Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="inicio",menu=menu_inicio)
menu_inicio.add_command(label="cerrar",command=salir)


menu_operaciones =tk.Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="operaciones", menu=menu_operaciones)
menu_operaciones.add_command(label="sumar",command=nueva_ventana_sumar)
menu_operaciones.add_command(label="restar",command=restar)


menu_ayuda =tk.Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="acerca de",command=acerca_de)
ventana.mainloop()





