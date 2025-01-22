import tkinter as tk

class BrickBreaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Brick Breaker")
        self.root.attributes("-fullscreen", True)  # Activar pantalla completa

        # Obtener el tamaño completo de la pantalla
        self.ANCHO = self.root.winfo_screenwidth()
        self.ALTO = self.root.winfo_screenheight()

        # Crear un contenedor principal
        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(fill="both", expand=True)

        # Crear un frame para los botones
        self.frame_botones = tk.Frame(self.frame_principal, bg="black")
        self.frame_botones.pack(side="bottom", fill="x")

        # Crear el canvas que ocupa toda la pantalla menos el espacio de los botones
        self.canvas = tk.Canvas(self.frame_principal, width=self.ANCHO, height=self.ALTO - 50, bg="black")
        self.canvas.pack(side="top", fill="both", expand=True)

        # Crear un botón de pausa dentro del frame de botones
        self.boton_pausa = tk.Button(
            self.frame_botones, text="Pausa", font=("Arial", 14), bg="yellow", fg="black", command=self.pausar_juego
        )
        self.boton_pausa.pack(side="left", padx=20, pady=10)

        # Crear un botón de salida dentro del frame de botones
        self.boton_salir = tk.Button(
            self.frame_botones, text="Salir", font=("Arial", 14), bg="red", fg="white", command=self.salir_juego
        )
        self.boton_salir.pack(side="right", padx=20, pady=10)

        # Atributos para el estado del juego
        self.en_juego = True

        # Iniciar el juego
        self.iniciar_juego()

    def iniciar_juego(self):
        # Crear objetos iniciales, como la bola y la raqueta
        self.bola = self.canvas.create_oval(
            self.ANCHO // 2 - 10, self.ALTO // 2 - 10, self.ANCHO // 2 + 10, self.ALTO // 2 + 10, fill="white"
        )
        self.raqueta = self.canvas.create_rectangle(
            self.ANCHO // 2 - 50, self.ALTO - 80, self.ANCHO // 2 + 50, self.ALTO - 70, fill="blue"
        )
        self.velocidad_x = 3
        self.velocidad_y = -3

        # Animar la bola
        self.actualizar()

    def actualizar(self):
        if self.en_juego:  # Solo actualiza si el juego no está en pausa
            self.canvas.move(self.bola, self.velocidad_x, self.velocidad_y)

            # Detectar colisiones con las paredes
            pos = self.canvas.coords(self.bola)
            if pos[0] <= 0 or pos[2] >= self.ANCHO:  # Pared izquierda/derecha
                self.velocidad_x *= -1
            if pos[1] <= 0:  # Pared superior
                self.velocidad_y *= -1
            if pos[3] >= self.ALTO - 50:  # Si la bola cae
                self.en_juego = False
                self.canvas.create_text(
                    self.ANCHO // 2, self.ALTO // 2, text="¡GAME OVER!", fill="white", font=("Arial", 24)
                )
                return

            # Continuar la animación
            self.root.after(20, self.actualizar)

    def pausar_juego(self):
        if self.en_juego:
            self.en_juego = False
            self.boton_pausa.config(text="Reanudar")
        else:
            self.en_juego = True
            self.boton_pausa.config(text="Pausa")
            self.actualizar()

    def salir_juego(self):
        self.root.quit()  # Cierra la aplicación


# Crear ventana principal
root = tk.Tk()
juego = BrickBreaker(root)
root.mainloop()
