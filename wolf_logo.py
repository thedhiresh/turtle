import turtle

def draw_wolf():
    screen = turtle.Screen()
    screen.title("Wolf Sketch")
    screen.bgcolor("white")

    # Create a turtle object
    pen = turtle.Turtle()
    pen.speed(3)
    pen.pensize(2)
    pen.color("black")

    # Function to draw a circle with given position, radius
    def draw_circle(x, y, radius):
        pen.penup()
        pen.goto(x, y - radius)
        pen.pendown()
        pen.circle(radius)

    # Function to draw an ellipse
    def draw_ellipse(x, y, a, b):
        pen.penup()
        pen.goto(x, y - b)
        pen.pendown()
        pen.setheading(0)
        pen.seth(45)
        for _ in range(2):
            pen.circle(a, 90)
            pen.circle(b, 90)

    # Drawing the face
    draw_circle(0, 0, 100) # Main face

    # Drawing the eyes
    draw_circle(-40, 50, 15) # Left eye
    draw_circle(40, 50, 15)  # Right eye

    # Drawing the nose
    pen.penup()
    pen.goto(0, 20)
    pen.pendown()
    pen.setheading(-90)
    pen.circle(20, 180)
    pen.setheading(0)
    pen.forward(40)

    # Drawing the ears
    pen.penup()
    pen.goto(-70, 120)
    pen.pendown()
    draw_ellipse(-70, 120, 30, 50) # Left ear
    pen.penup()
    pen.goto(70, 120)
    pen.pendown()
    draw_ellipse(70, 120, 30, 50) # Right ear

    # Hide the turtle
    pen.hideturtle()

    # Keep the window open until closed by the user
    turtle.done()

draw_wolf()
