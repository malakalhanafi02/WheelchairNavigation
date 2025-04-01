import turtle

# Set up screen
screen = turtle.Screen()
screen.title("Wheelchair Navigation House Map")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Turtle to draw walls
drawer = turtle.Turtle()
drawer.speed(0)
drawer.pensize(3)

# Function to draw a rectangle room
def draw_room(x, y, width, height, label):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    for _ in range(2):
        drawer.forward(width)
        drawer.right(90)
        drawer.forward(height)
        drawer.right(90)
    # Label the room
    drawer.penup()
    drawer.goto(x + width / 2, y - height / 2)
    drawer.write(label, align="center", font=("Arial", 12, "bold"))

# Draw rooms
draw_room(-350, 250, 150, 100, "Kitchen")
draw_room(-150, 250, 150, 100, "Living Room")
draw_room(50, 250, 150, 100, "Bedroom 1")
draw_room(250, 250, 150, 100, "Bedroom 2")
draw_room(-350, 100, 150, 100, "Bathroom")
draw_room(-150, 100, 150, 100, "Hallway")
draw_room(50, 100, 150, 100, "Study")
draw_room(250, 100, 150, 100, "Guest Room")
draw_room(-150, -50, 150, 100, "Entrance")

drawer.hideturtle()
turtle.done()
