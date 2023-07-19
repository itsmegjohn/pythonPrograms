import turtle

circle = turtle.Turtle()
count = 0
for i in range(360):
    circle.forward(2)
    circle.left(1)
    count+=1
turtle.done()
    