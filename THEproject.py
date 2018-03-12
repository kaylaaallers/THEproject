from turtle import *
canvas = Screen()
canvas.setup(400,200)

kayla = Turtle()
kayla.forward(50)
kayla.left(90)
kayla.forward(50)
kayla.left(90)
kayla.forward(50)
kayla.left(90)
kayla.forward(50)
kayla.left(90)

canvas.exitonclick()

from turtle import Turtle, Screen

wn = Screen()
wn.bgcolor('lightblue')

turtle = Turtle()
turtle.color('purple')
turtle.penup()

speed = 1

def travel():
    turtle.forward(speed)
    wn.ontimer(travel, 10)

wn.onkey(lambda: turtle.setheading(90), 'Up')
wn.onkey(lambda: turtle.setheading(180), 'Left')
wn.onkey(lambda: turtle.setheading(0), 'Right')
wn.onkey(lambda: turtle.setheading(270), 'Down')

wn.listen()

travel()

wn.mainloop()

