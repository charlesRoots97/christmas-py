import turtle

def balls(x,y):

    x+=30
    y+=10

    for _ in range(3):

        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(x+80,y)
        turtle.pendown()
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

        y+=50

    turtle.penup()
    turtle.goto(x+45,y+10)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

def star(x,y):
    turtle.penup()
    turtle.goto(x+50,y+250)
    turtle.pendown()

    turtle.fillcolor("yellow")
    turtle.begin_fill()

    for _ in range(5):
        turtle.forward(50)
        turtle.right(144)

    turtle.end_fill()

def triangles(x,y):
    for _ in range(3):

        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()

        turtle.fillcolor("green")
        turtle.begin_fill()

        for _ in range(3):
            turtle.forward(150)
            turtle.left(120)

        turtle.end_fill()
        y+=50

def trunk():
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()

    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)

        turtle.forward(100)
        turtle.left(90)

    turtle.end_fill()

x = -50
y = -50

turtle.speed(5)
turtle.Screen().bgcolor("#049ccc")

trunk()
triangles(x,y)
star(x,y)
balls(x,y)


turtle.penup()
turtle.goto(-250,-150)
turtle.pendown()

turtle.color("white")
turtle.write("¡Feliz Navidad! Sígueme para aprender más :)", font=("Arial", 16, "italic"))

turtle.Screen().exitonclick()
