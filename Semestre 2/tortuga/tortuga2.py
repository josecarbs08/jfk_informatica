from turtle import *

def dibujar_lineas():
    for i in range(400):
        forward(i * 2)
        left(91)

bgcolor("black")
speed(0)
color("yellow")

dibujar_lineas()

done()