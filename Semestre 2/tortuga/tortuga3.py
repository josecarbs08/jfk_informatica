from turtle import *

def dibujar_combinado():
    for i in range(300):
        forward(i)          
        circle(i * 0.5)      
        left(91)            

bgcolor("black")
speed(0)
color("yellow")

dibujar_combinado()

done()
