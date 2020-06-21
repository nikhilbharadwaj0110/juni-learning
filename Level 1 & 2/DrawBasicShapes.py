import turtle

tom = turtle.Turtle()
window = turtle.Screen()

tom.screen.colormode(255)

tom.color(0, 0, 255)
for z in range(4):
    tom.forward(100)
    tom.left(90)

tom.penup()
tom.goto(-175, 0)
tom.pendown()
tom.color(255, 0, 0)

for z in range(3):
    tom.forward(100)
    tom.left(120)

tom.penup()
tom.goto(250, 0)
tom.pendown()
tom.color(0, 255, 0)
tom.circle(50)

window.exitonclick()
