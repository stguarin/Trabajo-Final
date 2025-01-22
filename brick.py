import tkinter as tk
import random
from tkinter import font

# Colores para los ladrillos
COLOR_LADRILLOS = ["red", "orange", "yellow", "green", "blue"]

class BrickBreaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Brick Breaker")
        self.root.attributes("-fullscreen", True)  # Activar pantalla completa

        # Detectar el ancho y alto de la pantalla
        self.ANCHO = self.root.winfo_screenwidth()
        self.ALTO = self.root.winfo_screenheight()

        # Crear un contenedor principal
        self.frame_principal = tk.Frame(root, bg="black")
        self.frame_principal.pack(fill="both", expand=True)

        # Crear un frame para los botones
        self.frame_botones = tk.Frame(self.frame_principal, bg="black")
        self.frame_botones.pack(side="bottom", fill="x")

        # Crear el canvas para el juego
        self.canvas = tk.Canvas(self.frame_principal, width=self.ANCHO, height=self.ALTO - 50, bg="black")
        self.canvas.pack(side="top", fill="both", expand=True)

        # Crear la paleta del jugador
        self.paleta = self.canvas.create_rectangle(
            self.ANCHO // 2 - 50, self.ALTO - 80, self.ANCHO // 2 + 50, self.ALTO - 60, fill="white"
        )

        # Crear la bola
        self.bola = self.canvas.create_oval(
            self.ANCHO // 2 - 10, self.ALTO - 100, self.ANCHO // 2 + 10, self.ALTO - 80, fill="white"
        )

        # Definir la velocidad de la bola
        self.dx = random.choice([-3, 3])
        self.dy = -3

        # Crear los ladrillos
        self.ladrillos = []
        self.crear_ladrillos()

        # Crear los botones
        self.boton_pausa = tk.Button(
            self.frame_botones, text="Pausa", font=("Courier", 15, "bold"), bg="yellow", fg="black",
            command=self.pausar_juego
        )
        self.boton_pausa.pack(side="left", padx=20, pady=10)

        self.boton_salir = tk.Button(
            self.frame_botones, text="Salir", font=("Courier", 15, "bold"), bg="red", fg="white",
            command=self.salir_juego
        )
        self.boton_salir.pack(side="right", padx=20, pady=10)

        # Vincular teclas para mover la paleta
        self.root.bind("<Left>", lambda event: self.mover_paleta(-20))
        self.root.bind("<Right>", lambda event: self.mover_paleta(20))
        self.root.bind("<Escape>", lambda event: self.root.attributes("-fullscreen", False))

        # Atributos del estado del juego
        self.en_juego = True

        # Iniciar el juego
        self.actualizar()

    def crear_ladrillos(self):
        ladrillo_ancho = self.ANCHO // 10
        ladrillo_alto = 30
        filas = 5
        columnas = 10

        for fila in range(filas):
            for col in range(columnas):
                x1 = col * ladrillo_ancho + 5
                y1 = fila * ladrillo_alto + 5
                x2 = x1 + ladrillo_ancho - 5
                y2 = y1 + ladrillo_alto - 5

                color = COLOR_LADRILLOS[fila % len(COLOR_LADRILLOS)]
                ladrillo = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                self.ladrillos.append(ladrillo)

    def mover_paleta(self, dx):
        x1, _, x2, _ = self.canvas.coords(self.paleta)
        if 0 <= x1 + dx <= self.ANCHO - (x2 - x1):
            self.canvas.move(self.paleta, dx, 0)

    def actualizar(self):
        if not self.en_juego:
            return

        self.canvas.move(self.bola, self.dx, self.dy)
        x1, y1, x2, y2 = self.canvas.coords(self.bola)

        if x1 <= 0 or x2 >= self.ANCHO:
            self.dx = -self.dx
        if y1 <= 0:
            self.dy = -self.dy

        if self.colision(self.paleta):
            self.dy = -self.dy

        for ladrillo in self.ladrillos:
            if self.colision(ladrillo):
                self.ladrillos.remove(ladrillo)
                self.canvas.delete(ladrillo)
                self.dy = -self.dy
                break

        if y2 >= self.ALTO - 50:
            self.canvas.create_text(
                self.ANCHO // 2, self.ALTO // 2, text="¡GAME OVER!", fill="white", font=("Courier", 24)
            )
            self.en_juego = False
            return

        if not self.ladrillos:
            self.canvas.create_text(
                self.ANCHO // 2, self.ALTO // 2, text="¡GANASTE!", fill="white", font=("Courier", 24)
            )
            self.en_juego = False
            return

        self.root.after(20, self.actualizar)

    def colision(self, objeto):
        x1, y1, x2, y2 = self.canvas.coords(self.bola)
        ox1, oy1, ox2, oy2 = self.canvas.coords(objeto)
        return x1 < ox2 and x2 > ox1 and y1 < oy2 and y2 > oy1

    def pausar_juego(self):
        if self.en_juego:
            self.en_juego = False
            self.boton_pausa.config(text="Reanudar")
        else:
            self.en_juego = True
            self.boton_pausa.config(text="Pausa")
            self.actualizar()

    def salir_juego(self):
        self.root.quit()


# Crear la ventana principal y ejecutar el juego
root = tk.Tk()
juego = BrickBreaker(root)
root.mainloop()

