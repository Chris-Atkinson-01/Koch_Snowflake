import turtle

def koch_snowflake(turtle, divis, size):
    if(divis == 0):
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, divis - 1, size / 3)
            turtle.left(angle)

divis = 6
size = 2000


wn = turtle.Screen()
wn.setup(width=800, height=400)
turtle.speed(100)
turtle.pendown()

for i in range(3):
    koch_snowflake(turtle, divis, size)
    turtle.left(-120)

