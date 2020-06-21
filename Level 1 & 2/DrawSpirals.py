import turtle

tom = turtle.Turtle()
window = turtle.Screen()

tom.speed(100)
tom.penup()
tom.goto(0, 0)
tom.pendown()

for z in range(100):
    tom.forward(100)
    tom.left(115)

tom.penup()
tom.goto(-350, 200)
tom.pendown()
tom.color(0, 200, 50)

for z in range(100):
    tom.forward(100)
    tom.left(115)

tom.penup()
tom.goto(300, 200)
tom.pendown()
tom.color(0, 50, 200)

for z in range(100):
    tom.forward(100)
    tom.left(115)

tom.penup()
tom.goto(0, -200)
tom.pendown()
tom.color(255, 0, 0)

for z in range(100):
    tom.forward(100)
    tom.left(115)

window.exitonclick()
