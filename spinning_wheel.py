from turtle import*
setup()
t1=Turtle()
color=["orange","green","blue","pink","yellow","red"]
import random
t1.up()
t1.goto(-200,0)
t1.down()
t1.width(5)
t1.hideturtle()
t1.speed(7)
for i in range(90):
    colorchoice = random.choice(color)
    t1.color(colorchoice)
    t1.forward(200)
    t1.left(85)