from turtle import *


#we want to paint a house

#step 1: draw a square

speed(30)
width(7)
color("purple")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

#step 2: door
forward(70)
left(90)

color("yellow")
begin_fill()

forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()

#roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#windows
penup()
goto(190, 40)
pendown()

color("cyan")
begin_fill()

#window1
left(210)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

#window2
penup()
goto(50, 40)
pendown()

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill()

#window3
begin_fill()

penup()
goto(190, 130)
pendown()

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill()

#window4

begin_fill()

penup()
goto(50, 130)
pendown()

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill()

exitonclick()