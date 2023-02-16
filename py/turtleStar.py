import turtle
import random

swidth, sheight, pSize = 500, 500, 3
r, g, b, dist = [0] * 4

turtle.title('거북이가 랜덤한 별 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=swidth+30,height=sheight+30)

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b))
    starLen = random.randrange(10,200)
    x = random.randrange(-250,250)
    y = random.randrange(-250,250)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(5):
        turtle.forward(starLen)
        turtle.left(144)

turtle.done()
        
