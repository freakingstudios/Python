import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_oval(color, width, height, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(45)
    for i in range(2):
        turtle.ellipse(width, height)
        turtle.left(90)
    turtle.end_fill()

def draw_shinchan_face():
    turtle.speed(2)

    # Head
    draw_circle("#ffdebd", 100, 0, 0)

    # Eyes
    turtle.penup()
    turtle.goto(-35, 50)
    turtle.pendown()
    turtle.fillcolor("#ffffff")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(35, 50)
    turtle.pendown()
    turtle.fillcolor("#ffffff")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    # Eyebrows
    turtle.penup()
    turtle.goto(-50, 80)
    turtle.pendown()
    turtle.setheading(-20)
    turtle.width(8)
    turtle.forward(70)
    turtle.penup()
    turtle.goto(20, 80)
    turtle.pendown()
    turtle.setheading(20)
    turtle.forward(70)

    # Mouth
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.width(8)
    turtle.circle(50, 180)

    turtle.hideturtle()

draw_shinchan_face()
turtle.done()
