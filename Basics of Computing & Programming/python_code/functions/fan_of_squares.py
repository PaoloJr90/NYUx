import turtle
print("Please enter number of squares:")
n = int(input())

#draw a fan of n squares (100x100)
for count in range(n):
    #draw a square
    #turn left 360/n
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.left(360/n)
turtle.hideturtle()
turtle.done()