import turtle

# Function to draw a rectangle
def draw_rectangle(color, width, height):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Function to draw SpongeBob's face
def draw_spongebob():
    turtle.speed(3)

    # Draw the body
    turtle.penup()
    turtle.goto(-50, 100)
    turtle.pendown()
    draw_rectangle("yellow", 100, 150)

    # Draw the eyes
    turtle.penup()
    turtle.goto(-30, 170)
    turtle.pendown()
    draw_rectangle("white", 20, 30)

    turtle.penup()
    turtle.goto(10, 170)
    turtle.pendown()
    draw_rectangle("white", 20, 30)

    # Draw the pupils
    turtle.penup()
    turtle.goto(-20, 180)
    turtle.pendown()
    draw_rectangle("black", 10, 10)

    turtle.penup()
    turtle.goto(20, 180)
    turtle.pendown()
    draw_rectangle("black", 10, 10)

    # Draw the mouth
    turtle.penup()
    turtle.goto(-30, 140)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(30, 180)

    # Draw the nose
    turtle.penup()
    turtle.goto(-10, 150)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # Draw the pants
    turtle.penup()
    turtle.goto(-50, 100)
    turtle.pendown()
    draw_rectangle("brown", 100, 30)

    # Draw the legs
    turtle.penup()
    turtle.goto(-50, 70)
    turtle.pendown()
    draw_rectangle("yellow", 20, 70)

    turtle.penup()
    turtle.goto(30, 70)
    turtle.pendown()
    draw_rectangle("yellow", 20, 70)

    # Draw the shoes
    turtle.penup()
    turtle.goto(-50, 70)
    turtle.pendown()
    draw_rectangle("black", 20, 10)

    turtle.penup()
    turtle.goto(30, 70)
    turtle.pendown()
    draw_rectangle("black", 20, 10)

    # Hide turtle and finish
    turtle.hideturtle()
    turtle.done()

# Set up the turtle
turtle.bgcolor("skyblue")
draw_spongebob()
