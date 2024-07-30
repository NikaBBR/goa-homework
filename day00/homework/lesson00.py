from turtle import *
#we want to draw house

#step 1:   draw a square



speed(999999999999999999)
width(7)
color("brown")
forward(250) 
left(90)

forward(300)
left(90)

forward(250)
left(90)

forward(300)
left(90)

forward(100)
color("brown")
begin_fill()
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(0, 300)
pendown()
color("green")
begin_fill()
left(140)
forward(210)
right(105)
forward(200)
end_fill()
color("yellow")
penup()
goto(100, 180)
pendown()
begin_fill()
left(55.2)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
end_fill()

penup()
goto(-600,450)
pendown()
color("yellow")
begin_fill()
right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)
end_fill()










exitonclick()