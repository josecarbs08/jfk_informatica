import turtle

ventana = turtle.Screen()
ventana.title("Juego con imagen")

ventana.addshape("spider.gif")

personaje = turtle.Turtle()  
personaje.shape("spider.gif")
personaje.penup()

def derecha():
    x = personaje.xcor() + 20
    personaje.setx(x)

def izquierda():
    x = personaje.xcor() - 20
    personaje.setx(x)

ventana.listen()
ventana.onkey(derecha, "Right")
ventana.onkey(izquierda, "Left")
ventana.mainloop()
