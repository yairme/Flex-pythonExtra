import turtle
colors = [ "black","green","Blue", "red"]
turtle.speed(1)
my_pen = turtle.Pen()
turtle.bgcolor("grey")
for x in range(360):
    my_pen.pencolor(colors[x % 4])
    my_pen.width(x/100 + 5)
    my_pen.forward(x)
    my_pen.right(92)

turtle.done()
