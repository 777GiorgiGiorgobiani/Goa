# გაიმეორეთ გავლილი მასალა რაც იცით

from turtle import *

speed(30)
width(7)

# 1

color("red")
begin_fill()

forward(100)
left(120)
forward(100)
left(120)
forward(100)

end_fill()

# 2

penup()
goto(100, 0)
pendown()

color("orange")
begin_fill()

left(60)
forward(100)
right(120)
forward(200)
right(120)
forward(100)

end_fill()

# 3

penup()
goto(150, -90)
pendown()

begin_fill()
color("yellow")

right(120)
forward(100)
right(120)
forward(300)
right(120)
forward(100)

end_fill()

# 4

begin_fill()

penup()
goto(200, -180)
pendown()

begin_fill()
color("red")

right(120)
forward(100)
right(120)
forward(400)
right(120)
forward(100)

end_fill()

# 5

begin_fill()

penup()
goto(250, -270)
pendown()

begin_fill()
color("orange")

right(120)
forward(100)
right(120)
forward(500)
right(120)
forward(100)

end_fill()

# 6

begin_fill()

penup()
goto(300, -360)
pendown()

begin_fill()
color("yellow")

right(120)
forward(100)
right(120)
forward(600)
right(120)
forward(100)

end_fill()

exitonclick()