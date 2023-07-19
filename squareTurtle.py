import turtle
t = turtle.Turtle()
def sqr(t, x, y, length):
    
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)


sqr(t, 10, 15, 50)
