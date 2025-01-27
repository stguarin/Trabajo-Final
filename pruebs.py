import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Caja de Texto")
root.geometry("400x300")

# Crear una caja de texto
caja_texto = tk.Text(root, height=10, width=40)
caja_texto.pack(pady=20)

# Función para obtener el contenido de la caja de texto
def obtener_texto():
    texto = caja_texto.get("1.0", tk.END)  # Obtener desde la línea 1, carácter 0 hasta el final
    print("Texto en la caja:", texto.strip())

# Botón para mostrar el contenido
boton = tk.Button(root, text="Obtener Texto", command=obtener_texto)
boton.pack()

# Ejecutar la aplicación
root.mainloop()
