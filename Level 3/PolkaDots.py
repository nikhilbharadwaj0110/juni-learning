import turtle
import random

window = turtle.Screen()

tom = turtle.Turtle()
tom.screen.colormode(255)
tom.speed(100)

for p in range(100):
    size = random.randint(5, 50)

    y = random.randint(-350, 350)
    x = random.randint(-350, 350)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tom.penup()
    tom.goto(x, y)
    tom.pendown()
    tom.color(r, g, b)
    tom.begin_fill()
    tom.circle(size)
    tom.end_fill()

window.exitonclick()
