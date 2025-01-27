import tkinter as tk

# Función para obtener y usar el texto ingresado
def usar_texto():
    texto = caja_texto.get("1.0", tk.END).strip()  # Obtener texto desde la posición 1.0 hasta el final
    print(f"Texto ingresado:\n{texto}")  # Usar el texto (en este caso, imprimirlo)
    etiqueta.config(text=f"Texto capturado:\n{texto}")  # Mostrarlo en otra parte de la interfaz

# Crear ventana principal
root = tk.Tk()
root.title("Usar información de caja de texto")
root.geometry("400x300")

# Caja de texto (multilínea)
caja_texto = tk.Text(root, height=8, width=40, font=("Arial", 12))
caja_texto.pack(pady=10)

# Botón para procesar el texto
boton = tk.Button(root, text="Usar Texto", command=usar_texto)
boton.pack(pady=10)

# Etiqueta para mostrar el texto capturado
etiqueta = tk.Label(root, text="", font=("Arial", 10))
etiqueta.pack(pady=10)

root.mainloop()
