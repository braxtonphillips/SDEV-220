#Braxton Phillips
#SDEV 220
#Chapter 2 Exercise 2.23
#Due Oct 31, 2020

import turtle

userRadius = eval(input('Please enter a radius:\n'))

#cirlce 1 and 2
turtle.penup()
turtle.forward(userRadius)
turtle.pendown()
turtle.circle(userRadius)
turtle.right(180)
turtle.circle(userRadius)

#cirlce 3
turtle.left(90)
turtle.penup()
turtle.forward(userRadius * 2)
turtle.right(90)
turtle.pendown()
turtle.circle(userRadius)

#cirlce 4
turtle.penup()
turtle.forward(userRadius * 2)
turtle.pendown()
turtle.circle(userRadius)

#cirlce 5
turtle.right(90)
turtle.penup()
turtle.forward(userRadius * 2)
turtle.left(90)
turtle.pendown()
turtle.circle(userRadius)

#cirlce 6 
turtle.right(90)
turtle.penup()
turtle.forward(userRadius * 2)
turtle.left(90)
turtle.pendown()
turtle.circle(userRadius)

turtle.done()