import turtle

tom = turtle.Turtle()
window = turtle.Screen()

tom.speed(10)
tom.hideturtle()

tom.fillcolor("green")

tom.left(270)
tom.penup()
tom.goto(-175, 150)
tom.color("green")
tom.begin_fill()
tom.pendown()
tom.circle(270, 180)
tom.end_fill()

tom.fillcolor("pink")

tom.left(180)
tom.penup()
tom.goto(-105, 150)
tom.color("pink")
tom.begin_fill()
tom.pendown()
tom.circle(200, 180)
tom.end_fill()

tom.fillcolor("black")

tom.penup()
tom.goto(0, 0)
tom.begin_fill()
tom.pendown()
tom.color("black")
tom.circle(5)
tom.end_fill()

tom.fillcolor("black")
tom.penup()
tom.goto(150, 100)
tom.begin_fill()
tom.pendown()
tom.color("black")
tom.circle(5)
tom.end_fill()

tom.fillcolor("black")
tom.penup()
tom.goto(-50, 135)
tom.begin_fill()
tom.pendown()
tom.color("black")
tom.circle(5)
tom.end_fill()

tom.fillcolor("black")
tom.penup()
tom.goto(185, 30)
tom.begin_fill()
tom.pendown()
tom.color("black")
tom.circle(5)
tom.end_fill()

window.exitonclick()
