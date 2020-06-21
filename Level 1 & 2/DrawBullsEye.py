import turtle

tom = turtle.Turtle()
window = turtle.Screen()

tom.speed(50)

tom.fillcolor("red")

tom.penup()
tom.goto(0, -270)
tom.color("red")
tom.begin_fill()
tom.pendown()
tom.circle(270)
tom.end_fill()

tom.fillcolor("white")

tom.begin_fill()
tom.penup()
tom.goto(0, -200)
tom.pendown()
tom.circle(200)
tom.end_fill()

tom.fillcolor("red")

tom.penup()
tom.goto(0, -150)
tom.begin_fill()
tom.pendown()
tom.circle(150)
tom.end_fill()

tom.fillcolor("white")

tom.begin_fill()
tom.penup()
tom.goto(0, -100)
tom.pendown()
tom.circle(100)
tom.end_fill()

tom.fillcolor("red")

tom.penup()
tom.goto(0, -50)
tom.color("red")
tom.begin_fill()
tom.pendown()
tom.circle(50)
tom.end_fill()

tom.fillcolor("black")

tom.penup()
tom.goto(0, -20)
tom.begin_fill()
tom.pendown()
tom.circle(20)
tom.end_fill()

tom.penup()
tom.goto(250, 250)

window.exitonclick()
