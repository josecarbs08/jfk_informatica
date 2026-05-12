from turtle import *

def dibujar_combinado():
    for i in range(300):
        forward(i)          # Traza la línea
        circle(i * 0.5)     # Dibuja el círculo 
        left(91)            # Gira para formar el patrón

bgcolor("black")
speed(0)
color("yellow")

dibujar_combinado()

done()
