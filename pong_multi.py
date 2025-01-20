import tkinter as tk

# Configuración inicial
ANCHO = 800
ALTO = 400

class Pong:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong")
        
        # Canvas para el juego
        self.canvas = tk.Canvas(root, width=ANCHO, height=ALTO, bg="black")
        self.canvas.pack()

        # Dibujar paletas y pelota
        self.paleta_izquierda = self.canvas.create_rectangle(10, 150, 30, 250, fill="white")
        self.paleta_derecha = self.canvas.create_rectangle(770, 150, 790, 250, fill="white")
        self.pelota = self.canvas.create_oval(390, 190, 410, 210, fill="white")

        # Velocidad inicial
        self.dx = 3
        self.dy = 3

        # Movimiento de las paletas
        self.root.bind("<w>", lambda event: self.mover_paleta(self.paleta_izquierda, -20))
        self.root.bind("<s>", lambda event: self.mover_paleta(self.paleta_izquierda, 20))
        self.root.bind("<Up>", lambda event: self.mover_paleta(self.paleta_derecha, -20))
        self.root.bind("<Down>", lambda event: self.mover_paleta(self.paleta_derecha, 20))

        # Iniciar el juego
        self.actualizar()

    def mover_paleta(self, paleta, dy):
        # Mover paleta dentro de los límites
        self.canvas.move(paleta, 0, dy)
        coords = self.canvas.coords(paleta)
        if coords[1] < 0:  # Evitar que salga por arriba
            self.canvas.move(paleta, 0, -coords[1])
        elif coords[3] > ALTO:  # Evitar que salga por abajo
            self.canvas.move(paleta, 0, ALTO - coords[3])

    def actualizar(self):
        # Mover la pelota
        self.canvas.move(self.pelota, self.dx, self.dy)
        x1, y1, x2, y2 = self.canvas.coords(self.pelota)

        # Rebote en las paredes superior e inferior
        if y1 <= 0 or y2 >= ALTO:
            self.dy = -self.dy

        # Rebote en las paletas
        if self.colision(self.paleta_izquierda) or self.colision(self.paleta_derecha):
            self.dx = -self.dx

        # Reiniciar si la pelota sale de la pantalla
        if x1 <= 0 or x2 >= ANCHO:
            self.canvas.coords(self.pelota, 390, 190, 410, 210)
            self.dx = 3 * (-1 if x1 <= 0 else 1)

        # Llamar a la función de actualización
        self.root.after(20, self.actualizar)

    def colision(self, paleta):
        # Comprobar si la pelota colisiona con una paleta
        x1, y1, x2, y2 = self.canvas.coords(self.pelota)
        px1, py1, px2, py2 = self.canvas.coords(paleta)
        return x1 <= px2 and x2 >= px1 and y1 <= py2 and y2 >= py1

# Crear ventana y ejecutar el juego
root = tk.Tk()
juego = Pong(root)
root.mainloop()

