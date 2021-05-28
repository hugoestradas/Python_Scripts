import turtle

turtle.bgcolor("black")
turtle.pensize("23")
turtle.speed(50)

for i in range (100):
    for colors in ["red", "green", "magenta", "cyan", "white", "blue"]:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()