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
    for n in range (4):
        koch(sideLength,level)
        tommy.right(90)

#test
tommy.pensize(1)
snowflake(300,4)
turtle.done()