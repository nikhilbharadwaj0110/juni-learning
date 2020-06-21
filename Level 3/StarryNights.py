import turtle
import random

window = turtle.Screen()
window.bgcolor("black")

tom = turtle.Turtle()
tom.screen.colormode(255)
tom.speed(100)
tom.hideturtle()

for p in range(100):
    length = random.randint(10, 60)

    y = random.randint(-400, 400)
    x = random.randint(-400, 400)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tom.penup()
    tom.goto(x, y)
    tom.pendown()
    tom.color(r, g, b)
    tom.begin_fill()
    for e in range(5):
        tom.forward(length)
        tom.left(144)
    tom.end_fill()

window.exitonclick()
