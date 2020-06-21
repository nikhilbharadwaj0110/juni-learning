import turtle
import random

window = turtle.Screen()

tom = turtle.Turtle()
tom.screen.colormode(255)
tom.hideturtle()
tom.speed(100)

length = 150

window_color_r = random.randint(0, 255)
window_color_g = random.randint(0, 255)
window_color_b = random.randint(0, 255)
window.bgcolor(window_color_r, window_color_g, window_color_b)
tom.penup()
tom.goto(0, 0)
tom.pendown()
tom.begin_fill()
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
tom.color(r, g, b)
tom.right(30)
for e in range(3):
    tom.forward(length)
    tom.left(120)

tom.end_fill()

tom.right(180)

tom.begin_fill()
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
tom.color(r, g, b)
for t in range(3):
    tom.forward(length)
    tom.left(120)

tom.end_fill()

window.exitonclick()
