import turtle

# Setup window
window = turtle.Screen()
window.title("Wheelchair Navigation with Barcode Detection")
window.setup(width=600, height=600)
window.tracer(0)

# Grid settings
grid_size = 100
cols, rows = 6, 6

# Barcode mapping
barcodes = {
    (0, 0): "kitchen",
    (2, 0): "bathroom",
    (4, 4): "living room"
}
destinations = {
    "kitchen": (100, 400),
    "bathroom": (300, 400),
    "living room": (500, 100)
}

# Draw house grid
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.penup()

for i in range(cols):
    for j in range(rows):
        x, y = i * grid_size, j * grid_size
        drawer.goto(x, y)
        drawer.pendown()
        for _ in range(4):
            drawer.forward(grid_size)
            drawer.right(90)
        drawer.penup()

# Create turtle bot
bot = turtle.Turtle()
bot.shape("turtle")
bot.penup()
bot.speed(1)
bot.goto(0, 0)

# Barcode detection function
def detect_barcode():
    pos = (round(bot.xcor() // grid_size), round(bot.ycor() // grid_size))
    return barcodes.get(pos)

# Move to destination
def move_to(destination):
    x_target, y_target = destinations[destination]
    while round(bot.xcor()) < x_target:
        bot.setx(bot.xcor() + grid_size)
    while round(bot.ycor()) < y_target:
        bot.sety(bot.ycor() + grid_size)

# Simulate detection and action
detected_room = detect_barcode()
if detected_room:
    move_to(detected_room)

window.update()
window.mainloop()
