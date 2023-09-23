# Changed from the response by ChatGPT; See chatgpt.png
import turtle

# Create a Turtle screen and a Turtle object
screen = turtle.Screen()
pentagon_turtle = turtle.Turtle()


# Function to draw a pentagon
def draw_pentagon():
    for _ in range(5):
        pentagon_turtle.forward(100)  # Adjust the length of sides as needed
        pentagon_turtle.right(72)  # 360 / 5 = 72 degrees for each turn


# Set up the Turtle's attributes
pentagon_turtle.speed(1)  # You can adjust the drawing speed (1 = slowest, 10 = fastest)
pentagon_turtle.pencolor("#0000FF")  # You can change the pen color
pentagon_turtle.pensize(3)  # You can adjust the pen width

# Move the Turtle to a starting position
pentagon_turtle.goto(0, 0)  # Move to the starting position
pentagon_turtle.pendown()  # Put the pen down

# Draw the pentagon
draw_pentagon()

# Hide the Turtle cursor
pentagon_turtle.hideturtle()

# Close the Turtle graphics window when clicked
screen.exitonclick()
