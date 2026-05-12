import turtle

ventana = turtle.Screen()
ventana.title("Juego con tortuga")

personaje = turtle.Turtle()
personaje.shape("turtle") 
personaje.penup()

def derecha():
    x = personaje.xcor() + 20
    personaje.setx(x)

def izquierda():
    x = personaje.xcor() - 20
    personaje.setx(x)

def arriba():
    y = personaje.ycor() + 20
    personaje.sety(y)

def abajo():
    y = personaje.ycor() - 20
    personaje.sety(y)

ventana.listen()
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.mainloop()