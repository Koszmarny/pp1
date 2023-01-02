import turtle
from turtle import*

turtle.Screen().bgcolor('light blue')
#begin_fill()
speed(10)
up()

#kwadrat
def kwadrat(x,y,r):
    goto(x,y)
    down()
    left(r)
    color('green')
    while True:
        forward(30)
        left(90)
        if abs(pos()) < 1:
            break
    up()
    turtle.home()

#imie, nazwisko, grupa
def dane():
    up()
    goto(200,300)
    down()
    write("Paweł Byszewski ZZISN1-1112")
    up()
    turtle.home()

#trapez
down()
def trapez(x,y,r):
    goto(x,y)
    down()
    left(r)
    color('dark green')
    forward(60)
    right(120)
    forward(30)
    right(60)
    forward(30)
    right(60)
    forward(30)
    up()
    turtle.home()

#ring
def ring(x,y,r,s):
    goto(x,y)
    left(r)
    pensize(2)
    down()
    color("yellow")
    circle(s)
    up()
    left(90)
    forward(s/2)
    right(90)
    down()
    circle(s/2)
    up()
    pensize(1)
    turtle.home()

#elipsa
def elipsa(x,y,rad):
    goto(x,y)
    color('purple')
    down()
    left(135)
    for i in range(2):
        turtle.circle(rad//3,90)
        turtle.circle(rad,90)

    turtle.seth(100)
    up()
    turtle.home()

#koniczyna
def koniczyna(x,y,r):
    goto(x,y)
    color('red')
    down()
    left(r)
    for i in range(4):
        turtle.circle(20,180)
        right(90)
    up()
    turtle.home()


dane()
kwadrat(0,0,0)
trapez(-50,40,-30)
elipsa(25,-5,45)
koniczyna(15,40,-45)
ring(15,47,0,20)

#end_fill()
turtle.done()
