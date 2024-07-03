# hw 1

usernname = input("Hello user, what should I call you?: ")

print("Hello" + " " + usernname)



# hw 2

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
city = input("In what city do you reside in?: ")
age = input("How old are you?: ")

print("Hello! my name is", first_name + ",",
      "last name is", last_name + ",",
      "I am from the city of", city + ",",
        "I am", age, "years old" + ".")



# hw 3

# input - ითარგმნება როგორც "შეტანა" ან "შეყვანა". როდესაც მომხმარებელს შეაქვს რაიმე ინფორმაცია კომპიუტერში.
# output - ითარგმენა როგორც "გამოტანა" ან "გამოყვანა". როდესაც კომპიუტერში მყოფი ინფორმაცია გამოდის ეკრანზე ან სხვა რაიმე ხელსაწყოზე.



# hw 4

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