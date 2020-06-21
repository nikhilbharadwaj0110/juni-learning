import turtle

tom = turtle.Turtle()
window = turtle.Screen()

tom.speed(50)

tom.fillcolor("red")

tom.penup()
tom.goto(0, -300)
tom.color("red")
tom.begin_fill()
tom.pendown()
tom.circle(300)
tom.end_fill()

tom.fillcolor("light gray")

tom.penup()
tom.goto(0, -250)
tom.color("light gray")
tom.begin_fill()
tom.pendown()
tom.circle(250)
tom.end_fill()

tom.fillcolor("red")

tom.penup()
tom.goto(0, -200)
tom.color("red")
tom.begin_fill()
tom.pendown()
tom.circle(200)
tom.end_fill()

tom.fillcolor("blue")

tom.penup()
tom.goto(0, -150)
tom.color("blue")
tom.begin_fill()
tom.pendown()
tom.circle(150)
tom.end_fill()

tom.fillcolor("white")

tom.penup()
tom.goto(140, 40)
tom.right(180)
tom.pendown()

tom.color("white")
tom.begin_fill()
for z in range(5):
    tom.forward(270)
    tom.left(144)

tom.end_fill()

tom.penup()
tom.goto(300, 300)
tom.pendown()

window.exitonclick()
