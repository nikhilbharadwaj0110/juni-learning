import turtle

tom = turtle.Turtle()
window = turtle.Screen()

tom.speed(25)
tom.penup()
tom.goto(-200, -300)
tom.pendown()

tom.fillcolor("yellow")
tom.begin_fill()
tom.color("yellow")
tom.forward(450)
tom.left(90)
tom.forward(400)

tom.circle(230, 180)
tom.forward(395)

tom.end_fill()

tom.penup()
tom.goto(250, 135)
tom.pendown()

tom.fillcolor("black")
tom.begin_fill()
tom.color("black")
tom.right(90)
tom.forward(460)
tom.left(90)
tom.forward(50)
tom.left(90)
tom.forward(460)
tom.left(90)
tom.forward(50)

tom.end_fill()

tom.penup()
tom.goto(100, 125)
tom.pendown()

tom.fillcolor("gray")
tom.begin_fill()
tom.color("gray")
tom.circle(85)
tom.end_fill()

tom.penup()
tom.goto(80, 125)
tom.pendown()

tom.fillcolor("white")
tom.begin_fill()
tom.color("white")
tom.circle(65)
tom.end_fill()

tom.penup()
tom.goto(45, 125)
tom.pendown()

tom.fillcolor("red")
tom.begin_fill()
tom.color("red")
tom.circle(30)
tom.end_fill()

tom.penup()
tom.goto(-210, -200)
tom.pendown()

tom.fillcolor("blue")
tom.begin_fill()
tom.color("blue")

tom.right(90)
tom.forward(45)
tom.right(90)
tom.forward(65)
tom.left(90)
tom.forward(370)
tom.left(90)
tom.forward(65)
tom.right(90)
tom.forward(45)
tom.right(90)
tom.forward(105)
tom.right(90)
tom.forward(460)
tom.end_fill()

tom.penup()
tom.goto(-10, -55)
tom.pendown()

tom.left(180)
tom.color("black")
tom.circle(250, 45)

tom.penup()
tom.goto(0, 290)
tom.pendown()

tom.left(45)
tom.forward(100)
tom.left(180)
tom.forward(100)
tom.left(135)
tom.forward(100)
tom.left(180)
tom.forward(100)
tom.right(135)
tom.right(45)
tom.left(90)
tom.forward(100)
tom.penup()
tom.goto(400, 400)

window.exitonclick()
