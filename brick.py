import tkinter as tk
import random

# Configuración inicial
ANCHO = 800
ALTO = 600
COLOR_LADRILLOS = ["red", "orange", "yellow", "green", "blue"]

class BrickBreaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Brick Breaker")
        
        # Canvas para el juego
        self.canvas = tk.Canvas(root, width=ANCHO, height=ALTO, bg="black")
        self.canvas.pack()

        # Paleta
        self.paleta = self.canvas.create_rectangle(350, 550, 450, 570, fill="white")

        # Bola
        self.bola = self.canvas.create_oval(390, 540, 410, 560, fill="white")

        # Velocidad de la bola
        self.dx = random.choice([-3, 3])
        self.dy = -3

        # Ladrillos
        self.ladrillos = []
        self.crear_ladrillos()

        # Evento de movimiento de la paleta
        self.root.bind("<Left>", lambda event: self.mover_paleta(-20))
        self.root.bind("<Right>", lambda event: self.mover_paleta(20))

        # Iniciar el juego
        self.actualizar()

    def crear_ladrillos(self):
        """Crear una cuadrícula de ladrillos."""
        ladrillo_ancho = 75
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
        """Mover la paleta dentro de los límites."""
        x1, _, x2, _ = self.canvas.coords(self.paleta)
        if x1 + dx >= 0 and x2 + dx <= ANCHO:
            self.canvas.move(self.paleta, dx, 0)

    def actualizar(self):
        """Actualizar la posición de la bola y comprobar colisiones."""
        self.canvas.move(self.bola, self.dx, self.dy)
        x1, y1, x2, y2 = self.canvas.coords(self.bola)

        # Rebote en las paredes
        if x1 <= 0 or x2 >= ANCHO:
            self.dx = -self.dx
        if y1 <= 0:
            self.dy = -self.dy

        # Rebote en la paleta
        if self.colision(self.paleta):
            self.dy = -self.dy

        # Rebote en los ladrillos
        for ladrillo in self.ladrillos:
            if self.colision(ladrillo):
                self.ladrillos.remove(ladrillo)
                self.canvas.delete(ladrillo)
                self.dy = -self.dy
                break

        # Perder la bola
        if y2 >= ALTO:
            self.canvas.create_text(ANCHO // 2, ALTO // 2, text="¡GAME OVER!", fill="white", font=("Arial", 24))
            return  # Detener el juego

        # Ganar el juego
        if not self.ladrillos:
            self.canvas.create_text(ANCHO // 2, ALTO // 2, text="¡GANASTE!", fill="white", font=("Arial", 24))
            return  # Detener el juego

        # Actualizar el frame
        self.root.after(20, self.actualizar)

    def colision(self, objeto):
        """Comprobar colisión entre la bola y un objeto."""
        x1, y1, x2, y2 = self.canvas.coords(self.bola)
        ox1, oy1, ox2, oy2 = self.canvas.coords(objeto)
        return x1 < ox2 and x2 > ox1 and y1 < oy2 and y2 > oy1

# Crear la ventana principal y ejecutar el juego
root = tk.Tk()
juego = BrickBreaker(root)
root.mainloop()
