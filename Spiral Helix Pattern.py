import turtle

turtle.speed(10)

colors = ['red', 'purple', 'blue', 'green', 'white', 'yellow']

t = turtle.Pen()

turtle.bgcolor('black')

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
