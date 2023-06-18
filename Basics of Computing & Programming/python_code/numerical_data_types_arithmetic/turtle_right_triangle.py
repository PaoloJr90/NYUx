import turtle
import math

print("Please enter the length of the legs in a right triangle:")
a = float(input("Leg #1: "))
b = float(input("Leg #2: "))
c = math.sqrt(a**2+b**2)

alpha_in_radians = math.atan(a/b)
alpha = math.degrees(alpha_in_radians)
beta = 90-alpha

turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(180-alpha)
turtle.forward(c)
turtle.left(180-beta)

turtle.hideturtle
turtle.done()
