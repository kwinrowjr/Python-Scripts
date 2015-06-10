def moveTo(t, x, y):
    t.up()
    t.goto(x,y)
    t.down()


def drawCircle(t, xcenter, ycenter, radius, lcolor, flcolor):
    moveTo(t, xcenter, ycenter - radius)
    t.color(lcolor)
    t.fillcolor(flcolor)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def drawTriangle(t, x1, y1, x2, y2, x3, y3, lcolor, flcolor):
    t.color(lcolor)
    t.fillcolor(flcolor)
    t.begin_fill()
    moveTo(t,x1,y1)
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x1,y1)
    t.end_fill()
    


import turtle
t = turtle.Turtle()
t.width(3)

drawCircle(t,0,0,100,'red','green')

drawCircle(t,0,0,90,'red','blue')

drawTriangle(t,-60,70,12,12,-12,-12,'red','white')
drawTriangle(t,60,70,-12,12,12,-12,'red','white')
drawTriangle(t,60,-70,12,12,-12,-12,'red','white')
drawTriangle(t,-60,-70,12,-12,-12,12,'red','white')

drawCircle(t,0,0,60,'red','orange')
drawCircle(t,0,0,50,'red','yellow')

drawTriangle(t,0,95,15,0,-15,0,'red','white')
drawTriangle(t,95,0,0,15,0,-15,'red','white')
drawTriangle(t,0,-95,-15,0,15,0,'red','white')
drawTriangle(t,-95,0,0,15,0,-15,'red','white')

drawCircle(t,0,0,30,'red','blue')
drawCircle(t,0,0,20,'red','green')

moveTo(t,200,200)
