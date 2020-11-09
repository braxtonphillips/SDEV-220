#Braxton Phillips
#SDEV 220
#Chapter 1 Exercise 1.21
#Due Oct 31, 2020

import turtle

#draws minute hand 
turtle.pensize(3) #increases boldness of line
turtle.right(180) #left turn
turtle.forward(180) #draws line
turtle.right(180) #turn back right
turtle.forward(180) #back to origin

#draws hour hand
turtle.pensize(3)
turtle.right(90)
turtle.forward(120)
turtle.right(180)
turtle.forward(120)

#draws seconds hand
turtle.pensize(1)
turtle.forward(180)
turtle.right(180)
turtle.forward(180)

#draws clock face
turtle.left(90/12)
turtle.penup()
turtle.forward(270)
turtle.left(90)
turtle.down()
turtle.circle(270)

#apply ref numbers
turtle.penup()
turtle.goto(250, 0)#turtle goes to this point on grid
turtle.write(3) #displays text
turtle.goto(-250,0)
turtle.write(9)
turtle.goto(0,-250)
turtle.write(6)
turtle.goto(0,250)
turtle.write(12)

#write time
turtle.goto(0,-300)
turtle.write('6:45:00')

turtle.done() #pauses graphic when finnished