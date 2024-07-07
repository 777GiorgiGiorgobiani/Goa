from turtle import *

#Body of the castle

speed(100)
penup()
goto(-95, 0)
pendown()

color("grey")
width(3)

begin_fill()

forward(200)
left(90)

forward(100)
left(90)

forward(200)
left(90)

forward(100)

end_fill()

# Towers

penup()
goto(-80, 100)
pendown()

begin_fill()

left(180)
forward(75)

right(90)
forward(25)

right(90)
forward(75)

end_fill()



penup()
goto(-30, 100)
pendown()

begin_fill()

left(180)
forward(75)

right(90)
forward(25)

right(90)
forward(75)

end_fill()




penup()
goto(20, 100)
pendown()

begin_fill()

left(180)
forward(75)

right(90)
forward(25)

right(90)
forward(75)

end_fill()



penup()
goto(65, 100)
pendown()

begin_fill()

left(180)
forward(75)

right(90)
forward(25)

right(90)
forward(75)

end_fill()

# roof

color("red")

penup()
goto(-80, 175)
pendown()

begin_fill()

right(90)
forward(5)

right(115)
forward(50)

right(135)
forward(50)

right(110)
forward(5)

end_fill()



penup()
goto(-30, 175)
pendown()

begin_fill()

forward(5)

right(115)
forward(50)

right(135)
forward(50)

right(110)
forward(5)

end_fill()



penup()
goto(20, 175)
pendown()

begin_fill()

forward(5)

right(115)
forward(50)

right(135)
forward(50)

right(110)
forward(5)

end_fill()



penup()
goto(65, 175)
pendown()

begin_fill()

forward(5)

right(115)
forward(50)

right(135)
forward(50)

right(110)
forward(5)

end_fill()


# door

color("brown")

penup()
goto(-15, 0)
pendown()

begin_fill()

right(90)
forward(50)

right(90)
forward(40)

right(90)
forward(50)

end_fill()

exitonclick()