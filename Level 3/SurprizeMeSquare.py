import turtle
import random

window = turtle.Screen()

tom = turtle.Turtle()
tom.screen.colormode(255)

length = random.randint(50, 250)

y = random.randint(-250, 250)
x = random.randint(-250, 250)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

tom.penup()
tom.goto(x, y)
tom.pendown()
tom.color(r, g, b)
tom.begin_fill()
for e in range(4):
    tom.forward(length)
    tom.left(90)
tom.end_fill()

window.exitonclick()
