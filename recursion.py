# # George Lupu
# #12/5/24
# from random import *

# def randomNumber(times):
#     if(times == 0):
#         print("stop")
#     else:
#         print(randint(0,100))
#         randomNumber(times-1)

# randomNumber(5)


import turtle
tommy = turtle.Turtle()
tommy.speed(100000)
def koch(sideLength,level):
    if level > 0:
        for angle in [60,-120,60,0]:
            koch(sideLength/3, level-1)
            tommy.left(angle)
    else:
        tommy.forward(sideLength)

def snowflake(sideLength,level):
    for n in range (6):
        koch(sideLength,level)
        tommy.right(-60)


def snowflakeInverted(sideLength,level):
    for n in range (3):
        koch(sideLength,level)
        tommy.left(120)


#test
from random import *
tommy = turtle.Turtle()
tommy.speed(0)
tommy.pensize(1)
turtle.tracer(100)
tommy.hideturtle()


tommy.color('blue')
tommy.begin_fill()
snowflake(200,7)
tommy.end_fill()
tommy.penup()
tommy.goto(-50,88)
tommy.color('red')
tommy.begin_fill()
snowflakeInverted(300,7)
tommy.end_fill()
turtle.update()
turtle.done()