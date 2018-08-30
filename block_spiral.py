#Saurav Hossain
#08/29/18
#Draws a block that spirals

#Import turt and name
import turtle
t = turtle.Turtle()

#make it perrrrrrty
t.color("violetred2", "hotpink")
t.shape("turtle")

i = 0

while (i < 250): 
	t.forward(i)
	t.left(90)
	i = i + 10