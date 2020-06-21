import turtle

tom = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
tom.speed(5)

tom.penup()
tom.goto(-200, 200)

tom.fillcolor("magenta")
tom.color("magenta")
tom.begin_fill()
tom.pendown()
for i in range(6):
    tom.forward(100)
    tom.right(60)

tom.end_fill()

tom.penup()
tom.goto(200, 100)

tom.fillcolor("purple")
tom.color("purple")
tom.begin_fill()
tom.pendown()
for i in range(10):
    tom.forward(100)
    tom.right(36)

tom.end_fill()

tom.penup()
tom.goto(-300, -100)

tom.fillcolor("teal")
tom.color("teal")
tom.begin_fill()
tom.pendown()
for i in range(5):
    tom.forward(150)
    tom.right(144)

tom.end_fill()

window.exitonclick()
