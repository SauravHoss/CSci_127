#Saurav Hossain
#09/21/18
#Random

import turtle
import random

t = turtle.Turtle()
t.speed(10)

for i in range(100):
  t.forward(10)
  a = random.randrange(360)
  t.right(a)